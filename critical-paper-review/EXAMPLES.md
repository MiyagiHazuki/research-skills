# Examples

Schematic traces. Not reviews of real papers. Do not copy these quotes into a live review.

## 1. Conference paper, table row D=0 P=1 → 6 Weak accept

Venue: `conference_default`. Search ran. No gates.

Dimension vector:

```json
{
  "venue": "conference_default",
  "gates": {"G1": false, "G2": false, "G3": false, "G4": false, "G5": false, "G6": false},
  "dimensions": {
    "originality": "MEETS",
    "soundness": "MEETS",
    "evidence": "MEETS",
    "experiments": "PARTLY_MEETS",
    "significance": "MEETS",
    "literature": "MEETS",
    "clarity": "MEETS"
  }
}
```

Script output (must be reproduced by `python scripts/map_score.py`):

- `conference_score`: 6
- `verbal`: Weak accept
- `journal`: Minor revision
- `row`: `D=0,P=1,E=0`
- `provisional`: false

Letter sketch: Experiments `PARTLY_MEETS` because the headline ablation does not isolate routing from the claimed module (quote the ablation table). Originality `MEETS` after a closest-work table shows a real but bounded delta. No G4. Clarity does not raise the score.

## 2. Journal paper, TMLR overlay, hard gate G2 → 3 Reject

```json
{
  "venue": "tmlr",
  "gates": {"G1": false, "G2": true, "G3": false, "G4": false, "G5": false, "G6": false},
  "dimensions": {
    "originality": "MEETS",
    "soundness": "PARTLY_MEETS",
    "evidence": "DOES_NOT_MEET",
    "experiments": "MEETS",
    "significance": "MEETS",
    "literature": "MEETS",
    "clarity": "MEETS"
  }
}
```

G2 hit: abstract says "improves accuracy on all datasets"; Table 2 shows a drop on the largest dataset. Hard gate forces 3 regardless of the D=1 table row. TMLR journal field: Reject (TMLR has no Major revision). Do not "soften" to Accept with minor revision.

## 3. Search failure (provisional)

Originality `NOT_ASSESSED`, G4 forbidden. Other scientific dims assessed. Script sets `provisional: true`. Letter must say the literature was not independently checked. Do not fill the closest-work table from memory.

## 4. Clarity cap

All scientific dims `MEETS`, Clarity `DOES_NOT_MEET`, no gates → conference 6 (7 minus 1), journal Minor revision. A writing-only defect must not produce a 3.
