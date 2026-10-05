# 📐 Key Equations

[Catalog](../README.md) · [Reading order](reading-order.md) · [Method comparison](method-comparison.md) · [Benchmarks](benchmarks.md)

The prefix distribution, conditional target, and gradient estimator are separate parts of an OPD method. A loss name alone does not specify all three. This guide follows the [survey](https://arxiv.org/abs/2604.00626) and the linked method formulations.

## States and direct distribution matching

Let $\pi_\theta(a\mid s)$ be the student distribution and $q(a\mid s^T)$ the supervisory target. For autoregressive generation, $s=(x,y_{<t})$ and $a$ is a next token. The teacher view $s^T$ may contain privileged information. Let $d_\mu$ denote the state distribution induced by behavior policy $\mu$.

$$
\mathcal L_{\mathrm{match}}(\theta)
=\mathbb E_{s\sim d_\mu}
\left[w(s)D_f\!\left(q(\cdot\mid s^T)\parallel\pi_\theta(\cdot\mid s)\right)\right].
$$

Current-student sampling corresponds to $\mu=\pi_\theta$. Fixed teacher traces, mixtures, and stale student rollouts induce different state distributions. This formulation describes direct matching; teacher-derived rewards and preferences require their own update definitions. See [GKD](https://arxiv.org/abs/2306.13649) for sampling mixtures and [OPSD](https://arxiv.org/abs/2601.18734) for different teacher and student contexts.

## Forward and reverse KL at a fixed state

Assume comparable distributions on a common vocabulary $V$, with the support conditions needed for finite KL.

$$
D_{\mathrm{FKL}}(s)
=\sum_{a\in V}q(a\mid s^T)
\log\frac{q(a\mid s^T)}{\pi_\theta(a\mid s)}.
$$

$$
D_{\mathrm{RKL}}(s)
=\sum_{a\in V}\pi_\theta(a\mid s)
\log\frac{\pi_\theta(a\mid s)}{q(a\mid s^T)}.
$$

The vocabulary sum is essential: it integrates over alternative next tokens at the same state. An expectation over sampled prefixes does not replace this sum. Either conditional divergence can be evaluated on student-generated prefixes. Forward KL emphasizes teacher-supported alternatives; reverse KL penalizes student probability in regions weakly supported by the teacher. “Mode-covering” and “mode-seeking” describe distributional tendencies, not guarantees about correctness, diversity, or the best objective for a task. [GKD](https://arxiv.org/abs/2306.13649) compares several choices; [MiniLLM](https://arxiv.org/abs/2306.08543) develops sequence reverse KL.

## Generalized Jensen–Shannon divergence in GKD

At a fixed comparable state, abbreviate the teacher and student distributions as $q$ and $p$, and define

$$
m_\beta=\beta q+(1-\beta)p,\qquad 0<\beta<1.
$$

$$
D_{\mathrm{JSD},\beta}(q\parallel p)
=\beta D_{\mathrm{KL}}(q\parallel m_\beta)
+(1-\beta)D_{\mathrm{KL}}(p\parallel m_\beta).
$$

This is the generalized JSD used in [GKD, Eq. (1)](https://arxiv.org/abs/2306.13649). At $\beta=1/2$ it is symmetric. With this argument convention, the rescaled endpoint limits are

$$
\lim_{\beta\to0}\frac{D_{\mathrm{JSD},\beta}(q\parallel p)}{\beta}
=D_{\mathrm{KL}}(q\parallel p),\qquad
\lim_{\beta\to1}\frac{D_{\mathrm{JSD},\beta}(q\parallel p)}{1-\beta}
=D_{\mathrm{KL}}(p\parallel q).
$$

The normalization matters: unscaled JSD tends to zero at the endpoints. GKD's student-data mixture weight is a separate parameter controlling which trajectories are used, rather than the divergence at a visited prefix.

## An objective is not its sampled-token surrogate

For a sampled student token, a common local teacher signal and detached surrogate are

$$
r_t=\log\frac{p_T(y_t\mid c_t)}{p_\theta(y_t\mid c_t)},\qquad
\ell_t(\theta)=-\operatorname{sg}[r_t]\log p_\theta(y_t\mid c_t),
$$

where $c_t=(x,y_{<t})$ and $\operatorname{sg}$ stops gradients through the coefficient. Minimizing this surrogate increases the sampled token's likelihood when the detached teacher signal is positive. Directly differentiating the sampled log-ratio value gives a different update. A PPO-style implementation additionally specifies its behavior-policy ratio and clipping. See [AOPD](https://arxiv.org/abs/2605.06387) and [OPD+](https://arxiv.org/abs/2606.01039).

For a fixed teacher with support on the student's responses, [MiniLLM](https://arxiv.org/abs/2306.08543) starts from a sequence-level reverse-KL gradient with return-to-go

$$
R_t=\sum_{t'=t}^{|y|}\log\frac{p_T(y_{t'}\mid c_{t'})}{p_\theta(y_{t'}\mid c_{t'})},
$$

$$
\nabla_\theta D_{\mathrm{KL}}(p_\theta\parallel p_T)
=-\mathbb E_{y\sim p_\theta}
\left[\sum_{t=1}^{|y|}(R_t-1)\nabla_\theta\log p_\theta(y_t\mid c_t)\right].
$$

The constant score term vanishes in expectation. The future terms assign credit to earlier actions for later discrepancies; a token-local surrogate does not include them. MiniLLM's practical method uses a single-step decomposition and additional stabilizers. Full-vocabulary evaluation at a fixed prefix also remains different from differentiating through the distribution of future visited states.

## Adaptive supervision is method-specific

There is no single “adaptive KL” equation covering every routing or reweighting method. [EOPD](https://arxiv.org/abs/2603.07079) retains reverse KL and adds teacher-top-*K* forward KL above a teacher-entropy threshold. [AOPD](https://arxiv.org/abs/2605.06387) instead routes positive and non-positive teacher advantages to different update branches. A convex mixture of two named losses would omit these support and estimator choices.

Likewise, [DASD](https://arxiv.org/abs/2601.09088) changes teacher-data temperature and uses teacher completions of truncated student prefixes. Its sequence-level training should not be substituted into a generic tokenwise KL-mixture formula.

## TIP token selection

[TIP, Eqs. (5)–(7)](https://arxiv.org/abs/2604.14084) combines min–max-normalized student entropy $\hat h_t$ and teacher–student divergence $\hat\delta_t$ in a Soft-OR score,

$$
u_t=\hat h_t+\hat\delta_t-\hat h_t\hat\delta_t
=1-(1-\hat h_t)(1-\hat\delta_t).
$$

For a trajectory of $m$ tokens and a retention ratio $\rho$, it selects positions and applies reverse KL there,

$$
\mathcal T=\operatorname{TopK}\!\left(\{u_t\}_{t=1}^{m},\lfloor\rho m\rfloor\right),\qquad
\mathcal L_{\mathrm{TIP}}=\frac{1}{|\mathcal T|}\sum_{t\in\mathcal T}
D_{\mathrm{KL}}\!\left(p_S(\cdot\mid c_t)\parallel p_T(\cdot\mid c_t)\right).
$$

The score can retain confident disagreement as well as uncertain positions. The retention ratio is a hyperparameter, and disagreement alone does not certify a factual error. The loss mask also does not imply proportional savings in trajectory generation or teacher scoring.

## OPSD with an answer-conditioned self-teacher

For a problem–answer pair $(x,y^\star)$, [OPSD, Eq. (6)](https://arxiv.org/abs/2601.18734) samples $\hat y$ from the problem-only student and compares predictions at those prefixes,

$$
\mathcal L_{\mathrm{OPSD}}(\theta)
=\mathbb E_{(x,y^\star),\,\hat y\sim p_\theta(\cdot\mid x)}
\left[\frac{1}{|\hat y|}\sum_{t=1}^{|\hat y|}
D\!\left(
\operatorname{sg}[p_\theta(\cdot\mid x,y^\star,\hat y_{<t})]
\parallel p_\theta(\cdot\mid x,\hat y_{<t})
\right)\right].
$$

The teacher and student share a model but have different conditioning information. In the local matching update, the sampled tokens and teacher distribution are detached; gradients flow through the student predictions. The paper uses generalized JSD in its main experiments. Answer access can improve the supervisory view, but does not guarantee reliable correction on every student prefix.
