# ⚡ Method Quick-Reference Matrix

[Catalog](../README.md) · [Reading order](reading-order.md) · [Key equations](key-equations.md) · [Benchmarks](benchmarks.md) · [Codebases](codebases.md)

Compare methods by the states they supervise, the information used to construct targets, and the update they apply. The rows below describe mechanisms and prerequisites. Published results use different models, initializations, budgets, and evaluation protocols, so they do not form a common speed or accuracy ranking. The [survey](https://arxiv.org/abs/2604.00626) develops these comparisons across objectives, supervision, and training dynamics.

## Distribution matching and update design

| Method | Update or target | State and supervision requirements | What to check |
|---|---|---|---|
| [GKD](https://arxiv.org/abs/2306.13649) | Conditional forward KL, reverse KL, or generalized JSD | Teacher distributions on student-generated or fixed-data prefixes, with a configurable sampling mixture | Prefix source and divergence are separate choices; preferences vary by task. |
| [MiniLLM](https://arxiv.org/abs/2306.08543) | Sequence reverse KL with future-return estimation and variance controls | Teacher likelihoods and a stabilized student-sampling procedure | Its main evaluation is instruction following; distinguish the ideal gradient from teacher-mixed sampling, length normalization, and other stabilizers. |
| [DistiLLM](https://arxiv.org/abs/2402.03898) | Skewed KL and skewed reverse KL | Teacher logits and adaptive reuse of student-generated outputs | Reuse saves collection work while changing policy freshness; a skewed divergence is not necessarily symmetric. |
| [EOPD](https://arxiv.org/abs/2603.07079) | Reverse KL plus entropy-gated top-*K* forward KL | Sampled-token teacher probabilities, teacher entropy, and teacher top-*K* alternatives | Reverse KL remains active at high-entropy positions; the forward term is added there. |
| [AOPD](https://arxiv.org/abs/2605.06387) | Sampled policy-gradient updates at positive-advantage tokens; top-*K* forward guidance at non-positive tokens | Teacher–student probability gaps and alternative teacher-supported tokens | The method changes the update and its support, rather than only applying a scalar weight. |
| [G-OPD](https://arxiv.org/abs/2602.12125) | Teacher-to-reference log-ratio reward with a KL penalty to the reference; scaling extrapolates the target | Teacher and reference probabilities | The reward is an implicit policy contrast. Exceeding the teacher is an empirical result in evaluated settings, not a guarantee of distillation or evidence of an independent verifier reward. |

## Constructing a self-teacher

| Method | Information used for supervision | What remains necessary |
|---|---|---|
| [OPSD](https://arxiv.org/abs/2601.18734) | Ground-truth answer conditions a self-teacher on the student's prefixes | A useful answer-conditioned distribution; sharing weights does not remove the teacher–student information gap. |
| [SD-ZERO](https://arxiv.org/abs/2604.12002) | A learned reviser uses generator outputs and binary correctness feedback | Verifiable outcomes, reviser learning, and the cost of constructing revisions. |
| [SDPO](https://arxiv.org/abs/2601.20802) | Errors, tests, or judge feedback condition a self-teacher | Feedback that the self-teacher can use; text feedback is context for constructing a distribution, not automatically the distillation target itself. |
| [UniSD](https://arxiv.org/abs/2605.06597) | Teacher-view agreement alongside contrastive and representation supervision, EMA stabilization, and divergence clipping | Multiple teacher evaluations and validation of the combined mechanisms; agreement is not external verification. |

## Selection, reuse, and multi-turn learning

| Method | What changes | Evidence boundary or cost |
|---|---|---|
| [TIP](https://arxiv.org/abs/2604.14084) | Selects positions using student entropy and teacher–student divergence, including confident disagreement | Retention ratios are model- and task-dependent. Selecting a loss mask does not automatically reduce rollout generation. |
| [SCOPE](https://arxiv.org/abs/2604.10688) | Correctness routes rollouts to teacher-perplexity-weighted distillation or student-perplexity-weighted likelihood training | Requires outcome labels. The distinction is between incorrect and correct trajectories, not top-entropy tokens or two KL directions. |
| [Lightning-OPD](https://arxiv.org/abs/2604.13010) | Precomputes teacher probabilities on fixed trajectories for student-only optimization | Its offline approximation assumes teacher consistency and controlled discrepancy from online training. Acquisition and initial scoring remain costs. |
| [CLOOPD](https://arxiv.org/abs/2609.24141) | Reuses responses, teacher scores, and frozen advantages across proximal actor passes | Its evaluated three-pass setting reduces teacher-scored tokens and GPU-hours by different amounts; additional reuse is not uniformly better. |
| [Uni-OPD](https://arxiv.org/abs/2605.03677) | Couples difficulty and correctness balancing with outcome-guided margin calibration | Sampling allocation and teacher-score calibration contribute together in the tested pipeline. |
| [SOD](https://arxiv.org/abs/2605.07725) | Recursively weights tool-bounded distillation steps alongside GRPO; masks observation tokens | Evidence concerns Python-tool reasoning, not arbitrary long-horizon environments. |
| [MemOPD](https://arxiv.org/abs/2608.07068) | Reconstructs compact-memory invocation states before teacher scoring | Requires matching visibility, positions, and valid action masks; tested with a shared tokenizer. |

## Interfaces and related pipelines

| Method or report | Why it is a useful comparison | Boundary |
|---|---|---|
| [DSKD](https://arxiv.org/abs/2504.11426) | Projects representations into teacher and student spaces to construct comparable outputs | Projection and exact token alignment solve different problems; cross-tokenizer supervision is restricted to aligned positions. |
| [SimCT](https://arxiv.org/abs/2605.07711) | Compares short continuation units realizable by both tokenizers | The continuation interface must be defined before applying a divergence. |
| [GAD](https://arxiv.org/abs/2511.10643) | Uses teacher responses to train a discriminator that supplies a scalar reward | This is teacher-mediated optimization with a learned evaluator, rather than direct teacher-logit matching. |
| [Qwen3](https://arxiv.org/abs/2505.09388) | Off-policy initialization followed by on-policy refinement | Reported student-stage costs do not include the whole teacher-preparation pipeline. |
| [DeepSeek-V4](https://arxiv.org/abs/2606.19348) | Specialist consolidation through full-vocabulary multi-teacher OPD | A deployment recipe with additional engineering and teacher preparation; overall scores do not isolate OPD's effect. |

## Choosing candidates under a measured constraint

| Available information or bottleneck | Candidate comparison | What the comparison must include |
|---|---|---|
| Compatible teacher logits | GKD or MiniLLM, then an objective or estimator variant | The same initial student, prefix source, support, and evaluation budget. |
| Teacher text but no compatible logits | GAD, plus a teacher-trace baseline | Demonstration acquisition, evaluator costs, and the actual training-state distribution. |
| No separate stronger teacher | OPSD, SDPO, or SD-ZERO | The source of answers, feedback, or revisions and a control without that information. |
| Teacher scoring is expensive | DistiLLM, Lightning-OPD, or CLOOPD | Cached-data acquisition, score reuse, current-student computation, and loss from stale or restricted state coverage. |
| Dense supervision exceeds memory | TIP or a supported sparse estimator | Peak memory and end-to-end time at matched quality; retained positions alone are not a compute measurement. |
| Multi-turn state mismatch | SOD or MemOPD, depending on whether weighting or invocation reconstruction is the problem | Environment calls, observation masking, memory visibility, and final task success. |
| Several expert capabilities to retain | Multi-teacher consolidation and matched merging or pooled-RL controls | Per-domain retention and the cost of obtaining all experts; see the [controlled consolidation study](https://arxiv.org/abs/2608.27409). |

There is no source-backed GPU-hour threshold that selects one pipeline for every model. Measure teacher preparation, student generation, teacher scoring, student updates, and any later RL stage separately. Hardware, sequence lengths, teacher placement, and the required inference budget can change which stage dominates. The [benchmark guide](benchmarks.md) gives examples of the resulting measurement distinctions.
