#!/usr/bin/env python3
"""Deterministic conference/journal mapping. Do not edit numbers in prose."""

from __future__ import annotations

import argparse
import json
import sys

LABELS = frozenset(
    {"EXCEEDS", "MEETS", "PARTLY_MEETS", "DOES_NOT_MEET", "NOT_ASSESSED"}
)
SCIENTIFIC = (
    "originality",
    "soundness",
    "evidence",
    "experiments",
    "significance",
)
HARD_GATES = ("G1", "G2", "G4", "G6")
SOFT_GATES = ("G3", "G5")
VERBAL = {
    9: "Very strong accept",
    8: "Strong accept",
    7: "Accept",
    6: "Weak accept",
    5: "Borderline accept",
    4: "Borderline reject",
    3: "Reject",
    2: "Strong reject",
    1: "Very strong reject",
}
NEURIPS2025 = {9: 6, 8: 5, 7: 5, 6: 4, 5: 4, 4: 3, 3: 2, 2: 1, 1: 1}


def _label(dims: dict, key: str) -> str:
    raw = dims.get(key)
    if raw not in LABELS:
        raise ValueError(f"{key} must be one of {sorted(LABELS)}, got {raw!r}")
    return raw


def _counts(dims: dict) -> tuple[int, int, int, int]:
    assessed = 0
    d = p = e = 0
    for key in SCIENTIFIC:
        lab = _label(dims, key)
        if lab == "NOT_ASSESSED":
            continue
        assessed += 1
        if lab == "DOES_NOT_MEET":
            d += 1
        elif lab == "PARTLY_MEETS":
            p += 1
        elif lab == "EXCEEDS":
            e += 1
    return assessed, d, p, e


def _from_table(d: int, p: int, e: int) -> int:
    if d >= 2:
        return 3
    if d == 1 and p >= 2:
        return 4
    if d == 1:
        return 5
    if p >= 3:
        return 5
    if p >= 1:
        return 6
    if e >= 4:
        return 9
    if e >= 2:
        return 8
    return 7


def map_score(payload: dict) -> dict:
    dims = payload["dimensions"]
    gates = {g: bool(payload.get("gates", {}).get(g, False)) for g in HARD_GATES + SOFT_GATES}
    venue = payload.get("venue", "conference_default")
    _label(dims, "clarity")
    _label(dims, "literature")

    assessed, d, p, e = _counts(dims)
    if assessed < 3:
        raise ValueError(
            f"need at least 3 assessed scientific dimensions, got {assessed}"
        )

    originality_gap = _label(dims, "originality") == "NOT_ASSESSED"
    if originality_gap and gates["G4"]:
        raise ValueError("G4 cannot fire when Originality is NOT_ASSESSED")

    hard = any(gates[g] for g in HARD_GATES)
    soft = any(gates[g] for g in SOFT_GATES)
    if hard:
        conference = 3
        row = "hard_gate"
    elif soft:
        conference = 4
        row = "soft_gate"
    else:
        conference = _from_table(d, p, e)
        row = f"D={d},P={p},E={e}"

    clarity_penalty = _label(dims, "clarity") == "DOES_NOT_MEET"
    if clarity_penalty:
        conference = max(1, conference - 1)

    if conference <= 3:
        journal = "Reject"
    elif conference == 4:
        journal = "Reject" if soft else "Major revision"
    elif conference == 5:
        journal = "Major revision"
    elif conference in (6, 7):
        journal = "Minor revision"
    else:
        journal = "Accept"

    if venue == "tmlr":
        if journal == "Major revision":
            presentation_only = clarity_penalty and d == 0 and not hard and not soft
            journal = "Accept with minor revision" if presentation_only else "Reject"
        elif journal == "Minor revision":
            journal = "Accept with minor revision"
        elif journal == "Accept":
            journal = "Accept as is"

    result = {
        "conference_score": conference,
        "verbal": VERBAL[conference],
        "journal": journal,
        "row": row,
        "D": d,
        "P": p,
        "E": e,
        "assessed": assessed,
        "clarity_penalty": clarity_penalty,
        "provisional": originality_gap or assessed < 5,
        "calibration": "NOT_CALIBRATED",
        "venue": venue,
    }
    if venue == "neurips2025":
        result["neurips2025_score"] = NEURIPS2025[conference]
    return result


def _self_check() -> None:
    def run(dims, gates=None, venue="conference_default"):
        return map_score({"dimensions": dims, "gates": gates or {}, "venue": venue})

    base = {k: "MEETS" for k in (*SCIENTIFIC, "literature", "clarity")}
    assert run(base)["conference_score"] == 7
    two_ex = dict(base, originality="EXCEEDS", soundness="EXCEEDS")
    assert run(two_ex)["conference_score"] == 8
    four_ex = dict(two_ex, evidence="EXCEEDS", experiments="EXCEEDS")
    assert run(four_ex)["conference_score"] == 9
    assert run(dict(base, originality="PARTLY_MEETS"))["conference_score"] == 6
    assert run(dict(base, clarity="DOES_NOT_MEET"))["conference_score"] == 6
    assert run(base, {"G1": True})["conference_score"] == 3
    assert run(base, {"G3": True})["conference_score"] == 4
    dn = dict(base, originality="DOES_NOT_MEET", soundness="DOES_NOT_MEET")
    assert run(dn)["conference_score"] == 3
    assert run(base, venue="tmlr")["journal"] == "Accept with minor revision"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", help="JSON file; stdin if omitted")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        _self_check()
        print("ok")
        return 0
    raw = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    out = map_score(json.loads(raw))
    json.dump(out, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
