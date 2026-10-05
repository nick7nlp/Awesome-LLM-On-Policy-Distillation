# 📊 Benchmarks and Evaluation

[Catalog](../README.md) · [Reading order](reading-order.md) · [Method comparison](method-comparison.md) · [Key equations](key-equations.md)

OPD papers evaluate different combinations of accuracy, solution coverage, calibration, retention, and cost. The examples below locate evaluations in surveyed papers. They are neither a frequency census nor a leaderboard of results obtained under a shared protocol. The [survey](https://arxiv.org/abs/2604.00626) discusses why these measurements must be read together.

## Benchmark examples

| Evaluation area | Benchmark or task | Examples in the surveyed literature | Details needed for comparison |
|---|---|---|---|
| Mathematical reasoning | MATH-500 | [TIP](https://arxiv.org/abs/2604.14084), [KDRL](https://arxiv.org/abs/2506.02208) | Exact problem set, answer grader, generation length, and samples per problem. |
| Competition mathematics | AIME 2024/2025; HMMT 2025 | [Lightning-OPD](https://arxiv.org/abs/2604.13010), [Uni-OPD](https://arxiv.org/abs/2605.03677) | Competition year and session, benchmark packaging, and whether the metric is average success or any-success pass@*k*. |
| Arithmetic reasoning | GSM8K | [GKD](https://arxiv.org/abs/2306.13649) | Reasoning format, calculator access, decoding, and training split. |
| Code generation | LiveCodeBench | [Lightning-OPD](https://arxiv.org/abs/2604.13010) reports v5 and v6; [Uni-OPD](https://arxiv.org/abs/2605.03677) reports v6 | Release and date window, test execution, sample count, and generation budget. |
| Function-level code | HumanEval+; MBPP+ | [Uni-OPD](https://arxiv.org/abs/2605.03677) | The “+” test suite, execution limits, and treatment of invalid code. |
| Broad knowledge and science | MMLU; MMLU-Pro; GPQA-Diamond | [GKD](https://arxiv.org/abs/2306.13649) includes MMLU; [ORBIT](https://arxiv.org/abs/2601.08310) includes MMLU-Pro and GPQA-Diamond | Benchmark variant, response format, thinking mode, and token budget. |
| Summarization and translation | XSum; WMT English-to-German | [GKD](https://arxiv.org/abs/2306.13649) | ROUGE or BLEU configuration and decoding; these evaluations should not be collapsed into a reasoning-accuracy average. |
| Agentic planning | DeepPlanning | [TIP](https://arxiv.org/abs/2604.14084) | Planning constraints and environment or tool access, in addition to final success. |
| Software-engineering interaction | SWE-bench Verified | [Revisiting DAgger for LLM Agents](https://arxiv.org/abs/2605.12913) | Agent harness, tool permissions, task subset, and execution-based resolution. |
| Confidence and tool use | Science Q&A and Tool Use evaluations | [CaOPD](https://arxiv.org/abs/2604.16830) | Confidence format, calibration bins, correctness definition, and the cost of empirical confidence targets. |

## What to report alongside task accuracy

- **Mean success and solution coverage.** State whether Avg@*k* averages correctness across *k* samples or the paper uses another convention. Pass@*k* measures whether a successful solution is obtained within a sampling budget and should be accompanied by the sampling and estimation protocol. SCOPE reports both Avg@32 and pass@32; the [sampled-demonstration study](https://arxiv.org/abs/2606.26091) shows why competitive pass@1 need not preserve multi-sample coverage.
- **Length, termination, and validity.** Report generated tokens, truncation, stop behavior, and parseable outputs. Shorter responses can reflect useful compression or premature stopping; [termination-alignment experiments](https://arxiv.org/abs/2609.20511) show that improving stopping does not consistently improve accuracy.
- **Calibration.** Report confidence elicitation and metrics such as ECE or Brier score alongside accuracy. [CaOPD](https://arxiv.org/abs/2604.16830) studies privileged-information confidence mismatch; token entropy alone is not a calibration metric.
- **Retention across domains.** Include the starting checkpoint and earlier-domain evaluations. A [controlled consolidation comparison](https://arxiv.org/abs/2608.27409) finds small differences in aggregate scores alongside larger differences on individual benchmarks.
- **Complete costs.** Separate teacher preparation, rollout generation, teacher scoring, actor updates, environment calls, and serving-time inference. [Lightning-OPD](https://arxiv.org/abs/2604.13010) and [CLOOPD](https://arxiv.org/abs/2609.24141) reduce different parts of this accounting.

## Bounded findings from representative studies

### Selective supervision

[TIP](https://arxiv.org/abs/2604.14084) evaluates student entropy and teacher–student divergence jointly. Its mathematical experiments cover Qwen3, Llama, and Qwen2.5 pairs, and it also evaluates DeepPlanning. Entropy-based retention of half the tokens matches or improves the all-token baseline on most tested benchmarks, while more aggressive entropy-only retention can lose useful supervision. Low-entropy, high-disagreement positions provide an additional useful subset. The paper reports peak-memory savings of up to 47% for its half-token setting; this is a reported memory result, not evidence for a universal 50% compute saving or a fixed optimal token fraction.

[SCOPE](https://arxiv.org/abs/2604.10688) operates at trajectory level. Incorrect rollouts receive teacher-perplexity-weighted distillation; correct rollouts receive student-perplexity-weighted likelihood training. Its diagnostics show reduced pass@32 under some uniform-training choices and its proposed method improves both reported mean accuracy and pass@32 comparisons. These results motivate outcome-aware weighting without establishing that every OPD objective causes diversity collapse.

### Self-distillation and calibration

[OPSD](https://arxiv.org/abs/2601.18734) uses the ground-truth answer as privileged teacher context. Its reported comparisons favor OPSD at 4B and 8B while showing a small deficit to GRPO at 1.7B. This supports testing self-teacher usefulness at the actual initialization and capacity; it does not establish a parameter-count threshold or a generic gain over SFT.

[SD-ZERO](https://arxiv.org/abs/2604.12002) tests learned revision with binary correctness feedback, including comparisons that match training tokens. Its evidence concerns that Generator–Reviser construction. Binary feedback does not become dense supervision without a model capable of making useful revisions.

[CaOPD](https://arxiv.org/abs/2604.16830) replaces confidence-bearing supervision with targets derived from empirical student success rates. Its Science Q&A and Tool Use evaluations report better calibration while retaining competitive task accuracy. This result requires identifiable confidence expressions and additional rollout sampling; it does not show that all OPD-trained models share one overconfidence gap or one percentage reduction in calibration error.

### Teacher validity and diversity

[Rethinking OPD](https://arxiv.org/abs/2604.13016) studies compatible reasoning patterns and additional teacher capabilities in mathematics. Top-*k* overlap is a diagnostic for pattern compatibility in that setting. The study does not establish that increasing overlap and concentrating mass on overlap are two universal necessary conditions for successful OPD.

[Revisiting OPD](https://arxiv.org/abs/2603.25562) reports a mathematical average of 36.4 for its baseline, 41.5 for the full repair, and 40.7 for special-token masking alone. These controls prevent attributing the entire improvement to teacher-top-*K* support matching. Restricting support without the complementary changes can hurt.

The [sampled-demonstration diversity study](https://arxiv.org/abs/2606.26091) reports competitive pass@1 but lower pass@16 than GRPO in its evaluated self-distillation recipes. Its theoretical derivation assumes a frozen base teacher and demonstrations sampled from that base, whereas the empirical system uses an EMA teacher. The result is evidence about this conditioning and update mechanism, not a theorem that every on-policy method reduces solution diversity.

### Training efficiency

[Lightning-OPD, Table 2](https://arxiv.org/abs/2604.13010) reports 72 versus 20 GPU-hours at the 4B scale and 120 versus 30 GPU-hours at the 8B scale for its standard-OPD and cached comparisons. The reported ratios are 3.6× and 4.0×. The Lightning-OPD totals include rollout collection, teacher-log-probability precomputation, and student optimization. They do not establish these ratios for every teacher, hardware setup, or full teacher-and-student preparation pipeline. Fixed cached trajectories also differ from fresh current-student sampling. Its 4B code average is slightly below standard OPD in Table 1, despite an improvement in the reported mathematical average.

[CLOOPD](https://arxiv.org/abs/2609.24141) reports 67.2% fewer teacher-scored tokens and 28.0% fewer GPU-hours for its three-pass configuration at approximately matched quality, with comparable actor tokens. Its adaptive token-priced allocator does not outperform the fixed three-pass choice. These measurements concern one teacher–student pair and show why teacher-token savings and wall-clock savings are different claims.

The [controlled consolidation study](https://arxiv.org/abs/2608.27409) reports a fusion stage costing less than one-fifth of per-domain RL. Including prerequisite experts raises total cost to 1.14–1.19 times that baseline. Pipeline boundaries can therefore reverse an apparent efficiency conclusion.

## Comparisons that remain meaningful

Match the initial checkpoint, teacher and tokenizer versions, training data, feedback access, and evaluation protocol before interpreting a difference as a method effect. State which budget is matched: updates, generated tokens, teacher calls, and GPU-hours are not interchangeable. Record training-seed variation separately from repeated evaluation samples, and document checkpoint selection and any subsequent RL stage. The surveyed results support conditional comparisons; they do not support one pooled “typical OPD gain,” one overhead relative to SFT, or a universal GPU-hour budget guide.
