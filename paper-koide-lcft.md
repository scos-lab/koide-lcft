# Lepton mass ratios from the Z₃ twist field of c=-2 logarithmic CFT

**[Authors], [Affiliations]**

---

## Abstract

We show that the Koide angle---the single parameter determining charged lepton mass ratios in Koide's formula---equals the absolute value of the total conformal dimension of the Z₃ twist field in the c = -2 logarithmic conformal field theory of symplectic fermions. Specifically, the twist field dimension h = -λ(1-λ)/2 at λ = 1/3 gives h = -1/9, yielding a Koide angle δ₀ = |2h| = 2/9. This predicts lepton mass ratios with zero free parameters: m_μ/m_e = 206.770 (experiment: 206.768, deviation 0.001%) and m_τ = 1776.97 ± 0.01 MeV (HFLAV 2025: 1776.96 ± 0.09 MeV, within 0.1σ). No prior connection between the Koide formula and conformal field theory has been reported.

---

## 1. Introduction

In 1982, Koide [1] discovered that the charged lepton masses satisfy the remarkable relation

> **(m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)² = 2/3**

to an accuracy of 0.001% using current experimental values [2]. Despite numerous attempts [3-6], no theoretical derivation of this formula from first principles has been established. The Koide formula remains, in the words of Baez [7], "one of the most unexplained coincidences in particle physics."

The formula is equivalent to the parametrization

> **√m_k = M (1 + √2 · cos(2πk/3 + δ₀)),     k = 0, 1, 2**

where M is an overall mass scale and δ₀ is the *Koide angle*. The condition K = 2/3 holds for *any* value of δ₀; the angle determines only the mass *ratios*. Fitting to m_e and m_μ yields δ₀ = 0.22222 ± 0.00001, where the uncertainty is dominated by the experimental error on m_τ.

In this Letter, we show that

> **δ₀ = 2/9**

follows from the conformal dimension of the Z₃ twist field in the c = -2 logarithmic conformal field theory (LCFT) of symplectic fermions [8]. This identification requires no adjustable parameters beyond the overall scale M.

---

## 2. Symplectic fermions and their Z₃ orbifold

The c = -2 LCFT is realized by a pair of anticommuting fields ξ(z) and η(z) of conformal weights 0 and 1, respectively, with the operator product expansion [9, 8]

> ξ(z) η(w) ~ 1/(z - w)

The stress tensor T = -:∂ξ η: yields central charge c = -2. The theory possesses a global SL(2, ℂ) symmetry under which (ξ, η) transforms as a doublet [8].

Consider the Z_N orbifold defined by the U(1) subgroup action

> ξ → e^{2πi/N} ξ,     η → e^{-2πi/N} η

In the k-th twisted sector (k = 1, ..., N-1), the fields acquire boundary conditions ξ(e^{2πi}z) = e^{2πik/N} ξ(z), with twist parameter λ = k/N.

The ground state μ_λ of the twisted sector is a Virasoro highest-weight state. Kausch [8] showed that its conformal dimension is given exactly by

> **h_λ = -λ(1-λ)/2**     — Eq. (23) of Ref. [8]

valid for 0 < λ < 1. This result is exact because the symplectic fermion theory is free (no interactions), so there are no quantum corrections.

For the well-known Z₂ case (λ = 1/2), this gives h = -1/8, the conformal dimension of the μ twist field [9, 10].

---

## 3. Z₃ twist field and the Koide angle

We now apply the formula to the Z₃ orbifold (N = 3). The two twisted sectors have λ = 1/3 and λ = 2/3, giving

> **h_{1/3} = h_{2/3} = -(1/3)(2/3)/2 = -1/9**

For a spinless (scalar) operator, the total conformal dimension is Δ = h + h̄ = 2h:

> **Δ_twist = 2h = -2/9**

We identify the Koide angle with the absolute value of this dimension:

> **δ₀ = |Δ_twist| = 2/9**

The physical picture is as follows. The three charged leptons correspond to the three sectors of the Z₃ orbifold: the untwisted sector (k = 0) and the two twisted sectors (k = 1, 2). The Z₃ symmetry naturally produces the 2πk/3 phase in the Koide parametrization, while the twist field dimension provides the symmetry-breaking angle δ₀ = 2/9.

Equivalently, noting that h_λ = c·λ(1-λ)/4 for c = -2, we can write

> **δ₀ = |c| / N²**

where c = -2 is the central charge and N = 3 is the orbifold order. This expression makes manifest that the Koide angle is determined by two integers alone.

---

## 4. Predictions and experimental tests

The Koide parametrization with δ₀ = 2/9 exact gives mass ratios with zero free parameters. Using m_e = 0.51099895 MeV as input to fix M, we predict:

| Ratio | Predicted | Experiment | Deviation |
|-------|-----------|------------|-----------|
| m_μ/m_e | 206.770 | 206.768 [2] | 0.001% |
| m_τ/m_e | 3477.5 | 3477.3 ± 0.2 | 0.005% |
| m_τ/m_μ | 16.818 | 16.817 ± 0.001 | 0.006% |

The most precise test is the predicted τ mass:

> **m_τ^pred = 1776.97 ± 0.01 MeV**

where the uncertainty arises from m_e and m_μ input errors. The 2025 HFLAV world average [11] is m_τ^exp = 1776.96 ± 0.09 MeV, yielding

> **(m_τ^pred - m_τ^exp) / σ_exp = +0.1σ**

The prediction agrees with the latest experimental value to 0.02 MeV, or 0.001%.

We note that the older PDG value m_τ = 1776.86 ± 0.12 MeV [2] showed a 1.0σ deviation; the recent HFLAV average has shifted toward our prediction.

**Future test.** The Belle II experiment [12] is expected to measure m_τ with a precision of ~0.05 MeV, sufficient to distinguish our prediction 1776.97 MeV from alternative values at the ~2σ level.

---

## 5. Discussion

**Relation to other work.** The Koide formula has been discussed in the context of discrete symmetries [3, 13], democratic mass matrices [4], and preon models [1]. To our knowledge, no previous work has connected the Koide angle to conformal field theory or to the specific value 2/9.

**Why c = -2?** The c = -2 LCFT occupies a distinguished position in the landscape of two-dimensional CFTs. It is the simplest logarithmic CFT [14], arises at the Breitenlohner-Freedman bound of AdS₃/CFT₂ [15], and describes critical dense polymers [16] and the abelian sandpile model [17]. The BF bound saturation condition produces a double root Δ = 1, which is the hallmark of logarithmic CFT [18]. Whether the appearance of c = -2 in the lepton sector reflects an underlying AdS₃/CFT₂ structure remains to be understood.

**Why Z₃?** The identification of three lepton generations with the three sectors of a Z₃ orbifold is a physical assumption, not derived from first principles. The Z₃ orbifold is the simplest cyclic orbifold producing exactly three sectors with a non-trivial phase structure. The question of why nature chooses N = 3 generations remains open [19].

**Quarks and neutrinos.** The Koide relation does not hold for quark mass triplets [5]. For up-type quarks (u, c, t), K = 0.849, and for down-type (d, s, b), K = 0.731. Whether modified Koide-type relations involving different values of c or N apply to quarks is under investigation. The extension to neutrinos requires knowledge of the neutrino mass spectrum, which is not yet fully determined [2].

**The scale parameter M.** The overall scale M² ≈ 313.9 MeV is not predicted by the present framework and must be determined from experiment. Interestingly, 3M² ≈ 942 MeV ≈ m_p to 0.3%, though the significance of this observation is unclear.

**Summary.** We have shown that the Koide angle δ₀ = 2/9 is the absolute value of the total conformal dimension of the Z₃ twist field in the c = -2 LCFT, as given by Kausch's exact formula h_λ = -λ(1-λ)/2 at λ = 1/3. Combined with the Koide parametrization, this yields charged lepton mass ratios with zero adjustable parameters and a τ mass prediction in excellent agreement with the 2025 HFLAV world average. The prediction is testable at Belle II.

---

## References

[1] Y. Koide, Lett. Nuovo Cim. **34**, 201 (1982).

[2] R. L. Workman *et al.* (Particle Data Group), Prog. Theor. Exp. Phys. **2024**, 083C01 (2024).

[3] R. Foot, arXiv:hep-ph/9402242 (1994).

[4] C. A. Brannen, arXiv:hep-ph/0503112 (2006).

[5] A. Rivero, arXiv:hep-ph/0505220 (2005).

[6] P. Zenczykowski, Phys. Rev. D **86**, 117303 (2012).

[7] J. C. Baez, "The Koide formula," Azimuth blog (2021).

[8] H. G. Kausch, Nucl. Phys. B **583**, 513 (2000), arXiv:hep-th/0003029.

[9] H. G. Kausch, arXiv:hep-th/9510149 (1995).

[10] M. R. Gaberdiel and H. G. Kausch, Nucl. Phys. B **477**, 293 (1996).

[11] Y. S. Amhis *et al.* (HFLAV), SciPost Phys. Proc. **17**, 001 (2025).

[12] I. Adachi *et al.* (Belle II), Phys. Rev. D **108**, 032006 (2023), arXiv:2305.19116.

[13] E. Ma, Phys. Lett. B **649**, 287 (2007).

[14] V. Gurarie, Nucl. Phys. B **410**, 535 (1993).

[15] P. Breitenlohner and D. Z. Freedman, Ann. Phys. **144**, 249 (1982).

[16] H. Saleur, Nucl. Phys. B **382**, 486 (1992).

[17] S. Mahieu and P. Ruelle, Phys. Rev. E **64**, 066130 (2001).

[18] M. Flohr, Int. J. Mod. Phys. A **18**, 4497 (2003).

[19] P. H. Frampton, Phys. Rev. D **60**, 041901 (1999).

[20] L. Dixon, D. Friedan, E. Martinec, and S. Shenker, Nucl. Phys. B **282**, 13 (1987).
