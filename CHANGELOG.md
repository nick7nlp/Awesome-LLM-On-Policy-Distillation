# Changelog

All notable additions to this collection are documented here.

## [2026-06-04, later edit]
### Restored (audit correction)
After re-deriving the OPD inclusion principle ("**student rollout in training loop** is the hard line; loss form is dictated by teacher access — black-box methods physically cannot use `D_KL(π_θ ‖ π_T)` and must fall back to reward / discriminator / preference signals"), two papers removed earlier today / on 2026-06-03 were re-audited and restored. The original removal criterion ("no teacher-distribution KL term") was too strict and conflated black-box constraint with non-OPD.
- **PBSD** (2605.05040) → §5.3.1. Algorithm 1 line *"Generate student response y_i^- ~ π_θ(·|x_i)"* sits inside the gradient loop; per-step on-policy student rollouts paired with privileged-context self-teacher y⁺ via DPO log-ratio margin. Same inclusion criterion as ROPD (2605.07396, rubric reward) and PRISM (2604.28123, MoE discriminator) — three black-box OPD patterns differing only in teacher-signal form (preference vs reward vs discriminator).
- **ORPO-Distill** (2509.25100) → §5.2. External teacher model `p` (separate from student `q_θ`); positive traces y_P sampled K=8 times offline at init (fixed-teacher equivalent of PBSD's per-step refresh from a frozen teacher); negative traces y_N sampled per outer-iter from current student q_{θ_{t-1}} with prob ϕ. ORPO loss = L_SFT + λ·log-odds margin. Original 6/03 removal note ("same family as SPIN") was wrong — SPIN's positives come from a previous student snapshot, while ORPO-Distill's come from a separate teacher model.

Net effect: paper count 168 → 170; loss taxonomy 155 → 157; Preference class becomes 2 (PBSD + ORPO-Distill); Other class drops back to 23 (still includes PRISM).

### Standing removed (re-audit confirms)
- **SuperCorrect** (2410.09008): `rollout_frequency = once-before-training` is a structural R1 fail. Black-box constraint excuses preference loss form, not batch-precomputed rollouts.
- **On-Policy SFT** (2602.13407): no teacher of any kind, signal=PI(GT) + verifier-only, NLL on student rollouts filtered by ground-truth check. Pure STaR/RFT/ReST.
- **Retaining by Doing** (2510.18874): KL is to π_θ_0 (initial-policy snapshot, ref-policy regularization) — **not** a teacher distribution. Pure RL.

## [2026-06-04]
### Removed (Preference-class audit)
- Preference-class re-audit prompted by the question *"is the Preference category really OPD?"* — three papers were classified as `Preference` by the loss-taxonomy auditor; on inspection, two are pure DPO/Bradley-Terry frameworks with no teacher-distribution distill term, same family as SPIN / IRIS / ORPO-Distill that were removed on 2026-06-03. They are removed from the Awesome List; the third is reclassified.
  - **PBSD** (2605.05040) — *Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization*. Loss is `-log σ(β · [log π_θ/π_teach(y⁺) − log π_θ/π_teach(y⁻)])`, i.e. DPO with the teacher as the reference policy. `signal_source = self`, no `D_KL(π_θ ‖ π_T)`. Hits R3 (RL-only / DPO-style with no teacher distribution distill term).
  - **SuperCorrect** (2410.09008) — *Thought Template Distillation and Self-Correction*. Loss is `L_Cross-DPO`, but `rollout_frequency = once-before-training` (batch precomputed), which hits R1 (off-policy / self-play, no rollout in the loss loop). The 2026-06-03 re-confirmation that restored this paper was a misjudgment.
- **Reclassified, not removed:** PRISM (2604.28123) was tagged `Preference` because its loss carries a Bradley-Terry shape, but the actual mechanism is GAN-style adversarial alignment with an MoE discriminator, KL=0 disabled. Same family as Lion (2305.12870) and Black-Box OPD (2511.10643), both of which the auditor classifies as `Other`. PRISM moved from `Preference` to `Other` for consistency.

Net effect: paper count badge **170 → 168**; loss taxonomy total 157 → 155; the `Preference` class becomes empty (n=0) and is auto-hidden from the distribution chart.

## [2026-06-03]
### Added
- **TRB** (2605.31159) — *Trust-Region Behavior Blending for On-Policy Distillation* — added to §6.2 (Training Efficiency and Stabilization, curriculum/warmup) and Pending Papers. Trust-region warmup curriculum: behavior policy under student-centered KL constraint stabilizes early-stage OPD; standard reverse-KL distill loss unchanged. Pairs: Qwen3-1.7B-Base ← Qwen3-8B / Qwen3-0.6B-Base ← Qwen3-4B. Surfaced via community PR (#2 by @Myashka, closed in favour of in-pipeline insertion with corrected pair direction and base-variant tags).
- **TRAPO** (2512.17636) — *Trust-Region Adaptive Policy Optimization* — added to §4.1 (Objective Functions, Forward-KL family) and Pending Papers. TrSFT: dynamic trust-region forward-KL on expert prefixes, interleaved with RL on student completions; adaptive prefix selection by utility. Pairs: Qwen2.5-Math-7B / Qwen2.5-7B-Instruct ← DeepSeek-R1.

### Re-confirmed (v3-schema deep re-read, restored 3 of original 14-paper batch)
- After the initial audit flagged 14 papers as `is_opd=yes` but `student_rollout_in_training=no`, a follow-up v3-schema deep re-read of all 14 PDFs found 3 to actually qualify as OPD methods (the v3 reasoning text contradicted the rollout tag in those 3 cases, but the methods themselves do drive teacher feedback through student-generated content). Restored to README at the original sections via `scripts/awesome_list_inserter.py`:
  - **Lion** (2305.12870) → §6.2 (⭐ HoF early black-box OPD; iterative imitation-discrimination-generation loop on student-generated hard instructions, ChatGPT teacher).
  - **SuperCorrect** (2410.09008) → §5.1 (thought-template distillation + cross-model DPO on student-generated erroneous reasoning, Qwen2.5-Math-7B / Llama-3.1-8B / DeepSeekMath-7B ← o1-mini).
  - **Lightning OPD** (2604.13010) → §6.3 (offline precomputed teacher logprobs, theoretical equivalence to online OPD under teacher-consistency, Qwen3-Base ← Qwen3 / QwQ-32B).

### Removed
- 11 papers (revised from initial 14-paper list after re-read above) reclassified out of scope, all confirmed offline KD or pure self-distillation without rollout-in-loss-loop. Per scope rule (Awesome list = OPD methods + analysis-of-OPD only); these remain referenced in the survey LaTeX as background where appropriate (AKL §7.3 theory, MiniPLM / ULD §9 future work):
  - AKL (2404.02657, ⭐ HoF), MiniPLM (2410.17215), TAID (2501.16937), ToDi (2505.16297), AdaKD (2510.11615), Delta-KD (2509.14526), Cross-Tokenizer Distillation / ULD (2402.12030), Self-Distilled Trajectory-Aware Boltzmann / TABOM (2605.11854), Embarrassingly Simple Self-Distillation (2604.01193), SSB (2512.05105), Didactic-to-Constructive / DAIL (2602.02405).
- 3 additional papers reclassified out of scope after a follow-up scan triggered by spotting *On-Policy SFT for Efficient Reasoning* (2602.13407). All three share the same signature as the SPIN/IRIS boundary cases: signal source is self / PI(GT) / verifier-only and the loss has **no teacher-distribution KL term**, making them rejection-sampled self-training or DPO-style preference rather than distillation:
  - **On-Policy SFT for Efficient Reasoning** (2602.13407) — NLL on filtered correct rollouts, paper itself states "reward-free training recipe on-policy SFT"; STaR / RFT / ReST family.
  - **Retaining by Doing** (2510.18874) — GRPO with KL to *initial policy* (not teacher) plus a separate SFT branch; analysis of RL vs SFT for forgetting, no teacher-distill term.
  - **ORPO-Distill** (2509.25100) — ORPO preference loss `L_SFT + λ·log σ(log-odds(yP)/odds(yN))`; pairwise preference rather than distribution matching, same family as SPIN.
- Net effect (removals 14 → restored 3 → effective remove 11; plus separate 3-paper self-play removal; plus TRB / TRAPO additions): paper count badge **183 → 168**; survey latex-v4 also pruned of 11 method-introduction citations (49 → 3 background-only references retained at AKL §7.3, MiniPLM §9, ULD §9), references.bib pruned of 8 stale entries.

### Changed
- Model-pair fields corrected for 9 papers where v3 deep-read pairs disagreed with prior README entries (AOPD 2605.06387 / TGPO 2605.13230 / Long-Context OPD 2605.12227 / Best-of-N Teacher 2605.09725 / CoPD 2604.27083 / Speculative-KD 2410.11325 / TCOD 2604.24005 / VLA-OPD 2603.26666 / DAgger 2605.12913).
- `scripts/generate_loss_taxonomy.py` now restricts loss-distribution PNG / loss-evolution PNG / loss-taxonomy.md to papers actually present in this README, so taxonomy figures stay aligned with the published list when scope cleanups happen.
- Loss-taxonomy figures regenerated against the post-cleanup README, now covering **155 papers** (152 OPD-method + 3 restored after v3 re-read).

## [2026-05-30]
### Added
- **SOD** (2605.07725) added to Hall of Fame **🚀 Frontier (2025–2026)** subsection alongside OPSD / AlignDistil / Rethinking-OPD / SCOPE / SDZero. Step-level divergence reweighting for tool-integrated reasoning agents, surfacing the step-granularity unit that sits between token-level (TIP / SCOPE) and trajectory-level (TCOD) weighting.
- Daily pipeline cron added **2605.28791** (Skill-Conditioned Gated Self-Distillation for LLM Reasoning) to §5.3.1 (commit 9047e7c). Paper count badge: 175 → 176.

## [2026-05-29]
### Changed
- **Agentic OPD navigation references**: TCOD → SOD in 3 navigational locations (Trends takeaway #4, `resources/method-comparison.md` decision tree, `resources/reading-order.md` Level 4). SOD (2605.07725) is the more representative agentic OPD method now (step-level divergence reweighting for tool-integrated reasoning, +20.86% over the second-best baseline). TCOD's own paper entry, codebase row, the §6 dynamics toolbox listing in Quick-Start (where TCOD remains the §6.2 Curriculum representative), and historical changelog references are kept intact; only the high-level agentic-OPD pointers are updated.

### Reviewed (no list change)
- Reviewed 3 candidate papers from 5/27-5/28 daily-pipeline against the 5/15 inclusion scope (text/language model output only). All 3 had not entered the Awesome list, so no removal was needed; recording the boundary review here for completeness.
  - **AnyFlow** (2605.13724) — video diffusion (Wan2.1-14B + VBench), out of scope.
  - **Adversarial Dual OPD from Expressive Flow-based Teacher** (2605.27095) — embodied control, flow-matching policy teacher (no LLM backbone), out of scope.
  - **SERL** (2605.19447) — 5/27 commit message labelled it as "+OPD" but `paper_notes.json` had no entry; 5/28 three-condition review judged it RL-only (GRPO + env feedback reweighting, no teacher distill term). Stub added to `paper_notes.json` referencing `papers-meta/excluded-papers.md`.

## [2026-05-28]
### Removed
- **ThinkTuning** (2508.07616) — full-corpus audit reclassification. Paper's own title declares "without Distillation"; teacher provides text hints (opinions / reasons / phrases) appended to a fraction of student rollouts, not logit distributions. Loss is GRPO with Advantage-Aware Shaping on hint-augmented data — no KL-to-teacher term. Closer to teacher-augmented RL than distillation. Removed from Awesome List, V4 references.bib, paper_notes.json, INDEX.md; PDF moved to `pdfs/.trash-2026-05-28-thinktuning/`. Logged in `papers-meta/excluded-papers.md`.
- Paper count badge: 176 → 175

## [2026-05-17]
### Changed
- Removed 3 non-OPD papers: HPD (off-policy), Distillation Traps (analysis), VPG-EA (variational inference)
- Updated Key Takeaways with accurate pair statistics (83 models, 753 pairs)
- Regenerated heatmap: 83 models, 753 pairs, 148 OPD papers
- Fixed paper count badge (154)

## [2026-05-16]
### Added
- Batch: TGPO, EGRSD, MOPD, GEAR, RWOPD, DAgger-LLM, Prefix-Teach
- VPD, HyperEyes, Shadow Mask Distillation, UniSD, ProteinOPD, TRACE, TTS, Safactory
- AOPD, NPD, OPSD-post-RL, VISD

## [2026-05-08 polish v2]
### Added
- MiniPLM (§5.1) — Pre-training KD via difference sampling
- Visual upgrades: Mermaid evolution timeline, taxonomy mindmap
- Hall of Fame section with recommended reading orders by background

### Changed
- Paper count: 108 → 109 (107 arXiv + 2 tech reports)
- "Related Surveys" row: 108 methods → 109 methods

## [2026-05-08]
### Added
- PBSD (§5.3.1 + §4.3) — Preference-based self-distillation with DPO-style reward-regularized KL objective; first to replace pure KL with preference gap in OPD
- TT-OPD (§5.3.1 + §7.2 + §8.2) — Turn-level truncated OPD for medical agents; EMA teacher + outcome-privileged hints; first systematic agentic-OPD stability study
- Delta-KD (§5.1) — Base-to-Instruct delta signal isolation for white-box logit distillation
- TAID (§5.1) — Temporally adaptive interpolated distillation (2024)

### Changed
- Reclassified Latest Additions spotlight tags to match survey V2 fine-grained sections: CoPD §5.3.2→§5.3.3 (external feedback, mutual teacher), MAD-OPD §5.3.3→§5.1+§6.1+§8.2 (multi-teacher white-box), Uni-OPD §6→§6.2, PRISM §6→§6.2, PAINT §6.2→§5.3.2+§6.2.
- Paper count badge: 104 → 108.
- "Related Surveys" row: `104 methods across 13 subcategories` → `108 methods across 13 subcategories`.

## [2026-05-07]
### Added
- DeepSeek-V4 Technical Report (§7.1) — Multi-domain OPD consolidation via reverse-KL
- CaOPD (§7.2) — Discovers miscalibration scaling law in OPD
- OPSDL (§5.3.1) — Short-context as privileged teacher for long-context

## [2026-05-06]
### Added  
- Uni-OPD (§4.2) — Dual-perspective recipe unifying student exploration + teacher reliability
- MAD-OPD (§4.1) — Multi-agent debate for confidence-weighted OPD

## [2026-05-04]
### Added
- GUI-SD (§5.1) — Visual privileged context for GUI grounding
- MSD (§5.1) — Multilingual self-distillation for safety alignment

## [2026-05-01]
### Added
- TCOD (§4.2) — Temporal curriculum for multi-turn agent OPD
- PRISM (§4.2) — Pre-alignment via black-box OPD for multimodal RL
- PAINT (§4.2) — Partial-solution adaptive interpolated training
- CoPD (§5.3) — Co-evolving policy distillation
- IRIS (§5.2) — Interpolative Rényi iterative self-play

## [2026-04-26]
### Added
- π-Play (§5.1/§5.2) — Multi-agent self-play via privileged self-distillation
- ORBIT (§7.1) — Multi-teacher OPD fusion for controllable reasoning
- SCOPE (§4.2) — Dual-path adaptive weighting, reveals diversity collapse
- TIP (§4.2) — Token importance via 2D classification
- Lightning OPD (§4.2) — Teacher consistency + offline OPD 4x speedup

## [2026-04-24]
### Added
- Rethinking OPD (§6) — Two necessary conditions for OPD to work
- SDZero (§5.3) — Self-revision turns binary rewards into dense supervision

## [2026-04-20]
### Added
- Stable-OPD (§4.2) — Length inflation and stabilization strategies
- HY-Embodied-0.5 (§7.3) — Embodied foundation models for real-world agents
- DP-OPD (§7.3) — Differentially private on-policy distillation

## [2026-04-15]
### Added
- SRPO (§5.3) — Unifying group-relative and self-distillation policy optimization
- AKL (§4.1) — Rethinking Kullback-Leibler divergence (Adaptive KL)

## [2026-04-13]
### Added
- Initial creation of the Awesome LLM On-Policy Distillation list!
- A Survey of On-Policy Distillation for Large Language Models (§1)
- Foundational papers: GKD, MiniLLM, Lion, Distilling Step-by-Step.
