# 🛠️ Codebases & Implementations

Ready-to-run implementations for on-policy distillation research, extracted from the Awesome List.

## §4 Objective Functions and Optimization

| Method | Description | Link |
|--------|-------------|------|
| **MiniLLM** | Foundation for RKL formulation & policy gradient | [microsoft/LMOps (minillm)](https://github.com/microsoft/LMOps/tree/main/minillm) |
| **CSD** | Concrete Score Matching | [aailab-kaist/CSD](https://github.com/aailab-kaist/CSD) |
| **AdaKD** | LLM-Oriented Token-Adaptive KD | [SassyRong/AdaKD](https://github.com/SassyRong/AdaKD) |
| **ATKD** | Adaptive Token Teaching | [WHU-ZQH/ATKD](https://github.com/WHU-ZQH/ATKD) |
| **TSD-KD** | Token-Selective Dual KD | [kmswin1/TSD-KD](https://github.com/kmswin1/TSD-KD) |
| **PW-OPSD** | Position-Weighted On-Policy Self-Distillation (later-token clipped FKL) | [SaFo-Lab/PW-OPSD](https://github.com/SaFo-Lab/PW-OPSD) |
| **MAD-OPD** | Multi-Agent Debate OPD (confidence-weighted token aggregation) | [chiefovoavicii/MAD-OPD](https://github.com/chiefovoavicii/MAD-OPD) |
| **DistiLLM** | Streamlined Distillation | [jongwooko/distillm](https://github.com/jongwooko/distillm) |
| **DistiLLM-2** | Contrastive Approach Boosts Distillation | [jongwooko/distillm-2](https://github.com/jongwooko/distillm-2) |
| **DSKDv2** | Dual-Space General KD | [songmzhang/DSKDv2](https://github.com/songmzhang/DSKDv2) |
| **AlignDistil** | LM Alignment as Adaptive Policy Distillation | [songmzhang/AlignDistil](https://github.com/songmzhang/AlignDistil) |
| **SCOPE** | Signal-Calibrated OPD with Dual-Path Adaptive Weighting | [machine981/SCOPE](https://github.com/machine981/SCOPE) |
| **DASD** | Distribution-Aligned Sequence Distillation | [D2I-ai/dasd-thinking](https://github.com/D2I-ai/dasd-thinking) |
| **Towards-On-Policy-SFT** | Distribution discriminant theory & on-policy SFT | [zhangmiaosen2000/Towards-On-Policy-SFT](https://github.com/zhangmiaosen2000/Towards-On-Policy-SFT) |
| **LUFFY** | Learning to Reason under Off-Policy Guidance | [ElliottYan/LUFFY](https://github.com/ElliottYan/LUFFY) |
| **RLKD** | Distilling LLMs' Reasoning via RL | [xsc1234/RLKD](https://github.com/xsc1234/RLKD) |
| **SCoRe (easydistill)** | Reinforced Distillation of LLM Agents | [modelscope/easydistill](https://github.com/modelscope/easydistill) |

## §5 Signal Source and Teacher Architecture

### §5.1 White-Box Logit Supervision

| Method | Description | Link |
|--------|-------------|------|
| **G-OPD** | Generalized OPD with reward extrapolation | [RUCBM/G-OPD](https://github.com/RUCBM/G-OPD) |
| **Uni-OPD** | Dual-perspective recipe unifying exploration and reliability | [WenjinHou/Uni-OPD](https://github.com/WenjinHou/Uni-OPD) |
| **BRTS** | Best-of-N Teacher Rollout Selection (correctness-first OPD) | [BWGZK-keke/BRTS](https://github.com/BWGZK-keke/BRTS) |
| **MiniPLM** | KD for Pre-Training LMs (difference sampling, divergence-aware) | [thu-coai/MiniPLM](https://github.com/thu-coai/MiniPLM) |
| **PromptKD** | Prompt Tuning for KD | [gmkim-ai/PromptKD](https://github.com/gmkim-ai/PromptKD) |
| **Lion** | Adversarial Distillation | [YJiangcm/Lion](https://github.com/YJiangcm/Lion) |

### §5.2 Black-Box and API-Constrained

| Method | Description | Link |
|--------|-------------|------|
| **ROPD** | Rubric-based OPD (structured semantic rubrics replace teacher logits) | [Peregrine123/ROPD_official](https://github.com/Peregrine123/ROPD_official) |
| **PRISM** | Black-box OPD pre-alignment for Multimodal RL (adversarial MoE discriminator) | [XIAO4579/PRISM](https://github.com/XIAO4579/PRISM) |
| **ThinkTuning** | Cognitive Reflections without Distillation | [3rdAT/ThinkTuning](https://github.com/3rdAT/ThinkTuning) |
| **SuperCorrect** | Thought Template Distillation and Self-Correction | [YangLing0818/SuperCorrect-llm](https://github.com/YangLing0818/SuperCorrect-llm) |

### §5.3 Self-Distillation

| Method | Description | Link |
|--------|-------------|------|
| **OPSD** | On-Policy Self-Distillation | [siyan-zhao/OPSD](https://github.com/siyan-zhao/OPSD) |
| **OPCD** | On-Policy Context Distillation | [ZijunSong/On-Policy-Context-Distillation](https://github.com/ZijunSong/On-Policy-Context-Distillation) |
| **OPSD (Compression)** | On-Policy Self-Distillation for Reasoning Compression | [HJSang/OPSD_Reasoning_Compression](https://github.com/HJSang/OPSD_Reasoning_Compression) |
| **On-Policy-SFT** | On-Policy SFT for Efficient Reasoning | [EIT-NLP/On-Policy-SFT](https://github.com/EIT-NLP/On-Policy-SFT) |
| **SSD** | Simple Self-Distillation for Code Generation | [apple/ml-ssd](https://github.com/apple/ml-ssd) |
| **SDPO** | RL via Self-Distillation | [lasgroup/SDPO](https://github.com/lasgroup/SDPO) |
| **Semantic Soft Bootstrapping** | Long Context Reasoning without RL | [purbeshmitra/semantic-soft-bootstrapping](https://github.com/purbeshmitra/semantic-soft-bootstrapping) |
| **UniSD** | Unified Self-Distillation Framework (EMA + multi-teacher arbitration) | [Ahren09/UniSD](https://github.com/Ahren09/UniSD) |
| **OPSA** | Self-Distillation for Safety Alignment (reduces safety tax) | [FYYFU/OPSA](https://github.com/FYYFU/OPSA) |
| **WINO-DLLM** | Roll Out and Roll Back: Diffusion LLMs as Self-Teachers | [Feng-Hong/WINO-DLLM](https://github.com/Feng-Hong/WINO-DLLM) |
| **Vision-OPD** | Multimodal Self-Distillation (regional→global crop alignment) | [VisionOPD/Vision-OPD](https://github.com/VisionOPD/Vision-OPD) |
| **COPSD** | Crosslingual On-Policy Self-Distillation for Multilingual Reasoning | [cisnlp/COPSD](https://github.com/cisnlp/COPSD) |
| **AVSD** | Adaptive-View Self-Distillation (multi-view consensus + privileged signals) | [duykhuongnguyen/AVSD](https://github.com/duykhuongnguyen/AVSD) |
| **π-Play** | Multi-Agent Self-Play via Privileged Self-Distillation | [zhyaoch/pi-play](https://github.com/zhyaoch/pi-play) |
| **OPHSD** | On-Policy Harness Self-Distillation (draft-verify / plan-solve harnesses) | [zzy1127/OPHSD-On-Policy-Harness-Self-Distillation](https://github.com/zzy1127/OPHSD-On-Policy-Harness-Self-Distillation) |

## §6 Training Efficiency and Stabilization

| Method | Description | Link |
|--------|-------------|------|
| **TIP** | Token Importance in On-Policy Distillation | [HJSang/OPSD_OnPolicyDistillation](https://github.com/HJSang/OPSD_OnPolicyDistillation) |
| **Lightning-OPD** | Efficient Offline OPD Post-Training for Reasoning Models | [jet-ai-projects/Lightning-OPD](https://github.com/jet-ai-projects/Lightning-OPD) |
| **TCOD** | Temporal Curriculum OPD for Multi-turn Agents | [kokolerk/TCOD](https://github.com/kokolerk/TCOD) |

## §7 Understanding OPD

| Method | Description | Link |
|--------|-------------|------|
| **OPD Analysis** | Rethinking OPD (Phenomenology, Mechanism, Recipe) | [thunlp/OPD](https://github.com/thunlp/OPD) |
| **Minimal KD** | Why KD Works in Generative Models | [csm9493/kd-minimal-explanation](https://github.com/csm9493/kd-minimal-explanation) |
| **Survey (Tebmer)** | Awesome Knowledge Distillation of LLMs | [Tebmer/Awesome-Knowledge-Distillation-of-LLMs](https://github.com/Tebmer/Awesome-Knowledge-Distillation-of-LLMs) |
| **Distilling Step-by-Step** | Outperforming larger LLMs with rationales | [google-research/distilling-step-by-step](https://github.com/google-research/distilling-step-by-step) |
| **CaOPD** | Decoupling Capability and Calibration in OPD (miscalibration scaling law) | [SalesforceAIResearch/CaOPD](https://github.com/SalesforceAIResearch/CaOPD) |
| **Self-Distill Analysis** | Why Self-Distillation Sometimes Degrades Reasoning | [beanie00/self-distillation-analysis](https://github.com/beanie00/self-distillation-analysis) |

## §8 Applications, Systems & Emerging Domains

| Method | Description | Link |
|--------|-------------|------|
| **DeepSeek-R1** | RL Incentivizing Reasoning | [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |
| **Qwen3** | Qwen3 Technical Codebase | [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) |
| **MiMo-V2-Flash** | MiMo-V2 Technical Codebase | [XiaomiMiMo/MiMo-V2-Flash](https://github.com/XiaomiMiMo/MiMo-V2-Flash) |
| **MTP-LM** | Multi-Token Prediction via Self-Distillation | [jwkirchenbauer/mtp-lm](https://github.com/jwkirchenbauer/mtp-lm) |
| **HY-Embodied** | Embodied Foundation Models | [Tencent-Hunyuan/HY-Embodied](https://github.com/Tencent-Hunyuan/HY-Embodied) |
| **OpenClaw-RL** | Train Any Agent Simply by Talking | [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) |
| **Retaining by Doing** | Mitigating Forgetting | [princeton-pli/retaining-by-doing](https://github.com/princeton-pli/retaining-by-doing) |
| **Safactory** | Scalable Agentic Infrastructure for Trustworthy Autonomy | [AI45Lab/Safactory](https://github.com/AI45Lab/Safactory) |
| **HyperEyes** | Multimodal Search Agents (dual-grained efficiency RL) | [DeepExperience/HyperEyes](https://github.com/DeepExperience/HyperEyes) |
| **ProteinOPD** | Preference Alignment for Protein Design (multi-teacher consensus) | [THU-AI4S/ProteinOPD](https://github.com/THU-AI4S/ProteinOPD) |
| **SOD** | Step-wise OPD for Small LM Agents | [YoungZ365/SOD](https://github.com/YoungZ365/SOD) |

## Third-Party Frameworks

| Framework | Description | Link |
|-----------|-------------|------|
| **EasyDistill** | ModelScope OPD toolkit | [modelscope/easydistill](https://github.com/modelscope/easydistill) |
| **OpenRLHF** | RLHF + OPD support | [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) |
| **veRL** | RLHF framework (used by ThinkTuning, SAGE) | [volcengine/verl](https://github.com/volcengine/verl) |
| **vLLM** | High-throughput inference engine commonly integrated into OPD pipelines | [vllm-project/vllm](https://github.com/vllm-project/vllm) |
| **TensorRT-LLM** | NVIDIA inference framework commonly integrated into OPD pipelines | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) |
| **Tinker Cookbook** | Thinking Machines OPD reference recipes | [thinking-machines-lab/tinker-cookbook](https://github.com/thinking-machines-lab/tinker-cookbook) |
