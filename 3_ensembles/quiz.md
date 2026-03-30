# Quiz: Statistical Ensembles (NVE, NVT, $\mu$VT, and NPT)

---

**Q1.** In the microcanonical ensemble (NVE), the fundamental postulate states that all accessible microstates are:

- A) Weighted by the Boltzmann factor $e^{-\beta E}$
- B) Equally probable
- C) Distributed according to a Gaussian
- D) Weighted by their degeneracy only

**Answer:** B

---

**Q2.** The Boltzmann entropy formula $S = k_B \log \Omega$ relates entropy to the number of microstates. For $N$ non-interacting spins where each spin has two equally-energetic orientations, how does entropy scale with system size?

- A) $S \propto \log N$
- B) $S \propto N^2$
- C) $S \propto N$
- D) $S \propto e^N$

**Answer:** C

---

**Q3.** The inverse temperature $\beta = 1/k_BT$ is defined thermodynamically as:

- A) $\beta = \frac{\partial \Omega}{\partial E}$
- B) $\beta = \frac{\partial \log \Omega}{\partial E}$
- C) $\beta = -\frac{\partial S}{\partial E}$
- D) $\beta = \frac{\partial E}{\partial S}$

**Answer:** B

---

**Q4.** When two subsystems of an isolated system exchange energy, the equilibrium energy partition corresponds to:

- A) Equal energies in both subsystems
- B) Maximum total number of microstates (maximum entropy)
- C) Minimum total energy
- D) Equal number of microstates in both subsystems

**Answer:** B

---

**Q5.** In classical statistical mechanics, the phase space for $N$ indistinguishable particles is divided by $N! \, h^{fN}$. The factor of $N!$ corrects for:

- A) Quantum uncertainty in position
- B) The indistinguishability of identical particles
- C) Double counting of momentum states
- D) Relativistic effects at high energy

**Answer:** B

---

**Q6.** The canonical partition function $Z$ and the Helmholtz free energy $F$ are related by:

- A) $F = k_B T \log Z$
- B) $F = -k_B T \log Z$
- C) $F = -k_B T \, Z$
- D) $F = k_B T / Z$

**Answer:** B

---

**Q7.** For a system of $N$ non-interacting identical particles with single-particle partition function $z$, the full canonical partition function for indistinguishable particles is:

- A) $Z = z^N$
- B) $Z = N \cdot z$
- C) $Z = z^N / N!$
- D) $Z = (z/N)^N$

**Answer:** C

---

**Q8.** According to the equipartition theorem, each quadratic degree of freedom in a classical Hamiltonian contributes an average energy of:

- A) $k_B T$
- B) $\frac{3}{2} k_B T$
- C) $\frac{1}{2} k_B T$
- D) $2 k_B T$

**Answer:** C

---

**Q9.** The Maxwell-Boltzmann speed distribution $f(v)$ for an ideal gas has a factor of $4\pi v^2$ multiplying the Boltzmann exponential. This factor arises from:

- A) The normalization condition
- B) The three independent velocity components
- C) The Jacobian when converting from Cartesian velocity to spherical coordinates (speed)
- D) Quantum degeneracy of momentum states

**Answer:** C

---

**Q10.** The thermal de Broglie wavelength is $\lambda_T = h / \sqrt{2\pi m k_B T}$. The classical (non-quantum) treatment of a gas is valid when:

- A) $n \lambda_T^3 \gg 1$, where $n$ is the number density
- B) $n \lambda_T^3 \ll 1$
- C) $\lambda_T \gg L$, where $L$ is the box size
- D) $T \to 0$

**Answer:** B

---

**Q11.** The fluctuation-response theorem in the canonical ensemble states that energy fluctuations are related to:

- A) $\sigma_E^2 = k_B T \, C_V$
- B) $\sigma_E^2 = k_B T^2 \, C_V$
- C) $\sigma_E^2 = k_B T^2 / C_V$
- D) $\sigma_E^2 = C_V / k_B T$

**Answer:** B

---

**Q12.** For a quantum harmonic oscillator at low temperature ($k_B T \ll \hbar\omega$), the average energy approaches:

- A) $0$
- B) $k_B T$
- C) $\frac{1}{2}\hbar\omega$
- D) $\hbar\omega$

**Answer:** C

---

**Q13.** In the Debye model of solids, the heat capacity at low temperatures scales as:

- A) $C_V \propto T$
- B) $C_V \propto T^2$
- C) $C_V \propto T^3$
- D) $C_V = \text{const}$

**Answer:** C

---

**Q14.** The relative energy fluctuations $\sigma_E / \langle E \rangle$ in the canonical ensemble scale with system size $N$ as:

- A) $O(N)$
- B) $O(N^{1/2})$
- C) $O(N^{-1/2})$
- D) $O(N^{-1})$

**Answer:** C

---

**Q15.** The ratio of probabilities of two macrostates $A$ and $B$ in the canonical ensemble is given by $p_B/p_A = e^{-\beta(F_B - F_A)}$. This shows that macrostate populations are governed by:

- A) Energy differences alone
- B) Entropy differences alone
- C) Free energy differences
- D) Volume differences

**Answer:** C

---

## Grand Canonical and NPT Ensembles

---

**Q16.** In the grand canonical ensemble, the system exchanges energy and particles with a reservoir. The probability of a microstate with energy $E_i$ and particle number $N$ is proportional to:

- A) $e^{-\beta E_i}$
- B) $e^{-\beta(E_i + \mu N)}$
- C) $e^{-\beta(E_i - \mu N)}$
- D) $e^{-\beta E_i} / N!$

**Answer:** C

---

**Q17.** The grand canonical partition function $\Xi$ and the grand potential $\Psi = E - TS - \mu N$ are related by:

- A) $\Psi = k_B T \ln \Xi$
- B) $\Psi = -k_B T \ln \Xi$
- C) $\Psi = -k_B T \, \Xi$
- D) $\Psi = \mu \ln \Xi$

**Answer:** B

---

**Q18.** In the grand canonical ensemble, the thermodynamic identity $\beta PV = \ln \Xi$ tells us that the grand potential $\Psi$ equals:

- A) $+PV$
- B) $-PV$
- C) $TS$
- D) $\mu N$

**Answer:** B

---

**Q19.** The average particle number in the grand canonical ensemble can be obtained from $\Xi$ as:

- A) $\langle N \rangle = -\frac{\partial \ln \Xi}{\partial (\beta \mu)}$
- B) $\langle N \rangle = \frac{\partial \ln \Xi}{\partial (\beta \mu)}$
- C) $\langle N \rangle = \frac{\partial \Xi}{\partial \mu}$
- D) $\langle N \rangle = \beta \mu \ln \Xi$

**Answer:** B

---

**Q20.** The relative fluctuation in particle number $\sigma_N / \langle N \rangle$ in the grand canonical ensemble scales with system size as:

- A) $O(1)$
- B) $O(N^{1/2})$
- C) $O(N^{-1/2})$
- D) $O(N^{-1})$

**Answer:** C

---

**Q21.** The chemical potential $\mu$ governs the flow of particles between subsystems. At equilibrium, particles flow from regions of:

- A) Low $\mu$ to high $\mu$
- B) High $\mu$ to low $\mu$
- C) High $T$ to low $T$
- D) Low $P$ to high $P$

**Answer:** B

---

**Q22.** For an ideal gas, the chemical potential is $\mu = k_BT \ln(n\lambda^3)$, where $n$ is the number density and $\lambda$ is the thermal de Broglie wavelength. At fixed temperature, increasing the density causes $\mu$ to:

- A) Decrease
- B) Stay constant
- C) Increase
- D) Oscillate

**Answer:** C

---

**Q23.** The grand partition function for an ideal gas is $\Xi = \exp\left(e^{\beta\mu} V / \lambda^3\right)$. The quantity $z = e^{\beta\mu}$ is called the:

- A) Activity coefficient
- B) Fugacity
- C) Compressibility factor
- D) Partition number

**Answer:** B

---

**Q24.** In the Langmuir adsorption model, each surface site can be either empty (energy 0) or occupied by one molecule (energy $\epsilon$). The grand partition function for a single site is:

- A) $\xi = e^{-\beta\epsilon}$
- B) $\xi = 1 + e^{-\beta\epsilon}$
- C) $\xi = 1 + e^{-\beta(\epsilon - \mu)}$
- D) $\xi = e^{-\beta(\epsilon - \mu)}$

**Answer:** C

---

**Q25.** In the Langmuir model with $N_0$ independent adsorption sites, the average fractional occupancy $\langle N \rangle / N_0$ at high chemical potential ($\mu \gg \epsilon$) approaches:

- A) 0
- B) 1/2
- C) 1
- D) $\infty$

**Answer:** C

---

**Q26.** For a gas-phase reaction at equilibrium, the equilibrium constant $K(T)$ can be expressed in terms of molecular partition functions. The volume dependence from translational partition functions cancels when $K$ is written in terms of:

- A) $z_i$
- B) $z_i / V$ (partition functions per unit volume)
- C) $z_i \cdot V$
- D) $z_i / N_i$

**Answer:** B

---

**Q27.** The NPT ensemble describes a system at constant temperature and pressure. The probability of a microstate with energy $E$ and volume $V$ is proportional to:

- A) $e^{-\beta E}$
- B) $e^{-\beta(E - pV)}$
- C) $e^{-\beta(E + pV)}$
- D) $e^{-\beta E} \cdot V$

**Answer:** C

---

**Q28.** The NPT partition function $\Delta(T, p, N)$ is related to the canonical partition function $Z(N, V, T)$ by:

- A) $\Delta = Z \cdot e^{-\beta pV}$
- B) $\Delta = \sum_V Z(N, V, T)$
- C) $\Delta = \int_0^{\infty} Z(N, V, T)\, e^{-\beta p V}\, dV$
- D) $\Delta = Z / p$

**Answer:** C

---

**Q29.** The thermodynamic potential associated with the NPT ensemble is:

- A) Helmholtz free energy $F = E - TS$
- B) Gibbs free energy $G = E - TS + pV$
- C) Grand potential $\Psi = E - TS - \mu N$
- D) Enthalpy $H = E + pV$

**Answer:** B

---

**Q30.** In the NPT ensemble, the volume fluctuations are related to a thermodynamic response function by $\sigma_V^2 = k_BT V \kappa_T$. Here $\kappa_T$ is the:

- A) Thermal expansion coefficient
- B) Heat capacity at constant pressure
- C) Isothermal compressibility
- D) Adiabatic compressibility

**Answer:** C
