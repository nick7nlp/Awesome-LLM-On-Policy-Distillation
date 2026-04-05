<a name="readme-top"></a>

<div align="center">
  <a href="https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation/stargazers"><img src="https://img.shields.io/github/stars/nick7nlp/Awesome-LLM-On-Policy-Distillation?style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation/network/members"><img src="https://img.shields.io/github/forks/nick7nlp/Awesome-LLM-On-Policy-Distillation?style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation/graphs/contributors"><img src="https://img.shields.io/github/contributors/nick7nlp/Awesome-LLM-On-Policy-Distillation?style=for-the-badge" alt="Contributors"></a>
  <a href="https://github.com/nick7nlp/Awesome-LLM-On-Policy-Distillation/blob/master/LICENSE"><img src="https://img.shields.io/github/license/nick7nlp/Awesome-LLM-On-Policy-Distillation?style=for-the-badge" alt="License"></a>
</div>

<br/>

<h1 align="center">🔥 Awesome LLM On-Policy Distillation</h1>

<p align="center">
  <b>A curated collection of papers and resources on On-Policy Distillation for Large Language Models.</b>
</p>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <img src="https://img.shields.io/badge/Papers-80+-blue" alt="Papers">
  <img src="https://img.shields.io/badge/Last%20Updated-April%202026-green" alt="Last Updated">
</p>

<p align="center">
  On-policy distillation trains the student on its <b>own</b> generated outputs rather than the teacher's, eliminating exposure bias and enabling learning from self-generated mistakes. This paradigm has become central to modern LLM post-training pipelines.
</p>

---

<details>
  <summary>📑 <b>Table of Contents</b></summary>
  <ol>
    <li><a href="#-taxonomy">Taxonomy</a></li>
    <li><a href="#-background--foundations">Background & Foundations</a></li>
    <li><a href="#-white-box-on-policy-methods">White-Box On-Policy Methods</a>
      <ul>
        <li><a href="#token-level-divergence-minimization">Token-Level Divergence Minimization</a></li>
        <li><a href="#sequence-level-on-policy-methods">Sequence-Level On-Policy Methods</a></li>
        <li><a href="#hybrid--adaptive-approaches">Hybrid & Adaptive Approaches</a></li>
      </ul>
    </li>
    <li><a href="#-black-box--self-distillation">Black-Box & Self-Distillation</a>
      <ul>
        <li><a href="#black-box-on-policy-distillation">Black-Box On-Policy Distillation</a></li>
        <li><a href="#self-play--self-distillation">Self-Play & Self-Distillation</a></li>
      </ul>
    </li>
    <li><a href="#-reasoning-distillation">Reasoning Distillation</a>
      <ul>
        <li><a href="#chain-of-thought-distillation">Chain-of-Thought Distillation</a></li>
        <li><a href="#reward-guided-on-policy-distillation">Reward-Guided On-Policy Distillation</a></li>
      </ul>
    </li>
    <li><a href="#-industrial-systems--scaling">Industrial Systems & Scaling</a></li>
    <li><a href="#-evaluation--analysis">Evaluation & Analysis</a></li>
    <li><a href="#-related-topics">Related Topics</a></li>
    <li><a href="#-open-problems">Open Problems</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-citation">Citation</a></li>
  </ol>
</details>

---

## 🗺️ Taxonomy

We organize OPD methods along three orthogonal dimensions:

```
On-Policy Distillation
│
├── 📊 Feedback Signal
│   ├── Logit-Based ─── GKD, MiniLLM, DistiLLM, DSKD, EA-OPD ...
│   ├── Outcome-Based ── RLKD, AlignDistil, KDRL, SCoRe ...
│   └── Self-Play ────── SPIN, OPSD, GATES, SDPO ...
│
├── 🔑 Teacher Access
│   ├── White-Box ────── Full logit access
│   ├── Black-Box ────── API-only
│   └── Self ──────────── No external teacher
│
└── 🔍 Granularity
    ├── Token-Level ──── Per-step divergence
    ├── Sequence-Level ── Trajectory reward
    └── Hybrid ──────── Mixed granularity
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 📚 Background & Foundations

| Paper | Date | Key Contribution |
|-------|:----:|-----------------|
| [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 2024 | Process Reward Models |
| [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) | 2023 | Off-policy imitation limits |
| [f-Divergence Minimization for Sequence-Level Knowledge Distillation](https://arxiv.org/abs/2307.15190) | 2023 | f-divergence family for KD |
| [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 2022 | Chinchilla scaling laws |
| [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) | 2016 | Seq-level KD for NMT |
| [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | 2015 | Foundational KD framework |
| [A Reduction of Imitation Learning to No-Regret Online Learning (DAgger)](https://arxiv.org/abs/1011.0686) | 2011 | Foundational on-policy imitation learning |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔬 White-Box On-Policy Methods

### Token-Level Divergence Minimization

> The most active research direction. The student generates on-policy, and the teacher provides dense token-level logit supervision.

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [Entropy-Aware On-Policy Distillation](https://arxiv.org/abs/2603.07079) | 2026 | Dynamically switch Forward/Reverse KL by teacher entropy |
| [PACED: Principled and Adaptive Curriculum for OPD](https://arxiv.org/abs/2603.11178) | 2026 | Beta-kernel zone-of-proximal-development weighting |
| [Veto: Verification-Enhanced Token-Level OPD](https://arxiv.org/abs/2602.12674) | 2026 | Verifier-enhanced token selection |
| [DSKD: Dual-Space Knowledge Distillation](https://arxiv.org/abs/2504.11426) | 2025 | Cross-tokenizer OPD via dual-space projectors |
| [X-KD: Cross-Model Knowledge Distillation](https://arxiv.org/abs/2510.07842) | 2025 | Adaptive token-level switching with context-aware threshold |
| [REOPOLD: OPD as Policy Optimization](https://arxiv.org/abs/2503.00386) | 2025 | Reinterpret OPD as RL (teacher-student ratio = reward) |
| [KETCHUP: Token-wise Credit via Hierarchical Underwriting](https://arxiv.org/abs/2503.02832) | 2025 | Hierarchical credit assignment for token-level KD |
| [DDT: Distillation via Difference of Distributions](https://arxiv.org/abs/2505.16297) | 2025 | Sigmoid-weighted Forward+Reverse KL per token |
| [GKD: On-Policy Distillation of Language Models](https://arxiv.org/abs/2306.13649) | 2024 | ⭐ Foundational OPD: student generates, teacher scores |
| [MiniLLM: Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) | 2024 | ⭐ Reverse KL + policy gradient for OPD |
| [DistiLLM: Streamlined Distillation for LLMs](https://arxiv.org/abs/2402.03898) | 2024 | Skewed KL + adaptive off-policy sampling |
| [DistiLLM-2: Versatile On-Policy KD Framework](https://arxiv.org/abs/2412.15218) | 2024 | Generalized f-divergence OPD framework |
| **Fast OPD** [Fast OPD with Gradient-Level KD](https://arxiv.org/abs/2408.00118) | 2024 | Gradient-level supervision for efficiency |
| [Generalized On-Policy Distillation](https://arxiv.org/abs/2402.12842) | 2024 | Generalized divergence family |
| [TSD-KD: Token-Selective Distillation](https://arxiv.org/abs/2402.13116) | 2024 | Select informative tokens for distillation |
| [DASD: Dual Adaptive Self-Distillation](https://arxiv.org/abs/2407.14679) | 2024 | Self-distillation with dual adaptive mechanisms |

### Sequence-Level On-Policy Methods

> The student generates complete sequences; the loss is applied at the trajectory level.

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [SCoRe: Multi-Turn Self-Correction for Reasoning](https://arxiv.org/abs/2509.14257) | 2025 | Multi-turn correction with teacher feedback on earliest error |
| [MiniLLM](https://arxiv.org/abs/2306.08543) | 2024 | Policy gradient with teacher log-probs as reward |
| [Constrained On-Policy Distillation](https://arxiv.org/abs/2402.11890) | 2024 | KL-constrained sequence-level objective |

### Hybrid & Adaptive Approaches

> Combining token-level and sequence-level signals; adaptive divergence selection.

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [PACED](https://arxiv.org/abs/2603.11178) | 2026 | Minimax-robust curriculum + adaptive granularity |
| [AdaSwitch: Adaptive Switching for Token-Level Distillation](https://arxiv.org/abs/2510.07842) | 2025 | Context-aware threshold for teacher guidance |
| **Fast OPD** [Fast OPD](https://arxiv.org/abs/2408.00118) | 2024 | Gradient-level signal bridging token and sequence |
| [SuperCorrect: Hierarchical Thought Templates](https://arxiv.org/abs/2410.09008) | 2024 | Step-level reasoning distillation + cross-model DPO |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌐 Black-Box & Self-Distillation

### Black-Box On-Policy Distillation

> When the teacher is API-only (no logit access).

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [OVD: On-Policy Verifiable Distillation](https://arxiv.org/abs/2603.24596) | 2026 | Cross-modal OPD (text teacher → speech student) |
| [GAD: Generative Adversarial Distillation](https://arxiv.org/abs/2511.10643) | 2025 | Discriminator distinguishes student from API output |
| [LUFFY: Merging Exploration and Exploitation in OPD](https://arxiv.org/abs/2504.14945) | 2025 | Dynamic coefficient balancing exploration and imitation |
| [Lion: Adversarial Distillation of Proprietary LLMs](https://arxiv.org/abs/2305.12870) | 2023 | Teacher as preference annotator + curriculum designer |

### Self-Play & Self-Distillation

> No external teacher; the model improves through self-generated feedback.

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [OPSD: On-Policy Self-Distillation for LLMs](https://arxiv.org/abs/2601.18734) | 2026 | Privileged info (ground-truth) as teacher signal |
| [OPSDC: Self-Distillation for Reasoning Compression](https://arxiv.org/abs/2603.05433) | 2026 | "Be concise" self-distillation, 57-59% token reduction |
| [GATES: Gated Self-Distillation without Ground-Truth](https://arxiv.org/abs/2602.20574) | 2026 | Consensus-based gating for self-distillation |
| [SDPO: Self-Distillation Policy Optimization](https://arxiv.org/abs/2601.20802) | 2026 | Rich textual feedback → dense token-level self-distillation |
| [OEL: Online Experiential Learning](https://arxiv.org/abs/2603.16856) | 2026 | Continuous post-deployment on-policy context distillation |
| [SDFT: Self-Distillation for Continual Learning](https://arxiv.org/abs/2601.19897) | 2026 | On-policy self-distillation reduces catastrophic forgetting |
| [HDPO: Hybrid Distillation Policy Optimization](https://arxiv.org/abs/2503.00386) | 2026 | Privileged distillation for "cliff prompts" |
| [Privileged Information Distillation](https://arxiv.org/abs/2602.04942) | 2026 | Training-time privileged info for hard RL settings |
| [SPIN: Self-Play Fine-Tuning](https://arxiv.org/abs/2401.01335) | 2024 | Two-player game: distinguish self vs human |
| [OPCD: On-Policy Context Distillation](https://arxiv.org/abs/2402.12842) | 2024 | Internalize experiential knowledge via context distillation |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧠 Reasoning Distillation

### Chain-of-Thought Distillation

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [Qwen3: MTP Self-Distillation for Reasoning](https://arxiv.org/abs/2505.09388) | 2025 | Multi-teacher distillation + thinking mode control |
| [Distilling Reasoning Capabilities into Smaller LMs](https://arxiv.org/abs/2212.00193) | 2023 | Specialized reasoning distillation |
| [Distilling Step-by-Step](https://arxiv.org/abs/2305.02301) | 2023 | Extract rationales as training signal |

### Reward-Guided On-Policy Distillation

| Paper | Date | Key Innovation |
|-------|:----:|----------------|
| [KEPO: Knowledge-Enhanced Policy Optimization](https://arxiv.org/abs/2602.12125) | 2026 | Student exceeds teacher via reward-guided exploration |
| [RLKD: Reinforcement Learning via KD](https://arxiv.org/abs/2505.16142) | 2025 | RL objective with KD regularization |
| [AlignDistil: Align-then-Distill](https://arxiv.org/abs/2503.02832) | 2025 | Preference optimization + OPD |
| [KDRL: Joint KD and RL](https://arxiv.org/abs/2506.02208) | 2025 | Jointly optimize KD+RL to prevent forgetting |
| [RLAD: RL with Auxiliary Distillation](https://arxiv.org/abs/2512.23097) | 2025 | Unified KD+RL framework |
| [VOLD: Vision-Language On-Policy Distillation](https://arxiv.org/abs/2510.23497) | 2025 | Text teacher → VLM student with SFT cold-start |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🏭 Industrial Systems & Scaling

| Paper | Date | Key Insight |
|-------|:----:|-------------|
| [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | 2025 | 7B student achieves 92.8% on MATH-500 from 671B teacher (off-policy baseline) |
| [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025 | Multi-teacher OPD at scale; thinking mode distillation |
| [RL Post-Training Retains More Capabilities](https://arxiv.org/abs/2510.18874) | 2025 | RL retains more pre-training knowledge than SFT |
| [Distillation Scaling Laws](https://arxiv.org/abs/2502.08606) | 2025 | Off-policy distillation scaling (on-policy still open!) |
| [Precision-Recall Trade-off in Distillation](https://arxiv.org/abs/2505.13111) | 2025 | Entropy controls precision vs recall in KD |

---

## 📊 Evaluation & Analysis

| Paper | Date | Key Insight |
|-------|:----:|-------------|
| [OPD on Benchmarks vs. Distribution Shift](https://arxiv.org/abs/2603.25562) | 2026 | Benchmark performance ≠ true generalization |
| [Does RL Really Incentivize Reasoning in LLMs?](https://arxiv.org/abs/2504.13837) | 2025 | RLVR improves sampling efficiency, not reasoning ability |
| [Cross-Tokenizer KD](https://arxiv.org/abs/2402.12030) | 2025 | Optimal transport for vocabulary mismatch |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔗 Related Topics

| Topic | Paper | Date | Key Idea |
|:-----:|-------|:----:|----------|
| Speculative Decoding | [DistillSpec](https://arxiv.org/abs/2310.08461) | 2023 | Distillation improves speculative decoding draft models |
| Latent-Space KD | [Delta KD](https://arxiv.org/abs/2509.14526) | 2025 | Preserve distributional shift rather than match absolutes |
| Agent Distillation | [OEL](https://arxiv.org/abs/2603.16856) | 2026 | Continuous post-deployment learning |
| Agent Distillation | [SCoRe](https://arxiv.org/abs/2509.14257) | 2025 | Multi-step agent trajectory correction |

---

## 🗺️ Open Problems

> Key open research directions in on-policy distillation:

| # | Problem | Description |
|:-:|---------|-------------|
| 1 | **Scaling Laws** | No equivalent of Chinchilla for OPD; the student rollout cost adds a new compute axis |
| 2 | **Teacher Calibration** | Teacher logits may be miscalibrated on student-generated OOD prefixes |
| 3 | **Dynamic Curriculum** | Principled difficulty scheduling that adapts as the student improves |
| 4 | **Cross-Architecture OPD** | Distilling across model families with different tokenizers |
| 5 | **Agent OPD** | Multi-step, tool-using agents with delayed feedback |
| 6 | **Multimodal OPD** | Extending to vision-language and speech models |
| 7 | **KD-RL Loop** | Principled alternation between distillation and RL phases |
| 8 | **Beyond Benchmarks** | Dynamic adversarial testing for true generalization |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🤝 Contributing

We welcome contributions! Please submit a **Pull Request** with:

- 📎 Paper title, arXiv link, and date
- 📝 Brief description of the key contribution
- 📂 Correct category placement

Please **do not** fabricate venue information — if unsure, leave it blank or mark as arXiv preprint.

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

<div align="center">

**⭐ If you find this repository useful, please star it! ⭐**

*Last updated: April 2026*

</div>
