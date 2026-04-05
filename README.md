# Awesome LLM On-Policy Distillation 🔥

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Last Updated](https://img.shields.io/badge/Last%20Updated-April%202026-green)
![Papers](https://img.shields.io/badge/Papers-80+-blue)

A curated collection of papers, resources, and tools for **On-Policy Distillation (OPD)** of Large Language Models.

On-policy distillation trains the student model on its *own* generated outputs rather than the teacher's, eliminating exposure bias and enabling the student to learn from its own mistakes. This paradigm has become central to modern LLM post-training pipelines (DeepSeek-R1, Qwen3, etc.).

> 📖 This repository accompanies our survey: **"A Survey of On-Policy Distillation for Large Language Models"** (coming soon).

---

## 📑 Table of Contents

- [Survey & Overview](#-survey--overview)
- [Background & Foundations](#-background--foundations)
- [White-Box On-Policy Methods](#-white-box-on-policy-methods)
  - [Token-Level Divergence Minimization](#token-level-divergence-minimization)
  - [Sequence-Level On-Policy Methods](#sequence-level-on-policy-methods)
  - [Hybrid & Adaptive Approaches](#hybrid--adaptive-approaches)
- [Black-Box & Self-Distillation](#-black-box--self-distillation)
  - [Black-Box On-Policy Distillation](#black-box-on-policy-distillation)
  - [Self-Play & Self-Distillation](#self-play--self-distillation)
- [Reasoning Distillation](#-reasoning-distillation)
  - [Chain-of-Thought Distillation](#chain-of-thought-distillation)
  - [Reward-Guided On-Policy Distillation](#reward-guided-on-policy-distillation)
- [Industrial Systems & Scaling](#-industrial-systems--scaling)
- [Evaluation & Analysis](#-evaluation--analysis)
- [Related Topics](#-related-topics)
- [Contributing](#-contributing)

---

## 📖 Survey & Overview

| Paper | Date |
|-------|------|
| [A Survey of On-Policy Distillation for Large Language Models](#) | 2026 |

### Taxonomy

We organize OPD methods along three orthogonal dimensions:

```
On-Policy Distillation
├── Feedback Signal
│   ├── Logit-Based (GKD, MiniLLM, DistiLLM, DSKD, Entropy-Aware, ...)
│   ├── Outcome-Based (RLKD, AlignDistil, KDRL, SCoRe, ...)
│   └── Self-Play (SPIN, OPSD, GATES, SDPO, ...)
├── Teacher Access
│   ├── White-Box (full logits accessible)
│   ├── Black-Box (API-only)
│   └── Self-Distillation (no external teacher)
└── Granularity
    ├── Token-Level (per-step divergence)
    ├── Sequence-Level (trajectory reward)
    └── Hybrid / Adaptive (mixed granularity)
```

---

## 📚 Background & Foundations

| Paper | Date | Key Contribution |
|-------|------|-----------------|
| [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 2024 | Process Reward Models |
| [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) | 2023 | Off-policy imitation limits |
| [f-Divergence Minimization for Sequence-Level Knowledge Distillation](https://arxiv.org/abs/2307.15190) | 2023 | f-divergence family for KD |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 2022 | Chinchilla scaling laws |
| [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) | 2016 | Seq-level KD for NMT |
| [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | 2015 | Foundational KD framework |
| [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686) | 2011 | DAgger — foundational on-policy IL |

---

## 🔬 White-Box On-Policy Methods

### Token-Level Divergence Minimization

The most active research direction. The student generates on-policy, and the teacher provides dense token-level logit supervision.

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [Entropy-Aware On-Policy Distillation](https://arxiv.org/abs/2603.07079) | **EA-OPD** | 2026 | Dynamically switch Forward/Reverse KL by teacher entropy |
| [PACED: Principled and Adaptive Curriculum for On-Policy Distillation](https://arxiv.org/abs/2603.11178) | **PACED** | 2026 | Beta-kernel zone-of-proximal-development weighting |
| [Veto: Verification-Enhanced Token-Level OPD](https://arxiv.org/abs/2602.12674) | **Veto** | 2026 | Verifier-enhanced token selection |
| [DSKD: Dual-Space Knowledge Distillation for LLMs](https://arxiv.org/abs/2504.11426) | **DSKD** | 2025 | Cross-tokenizer OPD via dual-space projectors |
| [X-KD: Cross-Model Knowledge Distillation](https://arxiv.org/abs/2510.07842) | **X-KD** | 2025 | Adaptive token-level switching with context-aware threshold |
| [REOPOLD: On-Policy Distillation as Policy Optimization](https://arxiv.org/abs/2503.00386) | **REOPOLD** | 2025 | Reinterpret OPD as RL (teacher-student ratio = reward) |
| [KETCHUP: Knowledge Extraction for Token-wise Credit via Hierarchical Underwriting](https://arxiv.org/abs/2503.02832) | **KETCHUP** | 2025 | Hierarchical credit assignment for token-level KD |
| [DDT: Distillation via Difference of Distributions](https://arxiv.org/abs/2505.16297) | **DDT/ToDi** | 2025 | Sigmoid-weighted Forward+Reverse KL per token |
| [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649) | **GKD** | 2024 | Foundational OPD: student generates, teacher scores |
| [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) | **MiniLLM** | 2024 | Reverse KL + policy gradient for OPD |
| [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898) | **DistiLLM** | 2024 | Skewed KL + adaptive off-policy sampling |
| [DistiLLM-2: A Versatile Framework for On-Policy Knowledge Distillation](https://arxiv.org/abs/2412.15218) | **DistiLLM-2** | 2024 | Generalized f-divergence OPD framework |
| [Fast On-Policy Distillation with Gradient-Level KD](https://arxiv.org/abs/2408.00118) | **Fast OPD** | 2024 | Gradient-level supervision for efficiency |
| [Generalized On-Policy Distillation](https://arxiv.org/abs/2402.12842) | **G-OPD** | 2024 | Generalized divergence family |
| [TSD-KD: Token-Selective Distillation](https://arxiv.org/abs/2402.13116) | **TSD-KD** | 2024 | Select informative tokens for distillation |
| [DASD: Dual Adaptive Self-Distillation](https://arxiv.org/abs/2407.14679) | **DASD** | 2024 | Self-distillation with dual adaptive mechanisms |

### Sequence-Level On-Policy Methods

The student generates complete sequences; the loss is applied at the trajectory level.

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [SCoRe: Multi-Turn Self-Correction for Reasoning](https://arxiv.org/abs/2509.14257) | **SCoRe** | 2025 | Multi-turn correction with teacher feedback on earliest error |
| [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) | **MiniLLM** | 2024 | Policy gradient with teacher log-probs as reward |
| [Constrained On-Policy Distillation](https://arxiv.org/abs/2402.11890) | **Constrained** | 2024 | KL-constrained sequence-level objective |

### Hybrid & Adaptive Approaches

Combining token-level and sequence-level signals; adaptive divergence selection.

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [PACED](https://arxiv.org/abs/2603.11178) | **PACED** | 2026 | Minimax-robust curriculum + adaptive granularity |
| [AdaSwitch: Adaptive Switching for Token-Level Distillation](https://arxiv.org/abs/2510.07842) | **AdaSwitch** | 2025 | Context-aware threshold for token-level teacher guidance |
| [Fast OPD](https://arxiv.org/abs/2408.00118) | **Fast OPD** | 2024 | Gradient-level signal bridging token and sequence |
| [SuperCorrect: Teacher-Guided Hierarchical Thought Templates](https://arxiv.org/abs/2410.09008) | **SuperCorrect** | 2024 | Step-level reasoning distillation + cross-model DPO |

---

## 🌐 Black-Box & Self-Distillation

### Black-Box On-Policy Distillation

When the teacher is API-only (no logit access).

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [OVD: On-Policy Verifiable Distillation](https://arxiv.org/abs/2603.24596) | **OVD** | 2026 | Cross-modal OPD (text teacher → speech student) |
| [GAD: Generative Adversarial Distillation](https://arxiv.org/abs/2511.10643) | **GAD** | 2025 | Discriminator distinguishes student from API output |
| [LUFFY: Merging Exploration and Exploitation in OPD](https://arxiv.org/abs/2504.14945) | **LUFFY** | 2025 | Dynamic coefficient balancing exploration and imitation |
| [Lion: Adversarial Distillation of Proprietary LLMs](https://arxiv.org/abs/2305.12870) | **Lion** | 2023 | Teacher as preference annotator + curriculum designer |

### Self-Play & Self-Distillation

No external teacher; the model improves through self-generated feedback.

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [On-Policy Self-Distillation for LLMs (OPSD)](https://arxiv.org/abs/2601.18734) | **OPSD** | 2026 | Privileged info (ground-truth) as teacher signal |
| [OPSDC: On-Policy Self-Distillation for Reasoning Compression](https://arxiv.org/abs/2603.05433) | **OPSDC** | 2026 | "Be concise" self-distillation, 57-59% token reduction |
| [GATES: Gated Self-Distillation without Ground-Truth](https://arxiv.org/abs/2602.20574) | **GATES** | 2026 | Consensus-based gating for self-distillation |
| [SDPO: Self-Distillation Policy Optimization](https://arxiv.org/abs/2601.20802) | **SDPO** | 2026 | Rich textual feedback → dense token-level self-distillation |
| [OEL: Online Experiential Learning](https://arxiv.org/abs/2603.16856) | **OEL** | 2026 | Continuous post-deployment on-policy context distillation |
| [SDFT: Self-Distillation for Continual Learning](https://arxiv.org/abs/2601.19897) | **SDFT** | 2026 | On-policy self-distillation reduces catastrophic forgetting |
| [HDPO: Hybrid Distillation Policy Optimization](https://arxiv.org/abs/2503.00386) | **HDPO** | 2026 | Privileged distillation for "cliff prompts" |
| [Privileged Information Distillation](https://arxiv.org/abs/2602.04942) | **PI-Distill** | 2026 | Training-time privileged info for hard RL settings |
| [Self-Play Fine-Tuning Converts Weak to Strong Models](https://arxiv.org/abs/2401.01335) | **SPIN** | 2024 | Two-player game: distinguish self vs human |
| [OPCD: On-Policy Context Distillation](https://arxiv.org/abs/2402.12842) | **OPCD** | 2024 | Internalize experiential knowledge via context distillation |

---

## 🧠 Reasoning Distillation

### Chain-of-Thought Distillation

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [MTP Self-Distillation for Reasoning](https://arxiv.org/abs/2505.09388) | **Qwen3** | 2025 | Multi-teacher distillation + thinking mode control |
| [Distilling Reasoning Capabilities into Smaller LMs](https://arxiv.org/abs/2212.00193) | - | 2023 | Specialized reasoning distillation |
| [Distilling Step-by-Step](https://arxiv.org/abs/2305.02301) | **DSS** | 2023 | Extract rationales as training signal |

### Reward-Guided On-Policy Distillation

| Paper | Abbrev. | Date | Key Innovation |
|-------|---------|------|----------------|
| [KEPO: Knowledge-Enhanced Policy Optimization](https://arxiv.org/abs/2602.12125) | **KEPO** | 2026 | Student exceeds teacher via reward-guided exploration |
| [DeepSeek-R1: Incentivizing Reasoning in LLMs via RL](https://arxiv.org/abs/2501.12948) | **DeepSeek-R1** | 2025 | Off-policy reasoning distillation at scale |
| [RLKD: Reinforcement Learning via KD](https://arxiv.org/abs/2505.16142) | **RLKD** | 2025 | RL objective with KD regularization |
| [AlignDistil: Align-then-Distill](https://arxiv.org/abs/2503.02832) | **AlignDistil** | 2025 | Preference optimization + OPD |
| [KDRL: Joint KD and RL](https://arxiv.org/abs/2506.02208) | **KDRL** | 2025 | Jointly optimize KD+RL to prevent forgetting |
| [RLAD: Reinforcement Learning with Auxiliary Distillation](https://arxiv.org/abs/2512.23097) | **RLAD** | 2025 | Unified KD+RL framework |
| [VOLD: Vision-Language On-Policy Distillation](https://arxiv.org/abs/2510.23497) | **VOLD** | 2025 | Text teacher → VLM student with SFT cold-start |

---

## 🏭 Industrial Systems & Scaling

| Paper | Date | Key Insight |
|-------|------|-------------|
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 2025 | 7B student achieves 92.8% on MATH-500 from 671B teacher |
| [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025 | Multi-teacher OPD at scale; thinking mode distillation |
| [RL Post-Training Retains More Capabilities](https://arxiv.org/abs/2510.18874) | 2025 | RL retains more pre-training knowledge than SFT |
| [Distillation Scaling Laws](https://arxiv.org/abs/2502.08606) | 2025 | Off-policy distillation scaling (on-policy still open!) |
| [Precision-Recall Trade-off in Distillation](https://arxiv.org/abs/2505.13111) | 2025 | Entropy controls precision vs recall in KD |

---

## 📊 Evaluation & Analysis

| Paper | Date | Key Insight |
|-------|------|-------------|
| [OPD Can Appear Successful on Benchmarks While Failing on Distribution Shift](https://arxiv.org/abs/2603.25562) | 2026 | Benchmark performance ≠ true generalization |
| [Does RL Really Incentivize Reasoning in LLMs?](https://arxiv.org/abs/2504.13837) | 2025 | RLVR improves sampling efficiency, not reasoning ability |
| [Cross-Tokenizer KD](https://arxiv.org/abs/2402.12030) | 2025 | Optimal transport for vocabulary mismatch |

---

## 🔗 Related Topics

### Speculative Decoding + Distillation
| Paper | Date | Key Idea |
|-------|------|----------|
| [DistillSpec](https://arxiv.org/abs/2310.08461) | 2023 | Distillation improves speculative decoding draft models |

### Latent-Space Distillation
| Paper | Date | Key Idea |
|-------|------|----------|
| [Delta KD](https://arxiv.org/abs/2509.14526) | 2025 | Preserve distributional shift rather than match absolutes |

### Agent & Tool Distillation
| Paper | Date | Key Idea |
|-------|------|----------|
| [OEL](https://arxiv.org/abs/2603.16856) | 2026 | Continuous post-deployment learning in interactive environments |
| [SCoRe](https://arxiv.org/abs/2509.14257) | 2025 | Multi-step agent trajectory correction |

---

## 🗺️ Open Problems

The following remain open research directions:

1. **On-Policy Distillation Scaling Laws** — No equivalent of Chinchilla for OPD; the student rollout cost adds a new compute axis
2. **Teacher Calibration & Uncertainty** — Teacher logits may be miscalibrated on student-generated OOD prefixes
3. **Dynamic Curriculum** — Principled difficulty scheduling that adapts as the student improves
4. **Cross-Architecture OPD** — Distilling across model families with different tokenizers and architectures
5. **OPD for Autonomous Agents** — Multi-step, tool-using agents with delayed feedback
6. **Multimodal OPD** — Extending to vision-language and speech models
7. **Closing the KD-RL Loop** — Principled alternation between distillation and RL phases
8. **Evaluation Beyond Benchmarks** — Dynamic adversarial testing for true generalization

---

## 🤝 Contributing

We welcome contributions! Please submit a pull request with:
- Paper title, link, venue, and date
- Brief description of the key contribution
- Correct category placement

---

## ⭐ Star History

If you find this repository useful, please star it! ⭐

---

## 📄 Citation

If you find this collection helpful, please consider citing our survey (paper link coming soon):

```bibtex
@article{opd-survey-2026,
  title={A Survey of On-Policy Distillation for Large Language Models},
  author={},
  year={2026}
}
```

---

*Last updated: April 2026*
