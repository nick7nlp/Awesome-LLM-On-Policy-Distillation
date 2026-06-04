# 📊 Benchmarks & Performance

## Commonly Used Benchmarks in OPD Papers

### Mathematical Reasoning
| Benchmark | Description | Common in |
|-----------|-------------|-----------|
| MATH-500 | Competition-level math (500 problems from MATH) | OPSD, SCOPE, TIP, EAOD, G-OPD, RLKD |
| AIME 2024/2025 | AMC/AIME competition problems | SCOPE, Lightning OPD, RLKD, TRACE |
| GSM8K | Grade school math (8.5K problems) | GKD, MiniLLM, DistiLLM, EAOD |
| HMMT 2025 | Harvard-MIT Math Tournament | TRACE |

### Code Generation
| Benchmark | Description | Common in |
|-----------|-------------|-----------|
| LiveCodeBench v6 | Real-time competitive coding | SSD, RLKD, KDRL |
| HumanEval+ | Function-level code generation | Reasoning compression methods |

### General Reasoning
| Benchmark | Description | Common in |
|-----------|-------------|-----------|
| MMLU / MMLU-Pro | Broad multitask knowledge | DistiLLM, GKD, PromptKD |
| GPQA | Graduate-level science QA | G-OPD, SCOPE, OPSD |

---

## Key Findings by Method

> These are qualitative findings reported in the papers. Refer to original papers for exact numbers.

### Token Selection (TIP, SCOPE, SelecTKD)
- Applying KD loss to only **top 20-50% high-entropy tokens** achieves parity with full-token supervision
- TIP reports **47% memory reduction** with comparable accuracy
- SCOPE shows that standard OPD **degrades Pass@k** significantly (diversity collapse), while dual-path design preserves diversity

### Self-Distillation (OPSD, SDZero, OPCD)
- OPSD: Oracle answer as privileged context yields +5-8% on MATH-500 over SFT baseline (Qwen3-4B/8B)
- OPCD: Student-as-teacher with own context produces stable gains on long-context reasoning
- SDZero: Self-revision with binary reward signal matches teacher-dependent methods on math tasks

### Adaptive Divergence (EAOD, DASD)
- EAOD: Entropy-gated mixing of FKL and RKL outperforms either fixed direction alone on mixed-task suites
- DASD: Sequence-level distribution alignment improves over uniform KL on long reasoning traces

### RL-Augmented (G-OPD, AlignDistil, RLKD)
- G-OPD: Reward extrapolation enables student to exceed teacher on in-distribution tasks
- RLKD: Combining RL with distillation outperforms either alone, especially on hard problems

### Compute Efficiency
- **Lightning OPD**: Achieves 4× speedup over standard OPD via teacher consistency + offline distillation
- **TIP**: ~50% compute savings from token selection with minimal accuracy loss
- **Standard OPD vs SFT**: Typical overhead is 3-5× due to on-policy rollout generation

---

## Calibration (CaOPD, 2604.16830)

Key finding: Standard OPD produces **severely overconfident** models.
- Models trained with vanilla OPD show ~48% overconfidence gap (accuracy 49% but confidence 97%)
- CaOPD reduces ECE by ~45% through calibration-aware training

---

## Success Conditions (Rethinking OPD, 2604.13016)

Two **necessary conditions** for OPD to succeed:
1. Top-k overlap between student and teacher distributions must increase during training
2. Student must concentrate probability mass on the overlapping tokens

When either condition fails → OPD degrades or stagnates.

---

## Diversity Collapse (SCOPE, 2604.10688)

Critical finding:
- Standard OPD dramatically improves **Pass@1** but severely harms **Pass@k** (k > 1)
- The student distribution collapses to a narrow mode around the teacher's preferred outputs
- SCOPE's dual-path design alleviates this by maintaining exploration

---

## Notes

- Most OPD papers evaluate on **Qwen2.5/Qwen3** family (1.5B-8B student, 7B-32B teacher) as of 2025-2026
- Exact numbers vary significantly by model family, dataset split, and training compute — always refer to original papers
- "Typical OPD Gain" ranges are approximate synthesis across multiple papers; not from any single controlled study
