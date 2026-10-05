# 📚 Recommended Reading Order

[Catalog](../README.md) · [Method comparison](method-comparison.md) · [Key equations](key-equations.md) · [Benchmarks](benchmarks.md) · [Codebases](codebases.md)

Start with how student-generated states receive supervision, then compare the objective, the teacher's information, and the training schedule. The paths below follow the survey's three coupled design dimensions. Method papers, diagnostic studies, and deployment reports answer different questions; a successful system does not isolate the effect of its distillation stage. See the [survey](https://arxiv.org/abs/2604.00626) for scope and detailed comparisons.

## 1. Foundations

1. **[GKD](https://arxiv.org/abs/2306.13649)** introduces conditional divergence matching on student-generated sequences, with an explicit mixture of student and fixed-data trajectories. Read the formulation and sampling algorithm together. Its experiments use several divergences and find task-dependent preferences.
2. **[MiniLLM](https://arxiv.org/abs/2306.08543)** develops sequence-level reverse-KL optimization, including future returns and practical variance controls. It provides an instruction-following comparison, rather than a rule that reverse KL is best for every reasoning task.
3. **[DistiLLM](https://arxiv.org/abs/2402.03898)** couples skewed divergences with adaptive reuse of student-generated outputs. It connects loss design to the cost and freshness of training data.

For a short introduction, read GKD, MiniLLM, and **[Rethinking OPD](https://arxiv.org/abs/2604.13016)** before choosing a specialized method.

## 2. Objectives and supervision

4. **[Entropy-Aware OPD (EOPD)](https://arxiv.org/abs/2603.07079)** keeps reverse-KL supervision throughout and adds top-*K* forward-KL guidance where teacher entropy is high. The two terms can act at the same position; this is not a mutually exclusive direction switch.
5. **[OPSD](https://arxiv.org/abs/2601.18734)** uses an answer-conditioned self-teacher to supervise the problem-only student's prefixes. Read it for the distinction between shared model parameters and different information access. It still requires useful privileged information.
6. **[SDPO](https://arxiv.org/abs/2601.20802)** turns structured errors, failed tests, or judge feedback into a self-teacher context. The feedback provider and the model that produces the matched distribution need not be the same system.
7. **[SD-ZERO](https://arxiv.org/abs/2604.12002)** trains a Generator–Reviser pair that converts binary correctness feedback into revision-conditioned dense supervision. The absence of a separate stronger teacher does not remove feedback or reviser-training costs.

## 3. Selection, reuse, and interaction

8. **[TIP](https://arxiv.org/abs/2604.14084)** compares student entropy with teacher–student divergence. Its key distinction is that low-entropy, high-disagreement positions can carry useful supervision that entropy-only selection misses. Reported retention ratios are experimental settings, not universal prescriptions.
9. **[SCOPE](https://arxiv.org/abs/2604.10688)** routes incorrect rollouts to teacher-perplexity-weighted distillation and correct rollouts to student-perplexity-weighted likelihood training. Its pass@32 evaluation complements mean accuracy; the two paths are defined by correctness, not by a forward/reverse-KL split.
10. **[Lightning-OPD](https://arxiv.org/abs/2604.13010)** precomputes teacher probabilities on fixed trajectories and removes live teacher inference from student optimization. Read its teacher-consistency assumptions and acquisition-cost breakdown alongside its reported efficiency results.
11. **[Uni-OPD](https://arxiv.org/abs/2605.03677)** combines difficulty and correctness balancing with outcome-guided calibration of teacher scores. It is useful for studying how prompt allocation and signal reliability interact.
12. **[SOD](https://arxiv.org/abs/2605.07725)** weights distillation at tool-call boundaries alongside GRPO, excluding observation tokens from the loss. Its evidence concerns Python-tool reasoning. Pair it with **[MemOPD](https://arxiv.org/abs/2608.07068)** for a different interaction problem: reconstructing the student's actual memory and invocation state before teacher scoring.

## 4. Mechanisms, failures, and evaluation

13. **[Rethinking OPD](https://arxiv.org/abs/2604.13016)** studies reasoning-pattern compatibility and the teacher's additional capabilities in mathematical reasoning. Top-*k* overlap is a diagnostic in those experiments, not a universal necessary-and-sufficient test for transfer.
14. **[Revisiting OPD](https://arxiv.org/abs/2603.25562)** separates sampled-token signal imbalance, unreliable teacher guidance, and tokenizer or special-token mismatch. Read its component ablations before attributing the full improvement to support matching.
15. **[CaOPD](https://arxiv.org/abs/2604.16830)** distinguishes confidence justified by privileged teacher information from confidence justified by the deployed student's information. Its calibration procedure uses student rollouts and explicit confidence-bearing supervision.
16. **[On the Geometry of OPD](https://arxiv.org/abs/2606.07082)** examines early concentration of cumulative updates. **[Dense Supervision, Sparse Updates](https://arxiv.org/abs/2606.13657)** studies coordinate sparsity and feed-forward-layer concentration. Effective subspace concentration, coordinate sparsity, and numerical rank are different properties; neither study establishes that concentrated updates guarantee preserved capabilities.
17. **[On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity](https://arxiv.org/abs/2606.26091)** compares pass@1 with multi-sample coverage under demonstration-conditioned self-distillation. Its theoretical assumptions and empirical EMA-teacher setup should be read separately.

## 5. Deployment and useful comparators

18. **[Qwen3](https://arxiv.org/abs/2505.09388)** describes off-policy initialization followed by on-policy refinement of smaller students. **[DeepSeek-V4](https://arxiv.org/abs/2606.19348)** describes multi-teacher consolidation with full-vocabulary supervision. These reports show how OPD fits into larger training pipelines; their overall scores are not isolated OPD effects.
19. **[DeepSeek-R1](https://arxiv.org/abs/2501.12948)** and **[Gemma 2](https://arxiv.org/abs/2408.00118)** provide off-policy comparators: teacher-trace transfer and distillation during pretraining, respectively. They help test whether a proposed on-policy stage adds value over a suitable fixed-data baseline.

## Paths by research question

| Question | Suggested path |
|---|---|
| What does the update actually optimize? | GKD → MiniLLM → EOPD → [Key equations](key-equations.md) |
| What information makes a self-teacher useful? | OPSD → SDPO → SD-ZERO → CaOPD |
| Which costs can be reduced? | DistiLLM → TIP → Lightning-OPD → [CLOOPD](https://arxiv.org/abs/2609.24141), which reports teacher-token, actor-token, and GPU-hour costs separately |
| How does interaction change supervision? | SOD → MemOPD → [Revisiting DAgger for LLM Agents](https://arxiv.org/abs/2605.12913), which studies teacher intervention and action labeling |
| What can improve while something else degrades? | Rethinking OPD → SCOPE → CaOPD → the sampled-demonstration diversity study → [Benchmarks](benchmarks.md) |

These are routes through mechanisms and evidence. Use the [method comparison](method-comparison.md) to narrow candidates under a particular supervision interface and measured resource constraint.
