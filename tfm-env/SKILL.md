---
name: tfm-env
description: Local environment reference for Tabular Foundation Models (TabPFN and TabICL) on this machine. Stores weight file locations, conda environment, invocation snippets, and version-selection details. Use when writing or running code that imports tabpfn / tabicl, when training or evaluating tabular foundation models, or when user mentions TabPFN, TabICL, TFM, or tabular foundation models.
---

# TFM Environment (TabPFN + TabICL)

All facts below were verified on this machine. Full details: [REFERENCE.md](REFERENCE.md).

## Quick start

```powershell
conda activate tfm-env   # the ONLY env with both tabpfn 9.0.0 and tabicl 2.2.0
```

The env has `PYTHONNOUSERSITE=1` so user-level `pip --user` installs cannot leak in.

```python
# TabPFN (Prior Labs) — sklearn API
from tabpfn import TabPFNClassifier, TabPFNRegressor
clf = TabPFNClassifier()                       # model_path="auto", weights load from local cache
clf.fit(X_train, y_train)                      # pandas DataFrame / numpy, no preprocessing needed
proba = clf.predict_proba(X_test)

# TabICL (soda-inria / jingang) — sklearn API
from tabicl import TabICLClassifier, TabICLRegressor
clf = TabICLClassifier()                       # defaults to v2-20260212 checkpoint (cached)
clf.fit(X_train, y_train)
proba = clf.predict_proba(X_test)
```

Both run on the RTX 4080 SUPER (32 GB) with `device="auto"` — no code changes needed for GPU.

## Weight storage (verified locations)

| Model | Location | Status |
|---|---|---|
| TabPFN v2 / v2.5 / v2.6 / v3 (8 ckpts) + v3.5 (2 safetensors) | `C:\Users\WU yat-fan\AppData\Roaming\tabpfn\` | ALL downloaded |
| TabICL v2 clf + reg | `C:\Users\WU yat-fan\.cache\huggingface\hub\models--jingang--TabICL\` | downloaded |
| TabICL v1.1 clf | `C:\Users\WU yat-fan\.cache\huggingface\hub\models--jingang--TabICL-clf\` | downloaded |

Exact filenames and sizes: see [REFERENCE.md](REFERENCE.md).

## Selecting model versions

- **TabPFN**: pass a bare checkpoint filename to `model_path` (resolved against the cache dir), e.g.
  `TabPFNClassifier(model_path="tabpfn-v2.5-classifier-v2.5_default.ckpt")`. Default `"auto"` (TabPFN-3.5, one
  multitask checkpoint for both clf and reg).
  Or `TabPFNClassifier.create_default_for_version(ModelVersion.V2_6)` from `tabpfn.constants`
  (`V3_5`, `V3_5_FAST` also exist; `v3.5-fast` weights are NOT downloaded locally).
- **TabICL**: pass `checkpoint_version=`, e.g. `"tabicl-classifier-v1.1-0506.ckpt"` for v1.1.
  Default is `"tabicl-classifier-v2-20260212.ckpt"`.

## Gotchas

- Use the **tfm-env** conda env. The old `mt3` env no longer exists.
- `tabicl` has no `__version__` attribute; get the version via `importlib.metadata.version("tabicl")`.
- First run in a fresh env auto-downloads weights (TabPFN → `%APPDATA%\tabpfn`, TabICL → HF hub cache)
  unless `allow_auto_download=False` / offline. Sizes: TabICL ~105 MB per checkpoint, TabPFN v3 ~210–220 MB,
  **TabPFN v3.5 ~876 MB per checkpoint**.
- **tabpfn ≥ 9.0.0 download gate**: the package's own download path demands a one-time license flow
  (`TABPFN_TOKEN` from https://ux.priorlabs.ai). The HF repo `Prior-Labs/tabpfn_3_5` is **public**
  (`gated=false`), so weights can be fetched directly with
  `hf_hub_download(repo_id="Prior-Labs/tabpfn_3_5", filename=..., local_dir=get_cache_dir())`;
  once the files exist locally, loading needs **no token and no network** (verified).
- Neither package accepts raw text columns — encode categoricals first (TabPFN: `categorical_features_indices`;
  9.0.0 can also expand text/date columns via `inference_config={"TRANSFORM_TEXT": True}` opt-in).

## Verify installation

```powershell
conda activate tfm-env
python "C:\Users\WU yat-fan\.agents\skills\tfm-env\scripts\check_env.py"
```
