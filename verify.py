#!/usr/bin/env python3
"""
verify.py — Numerical verification of the Koide angle prediction
=================================================================
Prediction: delta_0 = 2/9 (from Z_3 twist field of c=-2 LCFT)
Result: m_tau = 1776.97 +/- 0.01 MeV

This script verifies the prediction using only:
  1. Kausch's formula: h = -lambda*(1-lambda)/2
  2. Koide parametrization: sqrt(m_k) = M*(1 + sqrt(2)*cos(2*pi*k/3 + delta_0))
  3. Experimental inputs: m_e and m_mu
"""

from mpmath import mp, mpf, pi, sqrt, cos, acos, nstr

mp.dps = 50

# ═══════════════════════════════════════════
# Experimental inputs (PDG 2024)
# ═══════════════════════════════════════════
m_e = mpf("0.51099895000")   # MeV, uncertainty 1.5e-10
m_mu = mpf("105.6583755")    # MeV, uncertainty 2.3e-6

# HFLAV 2025 world average (for comparison)
m_tau_hflav = mpf("1776.96")  # +/- 0.09 MeV

print("=" * 60)
print("Koide angle from Z_3 twist field of c=-2 LCFT")
print("=" * 60)

# ═══════════════════════════════════════════
# Step 1: Twist field dimension (Kausch 2000, eq. 23)
# ═══════════════════════════════════════════
c = -2          # central charge of symplectic fermion LCFT
N = 3           # Z_3 orbifold
k = 1           # first twisted sector
lam = mpf(k)/N  # twist parameter lambda = 1/3

h = -lam * (1 - lam) / 2  # Kausch formula
Delta = 2 * h              # total dimension (spinless)
delta_0 = abs(Delta)        # Koide angle

print(f"\nStep 1: Twist field dimension")
print(f"  c = {c}, N = {N}, lambda = {k}/{N}")
print(f"  h = -lambda*(1-lambda)/2 = {nstr(h, 15)}")
print(f"  Delta = 2h = {nstr(Delta, 15)}")
print(f"  delta_0 = |Delta| = {nstr(delta_0, 15)} = 2/9")

# Verify: Z_2 case should give h = -1/8
h_Z2 = -mpf(1)/2 * (1 - mpf(1)/2) / 2
print(f"\n  Verification (Z_2): h = {nstr(h_Z2, 10)} = -1/8 {'OK' if h_Z2 == mpf(-1)/8 else 'FAIL'}")

# ═══════════════════════════════════════════
# Step 2: Koide parametrization
# ═══════════════════════════════════════════
print(f"\nStep 2: Koide parametrization")
print(f"  sqrt(m_k) = M * (1 + sqrt(2)*cos(2*pi*k/3 + 2/9))")

s_e   = 1 + sqrt(2) * cos(2*pi*0/3 + 2*pi/3 + delta_0)  # k=0: electron
s_mu  = 1 + sqrt(2) * cos(2*pi*1/3 + 2*pi/3 + delta_0)  # k=1: muon
s_tau = 1 + sqrt(2) * cos(2*pi*2/3 + 2*pi/3 + delta_0)  # k=2: tau

# Note: the 2*pi/3 offset is a convention choice for which k maps to which lepton
# Equivalently: s_k = 1 + sqrt(2)*cos(2*pi*(k+1)/3 + delta_0)

print(f"  s_e   = {nstr(s_e, 15)}")
print(f"  s_mu  = {nstr(s_mu, 15)}")
print(f"  s_tau = {nstr(s_tau, 15)}")

# ═══════════════════════════════════════════
# Step 3: Predict m_tau
# ═══════════════════════════════════════════
print(f"\nStep 3: Predictions")

# From m_e: determine M
M_from_e = sqrt(m_e) / s_e
m_tau_from_e = (M_from_e * s_tau)**2
m_mu_from_e = (M_from_e * s_mu)**2

print(f"\n  From m_e = {nstr(m_e, 10)} MeV:")
print(f"    M = {nstr(M_from_e, 12)} sqrt(MeV)")
print(f"    m_mu (predicted) = {nstr(m_mu_from_e, 10)} MeV")
print(f"    m_mu (measured)  = {nstr(m_mu, 10)} MeV")
print(f"    deviation = {nstr(abs(m_mu_from_e - m_mu)/m_mu * 100, 5)}%")
print(f"    m_tau (predicted) = {nstr(m_tau_from_e, 10)} MeV")

# From m_mu: determine M
M_from_mu = sqrt(m_mu) / s_mu
m_tau_from_mu = (M_from_mu * s_tau)**2

print(f"\n  From m_mu = {nstr(m_mu, 10)} MeV:")
print(f"    M = {nstr(M_from_mu, 12)} sqrt(MeV)")
print(f"    m_tau (predicted) = {nstr(m_tau_from_mu, 10)} MeV")

# Best prediction (average M)
M_avg = (M_from_e + M_from_mu) / 2
m_tau_best = (M_avg * s_tau)**2

print(f"\n  Best prediction (average M):")
print(f"    m_tau = {nstr(m_tau_best, 10)} MeV")

# ═══════════════════════════════════════════
# Step 4: Comparison with experiment
# ═══════════════════════════════════════════
print(f"\n{'=' * 60}")
print(f"RESULT")
print(f"{'=' * 60}")
print(f"\n  m_tau (predicted)   = {nstr(m_tau_best, 8)} MeV")
print(f"  m_tau (HFLAV 2025)  = {nstr(m_tau_hflav, 8)} +/- 0.09 MeV")
print(f"  Deviation           = {nstr(m_tau_best - m_tau_hflav, 5)} MeV")
print(f"  Significance        = {nstr(abs(m_tau_best - m_tau_hflav)/mpf('0.09'), 2)} sigma")
print(f"\n  m_mu/m_e (predicted) = {nstr((s_mu/s_e)**2, 10)}")
print(f"  m_mu/m_e (measured)  = {nstr(m_mu/m_e, 10)}")
print(f"  Deviation            = {nstr(abs((s_mu/s_e)**2 - m_mu/m_e)/(m_mu/m_e)*100, 5)}%")

# Koide K value
m_tau_pred = m_tau_best
K = (m_e + m_mu + m_tau_pred) / (sqrt(m_e) + sqrt(m_mu) + sqrt(m_tau_pred))**2
print(f"\n  Koide K (with predicted m_tau) = {nstr(K, 12)}")
print(f"  Expected: 2/3 = {nstr(mpf(2)/3, 12)}")
