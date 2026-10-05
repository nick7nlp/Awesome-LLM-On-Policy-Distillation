# Contributing

Please include the paper identifier, exact version, and primary source supporting
a correction or addition.

## Update a record

The public source of truth is [resources/catalog.json](resources/catalog.json).
Edit its record, then run `python3 scripts/build_catalog.py` to regenerate the
README, code index and objective index. Do not edit only a generated duplicate.

Records contain the title, ordered authors, first-release date, canonical paper
URL, concise mechanism description, objective, evidence role, reading section,
and verified repository links. Use official paper or publisher metadata.

## Inclusion

The focus is teacher-derived learning on states visited by an evolving language-model
student. Direct OPD, mixed/replayed distillation, teacher-mediated RL, analyses,
and applications have distinct roles. Necessary foundations and off-policy
comparators belong in background. An OPD title is not sufficient for inclusion.

Evaluate relevance, support for the proposed contribution, information value and
checkability separately. Brief entries meet the same reliability bar. Reputation,
affiliation, venue, popularity and positive results cannot replace evidence.
Negative findings and simple methods can qualify. Identify unresolved evidence.

## Descriptions and links

- Describe who generates the states, what supervision is available, and how it enters the update.
- Do not infer a KL direction from the method name.
- Use one or two sentences; preserve limitations that change the interpretation.
- Avoid universal speedups, correctness guarantees and cross-paper performance rankings.
- A working code URL must also be associated with the paper. Prefer the canonical repository after a move.
- Keep code links empty when no paper-specific repository has been verified.
- Keep internal reviews, credentials and operational logs out of public records.

## Reading sections

| Home | Question |
|---|---|
| 4 | Objectives, gradients and reward coupling |
| 5 | Teacher information, feedback, composition and interfaces |
| 6 | Coverage, selection, refresh, lifecycle and compute |
| 7 | Multi-turn states, memory, credit and intervention |
| 8 | Mechanisms, diagnostics, failures and evaluation |
| 9 | Applications and system reports |
| background | Foundations, software and explicit comparators |

A home is a reading guide, not a mutually exclusive scientific category.
