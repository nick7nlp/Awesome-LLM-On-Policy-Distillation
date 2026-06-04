# 📚 Recommended Reading Order

## 🎯 Level 1: Foundations (Start Here)
1. **GKD** (2306.13649) — The paper that started modern OPD for LLMs.
2. **MiniLLM** (2306.08543) — Reverse-KL formulation + policy gradient interpretation.
3. **DeepSeek-V4** (Tech Report) — See how OPD works at industrial scale.

## 🔬 Level 2: Core Techniques
4. **Entropy-Aware OPD** (2603.07079) — Adaptive RKL on low-entropy tokens + FKL on high-entropy; clean illustration of why a single direction isn't always best.
5. **DistiLLM** (2402.03898) — Skewed KL + streaming computation.
6. **OPSD** (2601.18734) — Self-distillation without external teacher.
7. **TIP** (2604.14084) — Only 20% of tokens matter.

## 🧪 Level 3: Understanding & Failure Modes
8. **Rethinking OPD** (2604.13016) — Two necessary conditions for OPD to work.
9. **CaOPD** (2604.16830) — The calibration problem nobody talks about.
10. **SCOPE** (2604.10688) — Diversity collapse (Pass@k degradation).
11. **Revisiting OPD** (2603.25562) — Three failure modes and simple fixes.

## 🚀 Level 4: Frontier Methods
12. **Lightning OPD** (2604.13010) — Offline OPD, 4x faster.
13. **SDZero** (2604.12002) — No teacher needed, binary reward → dense signal.
14. **Uni-OPD** (2605.03677) — Unified dual-perspective recipe.
15. **SOD** (2605.07725) — Step-level divergence reweighting for tool-integrated reasoning agents.