# Prediction: Tau Lepton Mass from c=-2 Logarithmic CFT

**Date: 2026-03-14**
**Authors: wuko & Syn-claude (scos-lab)**

---

## Prediction

$$m_\tau = 1776.97 \pm 0.01 \text{ MeV}$$

This prediction has **zero free parameters** for mass ratios. It is derived from the conformal dimension of the Z₃ twist field in the c=-2 logarithmic conformal field theory of symplectic fermions.

## Current Experimental Status

| Source | m_τ (MeV) | Status |
|--------|-----------|--------|
| **This prediction** | **1776.97 ± 0.01** | **Testable at Belle II** |
| HFLAV 2025 world average | 1776.96 ± 0.09 | 0.1σ from prediction |
| Belle II 2023 | 1777.09 ± 0.14 | 0.9σ from prediction |
| PDG 2024 | 1776.86 ± 0.12 | 0.9σ from prediction |

## Derivation (3 steps)

### Step 1: Twist field dimension

The c=-2 LCFT (symplectic fermions) has an exact twist field dimension formula ([Kausch 2000, Nucl. Phys. B 583, eq. 23](https://arxiv.org/abs/hep-th/0003029)):

$$h_\lambda = -\frac{\lambda(1-\lambda)}{2}$$

### Step 2: Apply to Z₃ orbifold

For the Z₃ orbifold (λ = 1/3):

$$h_{1/3} = -\frac{(1/3)(2/3)}{2} = -\frac{1}{9}$$

Total (spinless) dimension: Δ = 2h = **-2/9**

### Step 3: Identify as Koide angle

The Koide formula parametrizes charged lepton masses as:

$$\sqrt{m_k} = M\left(1 + \sqrt{2}\cos\left(\frac{2\pi k}{3} + \delta_0\right)\right), \quad k=0,1,2$$

We identify the Koide angle with the twist field dimension:

$$\delta_0 = |\Delta_{\text{twist}}| = \frac{2}{9}$$

This gives mass ratios with **zero free parameters**:

| Ratio | Predicted | Experiment | Deviation |
|-------|-----------|------------|-----------|
| m_μ/m_e | 206.770 | 206.768 | 0.001% |
| m_τ/m_e | 3477.5 | 3477.3 ± 0.2 | 0.005% |
| m_τ/m_μ | 16.818 | 16.817 ± 0.001 | 0.006% |

## Verification

The formula is verified against the known Z₂ result:
- Z₂ (λ=1/2): h = -1/8 (the well-known μ twist field of c=-2 LCFT) ✓

The Z₃ result h = -1/9 is new and yields the Koide angle.

## Key Claim

**No prior connection between the Koide formula and conformal field theory has been reported.** The identification δ₀ = 2/9 = |c|/N² (where c=-2 is the central charge and N=3 is the orbifold order) is original to this work.

## Falsifiability

If Belle II measures m_τ = 1776.80 ± 0.03 MeV → this prediction is **falsified** at 5σ.

## References

1. Y. Koide, Lett. Nuovo Cim. **34**, 201 (1982).
2. H. G. Kausch, Nucl. Phys. B **583**, 513 (2000), [arXiv:hep-th/0003029](https://arxiv.org/abs/hep-th/0003029).
3. Y. S. Amhis *et al.* (HFLAV), SciPost Phys. Proc. **17**, 001 (2025).
4. I. Adachi *et al.* (Belle II), Phys. Rev. D **108**, 032006 (2023), [arXiv:2305.19116](https://arxiv.org/abs/2305.19116).

## Repository Contents

- `README.md` — This file (prediction + derivation)
- `paper-koide-lcft.md` — Full paper draft
- `verify.py` — Numerical verification script
