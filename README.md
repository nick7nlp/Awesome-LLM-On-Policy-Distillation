<a id="readme-top"></a>

<p align="center">
  <a href="https://nick7nlp.github.io/OPDHub/">
    <picture>
      <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/reading-room-mobile-dark.svg">
      <source media="(max-width: 600px)" srcset="assets/reading-room-mobile.svg">
      <source media="(prefers-color-scheme: dark)" srcset="assets/reading-room-dark.svg">
      <img src="assets/reading-room.svg" width="1200" alt="Awesome LLM On-Policy Distillation — learning from teachers on the student’s own trajectories.">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2604.00626"><strong>Read the survey</strong></a> &nbsp;·&nbsp; <a href="https://nick7nlp.github.io/OPDHub/"><strong>Explore OPDHub ↗</strong></a> &nbsp;·&nbsp; <a href="#browse-the-literature">Browse papers</a> &nbsp;·&nbsp; <a href="#citation">Cite</a>
</p>

<p align="center"><sub>362 entries · 124 with code · Updated&nbsp;2026&#8209;10&#8209;12</sub></p>

A reading companion to **[A Survey of On-Policy Distillation for Large Language Models](https://arxiv.org/abs/2604.00626)**.

<a id="a-few-good-starting-points"></a>

## Start reading

<table>
<thead><tr>
<th align="left" width="440">Follow a question</th>
<th align="left" width="440">Start with</th>
</tr></thead>
<tbody>
<tr>
<td><strong>How does the student learn?</strong><br><sub>Sampling, divergence, and the policy update.</sub></td>
<td><a href="https://arxiv.org/abs/2306.13649">GKD</a> · <a href="https://arxiv.org/abs/2306.08543">MiniLLM</a></td>
</tr>
<tr>
<td><strong>Where does supervision come from?</strong><br><sub>Solutions and feedback as teacher context.</sub></td>
<td><a href="https://arxiv.org/abs/2601.18734">OPSD</a> · <a href="https://arxiv.org/abs/2601.20802">SDPO</a></td>
</tr>
<tr>
<td><strong>What transfers, and what does not?</strong><br><sub>Reasoning compatibility, skills, and knowledge.</sub></td>
<td><a href="https://arxiv.org/abs/2604.13016">Rethinking OPD</a> · <a href="https://arxiv.org/abs/2610.09639">Skills vs. Knowledge</a></td>
</tr>
<tr>
<td><strong>How do multiple agents learn?</strong><br><sub>Joint trajectories and merging distilled experts.</sub></td>
<td><a href="https://arxiv.org/abs/2609.34234">MAS-OPD</a> · <a href="https://arxiv.org/abs/2609.34225">USA</a></td>
</tr>
</tbody>
</table>

**[Follow the full reading paths →](resources/reading-order.md)**

<a id="the-collection"></a>
<a id="find-your-question"></a>

## Browse the literature

Expand a topic to read the paper summaries, or **[search and filter on OPDHub ↗](https://nick7nlp.github.io/OPDHub/)**. Entries are ordered newest first within each topic.


<a id="papers-4"></a>

<a id="objectives-and-update-rules"></a>

<details><summary><strong>Objectives and update rules</strong> &nbsp;·&nbsp; 64</summary>

*What does the student update optimize?*

- **[Residual Advantage: Student-Relative Teacher Guidance for RL with Verifiable Rewards](https://arxiv.org/abs/2610.11519)**  
  <sub>2026-10-08 · Teacher-mediated RL</sub>  
  RA derives a local score update with a conditional squared-distance matching identity, then combines response-centered residual guidance with outcome RL. Its controls and Co-RA study distinguish teacher usefulness from standalone solver accuracy; the full clipped update is not exact L2 minimization.

- **[PIVOT: Perplexity-Informed KD-to-RL Transition Scheduling for Vertical-Domain Few-Shot Distillation](https://arxiv.org/abs/2610.11167)**  
  <sub>2026-10-08 · Hybrid OPD</sub>  
  PIVOT routes student-generated examples between teacher-distribution matching and GRPO using teacher-evaluated perplexity; on two few-shot intent-classification tasks, its step-matched recipe outperformed continued OPD and a global OPD-to-GRPO switch, while routing ablations favored sending lower-perplexity examples to GRPO earlier.

- **[Towards Unbiased On-Policy Distillation for Block Diffusion Language Models](https://arxiv.org/abs/2610.05373)**  
  <sub>2026-10-04 · Direct OPD</sub>  
  For block diffusion students with larger blocks than their teacher, Un-OPD filters context-misaligned trace steps and tempers high-support teacher targets; reported ablations improve math accuracy, while moderate trajectory reuse reduces reported GPU-hours with a staleness limit.

- **[ResOPD: Tail Residualization for Sparse On-Policy Distillation](https://arxiv.org/abs/2610.04882)**  
  <sub>2026-10-04 · Direct OPD</sub>  
  ResOPD uses observable aggregate tail mass to control a sampled fine-tail correction in sparse OPD. It is an unbiased full-vocabulary reverse-KL gradient estimator under ancestral student sampling, reduces covariance relative to HETS in the reported matched-prefix audits, and illustrates that lower estimator covariance need not yield better downstream accuracy.

- **[Unbiased Top-$k$ Estimation for On-Policy Distillation](https://arxiv.org/abs/2609.34447)**  
  <sub>2026-09-28 · Direct OPD</sub>  
  TT-OPD combines exact selected-token contributions with a sampled-token tail correction, yielding a conditionally unbiased per-state reverse-KL gradient estimator and improving the tested OPD recipes with little additional training time in the reported configurations.

- **[1% of Tokens Can Be Enough: On Gradient Estimation in On-Policy Distillation](https://arxiv.org/abs/2609.24432)**  
  <sub>2026-09-21 · Direct OPD · [Code](https://github.com/BruceSheng1202/IER-OPD)</sub>  
  This study separates useful teacher corrections from the reliability of estimating their gradients from sampled tokens. It approximates a fixed-prefix signal-to-noise measure to select positions in student rollouts, alone or with usefulness scores; sparse supervision still requires generating and scoring complete trajectories in its implementation.

- **[Beyond Token-Local Imitation: Reward-Compatible Temporal Credit Assignment for On-Policy Distillation](https://arxiv.org/abs/2609.16937)**  
  <sub>2026-09-15 · Hybrid OPD</sub>  
  The paper analyzes why token-local distillation credit omits a token's effects on later prefixes, then proposes discounted future teacher credit mixed with verifiable outcome feedback. Its horizon-independent variance bound applies to a fixed discount below one under the paper's assumptions, not to undiscounted credit.

- **[TV-Regulated OPD: Direction Matters in On-Policy Distillation](https://arxiv.org/abs/2609.08341)**  
  <sub>2026-09-08 · Direct OPD</sub>  
  The paper tests whether sampled-token likelihood-gap magnitudes matter beyond their signs, then uses teacher-relative signs with conditional total variation to regulate overall update intensity. Its gradient interpretation concerns the on-policy signal with fixed state occupancy, not a full sequence-level derivative.

- **[Distillation as Probability Transport: Routed On-Policy Distillation](https://arxiv.org/abs/2609.08337)**  
  <sub>2026-09-08 · Direct OPD</sub>  
  On student-visited prefixes, the method pairs tokens with excess student probability with tokens underweighted relative to the teacher, then fits localized pairwise log-odds changes to consistent, bounded targets. Its routing uses a sparse shared token support and is evaluated on mathematical reasoning.

- **[Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation](https://arxiv.org/abs/2608.29846)**  
  <sub>2026-08-30 · Direct OPD</sub>  
  IDA-OPD estimates each sampled-token update’s local entropy effect, preserves entropy-expanding updates, and shrinks contracting advantages according to teacher–student disagreement. The entropy sign result assumes a local logit-space step; behavior under full model training is evaluated empirically.

- **[SpikeOPD: Stable On-Policy Distillation for Autoregressive Spiking Language Models](https://arxiv.org/abs/2608.27857)**  
  <sub>2026-08-28 · Direct OPD</sub>  
  SpikeOPD adapts a distilled spiking language model on its own generated prefixes, combining teacher distribution matching with an anchor to the initial distilled checkpoint and layerwise firing-rate constraints. Its stability findings concern the evaluated spiking students, not language-model architectures generally.

- **[On-policy Distillation with Verifiable Reward](https://arxiv.org/abs/2608.24696)**  
  <sub>2026-08-25 · Hybrid OPD · [Code](https://github.com/LeapLabTHU/OPDVR)</sub>  
  On student-generated reasoning trajectories, this method gates each sampled token’s teacher–student log-probability signal by verified correctness, retaining updates that reinforce correct responses or suppress incorrect ones. Its group-relative variant uses the sign, not the magnitude, of the group advantage; the reported tests concern mathematical reasoning.

- **[Beyond Teacher Likelihood: Group-Calibrated On-Policy Distillation for Long-Context Reasoning](https://arxiv.org/abs/2608.19181)**  
  <sub>2026-08-19 · Hybrid OPD · [Code](https://github.com/SolereZhang/GC-OPD)</sub>  
  GC-OPD separately normalizes verifier rewards and mean teacher–student token scores within student rollout groups. It distributes their signed difference across tokens while retaining the original distillation advantage; the correction vanishes when either group-level signal has negligible variation.

- **[Mismatch Matters: On-Policy Distillation Beyond Token Agreement](https://arxiv.org/abs/2608.09836)**  
  <sub>2026-08-10 · Direct OPD · [Code](https://github.com/yzc-666/TIDE)</sub>  
  TIDE diagnoses repetitive rollouts where local teacher agreement masks failure, then independently gates severe student-excess and student-deficit positions. It uses bounded Hellinger-shaped sampled-token suppression and teacher top-K cross-entropy to recover missing mass; its experiments concern mathematical reasoning with fixed external teachers.

- **[SR-OPSD: Self-Referenced On-Policy Self-Distillation](https://arxiv.org/abs/2608.09745)**  
  <sub>2026-08-10 · Direct OPD</sub>  
  On student-generated prefixes, SR-OPSD geometrically mixes a privileged-context self-teacher with a frozen initial-policy reference, then minimizes forward Rényi divergence from that target to the student. Its variational characterization applies to fixed rollout contexts, not the full moving-policy dynamics.

- **[WDL-OPD: Weak-Driven On-Policy Distillation via Mixture-Constrained Co-Training](https://arxiv.org/abs/2608.09447)**  
  <sub>2026-08-10 · Direct OPD</sub>  
  An anchor policy supplies all rollouts while a trainable auxiliary evaluates the same prefixes; both receive gradients from matching their geometric token-distribution mixture to a frozen teacher. The reported stability evidence is descriptive because initialization, curriculum, and compute are not fully matched across comparisons.

- **[Matching Supervision to the Student's Learning Capacity: A Unified Framework for On-Policy Self-Distillation](https://arxiv.org/abs/2608.08176)**  
  <sub>2026-08-08 · Direct OPD · [Code](https://github.com/lauvlalala/USD)</sub>  
  The method jointly adjusts soft token weights and how much reference context a privileged self-teacher sees while scoring student rollouts. A fixed learning-difficulty budget drives both controls through online updates; it is a capacity model, not a measured or automatically changing student-capacity limit.

- **[Adaptive Supervised Anchoring for On-Policy Self-Distillation](https://arxiv.org/abs/2608.07935)**  
  <sub>2026-08-08 · Hybrid OPD</sub>  
  SDS separates teacher-distribution matching on student-generated prefixes from supervised anchoring on canonical answer prefixes. Its fixed-weight variants provide evidence about this context separation, independently of the unspecified similarity operator used by the adaptive variant.

- **[SPOT: Sparse Probing and Outcome Calibration for On-Policy Distillation](https://arxiv.org/abs/2608.04419)**  
  <sub>2026-08-05 · Hybrid OPD</sub>  
  SPOT ranks student-generated positions for sparse probing using teacher entropy, top-candidate mass and student–teacher mismatch. Verifier-scored student continuations then tilt a teacher-anchored target for an additional local distillation loss, applied only at selected positions with a positive-reward branch.

- **[DAPD: Dual-Anchored Policy Distillation](https://arxiv.org/abs/2608.01735)**  
  <sub>2026-08-03 · Direct OPD · [Code](https://github.com/uanu2002/DAPD)</sub>  
  DAPD addresses privilege illusion in on-policy self-distillation with a trainable, self-conditioned bridge. It aligns reference and rollout behavior along inference-context and privileged-context paths in both guidance directions, while retaining the original privileged-teacher supervision rather than replacing it entirely.

- **[Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2608.01263)**  
  <sub>2026-08-02 · Direct OPD</sub>  
  FP-OPD estimates a vision-language student’s local visual-response space with perturbation probes, then Fisher-projects the teacher correction to construct targets for student-generated prefixes. It models local reachability rather than global representational capacity, and the probes require additional forward passes.

- **[Distill Where You Fail: Recovering Learning Signals of Negative RL-Groups from Adaptive Teacher Guidance](https://arxiv.org/abs/2608.00782)**  
  <sub>2026-08-01 · Analysis</sub>  
  This study tests teacher supervision for all-failure rollout groups. Its sequential ablation reports a gain from teacher-based advantage weighting before adding token selection or teacher-response SFT, providing a bounded comparison for recovering a signal when group-relative outcome advantages vanish.

- **[CriPO: Enhancing Rubric-based RL via Self-Distillation](https://arxiv.org/abs/2607.18082)**  
  <sub>2026-07-20 · Hybrid OPD</sub>  
  CriPO retains rubric-reward policy optimization on policy-generated responses. A criterion-conditioned self-teacher supplies filtered forward-KL supervision for unmet criteria, while a counterfactual self-teacher locates useful tokens in negative-advantage responses for local advantage flipping. It is a hybrid update, not standalone distillation.

- **[Distilled Reinforcement Learning for LLM Post-training](https://arxiv.org/abs/2607.17247)**  
  <sub>2026-07-19 · Teacher-mediated RL</sub>  
  In the reported reasoning experiments, reverse-KL OPD improved rapidly but later plateaued, while larger rollout groups and a simple OPD–RL loss mixture did not yield sustained gains; the paper also contrasts these results with teacher-weighted reinforcement learning rather than another distillation-matching objective.

- **[Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399)**  
  <sub>2026-07-15 · Direct OPD</sub>  
  This study diagnoses sampled teacher signals and tests clipping or signed logarithmic compression of OPD advantages. Improvements over unregulated OPD depend on the teacher-student pair, so teacher strength alone does not determine the benefit of signal regulation.

- **[When Top-K Misses the Decision: Tool-Call Drift in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2607.07050)**  
  <sub>2026-07-08 · Analysis · [Code](https://github.com/shen-jiabin/decision-support-opd)</sub>  
  The study diagnoses decision-critical coordinates omitted by teacher-only top-K support and compares support restoration with loss shaping. In the reported Qwen setting, Soft Clamp lowers over-calling from 14.2% to 9.0% while lowering required-call recall from 91.5% to 86.5%.

- **[Geometric Self-Distillation for Reasoning Generalization](https://arxiv.org/abs/2607.06855)**  
  <sub>2026-07-07 · Direct OPD</sub>  
  GEOSD combines Hellinger matching, a Fisher–Rao penalty to recent checkpoints, and damped K-FAC preconditioning on student-generated prefixes. Geometric-mean token weights alone do not bound the parameter-gradient norm; objective and optimizer ablations evaluate the recipe.

- **[Trust Region Policy Distillation](https://arxiv.org/abs/2607.04751)**  
  <sub>2026-07-06 · Analysis</sub>  
  TOP-D interpolates an external teacher’s token probabilities with the rollout student’s to lower-bound the negative log-ratio reward, then uses clipped trust-region updates to reuse student-generated batches. Its gradient-variance analysis concerns autoregressive generation and assumes bounded score-function gradients and a finite vocabulary.

- **[Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.18810)**  
  <sub>2026-06-17 · Teacher-mediated RL</sub>  
  In a tested RLVR code-generation setting, five additive distillation variants using teachers conditioned on the student's verified solutions underperformed GRPO; the paper contrasts this result with using teacher–student divergence to weight reward-driven updates rather than to define a matching target.

- **[PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation](https://arxiv.org/abs/2606.17199)**  
  <sub>2026-06-15 · Direct OPD · [Code](https://github.com/EIT-NLP/PowerOPD)</sub>  
  PowerOPD replaces the detached teacher–student log-ratio coefficient on student-sampled tokens with a bounded, sign-preserving difference of powered token probabilities in a policy-gradient update. Its evaluations focus on mathematical reasoning and a limited set of teacher–student pairs.

- **[When Context Returns: Toward Robust Internalization in On-Policy Distillation](https://arxiv.org/abs/2606.11627)**  
  <sub>2026-06-10 · Direct OPD</sub>  
  After on-policy context distillation, reintroducing privileged context can worsen a student's answers. No-Context Anchoring adds a forward-KL consistency loss that treats the student's no-context output as a stop-gradient target for its context-conditioned output on reused student rollouts; it does not guarantee invariance.

- **[Self-Distilled Policy Gradient](https://arxiv.org/abs/2606.04036)**  
  <sub>2026-06-02 · Hybrid OPD · [Code](https://github.com/lauyikfung/SDPG)</sub>  
  SDPG combines outcome optimization, full-vocabulary reverse-KL matching to a privileged self-teacher, and fixed-reference regularization. Removing the teacher or reference component produces different accuracy, length, and entropy behavior in its mathematical-reasoning experiments.

- **[Physics-Guided Policy Optimization with Self-Distillation](https://arxiv.org/abs/2606.03620)**  
  <sub>2026-06-02 · Direct OPD</sub>  
  PGPO scales self-distillation updates using a capped batch-level entropy-gap signal between unassisted and feedback-conditioned predictions. Its reported domain comparisons favor the method in most tested domains, but do not distinguish the signal's value from ordinary step-size tuning.

- **[SafeSteer: Localized On-Policy Distillation for Efficient Safety Alignment](https://arxiv.org/abs/2606.02530)**  
  <sub>2026-06-01 · Direct OPD</sub>  
  SafeSteer builds a refusal-oriented self-teacher by activation steering, then votes on teacher–base-model probability contrasts to select safety-related vocabulary items. On student-generated responses to harmful prompts, it applies reverse-KL loss only over those items, rather than restricting generation or scoring to them.

- **[Trust Region On-Policy Distillation](https://arxiv.org/abs/2606.01249)**  
  <sub>2026-05-31 · Direct OPD</sub>  
  TrOPD classifies student-generated tokens by teacher–student decoding agreement, using sampled reverse-KL supervision in the trust region and top-k forward-KL guidance for outliers. It also imitates teacher-generated prefixes before student continuations, annealing those prefixes away during training.

- **[OPD+: Rethinking the Advantage Design for On-Policy Distillation](https://arxiv.org/abs/2606.01039)**  
  <sub>2026-05-31 · Direct OPD</sub>  
  OPD+ studies policy-gradient coefficients for student-sampled, single-token estimates of teacher–student f-divergences and restores the omitted direct dependence of divergence feedback on the student. For reverse KL the correction is a constant baseline in expectation; this immediate-token analysis does not by itself settle full-trajectory credit.

- **[Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding](https://arxiv.org/abs/2606.00564)**  
  <sub>2026-05-30 · Direct OPD</sub>  
  VGS augments multimodal OPD with a locally normalized target combining teacher image/no-image contrasts and the student's language prior. Visual versus language steering controls support task-dependent benefits from visual emphasis, without establishing the claimed exact sequence-level Bayesian decomposition.

- **[CAST: Non-Privileged Clipped Asymmetric Self-Teaching with Advantage Flipping for GRPO](https://arxiv.org/abs/2606.00172)**  
  <sub>2026-05-29 · Hybrid OPD</sub>  
  CAST uses an answer-free self-teacher gap to construct local advantage reversals and updates for uniform-reward groups. Controlled component comparisons support this teacher-dependent correction rule, while longer responses and generation-budget sensitivity limit interpretation as an unconditional reasoning gain.

- **[Tailoring Teaching to Aptitude: Direction-Adaptive Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.22263)**  
  <sub>2026-05-21 · Hybrid OPD</sub>  
  DASD routes privileged teacher feedback by entropy and modulates its direction in a policy-gradient update. Routing and sign controls evaluate the recipe; the action-dependent gate does not establish an exact signed-KL matching objective.

- **[Visual-Advantage On-Policy Distillation for Vision-Language Models](https://arxiv.org/abs/2605.21924)**  
  <sub>2026-05-21 · Direct OPD</sub>  
  On student-generated vision-language rollouts, a teacher compares token probabilities with intact and degraded images to estimate sensitivity to fine visual detail. The method reweights sibling rollouts and separately averages reverse KL over high- and low-sensitivity tokens; sensitivity is a proxy, not a direct measure of perception.

- **[When Are Teacher Tokens Reliable? Position-Weighted On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2605.21606)**  
  <sub>2026-05-20 · Direct OPD · [Code](https://github.com/SaFo-Lab/PW-OPSD)</sub>  
  PW-OPSD increases position weights on clipped forward-KL supervision from a privileged-answer self-teacher and averages losses per sequence. Its reliability diagnostic concerns ambiguous candidate tokens on correct reasoning traces; the reported method changes both weighting and aggregation, limiting attribution to weighting alone.

- **[Teacher-Guided Policy Optimization for On-Policy Reasoning Distillation under Large Policy Divergence](https://arxiv.org/abs/2605.13230)**  
  <sub>2026-05-13 · Hybrid OPD</sub>  
  TGPO studies teacher-selected next-token supervision on student-generated prefixes alongside reward optimization. Reported comparisons favor annealed guidance, while a sign inconsistency in the printed combined objective limits the exact update interpretation.

- **[A Recipe for Long-Context Reasoning in Large Language Models via On-Policy Optimization and Distillation](https://arxiv.org/abs/2605.12227)**  
  <sub>2026-05-12 · Hybrid OPD</sub>  
  After supervised warm-up, the long-context recipe combines group-relative outcome optimization with token-level reverse-KL matching to Qwen3-32B on student-generated prefixes. Objective and teacher-choice comparisons examine this combined training procedure.

- **[From Generic Correlation to Input-Specific Credit in On-Policy Self Distillation](https://arxiv.org/abs/2605.11613)**  
  <sub>2026-05-12 · Direct OPD</sub>  
  Under a posterior-compatibility assumption, the paper interprets feedback-conditioned self-distillation rewards as filtering increments and subtracts teacher scores for unrelated batch inputs to discount generic response patterns. CREDIT trains on student rollouts, requires extra teacher passes, and its interpretation need not hold without that assumption.

- **[STEPS: Selective On-Policy Self-Distillation for Reasoning](https://arxiv.org/abs/2605.10194)**  
  <sub>2026-05-11 · Hybrid OPD</sub>  
  STEPS uses annotated spans to route brief self-distillation, with a coarse diagnostic label conditioning the self-teacher. Key-span forward KL or error-span reverse KL is withdrawn as GRPO is restored on annotated positions by step 40. Matched-coverage controls test selection, and annotator comparisons show gains of varying magnitude.

- **[KL for a KL: On-Policy Distillation with Control Variate Baseline](https://arxiv.org/abs/2605.07865)**  
  <sub>2026-05-08 · Direct OPD · [Code](https://github.com/holi-lab/vOPD)</sub>  
  vOPD subtracts a detached, action-independent estimate of the per-token negative reverse KL as a baseline for the sampled-token policy-gradient update. Its top-k variant approximates the baseline rather than truncating the distillation objective; the study evaluates token-level reasoning distillation, not sequence-level objectives.

- **[Asymmetric On-Policy Distillation: Bridging Exploitation and Imitation at the Token Level](https://arxiv.org/abs/2605.06387)**  
  <sub>2026-05-07 · Direct OPD</sub>  
  On student-generated reasoning prefixes, AOPD retains log-probability-gap-weighted policy-gradient reinforcement for positive-advantage tokens but replaces non-positive updates with teacher-top-K forward-KL guidance, allowing unsampled alternatives to receive gradients. Its evaluations chiefly concern teacher–student mathematical-reasoning distillation, not self-distillation.

- **[Preference-Based Self-Distillation: Beyond KL Matching via Reward Regularization](https://arxiv.org/abs/2605.05040)**  
  <sub>2026-05-06 · Teacher-mediated RL</sub>  
  PBSD learns teacher-referenced preferences between privileged-teacher responses and current student samples. Its 8B experiments compare this sequence-preference route with token-level self-distillation; it is an adjacent transfer method rather than direct student-prefix distribution matching.

- **[Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing](https://arxiv.org/abs/2604.02288)**  
  <sub>2026-04-02 · Hybrid OPD</sub>  
  Sample routing sends correct student rollouts, and failures lacking teacher information, to reward-based policy optimization; failures with usable feedback receive distributional correction from a privileged-context self-teacher. Teacher-entropy weighting reduces uncertain token targets, so distillation does not supervise every failed rollout.

- **[Scaling Reasoning Efficiently via Relaxed On-Policy Distillation](https://arxiv.org/abs/2603.11137)**  
  <sub>2026-03-11 · Direct OPD</sub>  
  REOPOLD updates on student-generated reasoning with sampled-token teacher–student log-likelihood ratios treated as stopped-gradient rewards. It floors strongly negative rewards and changes token selection from reward-based filtering to high-entropy selection; its guidance does not match full teacher distributions at every token.

- **[Entropy-Aware On-Policy Distillation of Language Models](https://arxiv.org/abs/2603.07079)**  
  <sub>2026-03-07 · Direct OPD</sub>  
  Entropy-aware on-policy distillation uses student rollouts and retains a sampled, clipped reverse-KL update at every token, adding teacher-top-token forward KL where teacher entropy is high. The two terms can act together; its reported validation concentrates on mathematical reasoning.

- **[Explain in Your Own Words: Improving Reasoning via Token-Selective Dual Knowledge Distillation](https://arxiv.org/abs/2603.13260)**  
  <sub>2026-02-25 · Direct OPD · [Code](https://github.com/kmswin1/TSD-KD)</sub>  
  TSD-KD trains on student-generated reasoning using teacher rankings of student-proposed token candidates in an early response segment, alongside distribution matching gated by the student–teacher uncertainty gap and selective entropy minimization. The ranking loss supplies preferences, not full-distribution matching.

- **[$X$-KD: General Experiential Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2602.12674)**  
  <sub>2026-02-13 · Hybrid OPD</sub>  
  The generalized X-KD branch adds a learned reward-modeling and temporal-consistency term to GKD on mixed student and supervised prefixes. Comparisons with GKD show setting-dependent gains, while its black-box sequence branch uses offline teacher responses and does not establish recovery of the teacher's original reward.

- **[Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation](https://arxiv.org/abs/2602.12125)**  
  <sub>2026-02-12 · Direct OPD · [Code](https://github.com/RUCBM/G-OPD)</sub>  
  Generalized on-policy distillation scores student-generated trajectories with a teacher-to-reference log-probability ratio, scales that implicit reward, and penalizes divergence from the reference. Its extrapolation variants are studied in math and code; using a teacher’s pre-RL checkpoint as the reference requires access to that checkpoint.

- **[A Note on Hybrid Online Reinforcement and Imitation Learning for LLMs: Formulations and Algorithms](https://arxiv.org/abs/2512.23097)**  
  <sub>2025-12-28 · Analysis</sub>  
  This note combines trajectory-level student-to-reference KL with task reward, separating an analytic local token-KL gradient from a sampled gradient for future divergence and rewards. It supplies a gradient decomposition and proposed algorithm, while leaving empirical training validation to future work.

- **[Distillation of Large Language Models via Concrete Score Matching](https://arxiv.org/abs/2509.25837)**  
  <sub>2025-09-30 · Direct OPD · [Code](https://github.com/aailab-kaist/CSD)</sub>  
  Concrete Score Distillation matches weighted teacher–student logit differences across vocabulary pairs, allowing additive logit shifts. Factorized weights make gradient computation linear in vocabulary size. The objective requires a shared vocabulary and can complement on-policy training without itself requiring student rollouts.

- **[KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning](https://arxiv.org/abs/2506.02208)**  
  <sub>2025-06-02 · Hybrid OPD</sub>  
  KDRL combines rule-based outcome optimization on student reasoning rollouts with a directly backpropagated sampled-token squared-log-ratio loss toward the teacher. It also tests omitting this auxiliary loss for rewarded responses; the k2 surrogate is distinct from an exact full-vocabulary reverse-KL gradient.

- **[Online Knowledge Distillation with Reward Guidance](https://arxiv.org/abs/2505.18952)**  
  <sub>2025-05-25 · Direct OPD</sub>  
  White-box MM-PbKD matches teacher-weighted Q moments at student-visited states under preference-derived constraints. Comparisons with fixed-preference training and a separate RLHF-plus-KD pipeline support this joint formulation without establishing full teacher-policy recovery.

- **[DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://arxiv.org/abs/2503.07067)**  
  <sub>2025-03-10 · Direct OPD · [Code](https://github.com/jongwooko/distillm-2)</sub>  
  DistiLLM-2 applies skewed forward divergence to teacher-generated responses and skewed reverse divergence to student-generated responses. The paper proposes adaptive skew and loss weighting; student responses are generated before each epoch and reused within it.

- **[AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](https://arxiv.org/abs/2503.02832)**  
  <sub>2025-03-04 · Direct OPD · [Code](https://github.com/songmzhang/AlignDistil)</sub>  
  AlignDistil constructs a token-level target by extrapolating logits from normal and reverse preference-trained models, with token-specific weights based on their distributional difference. It matches this target on student-sampled prefixes, but also provides an off-policy loss on fixed responses.

- **[DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898)**  
  <sub>2024-02-06 · Hybrid OPD · [Code](https://github.com/jongwooko/distillm)</sub>  
  DistiLLM combines skewed token-distribution matching with an adaptive schedule that draws from fixed data or a replay buffer of student-generated responses. Because buffered responses are reused after collection, its data strategy is partly off-policy rather than continuously fresh student rollout.

- **[f-Divergence Minimization for Sequence-Level Knowledge Distillation](https://arxiv.org/abs/2307.15190)**  
  <sub>2023-07-27 · Hybrid OPD</sub>  
  f-DISTILL develops step-wise training losses for several sequence-level divergence objectives. Some variants sample current students while symmetric-loss variants also use fixed teacher samples; the student-sampling path is stop-gradient, and the implemented Jensen–Shannon conditional is an approximation rather than the exact sequence divergence.

- **[On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649)**  
  <sub>2023-06-23 · Direct OPD</sub>  
  GKD queries teacher next-token distributions on prefixes from student-generated sequences, optionally mixing them with fixed examples, and minimizes a chosen conditional divergence without backpropagating through sampling. Only the student-generated portion of that mixture is on-policy.

- **[MiniLLM: On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2306.08543)**  
  <sub>2023-06-14 · Direct OPD · [Code](https://github.com/microsoft/LMOps)</sub>  
  MiniLLM targets sequence-level reverse KL using student-generated responses and teacher probabilities. Its update separates an immediate full-vocabulary term from estimated future effects, with teacher-mixed sampling and other stabilizers; its reported evaluation centers on instruction following, not a general rule favoring reverse KL.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-5"></a>

<a id="teacher-and-supervision-construction"></a>

<details><summary><strong>Teacher and supervision construction</strong> &nbsp;·&nbsp; 98</summary>

*What makes a teacher useful on student trajectories?*

- **[Which Skill to Distill? SGUID: Selecting a Compact Skill Bank for Model-Skill Co-Evolution](https://arxiv.org/abs/2610.12367)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  SGUID selects skill-conditioned teachers using persistent, verifier-aligned signals observed during on-policy distillation. On the reported math benchmarks, compact selected banks matched or exceeded full-bank distillation for three of four models after one round and all four after a second; selection required an initial full-bank run.

- **[Distilling Routed 3D Privilege for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.12355)**  
  <sub>2026-10-08 · Hybrid OPD</sub>  
  GPD combines GRPO with self-distillation on RGB-conditioned student trajectories, using a teacher supplied with question-routed textual 3D cues and the reference answer. Controlled spatial-VLM comparisons favor this recipe over GRPO and answer-privileged OPSD on the reported averages, while ablations favor routed cues and incorrect-only distillation in the tested setting.

- **[ReTeach: Building a Self-Teacher through Multi-Round Reflection and Retry](https://arxiv.org/abs/2610.11529)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  ReTeach constructs an on-policy self-teacher through outcome-verified reflection and retry, then distills its context-conditioned token distributions on the student's original rollouts; ablations show benefits from explicit reflection and EMA targets, while supervision from unresolved attempts is task-dependent.

- **[Environmental Feedback Modeling Matters: Rethinking Feedback Treatment in Agentic Hindsight Self-Distillation](https://arxiv.org/abs/2610.11384)**  
  <sub>2026-10-08 · Hybrid OPD</sub>  
  SELF jointly trains feedback prediction and hindsight self-distillation on student-collected agent transitions; its reported ablations show improved task performance over distillation without feedback modeling, while a cross-rollout comparison suggests that exact transition sharing is not essential to the observed benefit.

- **[SpatialOPSD: Self-Distilling Spatial Intelligence from Verified Coding Agent Traces](https://arxiv.org/abs/2610.11366)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  SpatialOPSD uses verified coding-agent traces as privileged context for on-policy multimodal self-distillation; its ablations show that masking and unlikelihood trade off spatial-task accuracy against measured trace-related keyword disclosure.

- **[Recurrent Self-Improvement: Dynamic Cross-Loop On-Policy Distillation for Looped Language Models](https://arxiv.org/abs/2610.10623)**  
  <sub>2026-10-07 · Direct OPD</sub>  
  LoopOPD distills a LoopLM’s terminal-loop distribution into an intermediate-loop policy on that policy’s own prefixes; on the tested Ouro-Thinking models, refreshing the shared-parameter teacher is associated with further gains, while cross-loop analysis identifies conditions under which terminal-loop improvement is not guaranteed.

- **[Composing What Each Teacher Learned: Multi-Teacher On-Policy Distillation through Teacher-Relative Shifts](https://arxiv.org/abs/2610.10460)**  
  <sub>2026-10-07 · Direct OPD</sub>  
  Teacher-relative logit shifts re-anchored at the student's initialization offer a distinct target-construction choice in multi-teacher OPD. Paired experiments report more balanced targets and stronger three-teacher Math composition than endpoint targets, while interleaved single-teacher routing is comparable.

- **[A Good Self-Teacher Meets the Student Where They Are: Joint On-Policy Learning and Teaching](https://arxiv.org/abs/2610.10447)**  
  <sub>2026-10-07 · Hybrid OPD</sub>  
  JOLT jointly trains a privileged, reward-optimized self-teacher and an unprivileged student distilled on its own trajectories; its comparisons support recipe-level gains in several settings, while its reward-consistency result applies only to an ideal teacher's local student update.

- **[MIRROR: From Imitation to Internalization in LLM Personalization](https://arxiv.org/abs/2610.09795)**  
  <sub>2026-10-07 · Hybrid OPD</sub>  
  MIRROR evaluates reference-revealed self-distillation on student-generated prefixes for personalized generation; its MIRROR-F variant adds selective, teacher-forced anchoring of context-matched reference terms, improving several reported outcomes while showing task-dependent limits.

- **[Socio-Foundation: A Model for Generalizable Individual Behavior Simulation via Hierarchical Capability Distillation](https://arxiv.org/abs/2610.08967)**  
  <sub>2026-10-06 · Hybrid OPD</sub>  
  Socio-Foundation groups task-trained simulation experts into capability teachers and integrates them on student-generated histories; its tested hierarchical recipe outperforms the reported direct-integration and off-policy alternatives on IndiEval.

- **[Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability](https://arxiv.org/abs/2610.08448)**  
  <sub>2026-10-06 · Direct OPD</sub>  
  Across the tested heterogeneous-tokenizer OPD transfers, adding span log-probability MSE to strict alignment increased structural supervision coverage but reduced average accuracy, while student-selected top-16 supervision at strict positions retained most of the observed gain over the undistilled students.

- **[UP-MOPD: Update Projection in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.08398)**  
  <sub>2026-10-06 · Direct OPD</sub>  
  UP-MOPD projects the optimizer-produced update, rather than the mixed distillation gradient, onto current-domain first-order constraints; reported two- and three-teacher comparisons favor this intervention on aggregate scores, with added training cost and limited evidence for robust per-benchmark gains.

- **[Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution](https://arxiv.org/abs/2610.06804)**  
  <sub>2026-10-05 · Direct OPD</sub>  
  OPPD trains on student-generated, teacher-scored particle histories to approximate sequence-level power sharpening; reported comparisons show gains over token-level on-policy distillation, while the exact divergence-gradient interpretation of the resampled implementation remains unestablished.

- **[How Should Teachers Be Prepared? RL on Student-Induced States for On-Policy Distillation](https://arxiv.org/abs/2610.04950)**  
  <sub>2026-10-04 · Hybrid OPD</sub>  
  Training a teacher to continue fixed student-generated prefixes improves its measured continuation ability and, in the tested math-reasoning setting, improves downstream OPD both with and without teacher handoffs.

- **[Understanding Off- vs On-Policy Distillation: A Tale of Distinct Training Objectives](https://arxiv.org/abs/2609.38666)**  
  <sub>2026-09-29 · Direct OPD</sub>  
  In a sequential multi-teacher model, forward- and reverse-KL distillation induce arithmetic and geometric response aggregates; analytic constructions show when the reverse aggregate preserves a confident expert’s preference and when misleading feedback or long-horizon continuations reverse that advantage.

- **[On the Off-Policy Teacher in On-Policy Distillation](https://arxiv.org/abs/2609.38360)**  
  <sub>2026-09-29 · Hybrid OPD</sub>  
  SCOUT periodically trains a teacher to continue from student-generated prefixes while retaining student-side OPD. Across the reported math and code settings, this recipe improves on frozen-teacher OPD; fixed-prefix diagnostics and a teacher-GRPO control support a role for student-prefix conditioning.

- **[USA: Update-aware SAM for Cross-domain On-Policy Disitllation of Language Agents](https://arxiv.org/abs/2609.34225)**  
  <sub>2026-09-28 · Direct OPD</sub>  
  USA proposes preparing independently distilled language-agent experts for subsequent merging through update-aware sharpness training. Under the authors’ stated common OPD setup, they report improved merging outcomes and informative scale-assignment controls; the exact implemented gradient estimator is unspecified.

- **[LastOPD: Taming Collapse in Latent On-Policy Distillation](https://arxiv.org/abs/2609.28845)**  
  <sub>2026-09-23 · Direct OPD · [Code](https://github.com/Muyiiiii/LastOPD)</sub>  
  LastOPD aligns the student’s final pre-head representation with the teacher’s on student-generated responses, then fades that latent loss into token-level distillation. The crossfade is motivated by observed collapse under continued latent supervision in the tested cross-size model pairs.

- **[Counterfactual Constraint-Conditioned On-Policy Distillation for Multi-Constraint Instruction Following](https://arxiv.org/abs/2609.27421)**  
  <sub>2026-09-23 · Direct OPD · [Code](https://github.com/zhengyanzhao1997/cc-opd)</sub>  
  CC-OPD generates student responses under all constraints while a frozen teacher rescores the same tokens with each constraint removed in turn. Summed, clipped likelihood shifts shape the distillation reward; teacher scoring grows with the number of constraints, without requiring additional student rollouts.

- **[Distill What You Trust: Reliability-Aware Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2609.23697)**  
  <sub>2026-09-20 · Direct OPD</sub>  
  TrustMOPD weights specialist teachers at each student-generated prefix using calibrated changes in next-token preferences relative to a shared pre-RL reference. These changes serve as reliability proxies for token-level supervision; the interpretation depends on specialists derived from that common reference.

- **[Calibrating Teacher--Student Discrepancy for On-Policy Distillation](https://arxiv.org/abs/2609.21619)**  
  <sub>2026-09-18 · Direct OPD</sub>  
  Cal-OPD uses contrasting teacher contexts to estimate an interval of likelihood variation and removes the covered part of the original teacher-student gap. Matched-sparsity and scaling controls favor residual calibration in the tested settings, without proving that the removed variation is entirely task-irrelevant.

- **[GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation](https://arxiv.org/abs/2609.21432)**  
  <sub>2026-09-18 · Direct OPD</sub>  
  GVPO++ matches group-centered teacher-student sequence log-probability differences on student-generated responses, allowing different tokenizers. Its distillation experiments and length-weight sweeps support sequence-level matching, with benefits that depend on the weighting choice.

- **[OPD-Aha: From Linguistic Momentum to Visual Reflection in Multimodal On-Policy Distillation](https://arxiv.org/abs/2609.16459)**  
  <sub>2026-09-15 · Direct OPD · [Code](https://github.com/Echochef/OPD-Aha)</sub>  
  The method contrasts one privileged-vision teacher's predictions with a real image and a visual null under the same student-generated prefix, then distills a reconstructed target on that rollout. It addresses erroneous prefixes that can obscure visual correction; reflection tokens are an observed effect, not an explicit target.

- **[Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition](https://arxiv.org/abs/2609.14708)**  
  <sub>2026-09-13 · Hybrid OPD · [Code](https://github.com/jet-ai-projects/Lightning-Weave)</sub>  
  Lightning Weave combines aligned policy shifts into an explicit target on cached student states and fits a finite-support log-residual loss. Its composition comparisons favor joint target construction over data mixing and sequential application, while full-vocabulary KL identities do not transfer unchanged to the implemented surrogate.

- **[CompassOPD: Cross-Family On-Policy Distillation via Within-Family Likelihood Shifts](https://arxiv.org/abs/2609.10154)**  
  <sub>2026-09-09 · Direct OPD</sub>  
  CompassOPD scores student-generated actions with a strong teacher and a weaker reference from the same family, transferring their likelihood shift rather than the cross-family offset. A frozen initial student anchors updates; the evaluated MoE variant obtains its reference by reducing expert activation.

- **[Teacher Should Think Ahead: Adaptive Continuations for Reliable On-Policy Distillation](https://arxiv.org/abs/2609.22254)**  
  <sub>2026-09-06 · Hybrid OPD</sub>  
  AC-OPD supplements sampled-token OPD on student rollouts with teacher continuations from selected prefix anchors. It adapts how many branch tokens receive cross-entropy supervision using uncertainty and path-divergence proxies; a shuffled-length control tests local length assignment. Candidate branches are generated before masking, so shorter supervision does not itself save teacher decoding.

- **[RISE: Recursive Improvement via Self-Extrapolating Policy Distillation](https://arxiv.org/abs/2609.05295)**  
  <sub>2026-09-04 · Hybrid OPD</sub>  
  After a reward-based policy update, this method extrapolates from a trailing checkpoint in weight or logit space to form a refreshed teacher, then distills its token distributions into the student. Distillation reuses pre-update rollouts, making their contexts mildly off-policy for the updated student.

- **[Verify Before You Distill: Prompt-Level Teacher Gating for On-Policy Distillation](https://arxiv.org/abs/2609.02998)**  
  <sub>2026-09-02 · Hybrid OPD</sub>  
  Verifier-scored teacher probes estimate reliability for each prompt before its student rollouts receive supervision. A passing prompt uses token-level on-policy distillation; a failing one uses group-relative verifier rewards instead, with no blended update. The fallback yields no update when every student rollout has the same reward.

- **[Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Multi-Domain LLMs](https://arxiv.org/abs/2609.02548)**  
  <sub>2026-09-02 · Direct OPD · [Code](https://github.com/hexixiang/MT-SDPO)</sub>  
  MT-SDPO uses correct student peers as anchors and admits frozen teachers whose cached answers pass verification. Sanitized critiques condition a privileged moving-average self-teacher that supervises student tokens. The answer check does not certify subsequent critiques; evaluation uses multiple-choice science questions.

- **[Distill Skills into Weights, Not Prompts: Abstract Skills as Privileged Signals for On-Policy Self-Distillation](https://arxiv.org/abs/2608.09826)**  
  <sub>2026-08-10 · Hybrid OPD</sub>  
  SKALD scores question-only student rollouts with a shared-parameter teacher given answer-filtered abstract skill cards, combining gated, annealed tilted cross-entropy with group-relative reward optimization. Its fixed gate estimates initial teacher advantage, not whether the moving teacher remains better throughout training.

- **[PAST: Privileged Adaptation from Complete Student Trajectories for On-Policy Self-Distillation](https://arxiv.org/abs/2608.08726)**  
  <sub>2026-08-09 · Hybrid OPD</sub>  
  PAST adapts a hindsight-conditioned teacher using completed student trajectories, then distills it on original student prefixes. A fixed-step factorial comparison supports the combined recipe in the evaluated setting, without a universal guarantee for future-conditioned supervision.

- **[OPD-V: Visual On-Policy Self-Distillation with Modality Balance](https://arxiv.org/abs/2608.05131)**  
  <sub>2026-08-05 · Direct OPD · [Code](https://github.com/aniri15/OPD-V)</sub>  
  OPD-V uses an EMA self-teacher on an evidence-centered crop to supervise student rollouts from the original image. A positive log-probability margin over a masked-crop teacher both gates and weights Jensen–Shannon matching. The margin is a relative visual-context proxy, not a certificate of correctness or modality balance.

- **[SMOPD: Multi-Reward Reinforcement Learning via Specialize-and-Merge Online Policy Distillation](https://arxiv.org/abs/2608.03092)**  
  <sub>2026-08-04 · Hybrid OPD</sub>  
  SMOPD merges reward-specialized teachers on student-generated prefixes and combines distillation with a balanced task-reward anchor. Its explicitly defined sampled reverse-KL variant supports the merging recipe, while the default candidate-pooling target and claims about divergence direction require qualification.

- **[Rubrics as Privileged Information for Open-Ended Generation](https://arxiv.org/abs/2608.02948)**  
  <sub>2026-08-03 · Direct OPD</sub>  
  For open-ended responses, a self-teacher sees natural-language rubrics while the student generates prefixes without them; clipped token-level reverse KL transfers the teacher’s distribution rather than a scalar rubric reward. The main full-finetuning variant uses an EMA teacher, while an adapter variant uses a frozen-base teacher.

- **[Self-Improving Large Language Models via Progressive Experience Evolution](https://arxiv.org/abs/2608.02139)**  
  <sub>2026-08-03 · Hybrid OPD · [Code](https://github.com/rrrsj/SPEE)</sub>  
  SPEE consolidates experience from successful and failed trajectories into privileged self-teacher context for distillation on student-generated prefixes, followed by GRPO. Its reported single-round results support the combined experience-distillation recipe without establishing sustained improvement across repeated training cycles.

- **[Is More Privileged Information Better? From Solution Traces to Problem-Solving Structure in Self-Distilled Reasoning](https://arxiv.org/abs/2608.01589)**  
  <sub>2026-08-03 · Direct OPD</sub>  
  PS-OPSD compares complete reference solutions with structured problem-space guidance for the teacher while retaining the same student-prefix distillation objective. Mismatched and path-corrupted guidance test content, and checkpoint-specific results qualify claims of uniform improvement.

- **[Weak-to-Strong On-Policy Distillation](https://arxiv.org/abs/2607.26246)**  
  <sub>2026-07-28 · Direct OPD · [Code](https://github.com/Yu-Fangxu/W2S-OPD)</sub>  
  W2S-OPD forms a proxy teacher by adding the logit difference between weaker positive and negative sources to a frozen copy of the student’s base model, then distills it on student-generated rollouts. The tested contrasts and evaluations concern mathematical reasoning and code generation.

- **[Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation](https://arxiv.org/abs/2607.23125)**  
  <sub>2026-07-25 · Direct OPD</sub>  
  On corrupted-image student rollouts, a vision-language model matches its own stopped-gradient clean-image token distribution using reverse KL. The teacher view shares the student’s parameters rather than supplying external answers; the method depends on visual input corruption.

- **[Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization](https://arxiv.org/abs/2607.22334)**  
  <sub>2026-07-24 · Direct OPD</sub>  
  BPM maps teacher probability mass to student byte-prefix cells and a residual cell, with a separate stop-token bridge. Its exactness depends on stated tokenization assumptions; realized-path spanning corrections lower-bound the full marginal. Alignment masks and divergence choices affect the reported cross-tokenizer results.

- **[Contrastive On-Policy Distillation](https://arxiv.org/abs/2607.19046)**  
  <sub>2026-07-21 · Teacher-mediated RL</sub>  
  COPD uses light-versus-heavy-context teacher log-likelihood differences as token-level policy rewards on student-generated prefixes, rather than directly matching a teacher distribution. Its reported comparisons improve average accuracy–length trade-offs over tested OPD baselines, including with a frozen initial-model scorer, while exposing task-specific compression losses.

- **[LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110)**  
  <sub>2026-07-20 · Direct OPD</sub>  
  For open-ended tasks, a coach turns rubric assessments of policy-generated responses into reusable textual advice that conditions a teacher for token-level reverse-KL distillation along student rollouts. The coach supplies context rather than token probabilities, and the teacher may be frozen or iteratively updated.

- **[Trace-Based On-Policy Distillation for Masked Diffusion Language Models](https://arxiv.org/abs/2607.16872)**  
  <sub>2026-07-18 · Direct OPD</sub>  
  TOPD samples a masked diffusion student’s denoising trajectories and retains token decisions that survive into the final response. A frozen teacher supervises matching partially denoised states through reverse KL, implemented with sampled-token updates; the transfer experiments focus on mathematical reasoning.

- **[Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](https://arxiv.org/abs/2607.10805)**  
  <sub>2026-07-12 · Direct OPD</sub>  
  AD-OPSD blends a frozen base-model prior into privileged teacher targets at high-entropy positions where sampled tokens face suppression. This selective gate addresses declining epistemic-token density while retaining other teacher corrections; the diagnosis and evaluations focus on mathematical reasoning.

- **[Mach-Mind-4-Flash Technical Report](https://arxiv.org/abs/2607.09375)**  
  <sub>2026-07-10 · Direct OPD</sub>  
  Mach-Mind reports routed multi-teacher OPD and a teacher-pool comparison that adds a code expert while holding other components fixed. The added expert improves several measured domains, but full consolidation still retains specialist gains unevenly.

- **[Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394)**  
  <sub>2026-07-06 · Direct OPD</sub>  
  Direct-OPD uses a fixed teacher’s post-/pre-RL log-probability contrast as an immediate reward on student prefixes, with a separate reference penalty to the student’s initialization. Its reported AIME results improve students already stronger than the post-RL teacher; this is an adjacent reward-transfer comparison, not an established exact teacher-policy matching gradient.

- **[dOPSD: On-Policy Self-Distillation for Diffusion Language Models](https://arxiv.org/abs/2607.04428)**  
  <sub>2026-07-05 · Direct OPD · [Code](https://github.com/tuandattt/dOPSD)</sub>  
  For diffusion language models, dOPSD matches predictions at masked positions in a student decoding state to stop-gradient predictions from later states of the same trajectory. Its reported training keeps only final-answer-correct rollouts; the teacher’s extra context does not come from a reference solution.

- **[DOPD: Dual On-policy Distillation](https://arxiv.org/abs/2606.30626)**  
  <sub>2026-06-29 · Analysis</sub>  
  DOPD’s token-removal controls compare dropping equal fractions of high-gap, low-gap, or random tokens. Removing tokens with the largest privileged teacher–student log-probability gap is more damaging in the tested language and vision-language settings; this does not establish that the gap isolates transferable capability.

- **[MOPD: Multi-Teacher On-Policy Distillation for Capability Integration in LLM Post-Training](https://arxiv.org/abs/2606.30406)**  
  <sub>2026-06-29 · Direct OPD</sub>  
  After independently training domain specialists from a shared checkpoint, MOPD routes each student-generated trajectory to its matching frozen teacher for token-level supervision. It studies clipped sampled-token policy-gradient and corrected top-token distillation implementations; its teacher-replacement experiment shows a limitation when teacher and student distributions differ.

- **[Masked Self-Distillation: Internalizing the Chain-of-Thought in Language Models](https://arxiv.org/abs/2607.22629)**  
  <sub>2026-06-18 · Direct OPD</sub>  
  Masked distillation trains on student-sampled continuations using reverse KL toward a teacher conditioned on a collected reasoning trace. A suffix scaffold controls how much reasoning remains explicit; complete trace removal can fail in the evaluated puzzle setting.

- **[Be My Tutor: On-Policy Co-Distillation for Mutual LLM Improvement via Peer Feedback](https://arxiv.org/abs/2606.14368)**  
  <sub>2026-06-12 · Analysis</sub>  
  OPCoD studies peer feedback for privileged self-distillation. A diagnostic using initial models compares how often feedback damages correct answers, independently of the alternating-training procedure. It provides evidence about tutor-feedback risk.

- **[Rubric-Guided Self-Distillation: Post-Training Without Rubric Verifiers](https://arxiv.org/abs/2606.12507)**  
  <sub>2026-06-10 · Direct OPD</sub>  
  Rubric-Guided Self-Distillation matches a frozen, rubric-conditioned base teacher on student-generated prefixes without rollout-level judge calls during training. Rubrics may contain answer-specific facts, and the reported comparison with GRPO depends on the training judge and model family.

- **[RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation](https://arxiv.org/abs/2606.11709)**  
  <sub>2026-06-10 · Hybrid OPD · [Code](https://github.com/THU-BPM/RLCSD)</sub>  
  RLCSD separately tests contrastive teacher targets within an OPSD plugin, using helpful and incorrect contexts to alter student-prefix supervision. That distillation experiment is distinct from the paper's main verifier-advantage modulation algorithm.

- **[Beyond Absolute Imitation: Anchored Residual Guidance for Privileged On-Policy Distillation](https://arxiv.org/abs/2606.10385)**  
  <sub>2026-06-09 · Direct OPD</sub>  
  AR-OPD constructs a teacher target from a partially privileged view plus a fixed-strength, clipped log-probability residual from the full privileged view. It applies forward-KL matching on student-generated prefixes; the public implementation uses EMA teacher weights for both views. Its context and residual-strength comparisons do not establish a general no-leakage guarantee.

- **[Breaking the Tokenizer Barrier: On-Policy Distillation across Model Families](https://arxiv.org/abs/2606.09456)**  
  <sub>2026-06-08 · Direct OPD · [Code](https://github.com/ivanniu/On-Policy-Distill)</sub>  
  This cross-tokenizer method aligns student responses and teacher retokenizations into synchronized text chunks, then distributes teacher path likelihoods across student tokens. Two post-SFT comparisons evaluate the full recipe; they do not prove optimal allocation or lossless vocabulary mapping.

- **[Thinking Without Images: Internalizing Visual Manipulation with On-Policy Self-Distillation](https://arxiv.org/abs/2606.08719)**  
  <sub>2026-06-07 · Direct OPD</sub>  
  A student generates textual visual-inspection traces from the original image, while a fixed self-teacher scores the same prefixes with annotated-region crops and the answer. Token-level reverse-KL training transfers that guidance without test-time crops; training requires region annotations.

- **[Data-Efficient Autoregressive-to-Diffusion Language Models via On-Policy Distillation](https://arxiv.org/abs/2606.06712)**  
  <sub>2026-06-04 · Direct OPD · [Code](https://github.com/divelab/OPDLM)</sub>  
  OPDLM converts an autoregressive model into a diffusion language model by matching a frozen AR teacher at masked positions on student-generated denoising states. A block-size-four ablation finds comparable performance with random remasking of student completions, separating completion source from state selection.

- **[Learning Visual Spatial Planning from Symbolic State via Modality-Gap-Aware Self-Distillation](https://arxiv.org/abs/2606.06076)**  
  <sub>2026-06-04 · Direct OPD · [Code](https://github.com/Oranger-l/MGSD)</sub>  
  MGSD supervises visual student rollouts with a frozen self-teacher that receives privileged symbolic states and reference plans. Ablations distinguish the roles of perceptual preparation, symbolic information, reference plans, and teacher stability in the tested spatial-planning tasks.

- **[OPRD: On-Policy Representation Distillation](https://arxiv.org/abs/2606.06021)**  
  <sub>2026-06-04 · Direct OPD · [Code](https://github.com/ShenzhiYang2000/OPRD)</sub>  
  OPRD matches teacher hidden states on student-generated responses, with an optional frozen low-rank bridge for different architectures. Same-architecture comparisons support representation supervision and measured resource benefits, while heterogeneous transfer does not uniformly outperform output-space OPD.

- **[DuDi: Dual-Signal Distillation with Cross-Lingual Verbalizer](https://arxiv.org/abs/2606.04694)**  
  <sub>2026-06-03 · Hybrid OPD</sub>  
  DuDi combines live comparisons between ground-truth and student-generated responses with token distillation on both corpus responses and student rollouts. A cross-lingual demonstration prompt conditions the teacher’s token feedback; the evaluated multilingual setup does not establish a mapping between heterogeneous tokenizers.

- **[Constitutional On-Policy Safe Distillation](https://arxiv.org/abs/2606.03089)**  
  <sub>2026-06-02 · Direct OPD</sub>  
  COPSD calibrates a constitution-conditioned teacher with Cross-SFT before distilling on student-generated responses. Same-data teacher comparisons and calibration-data ablations examine the resulting safety–utility tradeoff; the proposed geometric explanation remains separate from this empirical evidence.

- **[Weak Critics Make Strong Learners: On-Policy Critique Distillation for Scalable Oversight](https://arxiv.org/abs/2606.00424)**  
  <sub>2026-05-29 · Direct OPD · [Code](https://github.com/jiakanglee/OPCD-Weak_critiques_strong)</sub>  
  On-Policy Critique Distillation uses a weaker critic to condition a frozen view of the stronger student, which supplies token targets on filtered student answers. The alignment results support the complete filtering-and-distillation recipe, while the reasoning experiment's loss description remains unresolved.

- **[Skill-Conditioned Gated Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.28791)**  
  <sub>2026-05-27 · Direct OPD · [Code](https://github.com/walawalagoose/SGSD)</sub>  
  The student samples from a plain problem prompt while skill-and-mistake-conditioned self-teachers score that same rollout. Verifier outcomes determine whether each teacher’s support should be followed, reversed, or ignored; a gated sampled-token loss limits weak and extreme disagreements rather than assuming retrieved skills are trustworthy.

- **[Beyond Imitation: Reflective On-Policy Self-Distillation for LLM Reasoning](https://arxiv.org/abs/2605.28014)**  
  <sub>2026-05-27 · Direct OPD · [Code](https://github.com/ZiqiZhao1/ROSD)</sub>  
  A self-reflector compares incorrect on-policy rollouts with successful ones to supply a corrective idea and locate the first error. The idea conditions a self-teacher, while distillation skips the valid prefix; correct rollouts and unmatched error quotes receive full-response supervision.

- **[Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation](https://arxiv.org/abs/2605.27115)**  
  <sub>2026-05-26 · Direct OPD</sub>  
  CaMOPD alternates general-capability recovery and domain-preservation updates on student rollouts. It selects recovery samples by absolute teacher–student log-probability gaps and preservation samples by positive gaps; experiments use proxy general prompts and cover role-play dialogue and medical reasoning.

- **[On-Policy Consistency Training Improves LLM Safety with Minimal Capability Degradation](https://arxiv.org/abs/2605.21834)**  
  <sub>2026-05-20 · Direct OPD</sub>  
  OPCT scores student-generated responses with a frozen self-teacher receiving a paired clean or safety-informed prompt. Its safety and capability comparisons support contrastive-input distillation over the tested offline consistency-training recipes, without isolating online sampling from other training differences.

- **[AVSD: Adaptive-View Self-Distillation by Balancing Consensus and Teacher-Specific Privileged Signals](https://arxiv.org/abs/2605.20643)**  
  <sub>2026-05-20 · Direct OPD · [Code](https://github.com/duykhuongnguyen/AVSD)</sub>  
  AVSD combines privileged views of the same model on student-generated trajectories. A geometric consensus anchors the target, while gated view-specific residuals adjust it; the student learns through reverse KL. Evaluation covers mathematical and code reasoning, with broader agent applications left untested.

- **[It Takes Two: Complementary Self-Distillation for Contextual Integrity in LLMs](https://arxiv.org/abs/2605.20258)**  
  <sub>2026-05-18 · Direct OPD · [Code](https://github.com/sw-programmer/SelfCI)</sub>  
  On student-generated responses, two feedback-conditioned self-teachers separately guide task-relevant retention and minimal disclosure through weighted token-level reverse KL, inducing a product-of-experts target. The construction uses explicit attribute partitions and synthetic disclosure decisions, and evaluation focuses on final responses.

- **[Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation](https://arxiv.org/abs/2605.18740)**  
  <sub>2026-05-18 · Direct OPD · [Code](https://github.com/VisionOPD/Vision-OPD)</sub>  
  Vision-OPD uses an EMA teacher conditioned on a regional crop to supervise student rollouts from the full image with bounding-box and spatial-prompt guidance during training. Its default Jensen–Shannon objective uses student top-100 tokens plus a residual tail; comparisons evaluate the regional-to-global recipe.

- **[Self-Supervised On-Policy Distillation for Reasoning Language Models](https://arxiv.org/abs/2605.17497)**  
  <sub>2026-05-17 · Hybrid OPD</sub>  
  SSOPD adds frontier-weighted, pointwise-clipped forward KL to verifier-based policy optimization. A fixed self-teacher sees the shortest correct group completion while supervising early prefixes of the longest wrong completion; this auxiliary signal requires a rollout group containing both successes and failures.

- **[Learning with Rare Success but Rich Feedback via Reflection-Enhanced Self-Distillation](https://arxiv.org/abs/2605.12741)**  
  <sub>2026-05-12 · Direct OPD · [Code](https://github.com/horizon-llm/RESD)</sub>  
  After a student rollout fails, RESD uses environmental feedback to generate a retrospective diagnosis and curate reusable lessons in a persistent playbook. That context guides a self-teacher’s token-level supervision on student rollouts, including when successful demonstrations are unavailable; it requires informative feedback.

- **[Multi-Rollout On-Policy Distillation via Peer Successes and Failures](https://arxiv.org/abs/2605.12652)**  
  <sub>2026-05-12 · Hybrid OPD · [Code](https://github.com/viviable/mopd_code)</sub>  
  For each prompt, the student generates multiple rollouts that a verifier divides into successes and failures. A teacher uses other rollouts from the group to supervise each target rollout through token-level divergence; the approach depends on reliable success labels and available peers.

- **[OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit Steering for LLM Reasoning](https://arxiv.org/abs/2605.12400)**  
  <sub>2026-05-12 · Direct OPD</sub>  
  OGLS-SD contrasts teacher logits conditioned on successful and failed guidance pools to form targets for failed student prefixes. A fixed base teacher supplies the distributions; short successful rollouts add tail SFT. Local ablations test steering and tail regularization.

- **[Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning](https://arxiv.org/abs/2605.11458)**  
  <sub>2026-05-12 · Direct OPD</sub>  
  Adaptive Teacher Exposure varies how much reference information the self-teacher sees. Fixed-exposure sweeps and internal controller comparisons study this design choice; headline results use benchmark-specific checkpoint selection and partly imported baselines.

- **[Crosslingual On-Policy Self-Distillation for Multilingual Reasoning](https://arxiv.org/abs/2605.09548)**  
  <sub>2026-05-10 · Direct OPD · [Code](https://github.com/cisnlp/COPSD)</sub>  
  COPSD trains on reasoning generated from low-resource-language problems, using a frozen self-teacher with privileged English translations and reference solutions. Experiments use full-vocabulary reverse KL on the same student prefixes; only the student is updated, and training requires English reference solutions.

- **[Training with Harnesses: On-Policy Harness Self-Distillation for Complex Reasoning](https://arxiv.org/abs/2605.08741)**  
  <sub>2026-05-09 · Direct OPD · [Code](https://github.com/zzy1127/OPHSD-On-Policy-Harness-Self-Distillation)</sub>  
  OPHSD prepares teacher context through a dynamic reasoning harness and supervises direct student rollouts with a frozen initial teacher. Comparisons with static privileged context evaluate the complete preparation recipe, including additional harness computation.

- **[SimCT: Recovering Lost Supervision for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2605.07711)**  
  <sub>2026-05-08 · Direct OPD · [Code](https://github.com/sunjie279/SimCT-)</sub>  
  SimCT compares teacher and student on shared tokens plus short text continuations jointly expressible under different tokenizers, using student-generated prefixes and retaining the reverse-KL OPD loss. Its normalized candidate scores are not a probability-preserving mapping of all continuations.

- **[UniSD: Towards a Unified Self-Distillation Framework for Large Language Models](https://arxiv.org/abs/2605.06597)**  
  <sub>2026-05-07 · Analysis · [Code](https://github.com/Ahren09/UniSD)</sub>  
  UniSD compares self-distillation variants using EMA targets, contrastive supervision, representation matching, and divergence clipping. Task-dependent results inform comparison of these components; they do not establish a benefit from the sequence-agreement scalar that cancels under the stated normalization.

- **[Multilingual Safety Alignment via Self-Distillation](https://arxiv.org/abs/2605.02971)**  
  <sub>2026-05-03 · Direct OPD</sub>  
  The on-policy MSD variant uses a frozen teacher initialized from the same model, conditioned on a parallel English query and safety-reasoning instruction, to supervise student-generated prefixes through weighted reverse KL. Its DPSW weights combine teacher confidence with student disagreement; high weight is not a certificate of causal safety relevance.

- **[MAD-OPD: Breaking the Ceiling in On-Policy Distillation via Multi-Agent Debate](https://arxiv.org/abs/2605.01347)**  
  <sub>2026-05-02 · Direct OPD · [Code](https://github.com/chiefovoavicii/MAD-OPD)</sub>  
  MAD-OPD uses a confidence-weighted sum of losses to debate-conditioned teachers. Agent training uses sampled actions on ToolACE step instances; complete histories need not come from the current student. Debate alone helps code but slightly lowers the agentic ablation average, while confidence weighting helps both.

- **[Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding](https://arxiv.org/abs/2605.00642)**  
  <sub>2026-05-01 · Analysis · [Code](https://github.com/zhangyan-ucas/GUI-SD-code)</sub>  
  GUI-SD compares privileged visual interfaces for GUI grounding. Its box-and-hint condition yields higher student grounding accuracy than textual coordinates despite lower teacher accuracy, showing that teacher accuracy alone does not determine transfer utility in the tested setting.

- **[Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL](https://arxiv.org/abs/2604.28123)**  
  <sub>2026-04-30 · Teacher-mediated RL · [Code](https://github.com/XIAO4579/PRISM)</sub>  
  PRISM inserts an adversarial pre-alignment stage between multimodal SFT and verifiable-reward RL, using separate perception and reasoning discriminators. Stage and discriminator comparisons support this teacher-mediated training recipe without establishing exact distribution matching or complete correction of rollout shift.

- **[Co-Evolving Policy Distillation](https://arxiv.org/abs/2604.27083)**  
  <sub>2026-04-29 · Hybrid OPD</sub>  
  CoPD alternates capability-specific reward-based training with bidirectional distillation between evolving branches, each learning from its own rollouts scored by another branch. The evaluated consolidation covers text and image reasoning, with a separate three-branch setting adding video.

- **[PAINT: Partial-Solution Adaptive Interpolated Training for Self-Distilled Reasoners](https://arxiv.org/abs/2604.26573)**  
  <sub>2026-04-29 · Direct OPD</sub>  
  PAINT studies how much reference-solution context a fixed self-teacher should receive when supervising student rollouts. Its masking-only comparisons vary overlap-dependent disclosure and block placement with target interpolation disabled, favoring moderate suffix masking in the tested Qwen3-1.7B setup.

- **[Distillation Traps and Guards: A Calibration Knob for LLM Distillability](https://arxiv.org/abs/2604.18963)**  
  <sub>2026-04-21 · Direct OPD</sub>  
  Distillability calibration modifies a teacher using task rewards, an original-teacher anchor, and a smaller proxy model before running student-side GKD. Opposite calibration directions produce different student outcomes under the tested recipe, without establishing universal protection against extraction.

- **[OPSDL: On-Policy Self-Distillation for Long-Context Language Models](https://arxiv.org/abs/2604.17535)**  
  <sub>2026-04-19 · Direct OPD</sub>  
  OPSDL uses short-context predictions of the same model to guide responses generated from long context. Multi-scale RULER and LongBench V2 comparisons evaluate the full recipe, without isolating every data-construction component or establishing the claimed gradient guarantee.

- **[π-Play: Multi-Agent Self-Play via Privileged Self-Distillation without External Data](https://arxiv.org/abs/2604.14054)**  
  <sub>2026-04-15 · Hybrid OPD · [Code](https://github.com/zhyaoch/pi-play)</sub>  
  In search-agent self-play, an examiner constructs questions and their search paths; a path-conditioned teacher supervises unprivileged student rollouts while the student also learns from outcome rewards. The teacher tracks the student by moving average, and evaluation is limited to search tasks.

- **[Self-Distillation Zero: Self-Revision Turns Binary Rewards into Dense Supervision](https://arxiv.org/abs/2604.12002)**  
  <sub>2026-04-13 · Direct OPD · [Code](https://github.com/princeton-pli/Self-Distillation-Zero)</sub>  
  After training on verified self-revisions, SD-Zero samples generator responses and uses a reviser conditioned on each response and its binary reward to provide token-level targets. The reviser is frozen between synchronizations; the method requires a binary verifier and successful revision traces.

- **[CRISP: Compressed Reasoning via Iterative Self-Policy Distillation](https://arxiv.org/abs/2603.05433)**  
  <sub>2026-03-05 · Direct OPD · [Code](https://github.com/HJSang/CRISP_Reasoning_Compression)</sub>  
  This reasoning-compression method scores student-generated continuations with a self-teacher given a conciseness instruction, then minimizes token-level reverse KL with periodic teacher refreshes. The teacher receives no ground-truth solution, and excessive compression can hurt harder problems.

- **[GATES: Self-Distillation under Privileged Context with Consensus Gating](https://arxiv.org/abs/2602.20574)**  
  <sub>2026-02-24 · Hybrid OPD</sub>  
  A model samples document-conditioned tutor reasoning, uses agreement on final answers to gate training, and teaches its document-free role through eligible full trajectories. Training is primarily off-policy imitation, supplemented by student-rollout updates; consensus can still reflect shared tutor errors.

- **[Privileged Information Distillation for Language Models](https://arxiv.org/abs/2602.04942)**  
  <sub>2026-02-04 · Analysis</sub>  
  The study compares privileged-information transfer through teacher-sampled π-Distill and a separate student-sampled OPSD procedure. Its experiments vary information type, model and objective strength, including failure cases. The teacher-sampled main algorithm and the on-policy comparison should be distinguished.

- **[Expanding the Capabilities of Reinforcement Learning via Text Feedback](https://arxiv.org/abs/2602.02482)**  
  <sub>2026-02-02 · Hybrid OPD</sub>  
  In two-turn training, the policy revises its own answer after receiving a critique. Self-distillation uses reward-weighted revisions to train the original-prompt policy, while a separate variant predicts critiques alongside multi-turn RL. Both target first-turn performance when external feedback is unavailable at inference.

- **[Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802)**  
  <sub>2026-01-28 · Direct OPD · [Code](https://github.com/lasgroup/SDPO)</sub>  
  SDPO samples current-policy attempts, then conditions that policy on feedback to re-evaluate those attempts as a self-teacher and distills its next-token distributions into the student. When only scalar outcomes are available, successful attempts can supply feedback; the mechanism relies on the model’s ability to use that context.

- **[Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)**  
  <sub>2026-01-26 · Direct OPD · [Code](https://github.com/siyan-zhao/OPSD)</sub>  
  OPSD distills a reference-solution-conditioned teacher into a problem-only student on the student’s rollout prefixes. Its main experiments freeze the initial teacher and use full-vocabulary forward KL with pointwise clipping; the reported selected-checkpoint comparisons favor OPSD over GRPO at 1.7B, 4B, and 8B.

- **[CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation](https://arxiv.org/abs/2601.16547)**  
  <sub>2026-01-23 · Hybrid OPD</sub>  
  CORD aligns audio-generated prefixes with text-conditioned predictions through divergence- and position-weighted reverse KL, alongside judge-rewarded sequence optimization. A cumulative comparison supports a small additional benefit from weighting, while the joint rollout-group configuration remains unclear.

- **[Stable On-Policy Distillation through Adaptive Target Reformulation](https://arxiv.org/abs/2601.07155)**  
  <sub>2026-01-12 · Direct OPD · [Code](https://github.com/jjun-0824/Veto)</sub>  
  Veto forms a product target from teacher probabilities and a detached student contribution. Its fixed-coefficient comparison tests target reweighting independently of annealing; the paper's parameter-gradient stability guarantee is not established by that empirical result.

- **[Black-Box On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2511.10643)**  
  <sub>2025-11-13 · Teacher-mediated RL · [Code](https://github.com/microsoft/LMOps/tree/main/gad)</sub>  
  GAD trains a discriminator to score teacher responses above current student responses, then uses its scalar score as reinforcement-learning feedback for student rollouts. This permits black-box teacher access, but the feedback is a learned response-level proxy, not teacher token probabilities.

- **[A Dual-Space Framework for General Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2504.11426)**  
  <sub>2025-04-15 · Direct OPD · [Code](https://github.com/songmzhang/DSKDv2)</sub>  
  DSKD constructs comparable teacher and student output spaces through learned projections. Cross-tokenizer losses use exactly aligned positions; the student-space term also masks positions where the projected teacher fails to reproduce its top prediction. The method does not provide a lossless mapping between arbitrary tokenizers.

- **[PromptKD: Distilling Student-Friendly Knowledge for Generative Language Models via Prompt Tuning](https://arxiv.org/abs/2402.12842)**  
  <sub>2024-02-20 · Direct OPD · [Code](https://github.com/gmkim-ai/PromptKD)</sub>  
  On student-generated responses, PromptKD alternates student-guided tuning of soft teacher prompts with reverse-KL updates of the student toward the prompted teacher. Teacher weights stay fixed, while an early, decaying regularizer limits how far the prompted teacher departs from its unprompted distribution.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-6"></a>

<a id="data-and-training-dynamics"></a>

<details><summary><strong>Data and training dynamics</strong> &nbsp;·&nbsp; 71</summary>

*Which states, tokens, and training stages matter?*

- **[MetaOPD: Meta-Learned Token Weighting for On-Policy Distillation](https://arxiv.org/abs/2610.11989)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  MetaOPD learns token weights for student-rollout distillation through a one-step reference-loss meta-update; in its reported Qwen3 math experiments it improves aggregate scores over uniform OPD, at roughly twice the measured training cost in the 1.7B setting.

- **[DIAL-OPD: Learning More from Fewer Tokens in On-Policy Distillation](https://arxiv.org/abs/2610.11659)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  DIAL-OPD ranks student-generated token positions using both teacher–student log-ratio magnitude and probability scale, then applies the original signed OPD update only at selected positions. Random-thinning, targeted-replacement, and probability-weighting comparisons support this allocation strategy in the reported mathematical-reasoning settings.

- **[ReCal: Calibrating Structured Pruning for On-Policy Distillation Recovery](https://arxiv.org/abs/2610.11332)**  
  <sub>2026-10-08 · Hybrid OPD</sub>  
  ReCal changes pruning calibration before a shared OPD recovery stage; its fixed-prefix 8B-Wanda diagnostic reduces high-damage residual KL. AIME terminal scores improve in seven of eight settings, while IFBench falls in all eight; better final scores need not mean greater marginal OPD recovery.

- **[When Do We Need On-Policy Distillation? Distilling on Offline Student Rollouts Is Often Better](https://arxiv.org/abs/2610.11291)**  
  <sub>2026-10-08 · Analysis</sub>  
  Across 17 reported teacher–student pairs, distillation on cached initial-student rollouts usually outperformed continually refreshed OPD rollouts on math evaluations; initial token overlap and rollout quality helped characterize when this trade-off changed.

- **[On-Policy Distillation with Negative-Policy Rollouts](https://arxiv.org/abs/2610.07874)**  
  <sub>2026-10-06 · Hybrid OPD</sub>  
  Negative-policy rollouts, mixed with or substituted for student rollouts, improved reported teacher-supervised reasoning results across several tested OPD formulations; token-level diagnostics support a teacher-relative shift, while fully negative-policy training is offline rather than strictly on-policy.

- **[Flash-OPD: Fast On-Policy Distillation](https://arxiv.org/abs/2610.06105)**  
  <sub>2026-10-05 · Direct OPD</sub>  
  Flash-OPD verifies teacher–student compatibility during student rollout collection and stops trajectories individually at a defined event-count boundary. Across the reported model pairs, its full training recipe substantially reduces wall-clock time while generally preserving average accuracy, although the results do not isolate every source of the speedup.

- **[Transfer-Stratified On-Policy Distillation for RL-Improved Reasoning Teachers](https://arxiv.org/abs/2610.05974)**  
  <sub>2026-10-05 · Direct OPD</sub>  
  For GRPO-improved reasoning teachers, transfer-stratified OPD combines pretraining teacher–student success strata with per-stratum KL routing and token gating; matched-pool controls show that routing and gating, rather than filtering alone, improve reported macro-average correctness in the tested Qwen3 mathematics setting.

- **[Finetuning with Sampling: SFT Learns Better Than You Think](https://arxiv.org/abs/2610.02140)**  
  <sub>2026-10-01 · Offline comparator</sub>  
  Model-matched, expert-conditioned sampling before SFT provides an offline alternative that outperformed the reported OPSD baseline on some chemistry and math evaluations, but not on every task or model; its implemented sampling rule does not inherit the paper’s exact-MH KL guarantee.

- **[Look Before You Select: Rethinking Vocabulary Sparsification in On-Policy Distillation](https://arxiv.org/abs/2609.34386)**  
  <sub>2026-09-28 · Direct OPD</sub>  
  SparseOPD computes full-vocabulary reverse-KL corrections on student-generated prefixes before selecting and compensating a sparse set of logits for backpropagation. At a matched average support budget, it improves all six reported task averages over TopK, while its measured memory benefit comes with additional complete-update time.

- **[Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD](https://arxiv.org/abs/2609.29142)**  
  <sub>2026-09-24 · Direct OPD</sub>  
  This work shows that a teacher’s post-RL versus pre-RL token log-ratio can remain unchanged as the probability mass behind it vanishes. It ranks student-visited states by teacher–reference divergence and retains log-ratio supervision only at the highest-ranked positions within each response.

- **[CLOOPD: Closing the Learner Loop in On-Policy Distillation](https://arxiv.org/abs/2609.24141)**  
  <sub>2026-09-21 · Analysis</sub>  
  CLOOPD compares additional student actor passes on frozen teacher-scored batches. The reported two-to-three-pass control improves the macro score without extra teacher scoring, while a matched-cap random allocator outperforms the proposed adaptive allocator.

- **[Trajectory Learnability for Offline On-Policy Distillation with Imperfect Teachers](https://arxiv.org/abs/2609.18321)**  
  <sub>2026-09-16 · Hybrid OPD</sub>  
  LWD estimates trajectory weights for cached student records by measuring how a reference student changes after learning from teacher-successful problems. Its comparisons favor graded retention over discarding every teacher-failed record, while code-side success labels indicate format validity rather than executable correctness.

- **[SEA-LION-v4.8: A Technical Report](https://arxiv.org/abs/2609.18310)**  
  <sub>2026-09-16 · Direct OPD</sub>  
  SEA-LION-v4.8 documents asynchronous OPD interleaved with SFT across concurrent agent environments. Token-level version tracking, staleness masking, and compressed teacher outputs specify its operating design, without an isolated comparison establishing a universal throughput advantage.

- **[Data-Free On-Policy Distillation: How Far Can We Go Without External Data?](https://arxiv.org/abs/2609.14193)**  
  <sub>2026-09-12 · Direct OPD</sub>  
  Data-Free OPD has the teacher write questions without external seeds or correctness-based selection; extraction, format checks, and deduplication still apply. Student rollouts receive teacher token supervision. Reported peaks, fixed-initial-student coverage diagnostics, and inconsistent empty-prompt results delimit the few-question finding.

- **[Miles v0.1: Production-Level Post-Training](https://arxiv.org/abs/2609.08368)**  
  <sub>2026-09-08 · Direct OPD · [Code](https://github.com/radixark/miles)</sub>  
  Miles integrates teacher log-probability scoring with configurable advantage estimators through served and in-process deployment paths. Its OPD contribution is the scoring and routing interface with explicit tokenizer and architecture constraints, while a five-step example demonstrates use without establishing a system speedup.

- **[Revisiting Complete Reasoning Traces for Post-Training](https://arxiv.org/abs/2609.07103)**  
  <sub>2026-09-07 · Analysis · [Code](https://github.com/naver-ai/revisiting-trace)</sub>  
  A small OPD comparison tests masking the middle 20% of tokens or reasoning steps against unmasked supervision. Step masking gives the highest reported average, while MATH-500 declines, illustrating a setting-dependent tradeoff in supervision coverage.

- **[Teaching a Moving Student: Rethinking the Curriculum of On-Policy Distillation](https://arxiv.org/abs/2609.25048)**  
  <sub>2026-09-06 · Hybrid OPD</sub>  
  R-OPD follows the evolving student before switching to replayed initial-student trajectories when changes in mean gradients become comparable to minibatch variation. Its mathematics experiments examine when revisiting earlier states helps; replayed trajectories are not fresh samples from the current policy.

- **[What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection](https://arxiv.org/abs/2609.05198)**  
  <sub>2026-09-04 · Analysis</sub>  
  This study selects mathematical prompts using teacher and student rollout accuracy, then distills on student-generated responses. Eight selected hard prompts and a random 1K subset both approach the 17K baseline in the reported configuration. Length-capping controls show a bounded selection effect, without isolating length as its sole cause.

- **[Extremely Sparse Supervision Incentivizes Reasoning Ability](https://arxiv.org/abs/2609.04565)**  
  <sub>2026-09-03 · Direct OPD</sub>  
  Sparse-OPD experiments restrict teacher supervision to a few selected tokens on each student trajectory. Random and extreme-signal selections reveal that dense supervision is not always necessary for the tested reasoning gains, while successful sparsification does not consistently reduce teacher-student KL or rollout cost.

- **[Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108)**  
  <sub>2026-09-03 · Hybrid OPD · [Code](https://github.com/StringNLPLAB/opd-rlvr)</sub>  
  This study compares distillation followed by verifier-reward reinforcement learning with joint updates. On logic and mathematics tasks, reverse-KL distillation expands coverage of teacher-supported solutions and subsequent reinforcement learning sharpens that support; this explanation is based on the evaluated training settings.

- **[When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation](https://arxiv.org/abs/2608.27960)**  
  <sub>2026-08-28 · Direct OPD</sub>  
  RA-OPD filters student trajectories when the sign of their aggregate teacher–student log-probability signal conflicts with a verified binary outcome. Retained trajectories receive sampled-token distillation updates. The rule requires outcome verification and selects complete trajectories, leaving their token-level rewards unchanged.

- **[Recovering General Capabilities via Uncertainty-Calibrated Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.26735)**  
  <sub>2026-08-27 · Direct OPD</sub>  
  For recovery after domain specialization, this method samples anchor and exploratory student trajectories, retains exploratory ones with sufficient positive teacher–student signal, then probabilistically filters token updates by agreement with teacher endorsement. It is tested in role-playing and medical settings, not as a general retention guarantee.

- **[D$^3$-MOPD: Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation](https://arxiv.org/abs/2608.24987)**  
  <sub>2026-08-25 · Direct OPD</sub>  
  D3-MOPD adjusts domain prompt sampling using each domain’s remaining normalized reverse KL and recent KL descent during multi-teacher distillation on student rollouts. The reverse-KL update stays unchanged, but the default scheduler can sharply reduce sampling when a domain’s KL temporarily rebounds.

- **[Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress](https://arxiv.org/abs/2608.19408)**  
  <sub>2026-08-19 · Direct OPD</sub>  
  R2-OPD estimates reasoning progress from student continuations, merges adjacent spans with consistent progress signs, and masks reverse-KL supervision where progress and teacher-disagreement rankings conflict. Progress controls which tokens receive distillation; responses without usable estimates retain their original supervision.

- **[Open-MOPD: Diagnosing and Fixing Capability Imbalance in Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2608.19098)**  
  <sub>2026-08-19 · Direct OPD</sub>  
  Open-MOPD studies uneven transfer from oracle-routed domain teachers to a shared student and adjusts domain token shares and remaining-gap weights. Across reused rollout minibatches, it refreshes student-dependent rewards while retaining teacher scores; sampled states and routing are not refreshed.

- **[Training Agents to Evolve with Their Harness: TaoLive Digital Avatar Agent Technical Report](https://arxiv.org/abs/2608.15763)**  
  <sub>2026-08-16 · Hybrid OPD</sub>  
  In TaoLive’s staged agent training, base-model on-policy distillation restored instruction-following scores after fixed-harness SFT; its additional gains were smaller after harness-augmented SFT had largely preserved those capabilities.

- **[Adaptive FastOPD: Progress-Aware Rollout Horizon Expansion for Efficient On-Policy Distillation](https://arxiv.org/abs/2607.29494)**  
  <sub>2026-07-31 · Direct OPD</sub>  
  Adaptive FastOPD expands student rollout horizons when teacher–student signals near the current boundary plateau relative to their starting values and enough rollouts use the available length. It retains token-level teacher supervision; evaluation covers mathematical reasoning with two teacher–student pairs.

- **[SAF-OPD: Stable Advantage Fusion for On-Policy Distillation](https://arxiv.org/abs/2607.29209)**  
  <sub>2026-07-31 · Hybrid OPD</sub>  
  SAF-OPD sparsifies, compresses, and schedules teacher log-ratio advantages before combining them with verifier-based GRPO advantages. Its complete recipe improves over the tested unit-coefficient fusion across three student scales and two domains, without establishing superiority over tuned fixed coefficients.

- **[Pass the Baton: Trajectory-Relayed On-Policy Distillation](https://arxiv.org/abs/2607.26057)**  
  <sub>2026-07-28 · Hybrid OPD · [Code](https://github.com/zju-real/Relay-OPD)</sub>  
  Relay-OPD detects when the teacher favors a reflection token absent from the student’s leading options, then inserts short, budgeted teacher continuations into student rollouts. The student resumes when the budget permits, and distillation uses the resulting mixed trajectories; evaluation focuses on mathematical reasoning.

- **[Solar Open 2 Technical Report](https://arxiv.org/abs/2607.20062)**  
  <sub>2026-07-22 · Direct OPD</sub>  
  Solar Open 2 documents routed full-vocabulary OPD using hidden-state transport and tiled logit reconstruction. Teacher-indexed caching and on-demand pool loading reduce tensor residency and transfer demands, without establishing proportional end-to-end speedups.

- **[CADENCE: Closing the Reasoning Gap via Coverage-Adaptive On-Policy Distillation](https://arxiv.org/abs/2607.16955)**  
  <sub>2026-07-18 · Hybrid OPD</sub>  
  CADENCE adjusts a scheduled token-level distillation update when measured coverage of teacher-preferred tokens exceeds a gate and additionally weights supervision by teacher entropy. Component removals support these choices within the tested reward-assisted recipe, but the coverage statistic is a training-level moving average rather than a per-prompt controller.

- **[Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation for Compressed Reasoning](https://arxiv.org/abs/2607.15736)**  
  <sub>2026-07-17 · Direct OPD · [Code](https://github.com/KawhiC/BIRD)</sub>  
  BIRD first learns verified concise self-generated traces, then performs on-policy matching to a conciseness-conditioned self-teacher. Stage and order comparisons favor this warm start under the reported accuracy-length metric, without isolating prefix quality as the causal mediator.

- **[ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation](https://arxiv.org/abs/2607.13124)**  
  <sub>2026-07-14 · Direct OPD · [Code 1](https://github.com/VisionOPD/Vision-OPD) · [Code 2](https://github.com/icip-cas/ShortX)</sub>  
  ShortOPD recovers a structurally pruned student by distilling its pre-pruning self on student-generated rollouts. A controller shortens future rollout horizons when terminal repetition is high and grows them when clean rollouts hit the limit; detected suffixes do not mask the current batch’s loss.

- **[Can a Language Model Learn Facts Continually in Its Weights?](https://arxiv.org/abs/2607.11020)**  
  <sub>2026-07-13 · Hybrid OPD</sub>  
  In a sequential fact-writing study, distillation on newly sampled student continuations retained more earlier-fact answer accuracy than distillation on reused teacher continuations, although both trailed supervised training on varied examples in the main Qwen3-4B LoRA comparison.

- **[Reward-Gated On-Policy Distillation](https://arxiv.org/abs/2607.04037)**  
  <sub>2026-07-04 · Direct OPD</sub>  
  RG-OPD selects student trajectories using agreement between reward advantages and teacher-student likelihood differences, then retains the same distillation objective on selected records. Its generation-based comparisons support the full gate, while reward-only and likelihood-only contributions are not separately isolated.

- **[Building Multi-Task Agentic LLMs via Two-Phase Distillation](https://arxiv.org/abs/2606.30044)**  
  <sub>2026-06-29 · Hybrid OPD</sub>  
  The method first fits a shared student to pooled trajectories from task-specific reinforcement-learning experts, then refines it on student-generated trajectories scored by the matching expert. The first phase provides initialization for the second, which requires the student to generate useful trajectories.

- **[AsyncOPD: How Stale Can On-Policy Distillation Be?](https://arxiv.org/abs/2606.24143)**  
  <sub>2026-06-23 · Direct OPD · [Code](https://github.com/furiosa-ai/async-opd)</sub>  
  AsyncOPD studies stale student rollouts when teacher scores are cached for limited token sets, then overlaps rollout, teacher scoring and learning. For reverse-KL updates it refreshes the student-dependent advantage and averages importance-weighted local token samples; this addresses sampled actions at fixed prefixes, not stale prefixes.

- **[RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection](https://arxiv.org/abs/2607.24771)**  
  <sub>2026-06-10 · Hybrid OPD</sub>  
  RoCo-ACE uses an EMA teacher to score student rollouts with and without authoritative references, then weights forward-KL distillation using their likelihood contrast. Sparse reference-side cross-entropy supplies factual anchors missing from rollouts; training therefore combines on-policy guidance with supervised reference tokens.

- **[Escaping the KL Agreement Trap in On-Policy Distillation](https://arxiv.org/abs/2606.09471)**  
  <sub>2026-06-08 · Direct OPD</sub>  
  KAT terminates student rollouts when teacher–student KL remains below an adaptively calibrated threshold across consecutive windows. Comparisons with full-rollout, random-stop, and fixed-prefix OPD support a trajectory-dependent accuracy–cost trade-off, with ambiguity in the exact retained-token boundary.

- **[Filter, Then Reweight: Rethinking Optimization Granularity in On-Policy Distillation](https://arxiv.org/abs/2606.02684)**  
  <sub>2026-06-01 · Direct OPD · [Code](https://github.com/YuYingLi0/FiRe-OPD)</sub>  
  FiRe-OPD filters student trajectories by mean teacher likelihood, then reweights retained token updates using teacher confidence and student uncertainty. Component and filtering-rate comparisons evaluate the two-level recipe; increasing the filtering rate does not monotonically improve results.

- **[Internalize the Temperature: On-Policy Self-Distillation as Policy Reheater for Reinforcement Learning](https://arxiv.org/abs/2606.00755)**  
  <sub>2026-05-30 · Direct OPD</sub>  
  Policy Reheater distills a temperature-softened, stop-gradient view of current student logits on fresh student rollouts before restarting RL. Comparisons with hotter sampling and alternative KL directions support parameter-level reheating in a low-entropy regime, while applying it to an untreated base model can be unstable.

- **[RAFT: Data Refinement and Adaptive Distillation for Domain Fine-Tuning with Alleviated Forgetting](https://arxiv.org/abs/2606.00147)**  
  <sub>2026-05-29 · Hybrid OPD</sub>  
  For domain fine-tuning, this pipeline refines answer data before combining supervised learning with distillation on student-generated responses. The original model supplies soft targets using privileged fused-answer context, with adaptive loss balancing; the studied scope is domain adaptation and retention of general capabilities.

- **[Are Full Rollouts Necessary for On-Policy Distillation?](https://arxiv.org/abs/2605.31490)**  
  <sub>2026-05-29 · Direct OPD</sub>  
  This study varies how much of each student-generated rollout receives token-level teacher feedback: one strategy gradually lengthens the training horizon, while another keeps it truncated. Its reasoning results concern training on partial rollouts; evaluation still permits full-length generation.

- **[Trust-Region Behavior Blending for On-Policy Distillation](https://arxiv.org/abs/2605.31159)**  
  <sub>2026-05-29 · Direct OPD</sub>  
  During warmup, a teacher-guided sampling policy stays within a student-centered KL trust region to collect prefixes, while the student retains its per-prefix reverse-KL update. The budget decays to student-only rollouts; online teacher decoding adds warmup overhead.

- **[Less is More: Early Stopping Rollout for On-Policy Distillation](https://arxiv.org/abs/2605.27028)**  
  <sub>2026-05-26 · Analysis</sub>  
  ESR compares fixed-prefix with full-rollout distillation. Same-generation model comparisons report higher averages under fixed-prefix supervision, with setting-dependent gains. This does not establish a dynamic reliability trigger or a cross-tokenizer guarantee.

- **[Not All Disagreement Is Learnable: Token Teachability in On-Policy Distillation](https://arxiv.org/abs/2605.26844)**  
  <sub>2026-05-26 · Analysis · [Code](https://github.com/wyy-code/TA-OPD)</sub>  
  Teachability-Aware OPD weights disagreement by teacher mass on student candidate support to select supervision positions. Fixed-token-budget benchmark comparisons test the resulting allocation rule; its diagnostic gain conventions and one appendix setting label require care.

- **[Backtracking When It Strays: Mitigating Dual Exposure Biases in LLM Reasoning Distillation](https://arxiv.org/abs/2605.19433)**  
  <sub>2026-05-19 · Hybrid OPD · [Code](https://github.com/wangbing1416/MOTAB)</sub>  
  MOTAB monitors student reasoning, backtracks when teacher likelihood crosses an adaptive boundary, and generates a corrective continuation from an earlier prefix. Training retains the student's deviation before the correction, and module ablations support backtracking and stitching without proving that the boundary certifies logical validity.

- **[f-OPD: Stabilizing Long-Horizon On-Policy Distillation with Freshness-Aware Control](https://arxiv.org/abs/2605.17862)**  
  <sub>2026-05-18 · Analysis</sub>  
  f-OPD studies delayed student rollouts and teacher supervision, combining freshness weighting, anchoring, and refresh. Its coding-agent results report partial recovery of the synchronous baseline’s task success. These observations do not establish a precise stability or efficiency advantage.

- **[MixSD: Mixed Contextual Self-Distillation for Knowledge Injection](https://arxiv.org/abs/2605.16865)**  
  <sub>2026-05-16 · Hybrid OPD · [Code](https://github.com/jiarui-liu/MixSD)</sub>  
  MixSD constructs a single offline collection of shared-prefix targets by mixing the initial model's factual-context and prompt-only conditionals, then fits the retained targets with NLL. Independent OPSD diagnostics examine memorization and capability retention, with MIXSD-KL underfitting kept distinct from OPSD results.

- **[DeltaPrompts: Escaping the Zero-Delta Trap in Multimodal Distillation](https://arxiv.org/abs/2605.15532)**  
  <sub>2026-05-15 · Analysis</sub>  
  Measures teacher–student disagreement over sampled final-answer distributions, then synthesizes multimodal questions from dataset seeds and student failure skills while rejecting ambiguous or zero-disagreement candidates. The prompts are evaluated with on-policy distillation and off-policy fine-tuning; answer-level agreement does not establish token-level agreement.

- **[Beyond GRPO and On-Policy Distillation: An Empirical Sparse-to-Dense Reward Principle for Language-Model Post-Training](https://arxiv.org/abs/2605.12483)**  
  <sub>2026-05-12 · Hybrid OPD</sub>  
  This verifiable-math study tests allocating scarce labeled examples first to teacher-side sparse-reward learning, then transferring behavior through a teacher-rollout forward-KL warm-up and student-rollout reverse-KL distillation, with optional later student reinforcement learning. The stages are sequential, not a joint RL–distillation update, and the allocation evidence is task-specific.

- **[On-Policy Distillation with Best-of-N Teacher Rollout Selection](https://arxiv.org/abs/2605.09725)**  
  <sub>2026-05-10 · Hybrid OPD · [Code](https://github.com/BWGZK-keke/BRTS)</sub>  
  BRTS supplements student-prefix distillation with a teacher-prefix branch selected for answer correctness and compatibility with the student. A recovery comparison supports answer-guided teacher resampling on difficult prompts, while the independent value of the compatibility tie-breaker remains unisolated.

- **[CoDistill-GRPO: A Co-Distillation Recipe for Efficient Group Relative Policy Optimization](https://arxiv.org/abs/2605.08873)**  
  <sub>2026-05-09 · Hybrid OPD</sub>  
  Two models train jointly with group-relative policy updates: the smaller model receives a scalar distillation reward derived from the larger model, while the larger model reuses smaller-model rollouts with importance reweighting. Early rollouts can include larger-model hints; this is not reciprocal token-level distillation.

- **[Reasoning Compression with Mixed-Policy Distillation](https://arxiv.org/abs/2605.08776)**  
  <sub>2026-05-09 · Interactive imitation</sub>  
  The student generates a reasoning trace, which a larger teacher rewrites concisely; the student then matches teacher token distributions on the rewritten trace. The training contexts are therefore not the original student prefixes, and the objective does not enforce answer correctness.

- **[Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning](https://arxiv.org/abs/2605.07804)**  
  <sub>2026-05-08 · Direct OPD</sub>  
  Prune-OPD weights teacher supervision by prefix compatibility and adjusts the next batch’s response budget. Reported time–accuracy comparisons differ between low- and high-compatibility pairs; they do not isolate compatibility selection from supervision quantity.

- **[Near-Policy: Accelerating On-Policy Distillation via Asynchronous Generation and Selective Packing](https://arxiv.org/abs/2605.05940)**  
  <sub>2026-05-07 · Direct OPD</sub>  
  Near-Policy Distillation periodically collects student responses, filters them by teacher–student difficulty discrepancy, and packs retained sequences for teacher scoring and supervised learner updates. Because generation and optimization are decoupled, sampled states can lag behind the current student rather than remain strictly on-policy.

- **[Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe](https://arxiv.org/abs/2605.03677)**  
  <sub>2026-05-05 · Hybrid OPD · [Code](https://github.com/WenjinHou/Uni-OPD)</sub>  
  Uni-OPD combines offline difficulty balancing and batch-level correctness balancing with outcome calibration of trajectory-average teacher–student log-ratio returns. Each calibrated return is broadcast to the trajectory’s token advantages; component ablations examine the combined recipe.

- **[Hybrid Policy Distillation for LLMs](https://arxiv.org/abs/2604.20244)**  
  <sub>2026-04-22 · Analysis · [Code](https://github.com/zwhong714/Hybrid-Policy-Distillation)</sub>  
  HPD is evaluated as offline-prefix initialization for a later rollout-based OPD stage. The study compares HPD and SFT starts and reports stronger subsequent OPD results from HPD, without making the offline HPD procedure itself an on-policy trajectory method.

- **[TIP: Token Importance in On-Policy Distillation](https://arxiv.org/abs/2604.14084)**  
  <sub>2026-04-15 · Direct OPD · [Code](https://github.com/HJSang/OPSD_OnPolicyDistillation)</sub>  
  TIP studies which positions in student-generated rollouts warrant distillation, selecting tokens using student entropy and teacher–student disagreement. Entropy alone misses confident disagreements; the combined selector retains them, but disagreement does not establish that the teacher’s preferred continuation is correct.

- **[Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation](https://arxiv.org/abs/2604.13010)**  
  <sub>2026-04-14 · Hybrid OPD · [Code](https://github.com/jet-ai-projects/Lightning-OPD)</sub>  
  Lightning OPD caches teacher scores on initial-student rollouts and reuses them during student-only optimization. Its experiments compare refresh costs and cross-stage teacher pairings, without establishing that arbitrary cached supervision is equivalent to fresh OPD.

- **[Online Experiential Learning for Language Models](https://arxiv.org/abs/2603.16856)**  
  <sub>2026-03-17 · Direct OPD</sub>  
  The method extracts reusable knowledge from deployment trajectories, then trains student-generated single-turn responses from recorded interaction prefixes against a knowledge-conditioned self-teacher. Consolidation needs no access to the user-side environment; the reported experiments use text-based games.

- **[PACED: Distillation and On-Policy Self-Distillation at the Frontier of Student Competence](https://arxiv.org/abs/2603.11178)**  
  <sub>2026-03-11 · Hybrid OPD</sub>  
  PACED weights each problem’s distillation loss by a pass-rate-based measure of student competence. Its forward-KL track uses teacher-forced reference sequences, whereas its reverse-KL self-distillation track uses student rollouts; the reported single-loss experiments estimate weights once rather than continuously adapting them.

- **[Fast and Effective On-policy Distillation from Reasoning Prefixes](https://arxiv.org/abs/2602.15260)**  
  <sub>2026-02-16 · Direct OPD</sub>  
  The method stops student-generated rollouts at a training prefix and applies token-level teacher supervision only there, with a schedule that lengthens the prefix over training. It is evaluated on long reasoning outputs; behaviors that emerge late receive less direct supervision.

- **[Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training](https://arxiv.org/abs/2602.12222)**  
  <sub>2026-02-12 · Hybrid OPD · [Code](https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT)</sub>  
  Hinted Decoding constructs training traces by mixing answer-conditioned and question-only predictions from the same model at shared prefixes. Adaptive mixing and an answer-region switch improve the tested supervised-training recipe, but the traces are collected before optimization rather than refreshed throughout training.

- **[Making Expert Reasoning Learnable with Self-Distillation](https://arxiv.org/abs/2602.02405)**  
  <sub>2026-02-02 · Hybrid OPD · [Code](https://github.com/ethanm88/DAIL)</sub>  
  DAIL uses an expert-solution-conditioned self-teacher to accept or replace student proposals and then trains on the collected prefixes with a negative-reference contrast. Its sampling and objective comparisons support the tested construction, with mixed generation helping long-reasoning models more consistently than shorter-reasoning variants.

- **[Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897)**  
  <sub>2026-01-27 · Direct OPD · [Code](https://github.com/idanshen/Self-Distillation)</sub>  
  SDFT distills a demonstration-conditioned EMA teacher on fresh student rollouts. Its practical experiments use full-vocabulary forward KL despite the paper’s reverse-KL motivation; they study continual skill and knowledge adaptation, rely on effective in-context learning, and reduce rather than eliminate forgetting.

- **[Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning](https://arxiv.org/abs/2601.09088)**  
  <sub>2026-01-14 · Hybrid OPD · [Code](https://github.com/D2I-ai/dasd-thinking)</sub>  
  DASD includes a mixed-policy stage in which a teacher completes retained prefixes from student-generated reasoning traces. Its masking comparison studies whether retaining the student segment helps subsequent fine-tuning, alongside substantial offline sequence-distillation stages.

- **[SelecTKD: Selective Token-Weighted Knowledge Distillation for LLMs](https://arxiv.org/abs/2510.24021)**  
  <sub>2025-10-28 · Hybrid OPD</sub>  
  SelecTKD weights teacher–student token divergences using teacher verification of student proposals. Experiments adding the selector to GKD and mixed-source distillation establish an OPD component, while the separate offline geometry study does not determine the provenance of every training prefix.

- **[AdaSwitch: Balancing Exploration and Guidance in Knowledge Distillation via Adaptive Switching](https://arxiv.org/abs/2510.07842)**  
  <sub>2025-10-09 · Hybrid OPD</sub>  
  AdaSwitch starts each training rollout with student-generated tokens, then lets the teacher finish when next-token divergence exceeds a threshold based on recent divergences. The student matches teacher token distributions along the mixed sequence; its one-time handoff leaves the remainder teacher-generated rather than returning control to the student.

- **[In Their Own Words: Reasoning Traces Tailored for Small Models Make Them Better Reasoners](https://arxiv.org/abs/2509.22230)**  
  <sub>2025-09-26 · Hybrid OPD</sub>  
  Interleaved-Policy Distillation builds reusable SFT traces by replacing low-support teacher proposals with student tokens and letting the teacher continue from the revised prefix. Across four tested small-model reasoning settings, its teacher-propose recipe outperforms the reported direct-distillation and teacher-RFT baselines; comparisons with filtering, masking, and student-propose generation qualify how trajectory compatibility and teacher-authored reasoning contribute.

- **[Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://arxiv.org/abs/2410.11325)**  
  <sub>2024-10-15 · Hybrid OPD</sub>  
  Speculative Knowledge Distillation builds training sequences by accepting student-proposed tokens that rank highly under the teacher and replacing rejected tokens with teacher samples. It then matches teacher and student token distributions on those mixed trajectories, rather than training solely on unmodified student rollouts.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-7"></a>

<a id="agentic-and-multi-turn-distillation"></a>

<details><summary><strong>Agentic and multi-turn distillation</strong> &nbsp;·&nbsp; 39</summary>

*How does supervision change across actions and turns?*

- **[SAIL: Scientific Agentic Intelligence via a Science-Aware Loop](https://arxiv.org/abs/2610.11451)**  
  <sub>2026-10-08 · Hybrid OPD</sub>  
  SAIL applies specialist-teacher distillation to student-generated scientific-agent trajectories, using recorded model-call contexts and episode-linked segments to supervise actions across tools and context compaction; its reported gains are for the full SFT–specialist–MOPD–RL recipe.

- **[Stochastic Teacher Intervention for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.10878)**  
  <sub>2026-10-07 · Hybrid OPD</sub>  
  STI-OPD uses discrepancy-conditioned stochastic teacher takeovers to shape multi-turn training histories and importance-weights teacher-generated tokens. In the reported agent benchmarks, its recipe outperforms tested OPD baselines and threshold variants; its importance-sampling identity applies to conditional token matching, not the intervention-induced history distribution.

- **[MIMESIS: Learning User Simulators as Training Environments for Interactive Agents](https://arxiv.org/abs/2610.09484)**  
  <sub>2026-10-07 · Hybrid OPD</sub>  
  MIMESIS adds coached on-policy self-distillation to simulated-user agent RL: a feedback-conditioned self-teacher reweights already sampled agent tokens, and the reported comparison improves aggregate performance across nine unseen evaluation simulators over GRPO with the same training user.

- **[TAP: Efficient Long-Horizon Agent Pruning via Trajectory-Anchored Recovery](https://arxiv.org/abs/2610.09074)**  
  <sub>2026-10-06 · Hybrid OPD</sub>  
  TAP recovers pruned long-horizon agents by matching a frozen teacher on student-generated response prefixes within fixed teacher-trajectory contexts, and uses the recovery objective to rescore channels between pruning stages. Its controlled comparisons support the value of anchoring relative to full student-trajectory OPD in the tested settings, while task-level measurements show that faster inference does not always lower cost per successful task.

- **[Language Models that Play Chess and Explain Their Moves](https://arxiv.org/abs/2610.03695)**  
  <sub>2026-10-02 · Hybrid OPD</sub>  
  QUEEN iteratively distills engine-checked, consolidated analyses of candidate successor positions into a chess-language model, using a mixture of model-play and external root positions. Its reported playing-strength gains support the full training recipe, while weaker conceptual coherence and the absence of component-isolating controls limit stronger claims.

- **[MLToolBench: Learning Tool-Augmented Agents for Machine Learning Development](https://arxiv.org/abs/2609.36679)**  
  <sub>2026-09-29 · Teacher-mediated RL</sub>  
  SPICE augments outcome-based agent training with signed likelihood ratios of student tool calls under solution-conditioned and ordinary policy contexts. Controls show that call–feedback correspondence contributes to the reported gain; the turn-return update is not an exact conditional KL estimator.

- **[MAS-OPD: On-Policy Distillation for Multi-agent Systems](https://arxiv.org/abs/2609.34234)**  
  <sub>2026-09-28 · Direct OPD</sub>  
  MAS-OPD trains multiple role policies on their joint trajectories using role-contrast teacher scores and privileged historical attribution; module-removal controls and role/conflict diagnostics support the reported coordination gains in the tested workflows.

- **[Know When to Stop, Where to Restart: Accelerating Multi-Turn Agentic On-Policy Distillation](https://arxiv.org/abs/2609.14636)**  
  <sub>2026-09-13 · Direct OPD</sub>  
  STRIDE stops multi-turn student rollouts using cumulative teacher log-probability, then restarts from a cached student prefix selected by a likelihood threshold. Buffer ablations and measured time per step support the tested recipe; the threshold does not certify prefix correctness.

- **[CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning](https://arxiv.org/abs/2609.29518)**  
  <sub>2026-08-25 · Hybrid OPD</sub>  
  CataOPD first attempts unguided recovery of all-failed rollout groups, then uses teacher hints to help the student produce verified training targets. Ablations support recovery, guidance, and guided-versus-unaided token weighting, while the additional sampling has a separate training cost.

- **[OPDSearch+: On-Policy Distillation with RL Refinement for Search-Augmented Reasoning](https://arxiv.org/abs/2608.24310)**  
  <sub>2026-08-25 · Hybrid OPD</sub>  
  OPDSearch+ first distills a frozen teacher on student trajectories that include live retrieval, then refines the student with outcome-based RL. Comparisons with offline preparation, RL alone, and simultaneous training support the sequential recipe in the tested search setting.

- **[Reading is not Reasoning: Bridging the Agentic Policy Gap in Vision-Text Compression](https://arxiv.org/abs/2608.08960)**  
  <sub>2026-08-09 · Hybrid OPD</sub>  
  CAPS first trains a visual-history student on successful text-policy responses, then combines environmental-reward training with forward-KL supervision from a frozen text-history self-teacher on student-visited states. The teacher receives the corresponding textual history, without ground-truth solutions; training requires paired history representations.

- **[Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2608.07371)**  
  <sub>2026-08-07 · Hybrid OPD · [Code](https://github.com/Chihaya-Anon-chan/TRIAL)</sub>  
  On student-generated multi-turn interactions, this method scores realized tokens with and without their turn’s post-action outcome, then uses signed probability gaps to guide updates. It normalizes gap magnitudes across turns to allocate dense hindsight feedback alongside outcome-based GRPO; evaluation covers two interactive environments.

- **[MemOPD: On-Policy Distillation through Memory State Alignment for Long-Horizon Agents](https://arxiv.org/abs/2608.07068)**  
  <sub>2026-08-07 · Hybrid OPD · [Code](https://github.com/TPssp/MemOPD)</sub>  
  For compact-memory agents, this method reconstructs each student invocation’s tokens, positions and causal visibility before a frozen teacher scores sampled actions, avoiding supervision under an unvisited flattened-history state. It combines teacher distribution matching with task-reward PPO; end-to-end training is tested on retrieval tasks.

- **[Look Ahead Before You Distill: Future Trajectory Validation of Teacher Guidance for Agentic On-Policy Distillation](https://arxiv.org/abs/2608.01953)**  
  <sub>2026-08-03 · Direct OPD · [Code](https://github.com/ChenChiShui/FutureBridge-OPD)</sub>  
  FutureBridge-OPD selects a student-controlled turn with weak sampled teacher support, substitutes a teacher action, and compares paired student continuations before retaining the bridge for distillation. This validation uses future teacher-preferred-token density, not task reward, and builds on a curriculum initialized from successful trajectories.

- **[PCSD: Persistent Consistency for Self-Distillation in Agentic Reinforcement Learning](https://arxiv.org/abs/2608.01837)**  
  <sub>2026-08-03 · Hybrid OPD</sub>  
  PCSD aggregates signed teacher-student log-probability gaps over local windows to modulate an auxiliary update on student-generated trajectories. Pointwise comparisons and component ablations support the tested recipe without establishing teacher-reliability detection or exact distribution matching.

- **[DASH-OPD: Discrepancy-Aware Switching with Hysteresis for On-Policy Distillation](https://arxiv.org/abs/2607.29078)**  
  <sub>2026-07-31 · Hybrid OPD · [Code](https://github.com/Lucian1115/DASH-OPD)</sub>  
  DASH-OPD accumulates drift and recovery evidence to alternate student and teacher execution, applying different losses to each source. Updated controls isolate recovery and evidence accumulation with matched tuning budgets. Fewer switches and teacher turns are measured execution properties, not a demonstrated end-to-end speedup.

- **[TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training](https://arxiv.org/abs/2607.05804)**  
  <sub>2026-07-07 · Direct OPD</sub>  
  TurnOPD collects student-generated agent trajectories to a depth chosen from periodic turn-level probes, then gradually shifts reverse-KL supervision from token-weighted to turn-balanced aggregation. It addresses shallow-turn loss concentration in long-horizon tasks; shortened rollouts can leave deeper decisions unobserved.

- **[Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763)**  
  <sub>2026-07-06 · Direct OPD</sub>  
  ReOPD samples earlier turns more often from recorded teacher interaction histories, has the student generate an action at the selected turn, and matches teacher token distributions there. The action is student-generated, but its preceding actions and tool observations are replayed, not student-on-policy.

- **[UI-MOPD: Multi-Platform On-Policy Distillation for Unified GUI Agents](https://arxiv.org/abs/2607.04425)**  
  <sub>2026-07-05 · Hybrid OPD · [Code](https://github.com/EliSpectre/UI-MOPD)</sub>  
  UI-MOPD routes desktop and mobile student rollouts to platform-specialized teachers and combines sampled-token guidance with task rewards. Routing and reward-conditioned masking improve balanced performance over the tested unified-teacher, random-routing, and unmasked alternatives.

- **[UCOB: Learning to Utilize and Evolve Agentic Skills via Credit-Aware On-Policy Bidirectional Self-Distillation](https://arxiv.org/abs/2606.29502)**  
  <sub>2026-06-28 · Hybrid OPD · [Code](https://github.com/TU2021/UCOB)</sub>  
  UCOB collects skill-conditioned and no-skill agent rollouts and groups records by task and anchor state. The highest-return sampled record selects a reference view, whose stopped token distribution supervises the opposite view on the winning response’s prefixes, alongside RL and skill-memory updates. Teacher direction can reverse.

- **[ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2606.27814)**  
  <sub>2026-06-26 · Hybrid OPD</sub>  
  ATOD combines detached, turn-weighted teacher log-probability gaps with outcome advantages in a clipped policy update. Coefficient annealing shifts their balance over training; its multi-scale agent experiments separately ablate turn weighting and annealing, without establishing direct matching to a teacher–reward mixture.

- **[HERO: Hindsight-Enhanced Reflection from Environment Observations for Agentic Self-Distillation](https://arxiv.org/abs/2606.11559)**  
  <sub>2026-06-10 · Direct OPD</sub>  
  HERO compresses completed student interactions into turn-specific hindsight hints. An EMA self-teacher uses the original decision history, next observation, terminal outcome, and parsed hint to supervise the original action tokens. Its prompt ablation favors reflection-conditioned supervision over raw observations in the tested setting.

- **[World Models Meet Language Models: On the Complementarity of Concrete and Abstract Reasoning](https://arxiv.org/abs/2606.03603)**  
  <sub>2026-06-02 · Direct OPD · [Code](https://github.com/yczhou001/PF-OPSD)</sub>  
  An external privileged evaluator sees future video and answers when scoring candidate actions at student-visited decision states. Discrete nodes match a stopped target distribution; text nodes use weighted likelihood. Deployment excludes the privileged future observations.

- **[CoMAP: Co-Evolving World Models and Agent Policies for LLM Agents](https://arxiv.org/abs/2606.02372)**  
  <sub>2026-06-01 · Hybrid OPD · [Code](https://github.com/loyiv/CoMAP)</sub>  
  CoMAP combines agent improvement with textual world-model self-distillation. A teacher view receives the observed next state and supervises the student world model’s generated prefixes. World-state prediction and component-removal experiments evaluate the combined recipe.

- **[Same Evidence, Different Answers: Canonical-Context On-Policy Distillation for Multi-Turn Language Models](https://arxiv.org/abs/2605.30251)**  
  <sub>2026-05-28 · Direct OPD</sub>  
  CCOPD trains a student answering from a multi-turn history against a frozen copy of the same base model given the same user evidence in a clean prompt. Reverse KL aligns student-generated final-answer prefixes; earlier conversational replies receive no direct distillation loss.

- **[GAPD: Gold-Action Policy Distillation for Agentic Reinforcement Learning in Knowledge Base Question Answering](https://arxiv.org/abs/2605.29584)**  
  <sub>2026-05-28 · Hybrid OPD</sub>  
  GAPD adds gold-action-conditioned teacher feedback to student knowledge-base trajectories. Its complete pipeline improves the reported outcome-only baseline; the separate contribution of action alignment and equivalent-state filtering remains unresolved.

- **[MAIGO: Mitigating Lost-in-Conversation with History-Cleaned On-Policy Self-Distillation](https://arxiv.org/abs/2605.27186)**  
  <sub>2026-05-26 · Direct OPD</sub>  
  MAIGO trains on the student's self-conditioned, multi-turn dialogue rollouts while an EMA self-reference scores middle replies without prior assistant messages and final answers using the completed user-side task view. A separate full-view branch preserves complete-prompt behavior; evaluation is limited to paired-view tasks.

- **[Unlocking Proactivity in Task-Oriented Dialogue](https://arxiv.org/abs/2605.22240)**  
  <sub>2026-05-21 · Hybrid OPD</sub>  
  For simulated multi-turn recruitment dialogues, a privileged view of the policy sees hidden user concerns and supplies token-level targets to its conversation-only view on the latter’s rollouts. A separate clipped policy-gradient update uses simulated final decisions and turn-level willingness shifts; deployment has no access to the hidden concerns.

- **[What and When to Distill: Selective Hindsight Distillation for Multi-Turn Agents](https://arxiv.org/abs/2605.19447)**  
  <sub>2026-05-19 · Hybrid OPD · [Code](https://github.com/OliverLeeXZ/SERL)</sub>  
  SERL combines hindsight-conditioned action-token matching with teacher-informed reweighting of outcome advantages. Experiments varying feedback source and placement show that richer context and coarser placement are not uniformly better, while the independent action-only forward-KL term distinguishes the method from reward modulation alone.

- **[SD-Search: On-Policy Hindsight Self-Distillation for Search-Augmented Reasoning](https://arxiv.org/abs/2605.18299)**  
  <sub>2026-05-18 · Hybrid OPD</sub>  
  SD-Search gives a shared-weight teacher a hindsight summary of the rollout group’s queries and outcomes, then matches its query-token distributions with Jensen–Shannon divergence alongside GRPO. The summary includes the current rollout; outcome contrast weakens when every rollout succeeds or fails.

- **[HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents](https://arxiv.org/abs/2605.17873)**  
  <sub>2026-05-18 · Direct OPD · [Code](https://github.com/wgcyeo/HINT-SD)</sub>  
  HINT-SD selects up to three failure-relevant turns and constructs local feedback for an EMA self-teacher. Reverse KL supervises the original student action spans; feedback-source and placement comparisons support the tested selective-guidance recipe.

- **[Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155)**  
  <sub>2026-05-14 · Hybrid OPD · [Code](https://github.com/ZJU-REAL/SDAR)</sub>  
  SDAR combines agentic RL with an independent, skill-conditioned auxiliary update whose token weights depend on teacher-student probability gaps. Within-recipe comparisons support gap gating over alternative gates, while the published frozen-reference baseline does not isolate gating alone.

- **[Revisiting DAgger in the Era of LLM-Agents](https://arxiv.org/abs/2605.12913)**  
  <sub>2026-05-13 · Direct OPD</sub>  
  The DAgger-style recipe queries teacher action labels at states reached by turn-level teacher–student mixing, then trains with cross-entropy on retained valid-submission trajectories. The teacher-execution probability decreases from 1.0 to a floor of 0.6.

- **[SOD: Step-wise On-policy Distillation for Small Language Model Agents](https://arxiv.org/abs/2605.07725)**  
  <sub>2026-05-08 · Hybrid OPD · [Code](https://github.com/YoungZ365/SOD)</sub>  
  SOD addresses tool-call errors that shift later reasoning contexts by weighting each step’s sampled-token teacher–student log-likelihood signal according to changes in their discrepancy, alongside outcome-based reinforcement learning. Tool observations are excluded from the distillation loss; the discrepancy score is a proxy, not full token KL.

- **[Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943)**  
  <sub>2026-05-01 · Hybrid OPD · [Code](https://github.com/minstar/Healthcare_GYM)</sub>  
  TT-OPD combines GRPO with turn-normalized reverse-KL supervision from an outcome-conditioned EMA teacher on student-generated medical-agent trajectories. Component comparisons examine teacher updates, privileged hints, and length control, while reporting inconsistencies limit quantitative stability claims.

- **[TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/abs/2604.24005)**  
  <sub>2026-04-27 · Direct OPD · [Code](https://github.com/kokolerk/TCOD)</sub>  
  TCOD addresses rising divergence across turns in interactive distillation by gradually extending the student’s training horizon. One variant lengthens student-generated prefixes; another starts student suffixes after successful teacher-executed prefixes, which require pre-collected trajectories and do not contribute gradients.

- **[Skill-SD: Skill-Conditioned Self-Distillation for Multi-turn LLM Agents](https://arxiv.org/abs/2604.10674)**  
  <sub>2026-04-12 · Hybrid OPD</sub>  
  For multi-turn agents, Skill-SD summarizes completed trajectories into skills available to a periodically synchronized teacher. The student acts without those skills and receives token-level self-distillation alongside task-reward optimization; the evidence concerns the tested agent environments.

- **[OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)**  
  <sub>2026-03-10 · Hybrid OPD · [Code](https://github.com/Gen-Verse/OpenClaw-RL)</sub>  
  OpenClaw-RL turns subsequent interaction feedback into hints for a privileged self-teacher that scores the student’s original response prefixes. The updated report compares overlap-based hint selection with random hints and tests support and clipping choices. Its asynchronous agent results have task-specific training and evaluation limits.

- **[KEPO: Knowledge-Enhanced Preference Optimization for Multimodal Reasoning with Applications to Medical VQA](https://arxiv.org/abs/2602.00400)**  
  <sub>2026-01-30 · Hybrid OPD</sub>  
  KEPO combines reward-thresholded teacher matching with a separate recovery branch for rollout groups that receive no positive reward. Gating and recovery comparisons support these two changes, while the threshold includes format reward and should not be described as a correctness-only filter.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-8"></a>

<a id="mechanisms-failures-and-evaluation"></a>

<details><summary><strong>Mechanisms, failures, and evaluation</strong> &nbsp;·&nbsp; 46</summary>

*What transfers, what fails, and why?*

- **[Policy Alignment: New Signals for Membership Auditing in On-Policy Distillation](https://arxiv.org/abs/2610.11423)**  
  <sub>2026-10-08 · Analysis</sub>  
  Teacher Alignment Gain audits OPD prompt membership through the change in teacher discrepancy on fixed student-generated contexts; reported projection checks and feature ablations show information beyond checkpoint drift under the evaluated access assumptions.

- **[Why On-Policy Distillation Sometimes Fails: Vanishing Learning Signals](https://arxiv.org/abs/2610.11247)**  
  <sub>2026-10-08 · Analysis</sub>  
  For an idealized full-KL OPD flow, Zhao et al. decompose loss decay into a fixed-prefix learning signal and a rollout-occupancy term, and prove a finite-local-time recovery bound for sufficiently nearby teachers sharing the student's parameterization. Their single-run training logs show associated plateaus and declining gradient proxies, not a causal explanation of them.

- **[On-Policy Distillation Teaches New Skills but Not New Knowledge](https://arxiv.org/abs/2610.09639)**  
  <sub>2026-10-07 · Direct OPD</sub>  
  In controlled lookup-table reasoning tasks, reverse-KL OPD transferred execution skill to unseen tree structures much more reliably than held-out facts; a prefix-by-objective comparison found that forward KL substantially improved factual transfer, while student-generated prefixes improved the likelihood of correct multi-step executions.

- **[Does On-Policy Distillation for Safety Pose Backdoor Risks?](https://arxiv.org/abs/2610.07654)**  
  <sub>2026-10-06 · Direct OPD</sub>  
  In tested safety-OPD setups, a backdoored teacher and a small number of triggered prompts can yield trigger-conditioned harmful behavior despite improved trigger-free safety; additional training and the choice of token-level KL update materially affect when that behavior appears, while reward clipping only delays it in some settings.

- **[Divergence controls entropy in distillation](https://arxiv.org/abs/2610.03529)**  
  <sub>2026-10-02 · Hybrid OPD</sub>  
  Under fixed-context stationarity assumptions, forward-KL distillation has an exact average entropy–residual-KL identity. In the reported OPD comparisons, token-level divergence affected student entropy more than whether prefixes came from student or teacher rollouts; self-distillation ablations identified divergence, teacher-update, and tail-handling choices associated with entropy collapse.

- **[Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective](https://arxiv.org/abs/2610.03185)**  
  <sub>2026-10-02 · Direct OPD</sub>  
  In the studied math-reasoning OPD runs, small-budget gains accompanied increased sampling of initially accessible solutions, while a failing run favored overlong student responses; masking truncated rollouts mitigated the reported degeneration.

- **[When and Where to Trust the Teacher: Unifying On-Policy Distillation and GRPO through Entropy-Calibrated Credit Assignment](https://arxiv.org/abs/2609.28385)**  
  <sub>2026-09-23 · Analysis</sub>  
  The UECR study separates response-level teacher utility from a mean-preserving redistribution of verifier-derived token credit. A blinded audit at shared initialization compares the resulting weights with labeled reasoning errors and shuffled-entropy controls, without establishing downstream superiority from those diagnostics.

- **[RL Starts before RL: On Policy Distillation for Better Reinforcement Learning](https://arxiv.org/abs/2609.28145)**  
  <sub>2026-09-23 · Analysis</sub>  
  This study tests whether distillation on student-generated trajectories prepares a model for later reinforcement learning beyond improving its initial accuracy. In its comparisons, the preferred KL direction changes after RL on student trajectories; that ranking does not extend to teacher-generated trajectories.

- **[When EOS Tokens Disagree: Understanding Length Inflation in On-Policy Distillation](https://arxiv.org/abs/2609.20511)**  
  <sub>2026-09-17 · Analysis · [Code](https://github.com/UNCSciML/opd-eos)</sub>  
  This study traces some response-length inflation in sampled-token distillation to students and teachers preferring different tokens for the same stopping action. Aggregating equivalent termination tokens in the training signal mitigates that mismatch in single-turn math tests, but late-run inflation can remain.

- **[Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172)**  
  <sub>2026-09-03 · Analysis · [Code](https://github.com/Thinking-Space/One-Shot-OPD)</sub>  
  This study compares repeated distillation from very few queries with full-data training. A top-k configuration tests task performance; separate sampled-token runs measure semantic-cluster coverage and alignment rates. The coverage proxy does not measure visitation frequency or instructional value.

- **[Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement](https://arxiv.org/abs/2608.31046)**  
  <sub>2026-08-31 · Analysis</sub>  
  This study tests whether sampled-token OPD gains require teacher guidance, finding that answer-token advantage signs can conflict with verified correctness and that suppressing low-probability student tokens can reproduce gains in its tests. Its resulting self-adaptation method uses no teacher, so these findings do not establish a mechanism for full-distribution OPD.

- **[Consolidating RLVR Capabilities Across Domains: A Deep Dive into Fusion Paradigms](https://arxiv.org/abs/2608.27409)**  
  <sub>2026-08-27 · Analysis</sub>  
  Using shared domain experts and data, this study compares weight merging, pooled reward training, and multi-teacher OPD. Domain retention and complete training costs distinguish the methods. The 4B pass@32 and held-out tests do not establish broader solution coverage than the base model.

- **[A Token-Level Analysis of Sampled-Token Reverse-KL On-Policy Distillation](https://arxiv.org/abs/2608.25643)**  
  <sub>2026-08-26 · Analysis</sub>  
  This study analyzes logit gradients of a directly backpropagated sampled-token squared-log-ratio loss and tests detached surprise weights in mathematical reasoning. The analysis holds sampled prefixes fixed; experiments leave unresolved how much improvement comes from exact surprise alignment versus more general nonuniform weighting.

- **[Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning](https://arxiv.org/abs/2608.21811)**  
  <sub>2026-08-22 · Analysis</sub>  
  In a vision-language mathematical-reasoning comparison, one validation slice reverses training-arm rankings relative to cross-domain transfer, whereas a harder slice correlates positively. The study illustrates validation-set sensitivity; single-seed results and differing answer access limit method rankings.

- **[Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling](https://arxiv.org/abs/2608.11829)**  
  <sub>2026-08-12 · Analysis</sub>  
  Across evaluated OPD settings, pass@K gains sometimes persist and sometimes reverse at larger sampling budgets; a budget-weighted analysis explains how mixed problem-level changes permit reversal, while pre-training TAS@K agrees with the resulting teacher ordering in 148 of 177 reported comparisons.

- **[Privileged Likelihood Is Not Automatically Value: Three Checks for Token Credit in On-Policy Self-Distillation](https://arxiv.org/abs/2608.09263)**  
  <sub>2026-08-10 · Analysis</sub>  
  This analysis asks whether token likelihood changes under hindsight feedback track task success, whether feedback written about the scored rollout creates self-dependence, and what token-weighted updates reinforce. Its mathematics experiments show a failure case, not that every privileged likelihood signal lacks outcome value.

- **[Privileged Solutions or Context-Induced Teacher Behavior? Dissecting On-Policy Self-Distillation](https://arxiv.org/abs/2608.09228)**  
  <sub>2026-08-10 · Analysis · [Code](https://github.com/MBZUAI-reasoninglab/OP2SD)</sub>  
  This diagnostic study replaces the target problem’s reference solution with another mathematics problem’s worked solution in the self-teacher’s context, while preserving student rollouts and the distillation objective. The results challenge a purely answer-transfer explanation but do not identify a unique causal mechanism.

- **[Privileged, but Biased: How PI-Conditioned Teachers Break Self-Distillation](https://arxiv.org/abs/2608.04794)**  
  <sub>2026-08-05 · Analysis</sub>  
  This analysis tests privileged-information self-distillation without a reward term. On the harder tasks studied, a teacher conditioned on one solution favors that path, while token-level loss falls without corresponding accuracy gains; the study does not evaluate reward–distillation hybrids.

- **[Verifier-Induced Support Reshaping in On-Policy Optimization](https://arxiv.org/abs/2608.00220)**  
  <sub>2026-07-31 · Direct OPD</sub>  
  In a controlled OPD comparison, IF-RLVR teacher checkpoints produced different trade-offs between instruction-following transfer and math retention; distillation from the tested converged teacher did not preserve math performance.

- **[The Physics of Multi-Turn Long-Horizon Planning: From Pre-training to Post-training via Single- and Multi-Teacher On-Policy Agentic Distillation](https://arxiv.org/abs/2607.24720)**  
  <sub>2026-07-27 · Analysis · [Code](https://github.com/Quester-one/PlanPhysCode)</sub>  
  This synthetic-planning study compares OPD and outcome-reward training across data quality and horizon. Its idealized teacher’s described training source includes evaluation instantiations, whereas the student uses separate pools. The evidence concerns this oracle-teacher setting.

- **[Outcome-Confounded Local Supervision in On-Policy Distillation](https://arxiv.org/abs/2607.23731)**  
  <sub>2026-07-26 · Analysis</sub>  
  This diagnostic separates sampled-token teacher–student discrepancy from trajectory correctness. In independent threshold runs, most incorrect responses contain predominantly low-discrepancy tokens. Local agreement therefore does not locate the decisive error; the analysis does not prove a general impossibility of credit assignment.

- **[Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback](https://arxiv.org/abs/2606.30923)**  
  <sub>2026-06-29 · Analysis · [Code](https://github.com/plau666/NAIL)</sub>  
  This analysis asks why learner-state queries can outperform offline cloning when expert feedback is noisy. It derives an offline horizon barrier and studies interactive imitation through augmented-trajectory matching; its guarantees depend on a finite policy class and corruption assumptions, not on arbitrary OPD procedures.

- **[On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity](https://arxiv.org/abs/2606.26091)**  
  <sub>2026-06-24 · Analysis</sub>  
  This analysis asks whether self-distillation conditioned on sampled correct demonstrations narrows solution coverage. A fixed-base-teacher derivation shows how expected reverse-KL targets can favor demonstration-aligned correct paths; graph and science-question experiments examine reduced functional and semantic diversity, rather than proposing a new update.

- **[Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients](https://arxiv.org/abs/2606.18216)**  
  <sub>2026-06-16 · Analysis</sub>  
  Across four student scales, the tested prompt-replay JSD OPD variant produced small VLM gains but reduced video and pooled LLM–video performance relative to the starting models. This is a bounded comparison with prompt-guided RL, not evidence that OPD generally harms generalization.

- **[Dense Supervision, Sparse Updates: On the Sparsity and Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.13657)**  
  <sub>2026-06-11 · Analysis · [Code](https://github.com/SydCS/OPD-Param-Analysis)</sub>  
  This study measures coordinate-sparse and spectrally concentrated updates at checkpoint precision. Visible updates span layers and modules. Retraining on support identified from completed OPD runs nearly recovers full performance and outperforms density-matched random masks in the tested settings.

- **[Trajectory-Refined Distillation](https://arxiv.org/abs/2606.08432)**  
  <sub>2026-06-07 · Analysis · [Code](https://github.com/louieworth/trd)</sub>  
  TRD reports low teacher–student KL even on incorrect student trajectories and compares these diagnostics with teacher-refined prefixes. Its proposed training method uses teacher-rewritten offline trajectories, so the retained contribution is the diagnostic comparison rather than a new core OPD algorithm.

- **[On the Geometry of On-Policy Distillation](https://arxiv.org/abs/2606.07082)**  
  <sub>2026-06-05 · Analysis</sub>  
  In Qwen3 experiments, this study observes early concentration of cumulative OPD updates and reports that projection of gradients onto an early top-16 right-singular subspace largely preserves measured OPD performance. Token sparsification and teacher-generated rollout controls retain similar stable-rank trajectories. Cross-paradigm comparisons use different training stages and configurations.

- **[Reinforcement Learning from Rich Feedback with Distributional DAgger](https://arxiv.org/abs/2606.05152)**  
  <sub>2026-06-03 · Analysis · [Code](https://github.com/rishabh-1086/distIL)</sub>  
  Distributional DAgger gives finite-state counterexamples separating teacher quality from the effect of a distillation update: a higher-reward teacher need not yield a reward-improving reverse-KL natural-gradient step, and local prefix updates can miss consequential early decisions in a restricted policy class.

- **[Rethinking Continual Experience Internalization for Self-Evolving LLM Agents](https://arxiv.org/abs/2606.04703)**  
  <sub>2026-06-03 · Analysis · [Code](https://github.com/RUCBM/ExpInternalization)</sub>  
  This web-agent study compares repeated experience internalization, including global versus step-wise context injection and later use of new experience. Degradation varies by task and recipe; its student-rollout versus filtered-teacher-rollout comparison also changes the KL direction and success filtering.

- **[Your Teacher Can't Help You Here: Combating Supervision Fidelity Decay in On-Policy Distillation](https://arxiv.org/abs/2605.30833)**  
  <sub>2026-05-29 · Analysis · [Code](https://github.com/zui-jiang/LGR)</sub>  
  This study hands reasoning prefixes of different lengths from a student to a fixed teacher and measures teacher continuation performance. The reported decline on longer student prefixes motivates state-dependent supervision assessment, independently of the paper's unresolved lookahead-loss formulation.

- **[Decoupling KL and Trajectories: A Unified Perspective for SFT, DAgger, Offline RL, and OPD in LLM Distillation](https://arxiv.org/abs/2605.16826)**  
  <sub>2026-05-16 · Analysis</sub>  
  Compares forward and reverse token-level KL on teacher- or student-generated prefixes, then tests KL mixing and an entropy-gated response-length curriculum. Its tradeoffs are studied chiefly in mathematical reasoning, including initialization for an accuracy-reward RL follow-up, rather than across RL algorithms.

- **[Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation](https://arxiv.org/abs/2605.13643)**  
  <sub>2026-05-13 · Direct OPD</sub>  
  This study finds that late teacher feedback can lose local discrimination despite a nonzero teacher–student gap. A change point in teacher margins over student candidates masks later advantage-weighted supervision. The rule changes training supervision while preserving complete response generation.

- **[Learning to Foresee: Unveiling the Unlocking Efficiency of On-Policy Distillation](https://arxiv.org/abs/2605.11739)**  
  <sub>2026-05-12 · Analysis · [Code](https://github.com/caiyuchen-ustc/EffOPD)</sub>  
  This parameter-dynamics study compares where on-policy distillation and reinforcement learning place updates and how early update subspaces align with final directions. An accompanying accelerator validates extrapolations of recent parameter displacements; its studied distillation typically uses a separate stronger teacher, not necessarily a self-teacher.

- **[Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information](https://arxiv.org/abs/2605.11609)**  
  <sub>2026-05-12 · Analysis · [Code](https://github.com/FloyedShen/AntiSD)</sub>  
  AntiSD's analysis examines how solution-conditioned self-teachers suppress deliberative tokens and compares standard self-distillation with reward-only training. These diagnostics identify a setting-dependent failure pattern rather than a proved cause of all OPD failures.

- **[The Many Faces of On-Policy Distillation: Pitfalls, Mechanisms, and Fixes](https://arxiv.org/abs/2605.11182)**  
  <sub>2026-05-11 · Analysis</sub>  
  The study tests on-policy distillation across math reasoning, prompt internalization and alignment. It attributes failures to teacher mismatch on student prefixes, biased top-K reverse-KL gradients, and aggregation of instance-specific privileged teachers by a context-free student; its proposed fixes are setting-dependent.

- **[The Extrapolation Cliff in On-Policy Distillation of Near-Deterministic Structured Outputs](https://arxiv.org/abs/2605.08737)**  
  <sub>2026-05-09 · Analysis</sub>  
  This study varies reward extrapolation and training duration in OPD for near-deterministic structured outputs. It finds abrupt losses of parsing validity despite comparatively stable ranking among valid outputs, while the proposed closed-form clipping threshold is not established by the reported implementation.

- **[Hindsight Compacts but Does Not Repair: Rethinking On-Policy Self-Distillation in Reasoning Models](https://arxiv.org/abs/2605.06188)**  
  <sub>2026-05-07 · Analysis</sub>  
  In mathematical reasoning, this study applies hindsight-conditioned self-distillation separately to correct and incorrect student rollouts to distinguish compaction from repair. Correct-only training shortens responses while largely preserving accuracy; incorrect-only training degrades accuracy, limiting claims that hindsight reliably repairs failed reasoning.

- **[Learning from the Near Future: Temporal Self-Distillation for RLVR](https://arxiv.org/abs/2604.20733)**  
  <sub>2026-04-22 · Direct OPD</sub>  
  In a two-checkpoint comparison, distilling an 8B student on its own rollouts from a near-future GRPO checkpoint led to a higher eight-benchmark average after continued RL than distillation from a farther checkpoint, despite a lower pre-RL validation score; the distillation runs selected checkpoints at different training steps.

- **[The Illusion of Certainty: Decoupling Capability and Calibration in On-Policy Distillation](https://arxiv.org/abs/2604.16830)**  
  <sub>2026-04-18 · Direct OPD · [Code](https://github.com/SalesforceAIResearch/CaOPD)</sub>  
  CaOPD examines how privileged-context self-teaching can transfer unjustified confidence alongside task behavior. It replaces verbalized confidence in the training completion and teacher context with a verifier-based success estimate from student rollouts, then distills on the revised completion; this requires parseable confidence and additional training rollouts.

- **[Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe](https://arxiv.org/abs/2604.13016)**  
  <sub>2026-04-14 · Analysis · [Code](https://github.com/Thinking-Space/Rethinking-OPD)</sub>  
  This study compares teacher preparation, supervised cold starts, and prompt formats in mathematical-reasoning distillation. Its cold-start control fixes the subsequent teacher and prompt set; a separate experiment changes only the prompt template. Token overlap is a diagnostic rather than a universal test of transferable capability.

- **[SCOPE: Signal-Calibrated On-Policy Distillation Enhancement with Dual-Path Adaptive Weighting](https://arxiv.org/abs/2604.10688)**  
  <sub>2026-04-12 · Analysis · [Code](https://github.com/machine981/SCOPE)</sub>  
  SCOPE includes a diagnostic that groups erroneous student responses by teacher perplexity and tests teacher recovery after prefix truncation. Lower perplexity is associated with higher recovery in its mathematical-reasoning setting. This supports a bounded diagnostic comparison, without certifying each teacher token target or the effect of the proposed weighting implementation.

- **[Demystifying OPD: Length Inflation and Stabilization Strategies for Large Language Models](https://arxiv.org/abs/2604.08527)**  
  <sub>2026-04-09 · Hybrid OPD</sub>  
  Stable-OPD studies abrupt generation-budget exhaustion and accuracy deterioration during distillation, and compares adding reference-policy anchoring and off-policy demonstrations. Its intervention evidence is setting-specific; the printed repetition-rate condition does not consistently define the reported metric.

- **[Self-Distilled RLVR](https://arxiv.org/abs/2604.03128)**  
  <sub>2026-04-03 · Analysis</sub>  
  The RLSD study tracks references to unavailable context, validation accuracy, and teacher-student divergence during privileged-context self-distillation. Its full-distribution and restricted-target comparisons provide an empirical failure diagnostic, but do not establish inevitable leakage or a leakage-free guarantee for reward reweighting.

- **[Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/abs/2603.25562)**  
  <sub>2026-03-26 · Direct OPD</sub>  
  This paper analyzes why sampled-token supervision can become brittle on student rollouts, then compares renormalized teacher and student distributions over the teacher’s top-ranked tokens at each prefix. The update remains token-local rather than optimizing sequence-level reverse KL.

- **[Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](https://arxiv.org/abs/2603.24472)**  
  <sub>2026-03-25 · Analysis · [Code](https://github.com/beanie00/self-distillation-analysis)</sub>  
  In the studied mathematical-reasoning settings, solution-conditioned self-distillation is associated with shorter responses, reduced uncertainty expression, and poorer OOD performance.

- **[On Teacher Hacking in Language Model Distillation](https://arxiv.org/abs/2502.02671)**  
  <sub>2025-02-04 · Analysis</sub>  
  The teacher-hacking study separates progress toward a distillation teacher from progress toward an independently evaluated oracle. Controlled comparisons show that refreshing teacher or student generations can reduce the divergence between these metrics, with task-dependent effects from prompt diversity.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-9"></a>

<a id="applications-and-systems"></a>

<details><summary><strong>Applications and systems</strong> &nbsp;·&nbsp; 24</summary>

*How does distillation fit into a deployed system?*

- **[Lapras: Latent Reasoning for Time Series Language Models](https://arxiv.org/abs/2610.11111)**  
  <sub>2026-10-08 · Direct OPD</sub>  
  Lapras applies CoT-conditioned hidden-state distillation to student-generated continuous thoughts in time-series QA; its reported multi-backbone comparisons and a no-distillation ablation support the value of this supervision in the tested settings, while early-answering results only suggest a verbalization-related failure mode.

- **[Simplex Diffusion Models](https://arxiv.org/abs/2609.35553)**  
  <sub>2026-09-28 · Direct OPD</sub>  
  Simplex DMD queries a pretrained denoiser on re-noised student outputs to train a few-step diffusion-language generator. Its reported recipe improves low-NFE GSM8K code-generation accuracy while reducing AST diversity and saturating earlier at larger sampling budgets.

- **[Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](https://arxiv.org/abs/2609.26708)**  
  <sub>2026-09-22 · Hybrid OPD</sub>  
  After fixed-prefix quantization-aware distillation, the student samples through its deployment quantized forward path; a frozen full-precision teacher supervises those student prefixes alongside task-verifier feedback. The stage targets long-form repetition attributed to quantization-amplified exposure bias and starts from a quantization-aware checkpoint.

- **[One to More, More to One: Category-Aware Iterative Expert Training for Software Engineering Agents](https://arxiv.org/abs/2609.23377)**  
  <sub>2026-09-20 · Application / system report</sub>  
  This software-engineering pipeline trains category experts and consolidates them through teacher feedback on student rollouts. Reported expert-gain retention is 80.8%, 111.1%, and 84.8% across three categories. The Pro-618 evaluation also selects checkpoints; differing training pools and budgets prevent an isolated consolidation advantage.

- **[KuaiRP Series Role-playing Models Technical Report](https://arxiv.org/abs/2609.11127)**  
  <sub>2026-09-10 · Application / system report</sub>  
  KuaiRP restarts from the original base model to transfer a role-play specialist’s behavior and world knowledge in separate stages. It compares sampled-token policy-gradient distillation with teacher-top-k forward-KL training. Results include weak knowledge transfer under sampled-token updates and failures on the evaluated 9B model.

- **[Video-MOPD: Multi-Teacher On-Policy Distillation for Video Understanding](https://arxiv.org/abs/2609.09300)**  
  <sub>2026-09-08 · Direct OPD</sub>  
  Video-MOPD consolidates video-domain experts using routed teacher supervision on student rollouts. It compares the resulting model with direct averaging of the same experts and tests token-support choices. The full-pipeline results do not isolate data selection or establish equal-compute superiority.

- **[SecOPD: Mitigating Adaptive Prompt Injections by On-Policy Distillation](https://arxiv.org/abs/2608.21500)**  
  <sub>2026-08-21 · Application / system report · [Code](https://github.com/pppyb/SecOPD)</sub>  
  For indirect prompt-injection defense, this application samples student responses to attacked inputs and scores each token with a frozen initialization model given the corresponding clean input, using detached token advantages for policy updates. It assumes trusted instructions and untrusted data are distinguishable.

- **[Capek 0.5: An Execution-Centric Vision-Language Model for Embodied Intelligence](https://arxiv.org/abs/2608.06756)**  
  <sub>2026-08-07 · Direct OPD</sub>  
  Capek combines specialist weight merging with routed teacher matching on student-generated prefixes. Its consolidation comparisons support complementary roles for TIES initialization and subsequent OPD, with uneven retention across individual capabilities.

- **[AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters](https://arxiv.org/abs/2607.19223)**  
  <sub>2026-07-21 · Hybrid OPD</sub>  
  AdaFlash studies live on-policy distillation of diffusion speculative drafters with a clipped reverse-KL and hard-label objective, alongside online verification-length control; its ablations and serving comparisons show conditional acceptance and throughput gains, without establishing net savings after accounting for separate training resources.

- **[MOPDA: Mixed-Trajectory On-Policy Distillation for Language-Guided Industrial Anomaly Detection](https://arxiv.org/abs/2607.18850)**  
  <sub>2026-07-21 · Hybrid OPD</sub>  
  MOPDA mixes fresh student rollouts with gated, evidence-conditioned EMA-teacher rollouts for token-level distillation; controlled recipe comparisons and paired judgments show benefits on several held-out anomaly datasets, while a separate anchoring ablation tests how the generated judgment guides visual localization.

- **[GR2 Technical Report](https://arxiv.org/abs/2606.31984)**  
  <sub>2026-06-30 · Hybrid OPD</sub>  
  GR2 studies teacher-anchored training of student reasoning and ranked lists before subsequent ranking RL. Its recipe comparisons retain similar ranking performance with better judged reasoning than RL alone, while the reported serving-ROI calculation is not a measured deployment speedup.

- **[Reducing the Safety Tax in LLM Safety Alignment with On-Policy Self-Distillation](https://arxiv.org/abs/2605.15239)**  
  <sub>2026-05-14 · Direct OPD · [Code](https://github.com/FYYFU/OPSA)</sub>  
  For safety alignment, the student generates responses to harmful and benign prompts while a frozen copy conditioned on type-specific safety or helpfulness context supplies token-distribution targets. Context search uses teacher flip rate; the approach depends on privileged prompts eliciting safer behavior.

- **[Reward-Weighted On-Policy Distillation with an Open Property-Equivalence Verifier for NL-to-SVA Generation](https://arxiv.org/abs/2605.13501)**  
  <sub>2026-05-13 · Direct OPD</sub>  
  For natural-language-to-hardware-assertion generation, the student samples candidate assertions, and a property checker retains equivalent or one-way-implying rollouts for reward-weighted, frozen-teacher forward-KL supervision. The checker abstains on unsupported liveness cases, which receive no direct verifier-weighted update.

- **[Self-Distilled Trajectory-Aware Boltzmann Modeling: Bridging the Training-Inference Discrepancy in Diffusion Language Models](https://arxiv.org/abs/2605.11854)**  
  <sub>2026-05-12 · Hybrid OPD</sub>  
  TABOM reuses base-model denoising trajectories for token reconstruction and local entropy-ranking supervision. The ranking component improves over trajectory masking alone in the reported diffusion-language-model experiments, without establishing the proposed global KL interpretation.

- **[LiteGUI: Distilling Compact GUI Agents with Reinforcement Learning](https://arxiv.org/abs/2605.07505)**  
  <sub>2026-05-08 · Direct OPD</sub>  
  LiteGUI distills on student-generated GUI outputs while giving the teacher a matched, human-verified valid action unavailable to the student, then applies dual-level reinforcement learning for planning and execution. Guidance and action rewards depend on a finite annotated set that can miss valid actions.

- **[HyperEyes: Dual-Grained Efficiency-Aware Reinforcement Learning for Parallel Multimodal Search Agents](https://arxiv.org/abs/2605.07177)**  
  <sub>2026-05-08 · Hybrid OPD · [Code](https://github.com/DeepExperience/HyperEyes)</sub>  
  HyperEyes trains a multimodal search agent with an adaptive trajectory-level reward for tool use and external-teacher token correction on failed student rollouts. Its parallel grounded-search action also changes; OPD is enabled for the smaller variant, so full-system results cannot isolate distillation.

- **[DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348)**  
  <sub>2026-04-26 · Application / system report</sub>  
  DeepSeek-V4 consolidates domain specialists through weighted full-vocabulary reverse KL on student-generated trajectories. Its training system caches teacher hidden states and reconstructs logits while scheduling prediction heads by teacher index; this describes the report’s post-training application, with teacher selection tied to task context.

- **[Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220)**  
  <sub>2026-03-19 · Hybrid OPD</sub>  
  Nemotron-Cascade 2 selects strong intermediate checkpoints as domain teachers and distills their sampled-token guidance on student responses during cascade training. Truncated importance weights address differences between generation and training policies; the final model also reflects supervised training and multiple reinforcement learning stages.

- **[Multi-Token Prediction via Self-Distillation](https://arxiv.org/abs/2602.06019)**  
  <sub>2026-02-05 · Direct OPD · [Code](https://github.com/jwkirchenbauer/mtp-lm)</sub>  
  A pretrained autoregressive model learns to propose token blocks in one pass while a frozen copy scores the student’s own greedy proposals. The resulting predictor uses confidence-adaptive decoding; the conversion is evaluated on selected generation tasks rather than all text domains.

- **[ORBIT: On-policy Exploration-Exploitation for Controllable Multi-Budget Reasoning](https://arxiv.org/abs/2601.08310)**  
  <sub>2026-01-13 · Direct OPD</sub>  
  ORBIT trains reasoning-budget specialists through staged reinforcement learning under progressively tighter context limits, then initializes a unified student by merging them and distills their mode-specific behavior on student-generated responses. Its evaluation mainly covers reasoning tasks with structured correctness signals.

- **[MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780)**  
  <sub>2026-01-06 · Hybrid OPD · [Code](https://github.com/XiaomiMiMo/MiMo-V2-Flash)</sub>  
  The report uses multi-teacher on-policy distillation to consolidate domain-specialist capabilities, combining dense token-level teacher rewards with verifiable outcome rewards. This is one stage of a broader post-training pipeline, so the final model’s capabilities cannot be attributed to distillation alone.

- **[VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation](https://arxiv.org/abs/2510.23497)**  
  <sub>2025-10-27 · Hybrid OPD</sub>  
  VOLD transfers text reasoning into a vision-language model through teacher-trace preparation followed by joint reward learning and student-prefix distillation. Controlled comparisons show that the value of the distillation stage depends on preparation and selective supervision, while inconsistent divergence descriptions limit a precise estimator interpretation.

- **[Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)**  
  <sub>2025-05-14 · Application / system report · [Code](https://github.com/QwenLM/Qwen3)</sub>  
  The report describes a small-model compression pipeline that uses off-policy transfer from stronger models before on-policy distillation with teacher-logit guidance. It also describes separate supervised and reinforcement-learning stages for preparing larger models; its student-stage comparison does not account for preparing the stronger teacher.

- **[DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://arxiv.org/abs/2310.08461)**  
  <sub>2023-10-12 · Application / system report</sub>  
  DistillSpec trains a speculative-decoding draft model on draft-generated contexts to match a target model’s next-token distributions, choosing the divergence according to the task and decoding strategy. Its purpose is draft–target alignment for deployment-time verification, not faster distillation training.

[↑ Back to topics](#browse-the-literature)

</details>

<a id="papers-background"></a>

<a id="foundations-and-related-background"></a>

<details><summary><strong>Foundations and related background</strong> &nbsp;·&nbsp; 20</summary>

*Which foundations and comparators clarify OPD?*

- **[SAPD: Step-Aligned Privileged Distillation](https://arxiv.org/abs/2610.09665)**  
  <sub>2026-10-07 · Offline comparator</sub>  
  SAPD matches step-conditioned targets on fixed reference prefixes and reports mathematics accuracy close to the tested OPSD recipe with lower training-loop cost under their respective configurations.

- **[On-Policy Distillation](https://www.thinkingmachines.ai/blog/on-policy-distillation/)**  
  <sub>2025-10-26 · Background · [Code](https://github.com/thinking-machines-lab/tinker-cookbook/tree/main/tinker_cookbook/recipes/distillation)</sub>  
  Student-generated trajectories are scored using teacher log probabilities for sampled tokens, and a policy-gradient-style update uses the negative log-ratio as per-token feedback. This implementation uses immediate next-token credit, not full-vocabulary teacher distributions or future-token returns; the citation here supports sampled-token supervision.

- **[Why Knowledge Distillation Works in Generative Models: A Minimal Working Explanation](https://arxiv.org/abs/2505.13111)**  
  <sub>2025-05-19 · Background · [Code](https://github.com/csm9493/kd-minimal-explanation)</sub>  
  This analysis asks how teacher selectivity changes a distilled generator’s balance between sample quality and distributional coverage. Gaussian-mixture simulations and language-model pretraining experiments find higher precision with lower recall when teacher samples become more selective; they do not test on-policy distillation or post-training.

- **[Distillation Scaling Laws](https://arxiv.org/abs/2502.08606)**  
  <sub>2025-02-12 · Background</sub>  
  This study fits a scaling law for student validation cross-entropy as teacher quality, student size and distillation data vary, then examines compute allocation with different teacher-cost assumptions. It analyzes distillation pre-training, not an on-policy rollout or refresh procedure.

- **[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)**  
  <sub>2025-01-22 · Background</sub>  
  DeepSeek-R1 develops reasoning through reinforcement learning and a staged supervised training pipeline. Its smaller distilled models learn from curated model-generated responses using supervised fine-tuning only; this distillation stage does not train on the smaller students’ own rollouts.

- **[MiniPLM: Knowledge Distillation for Pre-Training Language Models](https://arxiv.org/abs/2410.17215)**  
  <sub>2024-10-22 · Background · [Code](https://github.com/thu-coai/MiniPLM)</sub>  
  MiniPLM selects pre-training texts offline using the probability difference between a teacher and a small reference model, then trains students with ordinary next-token prediction on the selected corpus. Selection does not use current student rollouts or require teacher inference during student training.

- **[HybridFlow: A Flexible and Efficient RLHF Framework](https://arxiv.org/abs/2409.19256)**  
  <sub>2024-09-28 · Background · [Code](https://github.com/verl-project/verl)</sub>  
  HybridFlow is an RLHF execution framework that centrally coordinates dependencies between distributed models while letting each model manage its own computation. It also reshards actor weights between generation and training; these systems mechanisms do not specify teacher targets for on-policy distillation.

- **[Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118)**  
  <sub>2024-07-31 · Background</sub>  
  Gemma 2 pretrains its smaller models by matching a larger teacher’s next-token probabilities on training text. The report separately describes post-training distillation on the student’s distribution, but does not specify the loss or sampling procedure for that stage.

- **[Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2404.02657)**  
  <sub>2024-04-03 · Background · [Code](https://github.com/wutaiqiang/LLM_KD_AKL)</sub>  
  AKL weights forward and reverse token KL according to teacher–student gaps in the distribution’s head and tail, motivated by their different early training behavior. The study uses instruction-response training data and does not establish distillation on student-generated prefixes.

- **[A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116)**  
  <sub>2024-02-20 · Background · [Code](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs)</sub>  
  This survey organizes language-model knowledge distillation by algorithms, transferred skills, and domain-specific uses, including data augmentation and self-generated knowledge. It synthesizes prior work rather than introducing a training rule or establishing which surveyed methods use student-generated prefixes.

- **[Revisiting Knowledge Distillation for Autoregressive Language Models](https://arxiv.org/abs/2402.11890)**  
  <sub>2024-02-19 · Background</sub>  
  This paper separates token-level teacher matching into target-token and non-target-token terms, then adapts their use according to teacher uncertainty: easy tokens omit target-oriented teaching, while hard tokens retain both terms. Its described training uses an instruction-response dataset, not a required student-rollout procedure.

- **[Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335)**  
  <sub>2024-01-02 · Background · [Code](https://github.com/uclaml/SPIN)</sub>  
  SPIN repeatedly generates responses from a previous version of a supervised fine-tuned model and trains the next version to favor existing human demonstrations over those responses. Its comparison target is a fixed demonstration dataset, not a teacher’s token distributions on current student rollouts.

- **[Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180)**  
  <sub>2023-09-12 · Background · [Code](https://github.com/vllm-project/vllm)</sub>  
  PagedAttention stores attention key–value caches in fixed-size blocks that need not occupy contiguous memory, allowing an LLM serving engine to allocate and share cache space across sequences. It addresses generation-time memory management, not teacher supervision or a distillation update.

- **[The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717)**  
  <sub>2023-05-25 · Background</sub>  
  This study fine-tunes models on previously collected outputs from a proprietary language model and compares human ratings with targeted task evaluations. The imitators reproduce response style and instruction following, but show limited gains on tasks poorly represented in the imitation data.

- **[Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://arxiv.org/abs/2305.02301)**  
  <sub>2023-05-03 · Background · [Code](https://github.com/google-research/distilling-step-by-step)</sub>  
  A teacher generates labels and natural-language rationales for task examples; a smaller model learns separate label-prediction and rationale-generation tasks from those outputs. Training uses collected teacher responses rather than student-visited prefixes, and the student can predict labels without requesting a rationale at test time.

- **[Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)**  
  <sub>2022-11-16 · Background · [Code](https://github.com/stanford-crfm/helm)</sub>  
  This evaluation framework organizes language-model use cases and metrics, then benchmarks models across shared scenarios using multiple measures beyond accuracy. Its implemented coverage is selective, and its standardized prompting evaluations are not a training or on-policy distillation method.

- **[Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556)**  
  <sub>2022-03-29 · Background</sub>  
  This study estimates how to allocate a fixed pre-training compute budget between language-model size and training tokens by fitting losses from varied training runs. Its proposed allocation concerns autoregressive pre-training, not the additional generation, teacher, and update costs of on-policy distillation.

- **[Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947)**  
  <sub>2016-06-25 · Background · [Code 1](https://github.com/harvardnlp/nmt-android) · [Code 2](https://github.com/harvardnlp/seq2seq-attn)</sub>  
  For neural machine translation, sequence-level distillation trains a student on teacher beam-search outputs; an alternative selects a beam candidate close to the reference translation. These are teacher-generated training targets, not trajectories sampled from the student during learning.

- **[Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)**  
  <sub>2015-03-09 · Background</sub>  
  Classical distillation trains a smaller model to match a pretrained model’s softened class probabilities on a fixed transfer set, optionally adding a loss on known labels. Its experiments concern classification and speech acoustic models, not student-generated language prefixes.

- **[A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686)**  
  <sub>2010-11-02 · Background</sub>  
  DAgger collects states visited by the learner or an optional learner–expert mixture, obtains expert action labels, and retrains on the accumulated data. Its no-regret analysis concerns sequential imitation under additional assumptions, not language-model token distillation.

[↑ Back to topics](#browse-the-literature)

</details>

<details><summary>About the collection</summary>

The central topic is research that improves, explains, or implements teacher-to-student transfer on student-generated states. Direct matching, hybrid training, teacher-mediated RL, and related comparators are labeled separately. Each topic brings together mechanisms and evidence; it is a reading guide rather than a performance ranking.

Dates denote first public release. Code links identify associated resources; unofficial reproductions are labeled. The public survey is arXiv v4; the reading list includes later work.

</details>

## Research tools

<table>
<thead><tr>
<th align="left" width="440">Compare and understand</th>
<th align="left" width="440">Implement and evaluate</th>
</tr></thead>
<tbody>
<tr>
<td><strong><a href="resources/method-comparison.md">Method comparison</a></strong><br><sub>Supervision requirements and practical trade-offs.</sub></td>
<td><strong><a href="resources/codebases.md">Code index</a></strong><br><sub>Implementations and associated resources.</sub></td>
</tr>
<tr>
<td><strong><a href="resources/loss-taxonomy.md">Objectives</a> · <a href="resources/key-equations.md">Key equations</a></strong><br><sub>Targets, gradients, and sampling assumptions.</sub></td>
<td><strong><a href="resources/benchmarks.md">Evaluation guide</a></strong><br><sub>Benchmarks, costs, and transfer diagnostics.</sub></td>
</tr>
<tr>
<td><strong><a href="resources/related-surveys.md">Related surveys</a></strong><br><sub>Connections to the broader literature.</sub></td>
<td><strong><a href="CONTRIBUTING.md">Suggest a paper or correction</a></strong><br><sub>Help keep the reading list useful.</sub></td>
</tr>
</tbody>
</table>

<a id="updates"></a>
<a id="visual-reference-snapshots"></a>

## Updates and visual references

<details><summary>Latest additions and survey releases</summary>

- **2026-10-12** — Added 59 papers, including MAS-OPD and USA, with expanded reading paths for sparse estimators, adaptive teachers, multi-agent learning, and transfer limits. Redesigned the reading list and OPDHub for easier browsing and comparison. [Explore the collection](https://nick7nlp.github.io/OPDHub/)
- **2026-10-06** — Updated the reading collection to 303 entries, covering OPD objectives, teacher construction, training, analysis, and systems. Expanded the method comparisons and refreshed paper descriptions, references, and repository links across the reading list and OPDHub. [Browse the reading list](https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation)

[All updates and survey releases](CHANGELOG.md)

</details>

<details><summary>Teacher–student model atlas · June 2026</summary>

Rows represent teacher models, columns represent student models, and cells show reported pair occurrences in the June 2026 catalog snapshot. Same-name models can use different conditioning information. This historical view is not a ranking of model quality or a count of the current collection.

<a href="assets/model-atlas-heatmap.png"><img src="assets/model-atlas-heatmap.png" width="960" alt="Teacher–student model-pair matrix, June 2026 snapshot"></a>

</details>

<details><summary>A direct-matching loop</summary>

<img src="assets/opd-overview.png" width="680" alt="Conceptual teacher–student on-policy learning loop">

One direct-matching loop. Teacher feedback is not certified ground truth; other methods use different targets, divergences, or teacher-mediated rewards.

</details>

<details><summary>Earlier loss-label snapshots</summary>

![Historical loss-label distribution](assets/loss-distribution.png)

![Historical loss-label evolution](assets/loss-evolution.png)

The older display classes grouped several non-equivalent mechanisms. Use the current [objective index](resources/loss-taxonomy.md) and [equation guide](resources/key-equations.md) for method-specific descriptions.

</details>

## Citation

```bibtex
@article{song2026opdsurvey,
  title = {A Survey of On-Policy Distillation for Large Language Models},
  author = {Mingyang Song and Mao Zheng},
  journal = {arXiv preprint arXiv:2604.00626},
  year = {2026}
}
```

For corrections, provide the paper version and the primary source supporting the change. See [CONTRIBUTING.md](CONTRIBUTING.md).

[MIT License](LICENSE) · [↑ Back to top](#readme-top)
