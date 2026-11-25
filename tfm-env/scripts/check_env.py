#!/usr/bin/env python
"""TFM env health check. Run: conda activate tfm-env && python check_env.py"""
from __future__ import annotations

import importlib.metadata
import os
import sys
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Final

PACKAGES: Final[tuple[str, ...]] = ("tabpfn", "tabicl", "torch")
TABPFN_CKPTS: Final[tuple[str, ...]] = (
    "tabpfn-v2-classifier-finetuned-zk73skhh.ckpt",
    "tabpfn-v2-regressor.ckpt",
    "tabpfn-v2.5-classifier-v2.5_default.ckpt",
    "tabpfn-v2.5-regressor-v2.5_default.ckpt",
    "tabpfn-v2.6-classifier-v2.6_default.ckpt",
    "tabpfn-v2.6-regressor-v2.6_default.ckpt",
    "tabpfn-v3-classifier-v3_default.ckpt",
    "tabpfn-v3-regressor-v3_default.ckpt",
    "tabpfn-v3.5-20260909.safetensors",
    "tabpfn-v3.5-20260909_multiclass.safetensors",
)
TABICL_CKPTS: Final[tuple[tuple[str, str], ...]] = (
    ("models--jingang--TabICL", "tabicl-classifier-v2-20260212.ckpt"),
    ("models--jingang--TabICL", "tabicl-regressor-v2-20260212.ckpt"),
    ("models--jingang--TabICL-clf", "tabicl-classifier-v1.1-0506.ckpt"),
)


@dataclass(slots=True)  # noqa: MUTABLE_OK — CLI accumulator
class Report:
    """Accumulator for CLI checks; mutation is the purpose."""

    items: list[tuple[str, bool]] = field(default_factory=list)

    def add(self, label: str, ok: bool, detail: str = "") -> None:
        self.items.append((label, ok))
        extra = f"  {detail}" if detail else ""
        print(f"[{'OK' if ok else 'MISS'}] {label}{extra}")

    @property
    def failed(self) -> list[str]:
        return [label for label, ok in self.items if not ok]


def _pkg_version(name: str) -> str | None:
    try:
        return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        return None


def _missing_tabpfn() -> list[str]:
    root = Path(os.environ.get("APPDATA", "")) / "tabpfn"
    return [name for name in TABPFN_CKPTS if not (root / name).is_file()]


def _missing_tabicl() -> list[str]:
    hub = Path.home() / ".cache" / "huggingface" / "hub"
    missing: list[str] = []
    for repo, name in TABICL_CKPTS:
        snaps = hub / repo / "snapshots"
        found = snaps.is_dir() and any(
            (snap / name).exists() for snap in snaps.iterdir() if snap.is_dir()
        )
        if not found:
            missing.append(name)
    return missing


def _construct(factory: Callable[[], object]) -> str | None:
    try:
        factory()
    except (ImportError, OSError, RuntimeError, ValueError) as exc:
        return f"{type(exc).__name__}: {exc}"
    return None


def main() -> int:
    print(f"{sys.executable}  {sys.version.split()[0]}  no_user_site={sys.flags.no_user_site}")
    report = Report()

    for name in PACKAGES:
        ver = _pkg_version(name)
        report.add(name, ver is not None, ver or "not installed")

    try:
        import torch
    except ImportError as exc:
        report.add("CUDA", False, str(exc))
    else:
        ok = torch.cuda.is_available()
        detail = ""
        if ok:
            detail = f"{torch.version.cuda} {torch.cuda.get_device_name(0)}"
        report.add("CUDA", ok, detail)

    def tabpfn_clf() -> object:
        from tabpfn import TabPFNClassifier

        return TabPFNClassifier()

    def tabicl_clf() -> object:
        from tabicl import TabICLClassifier

        return TabICLClassifier()

    err = _construct(tabpfn_clf)
    report.add("TabPFNClassifier", err is None, err or "")
    err = _construct(tabicl_clf)
    report.add("TabICLClassifier", err is None, err or "")

    pfn_miss = _missing_tabpfn()
    report.add(
        "TabPFN weights",
        not pfn_miss,
        f"{len(TABPFN_CKPTS) - len(pfn_miss)}/{len(TABPFN_CKPTS)}"
        + (f" missing {pfn_miss}" if pfn_miss else ""),
    )
    icl_miss = _missing_tabicl()
    n_icl = len(TABICL_CKPTS)
    report.add(
        "TabICL weights",
        not icl_miss,
        f"{n_icl - len(icl_miss)}/{n_icl}" + (f" missing {icl_miss}" if icl_miss else ""),
    )

    failed = report.failed
    if failed:
        print(f"FAIL {len(failed)}: {failed}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
