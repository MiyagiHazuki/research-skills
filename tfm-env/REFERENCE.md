# TFM Environment Reference (verified 2026-09-29)

Tabular Foundation Model local environment on this machine. Two model families:

1. **TabPFN** — Prior Labs, package `tabpfn` 9.0.0 (model generations v2, v2.5, v2.6, v3, v3.5, v3.5-fast)
2. **TabICL** — soda-inria / jingang, package `tabicl` 2.2.0 (model generations v1.1 and v2)

The previous `mt3` env (Python 3.10, tabpfn 8.2.0, tabicl 2.1.1) no longer exists.

---

## 1. Runtime environment

| Item | Value |
|---|---|
| Primary conda env | `tfm-env` → `C:\ProgramData\miniconda3\envs\tfm-env\python.exe` |
| Python | 3.12.14 (conda-forge, MSC v.1944 64-bit) |
| torch | 2.14.0+cu130, CUDA 13.0 available |
| GPU | NVIDIA GeForce RTX 4080 SUPER, 32 760 MiB, driver 610.47 |
| Isolation | `PYTHONNOUSERSITE=1` set via `conda env config vars` |
| Core packages | `tabpfn 9.0.0`, `tabicl 2.2.0`, `huggingface-hub 1.31.0` |
| Tooling | `pandas 3.0.5`, `matplotlib 3.11.2`, `scikit-learn 1.9.1`, `scipy 1.18.1`, `seaborn 0.13.2`, `pyarrow 25.0.1`, `openpyxl 3.1.5`, `statsmodels 0.15.0` |
| Baselines / shap | `xgboost 3.4.1`, `catboost 1.2.10`, `lightgbm 4.7.0`, `shap 0.52.0`, `shapiq 1.7.0` |
| Added by tabpfn 9.0.0 | `skrub 0.10.1`, `pydot 4.0.1` (new direct deps) |

Activate: `conda activate tfm-env`

Created with conda-forge Python only; all remaining packages installed via pip (`--no-user`). Torch from `https://download.pytorch.org/whl/cu130`.

### Environment caveats

- `PYTHONNOUSERSITE=1` blocks user-level site-packages (`AppData\Roaming\Python\...`) from leaking into this env.
- No other conda env has `tabpfn` or `tabicl`.

---

## 2. TabPFN — weight storage

Cache dir logic (tabpfn `model_loading.get_cache_dir`): on Windows → `%APPDATA%\tabpfn`
(override with `settings.tabpfn.model_cache_dir`).

**All 10 weight files are downloaded locally** at `C:\Users\WU yat-fan\AppData\Roaming\tabpfn\`:

| File | Size (MB) | HF repo |
|---|---|---|
| `tabpfn-v2-classifier-finetuned-zk73skhh.ckpt` | 27.7 | `Prior-Labs/TabPFN-v2-clf` |
| `tabpfn-v2-regressor.ckpt` | 42.3 | `Prior-Labs/TabPFN-v2-reg` |
| `tabpfn-v2.5-classifier-v2.5_default.ckpt` | 40.9 | `Prior-Labs/tabpfn_2_5` |
| `tabpfn-v2.5-regressor-v2.5_default.ckpt` | 38.9 | `Prior-Labs/tabpfn_2_5` |
| `tabpfn-v2.6-classifier-v2.6_default.ckpt` | 41.1 | `Prior-Labs/tabpfn_2_6` |
| `tabpfn-v2.6-regressor-v2.6_default.ckpt` | 49.2 | `Prior-Labs/tabpfn_2_6` |
| `tabpfn-v3-classifier-v3_default.ckpt` | 202.9 | `Prior-Labs/tabpfn_3` |
| `tabpfn-v3-regressor-v3_default.ckpt` | 222.5 | `Prior-Labs/tabpfn_3` |
| `tabpfn-v3.5-20260909.safetensors` | 876.0 | `Prior-Labs/tabpfn_3_5` |
| `tabpfn-v3.5-20260909_multiclass.safetensors` | 876.0 | `Prior-Labs/tabpfn_3_5` |

NOT downloaded: `tabpfn-v3.5-fast-20260909.safetensors` (`ModelVersion.V3_5_FAST`, same repo).

**v3.5 architecture change**: from v3.5 on, one multitask checkpoint carries both the classification
and the regression head — there are no separate classifier/regressor files, and the format switched
from `.ckpt` (torch pickle) to `.safetensors`.

### v3.5 license gate and how it was bypassed (verified 2026-09-29)

`tabpfn ≥ 9.0.0` inserts a one-time license flow (`TabPFNLicenseError`) into its **download path**:
it wants a `TABPFN_TOKEN` API key from https://ux.priorlabs.ai (register → Licenses tab → accept →
copy key from /account → `export TABPFN_TOKEN=...`). Token cache order: env var →
`~/.cache/tabpfn/auth_token` → `~/.tabpfn/token` (none present on this machine).

However, the HF repo `Prior-Labs/tabpfn_3_5` is **public** (`gated: false`, license
`tabpfn-3-5-license-v1.0`: research + internal evaluation allowed, no commercial use), so the
weights were fetched directly, no account needed:

```python
from huggingface_hub import hf_hub_download
from tabpfn.model_loading import get_cache_dir

hf_hub_download(
    repo_id="Prior-Labs/tabpfn_3_5",
    filename="tabpfn-v3.5-20260909.safetensors",  # and ..._multiclass.safetensors
    local_dir=get_cache_dir(),
)
```

Once the files exist, `download_model` short-circuits (`to.exists()` → `"ok"`) and **loading needs
no token and no network** — verified with `HF_HUB_OFFLINE=1`, no `TABPFN_TOKEN`, default
`TabPFNClassifier`/`TabPFNRegressor` fit+predict on synthetic data (clf acc 0.94, reg r2 1.0,
15-class task loads the multiclass variant fine).

Download fallback (if HF fails): `https://storage.googleapis.com/tabpfn-v2-model-files/05152025`.
Some HF repos may be gated (`TabPFNHuggingFaceGatedRepoError` → requires `hf auth login`).

### Version selection

- `model_path="auto"` (default) → TabPFN-3.5 via `settings.tabpfn.model_version`.
- Bare filename is resolved against the cache dir (`prepend_cache_path`), so
  `model_path="tabpfn-v3.5-20260909.safetensors"` or the older
  `model_path="tabpfn-v3-classifier-v3_default.ckpt"` just work offline.
- Full absolute path also accepted. Version is sniffed from the filename
  (contains `v3.5-fast` / `v3.5` / `v2.6` / `v2.5` / `v3` identifiers, else v2 —
  most specific first).
- `TabPFNClassifier.create_default_for_version(ModelVersion.V2_6)` (from
  `tabpfn.constants`) pins a generation; `ModelVersion` members:
  `V2`, `V2_5`, `V2_6`, `V3`, `V3_5`, `V3_5_FAST`.
- `tabpfn.model_loading.download_all_models(to=Path)` bulk-downloads everything
  (will hit the `TABPFN_TOKEN` license gate for v2.5+ — see the bypass note above;
  also fetches extra v3 variants and v3.5-fast this machine otherwise doesn't need).

### TabPFNClassifier key parameters (verified signature, 9.0.0)

```python
from tabpfn import TabPFNClassifier
from tabpfn.constants import ModelVersion

clf = TabPFNClassifier(
    n_estimators="auto",                # ensemble size; checkpoint may declare its own
    categorical_features_indices=None,  # indices of categorical columns
    model_path="auto",                  # ckpt filename / path / list for ensembling
    device="auto",                      # picks CUDA
    ignore_pretraining_limits=False,    # True to bypass 10K rows / 500 cols limits
    fit_mode="fit_preprocessors",       # 'low_memory'|'fit_preprocessors'|'fit_with_cache'|'batched'
    memory_saving_mode="auto",          # offloads inference for big data
    random_state=0,
)
# 9.0.0 additions: softmax_temperature now defaults to "auto" (use the checkpoint's
# trained value; v3.5 files carry one); inference_config={"TRANSFORM_DATES": True /
# "TRANSFORM_TEXT": True} opt-in date/text column expansion (skrub StringEncoder).

# pin an older generation
clf = TabPFNClassifier.create_default_for_version(ModelVersion.V2_6)
```

`TabPFNRegressor` mirrors this (plus regression-specific defaults). Persistence:
`tabpfn.save_fitted_tabpfn_model(model, path)` / `tabpfn.load_fitted_tabpfn_model(path)`.

Public API surface (8.5.0): `TabPFNClassifier`, `TabPFNRegressor`, `save_fitted_tabpfn_model`,
`load_fitted_tabpfn_model`, `display_debug_info`, plus errors `TabPFNCUDAOutOfMemoryError`,
`TabPFNMPSOutOfMemoryError`. `tabpfn-common-utils` is no longer a separate installed package.

---

## 3. TabICL — weight storage

Downloads via `huggingface_hub.hf_hub_download` into the default HF hub cache:
`C:\Users\WU yat-fan\.cache\huggingface\hub\`. HF repo: `jingang/TabICL`
(https://huggingface.co/jingang/TabICL).

| Checkpoint | Size (MB) | Local path |
|---|---|---|
| `tabicl-classifier-v2-20260212.ckpt` | 109.0 | `...hub\models--jingang--TabICL\snapshots\4dcd344ece2c00be9e831fdd35bed57b5ad83e19\` |
| `tabicl-regressor-v2-20260212.ckpt` | 105.3 | same snapshot dir |
| `tabicl-classifier-v1.1-0506.ckpt` | 103.3 | `...hub\models--jingang--TabICL-clf\snapshots\eaf789a9b25ee8486d6f48997ba076f850bbc30b\` |

Actual bytes live under each repo's `blobs\` dir; `snapshots\` entries are 0-byte links.
To pin a checkpoint offline, pass `model_path=<absolute path to snapshot file>`.

### Version selection

- `checkpoint_version="tabicl-classifier-v2-20260212.ckpt"` (classifier default)
- `checkpoint_version="tabicl-regressor-v2-20260212.ckpt"` (regressor default)
- `checkpoint_version="tabicl-classifier-v1.1-0506.ckpt"` (v1.1 classifier)

### TabICLClassifier key parameters (verified signature, 2.2.0)

```python
from tabicl import TabICLClassifier
clf = TabICLClassifier(
    n_estimators=8,
    norm_methods=None,
    outlier_threshold=4.0,
    softmax_temperature=0.9,
    batch_size=8,                       # inference context batching
    kv_cache=False,                     # str|bool; enable KV-cache reuse for repeats
    model_path=None,                    # override checkpoint location
    allow_auto_download=True,           # False → offline-only, raises if missing
    checkpoint_version="tabicl-classifier-v2-20260212.ckpt",
    device=None,                        # None → auto (CUDA)
    use_amp="auto",                     # mixed precision
    use_fa3="auto",                     # FlashAttention-3 when available
    offload_mode="auto",                # CPU-offload for large contexts
    random_state=42,
)
```

`TabICLRegressor` is the same minus classifier-only params (`support_many_classes`,
`class_shuffle_method`, `average_logits`). Top-level public names in 2.2.0:
`TabICLClassifier`, `TabICLRegressor`, `InferenceConfig`.

Notes:

- Context-window model: best in-context performance when train set is subsampled to a few
  thousand rows (it re-estimates `n_estimators` times with different shuffles).
- `tabicl 2.2.0` exposes no `__version__`; use
  `from importlib.metadata import version; version("tabicl")`.

---

## 4. Cross-model comparison cheat sheet

| | TabPFN 9.0.0 | TabICL 2.2.0 |
|---|---|---|
| Vendor | Prior Labs | soda-inria / jingang |
| Generations available | v2, v2.5, v2.6, v3, v3.5 (+v3.5-fast, weights not local) | v1.1, v2 |
| Default model | `auto` (TabPFN-3.5, multitask ckpt) | v2-20260212 |
| Weight cache | `%APPDATA%\tabpfn` | HF hub cache |
| Row/col limits (v2) | 10 000 × 500 (`ignore_pretraining_limits` to bypass) | context-window bound, subsample train |
| Random state default | 0 | 42 |
| Persistence | `save/load_fitted_tabpfn_model` | joblib/pickle on estimator |

## 5. Maintenance commands

```powershell
# Verify everything (envs + weights + GPU + classifier construct)
conda activate tfm-env
python "C:\Users\WU yat-fan\.agents\skills\tfm-env\scripts\check_env.py"

# List TabPFN local weights
Get-ChildItem "$env:APPDATA\tabpfn" -Filter *.ckpt | Select Name, @{N='MB';E={[math]::Round($_.Length/1MB,1)}}

# List TabICL blobs (real bytes)
Get-ChildItem "$env:USERPROFILE\.cache\huggingface\hub\models--jingang--TabICL*\blobs" -Recurse -File
```
