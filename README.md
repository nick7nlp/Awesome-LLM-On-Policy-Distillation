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
  <img src="https://img.shields.io/badge/Papers-95-blue" alt="Papers">
  <img src="https://img.shields.io/badge/Last%20Updated-April%202026-green" alt="Last Updated">
</p>

<p align="center">
  On-policy distillation trains the student on its <b>own</b> generated outputs rather than the teacher's, eliminating exposure bias and enabling learning from self-generated mistakes. This paradigm has become central to modern LLM post-training pipelines.
</p>

<p align="center">
  📖 <b>Survey Paper:</b> <a href="https://arxiv.org/abs/2604.00626">A Survey of On-Policy Distillation for Large Language Models</a>
</p>

<p align="center">
  🟢 = In survey &nbsp;&nbsp; 🟡 = New (not yet in survey)
</p>

<p align="center">
</p>

---

<details>
  <summary>📑 <b>Table of Contents</b></summary>
  <ol>
    <li><a href="#-taxonomy">Taxonomy</a></li>
    <li><a href="#-background--foundations">Background & Foundations</a></li>
    <li><a href="#-token-level-on-policy-methods">Token-Level On-Policy Methods</a></li>
    <li><a href="#-sequence-level--hybrid-methods">Sequence-Level & Hybrid Methods</a></li>
    <li><a href="#-black-box-on-policy-distillation">Black-Box On-Policy Distillation</a></li>
    <li><a href="#-self-play--self-distillation">Self-Play & Self-Distillation</a></li>
    <li><a href="#-reasoning-distillation">Reasoning Distillation</a></li>
    <li><a href="#-reward-guided-on-policy-distillation">Reward-Guided On-Policy Distillation</a></li>
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

```
On-Policy Distillation
│
├── 📊 Feedback Signal
│   ├── Logit-Based ─── GKD, MiniLLM, DistiLLM, DSKD, EA-OPD ...
│   ├── Outcome-Based ── RLKD, AlignDistil, KDRL ...
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

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/openai/prm800k) |
| 🟢 [f-Divergence Minimization for Sequence-Level Knowledge Distillation](https://arxiv.org/abs/2307.15190) | 2023 |  |
| 🟢 [The False Promise of Imitating Proprietary LLMs](https://arxiv.org/abs/2305.15717) | 2023 |  |
| 🟢 [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | 2022 |  |
| 🟢 [Sequence-Level Knowledge Distillation](https://arxiv.org/abs/1606.07947) | 2016 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/harvardnlp/seq2seq-attn) |
| 🟢 [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) | 2015 |  |
| 🟢 [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning](https://arxiv.org/abs/1011.0686) | 2011 |  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔬 Token-Level On-Policy Methods

> The student generates on-policy; the teacher provides dense token-level logit supervision.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟡 [Stable-OPD: Length Inflation and Stabilization Strategies for Large Language Models](https://arxiv.org/abs/2604.08527) | 2026 |  |
| 🟡 [On-Policy Distillation of Language Models for Autonomous Vehicle Motion Planning](https://arxiv.org/abs/2604.07944) | 2026 |  |
| 🟡 [DP-OPD: Differentially Private On-Policy Distillation for Language Models](https://arxiv.org/abs/2604.04461) | 2026 |  |
| 🟡 [VLA-OPD: Bridging Offline SFT and Online RL for Vision-Language-Action Models via On-Policy Distillation](https://arxiv.org/abs/2603.26666) | 2026 |  |
| 🟢 [Explain in Your Own Words: Improving Reasoning via Token-Selective Dual Knowledge Distillation](https://arxiv.org/abs/2603.13260) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/kmswin1/TSD-KD) |
| 🟢 [PACED: Distillation and Self-Distillation at the Frontier of Student Competence](https://arxiv.org/abs/2603.11178) | 2026 |  |
| 🟢 [Scaling Reasoning Efficiently via Relaxed On-Policy Distillation](https://arxiv.org/abs/2603.11137) | 2026 |  |
| 🟢 [Entropy-Aware On-Policy Distillation of Language Models](https://arxiv.org/abs/2603.07079) | 2026 |  |
| 🟢 [X-KD: General Experiential Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2602.12674) | 2026 |  |
| 🟢 [Stable On-Policy Distillation through Adaptive Target Reformulation](https://arxiv.org/abs/2601.07155) | 2026 |  |
| 🟢 [SelecTKD: Selective Token-Weighted Knowledge Distillation for LLMs](https://arxiv.org/abs/2510.24021) | 2025 |  |
| 🟢 [LLM-Oriented Token-Adaptive Knowledge Distillation](https://arxiv.org/abs/2510.11615) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/SassyRong/AdaKD) |
| 🟢 [AdaSwitch: Balancing Exploration and Guidance in Knowledge Distillation via Adaptive Switching](https://arxiv.org/abs/2510.07842) | 2025 |  |
| 🟢 [ToDi: Token-wise Distillation via Fine-Grained Divergence Control](https://arxiv.org/abs/2505.16297) | 2025 |  |
| 🟢 [KETCHUP: K-Step Return Estimation for Sequential Knowledge Distillation](https://arxiv.org/abs/2504.19024) | 2025 |  |
| 🟢 [A Dual-Space Framework for General Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2504.11426) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/songmzhang/DSKDv2) |
| 🟢 [DistiLLM-2: A Contrastive Approach Boosts the Distillation of LLMs](https://arxiv.org/abs/2503.07067) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/jongwooko/distillm-2) |
| 🟢 [Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2404.02657) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/wutaiqiang/LLM_KD_AKL) |
| 🟢 [Revisiting Knowledge Distillation for Autoregressive Language Models](https://arxiv.org/abs/2402.11890) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/WHU-ZQH/ATKD) |
| 🟢 [DistiLLM: Towards Streamlined Distillation for Large Language Models](https://arxiv.org/abs/2402.03898) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/jongwooko/distillm) |
| 🟢 [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://arxiv.org/abs/2306.13649) | 2024 |  |
| 🟢 [MiniLLM: On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2306.08543) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/microsoft/LMOps/tree/main/minillm) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔄 Sequence-Level & Hybrid Methods

> Complete sequence generation + trajectory-level loss, or mixing token and sequence signals.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟡 [Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing](https://arxiv.org/abs/2604.02288) | 2026 |  |
| 🟢 [Fast and Effective On-policy Distillation from Reasoning Prefixes](https://arxiv.org/abs/2602.15260) | 2026 |  |
| 🟢 [Towards On-Policy SFT: Distribution Discriminant Theory and its Applications in LLM Training](https://arxiv.org/abs/2602.12222) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT) |
| 🟢 [TMS: Trajectory-Mixed Supervision for Reward-Free, On-Policy SFT](https://arxiv.org/abs/2602.03073) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/UNITES-Lab/tms) |
| 🟢 [Didactic to Constructive: Turning Expert Solutions into Learnable Reasoning](https://arxiv.org/abs/2602.02405) | 2026 |  |
| 🟡 [CORD: Bridging the Audio-Text Reasoning Gap via Weighted On-policy Cross-modal Distillation](https://arxiv.org/abs/2601.16547) | 2026 |  |
| 🟢 [Rethinking Large Language Model Distillation: A Constrained Markov Decision Process Perspective](https://arxiv.org/abs/2509.22921) | 2025 |  |
| 🟢 [SuperCorrect: Advancing Small LLM Reasoning with Thought Template Distillation and Self-Correction](https://arxiv.org/abs/2410.09008) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/YangLing0818/SuperCorrect-llm) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/BitStarWalkin/SuperCorrect-7B) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🌐 Black-Box On-Policy Distillation

> When the teacher is API-only (no logit access).

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs](https://arxiv.org/abs/2603.24596) | 2026 |  |
| 🟢 [Black-Box On-Policy Distillation of Large Language Models](https://arxiv.org/abs/2511.10643) | 2025 |  |
| 🟢 [Learning to Reason under Off-Policy Guidance](https://arxiv.org/abs/2504.14945) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/ElliottYan/LUFFY) |
| 🟢 [Lion: Adversarial Distillation of Proprietary Large Language Models](https://arxiv.org/abs/2305.12870) | 2023 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/YJiangcm/Lion) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔁 Self-Play & Self-Distillation

> No external teacher; the model improves through self-generated feedback.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟡 [Self-Distilled RLVR](https://arxiv.org/abs/2604.03128) | 2026 |  |
| 🟡 [Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/abs/2604.01193) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/apple/ml-ssd) |
| 🟢 [Why Does Self-Distillation (Sometimes) Degrade the Reasoning Capability of LLMs?](https://arxiv.org/abs/2603.24472) | 2026 |  |
| 🟢 [HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation](https://arxiv.org/abs/2603.23871) | 2026 |  |
| 🟢 [Online Experiential Learning for Language Models](https://arxiv.org/abs/2603.16856) | 2026 |  |
| 🟡 [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/Gen-Verse/OpenClaw-RL) |
| 🟢 [On-Policy Self-Distillation for Reasoning Compression](https://arxiv.org/abs/2603.05433) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/HJSang/OPSD_Reasoning_Compression) |
| 🟢 [GATES: Self-Distillation under Privileged Context with Consensus Gating](https://arxiv.org/abs/2602.20574) | 2026 |  |
| 🟡 [On-Policy Supervised Fine-Tuning for Efficient Reasoning](https://arxiv.org/abs/2602.13407) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/EIT-NLP/On-Policy-SFT) |
| 🟢 [Multi-Token Prediction via Self-Distillation](https://arxiv.org/abs/2602.06019) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/jwkirchenbauer/mtp-lm) |
| 🟢 [Privileged Information Distillation for Language Models](https://arxiv.org/abs/2602.04942) | 2026 |  |
| 🟡 [Expanding the Capabilities of Reinforcement Learning via Text Feedback](https://arxiv.org/abs/2602.02482) | 2026 |  |
| 🟢 [Reinforcement Learning via Self-Distillation](https://arxiv.org/abs/2601.20802) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/lasgroup/SDPO) |
| 🟢 [Self-Distillation Enables Continual Learning](https://arxiv.org/abs/2601.19897) | 2026 |  |
| 🟢 [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/siyan-zhao/OPSD) |
| 🟢 [Distribution-Aligned Sequence Distillation for Superior Long-CoT Reasoning](https://arxiv.org/abs/2601.09088) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/D2I-ai/dasd-thinking) |
| 🟡 [Semantic Soft Bootstrapping: Long Context Reasoning in LLMs without Reinforcement Learning](https://arxiv.org/abs/2512.05105) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/purbeshmitra/semantic-soft-bootstrapping) |
| 🟢 [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models](https://arxiv.org/abs/2401.01335) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/uclaml/SPIN) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/UCLA-AGI/zephyr-7b-sft-full-SPIN-iter3) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🧠 Reasoning Distillation

> Distilling chain-of-thought and step-by-step reasoning capabilities from stronger to weaker models.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [On-Policy Context Distillation for Language Models](https://arxiv.org/abs/2602.12275) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/ZijunSong/On-Policy-Context-Distillation) |
| 🟢 [From Correction to Mastery: Reinforced Distillation of Large Language Model Agents](https://arxiv.org/abs/2509.14257) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/modelscope/easydistill) |
| 🟢 [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/QwenLM/Qwen3) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f) |
| 🟢 [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://arxiv.org/abs/2305.02301) | 2023 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/google-research/distilling-step-by-step) |

---

## 🎯 Reward-Guided On-Policy Distillation

> Combining on-policy generation with reward models or RL objectives to guide distillation.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [Reinforcement-aware Knowledge Distillation for LLM Reasoning](https://arxiv.org/abs/2602.22495) | 2026 |  |
| 🟢 [Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation](https://arxiv.org/abs/2602.12125) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/RUCBM/G-OPD) |
| 🟢 [KEPO: Knowledge-Enhanced Preference Optimization for Reinforcement Learning with Reasoning](https://arxiv.org/abs/2602.00400) | 2026 |  |
| 🟢 [A Note on Hybrid Online Reinforcement and Imitation Learning for LLMs: Formulations and Algorithms](https://arxiv.org/abs/2512.23097) | 2025 |  |
| 🟢 [VOLD: Reasoning Transfer from LLMs to Vision-Language Models via On-Policy Distillation](https://arxiv.org/abs/2510.23497) | 2025 |  |
| 🟢 [KDRL: Post-Training Reasoning LLMs via Unified Knowledge Distillation and Reinforcement Learning](https://arxiv.org/abs/2506.02208) | 2025 |  |
| 🟢 [RLKD: Distilling LLMs' Reasoning via Reinforcement Learning](https://arxiv.org/abs/2505.16142) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/xsc1234/RLKD) |
| 🟢 [AlignDistil: Token-Level Language Model Alignment as Adaptive Policy Distillation](https://arxiv.org/abs/2503.02832) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/songmzhang/AlignDistil) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🏭 Industrial Systems & Scaling

> Large-scale deployments and system-level applications of on-policy distillation.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟡 [KAT-Coder-V2 Technical Report](https://arxiv.org/abs/2603.27703) | 2026 |  |
| 🟢 [Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation](https://arxiv.org/abs/2603.19220) | 2026 |  |
| 🟡 [KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models](https://arxiv.org/abs/2603.01875) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/songmzhang/KDFlow) |
| 🟢 [Video-OPD: Efficient Post-Training of Multimodal Large Language Models for Temporal Video Grounding via On-Policy Distillation](https://arxiv.org/abs/2602.02994) | 2026 |  |
| 🟢 [OVD: On-policy Verbal Distillation](https://arxiv.org/abs/2601.21968) | 2026 |  |
| 🟢 [MiMo-V2-Flash Technical Report](https://arxiv.org/abs/2601.02780) | 2026 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/XiaomiMiMo/MiMo-V2-Flash) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash) |
| 🟢 [Retaining by Doing: The Role of On-Policy Data in Mitigating Forgetting](https://arxiv.org/abs/2510.18874) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/princeton-pli/retaining-by-doing) |
| 🟢 [Why Knowledge Distillation Works in Generative Models: A Minimal Working Explanation](https://arxiv.org/abs/2505.13111) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/csm9493/kd-minimal-explanation) |
| 🟢 [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/QwenLM/Qwen3) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f) |
| 🟢 [Distillation Scaling Laws](https://arxiv.org/abs/2502.08606) | 2025 |  |
| 🟢 [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/deepseek-ai/DeepSeek-R1) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/deepseek-ai/DeepSeek-R1) |
| 🟢 [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://arxiv.org/abs/2410.11325) | 2024 |  |

---

## 📊 Evaluation & Analysis

> Empirical studies, theoretical analysis, and benchmarks for understanding distillation.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](https://arxiv.org/abs/2603.25562) | 2026 |  |
| 🟢 [Towards Cross-Tokenizer Distillation: the Universal Logit Distillation Loss for LLMs](https://arxiv.org/abs/2402.12030) | 2025 |  |
| 🟢 [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## 🔗 Related Topics

> Off-policy, cross-tokenizer, speculative decoding, and other related distillation methods.

| Paper | Date | Resources |
|-------|:----:|:---:|
| 🟢 [Distillation of Large Language Models via Concrete Score Matching](https://arxiv.org/abs/2509.25837) | 2025 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/aailab-kaist/CSD) |
| 🟢 [ORPO-Distill: Mixed-Policy Preference Optimization for Cross-Architecture LLM Distillation](https://arxiv.org/abs/2509.25100) | 2025 |  |
| 🟢 [Delta Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2509.14526) | 2025 |  |
| 🟢 [TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models](https://arxiv.org/abs/2501.16937) | 2025 |  |
| 🟢 [MiniPLM: Knowledge Distillation for Pre-Training Language Models](https://arxiv.org/abs/2410.17215) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/thu-coai/MiniPLM) |
| 🟢 [Gemma 2: Improving Open Language Models at a Practical Size](https://arxiv.org/abs/2408.00118) | 2024 | [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/google/gemma-2-27b) |
| 🟢 [Compact Language Models via Pruning and Knowledge Distillation](https://arxiv.org/abs/2407.14679) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/NVlabs/Minitron) [![Model](https://img.shields.io/badge/Model-🤗-yellow)](https://huggingface.co/nvidia/Minitron-8B-Base) |
| 🟢 [PromptKD: Distilling Student-Friendly Knowledge for Generative Language Models via Prompt Tuning](https://arxiv.org/abs/2402.12842) | 2024 | [![Code](https://img.shields.io/badge/Code-GitHub-blue)](https://github.com/gmkim-ai/PromptKD) |
| 🟢 [DistillSpec: Improving Speculative Decoding via Knowledge Distillation](https://arxiv.org/abs/2310.08461) | 2023 |  |

---

## 🗺️ Open Problems

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

---

## 📄 Citation

If you find this collection helpful, please consider citing our survey:

```bibtex
@article{song2026survey,
  title={A Survey of On-Policy Distillation for Large Language Models},
  author={Song, Mingyang and Zheng, Mao},
  journal={arXiv preprint arXiv:2604.00626},
  year={2026}
}
```

---

<div align="center">

**⭐ If you find this repository useful, please star it! ⭐**

*Last updated: April 2026*

</div>
