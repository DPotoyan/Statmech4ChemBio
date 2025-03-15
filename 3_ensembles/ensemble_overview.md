
# Summary of Ensembles
  
![](./figs/ensembl.png)


Here’s your revised **Markdown-friendly LaTeX** version with corrected equations and formatting.


## Entropy as a Function of Microstate Probabilities

Entropy is given by the **Shannon-Gibbs entropy formula**:

$$
S([p]) = -k_B \sum_{i} p_i \log p_i
$$

where $ p_i $ is the probability of the $ i $th microstate.

### Physical Constraints for Equilibrium

For a system to maintain equilibrium values, the microstate probabilities must satisfy the following conditions:

1. **Normalization:**
   $$
   \sum_{i} p_i = 1
   $$

2. **Constraint to Maintain the Expectation Value of an Observable $X$ (e.g., Energy or Volume):**

   $$
   \sum_{i} p_i X_i = \langle X \rangle, \quad \sum_{i} p_i Y_i = \langle Y \rangle
   $$

   The probability of a macrostate $ (X, Y, \dots) $ follows the general form:

   $$
   P(X, Y, \dots) = \frac{e^{S(X, Y, \dots)/k_B - \beta (X + Y + \dots)}}{Z}
   $$

   where $Z$ is a normalization factor.

### **Comparison of Ensembles**


**Exponential dependence can be appreciated by considering exhcnage with environment or large reserovoir**

$$E_r\gg E,\quad V_r \gg V, \quad N_t \gg N$$

$$log \Omega_r(E_t-E, V_r-V, N_r-N,)\approx  const - \beta E + \beta\mu -\beta PV $$

$$P(E, N, V) \sim \Omega \cdot \Omega_r \sim e^{S(E, N, V)} \cdot e^{-\beta E} \cdot e^{\beta \mu N} \cdot e^{-\beta PV} $$


| **Ensemble** | **$ P(\text{microstate}) $** | **$ P(\text{macrostate}) $** |
|-------------|------------------------------------------------------|------------------------------------------------------|
| **Microcanonical (NVE)** | $ P(\text{microstate}) = \frac{1}{\Omega(E)} $ (all accessible microstates are equally probable) | $ P(E) \sim e^{S(E)/k_B} $ (entropy-dominated) |
| **Canonical (NVT)** | $ P(\text{microstate}) \sim e^{-\beta E} $ (Boltzmann distribution) | $ P(E) \sim e^{S(E)/k_B - \beta E} $ (entropy-weighted by energy) |
| **Grand Canonical (µVT)** | $ P(\text{microstate}) \sim e^{\beta (\mu N - E)} $ | $ P(N, E) \sim e^{S(N,E)/k_B + \beta (\mu N - E)} $ |
| **Isothermal-Isobaric (NPT)** | $ P(\text{microstate}) \sim e^{-\beta (E + PV)} $ | $ P(E, V) \sim e^{S(E, V)/k_B - \beta (E + PV)} $ |

---

**Key Highlights**
- **Entropy dependence** $e^{S/k_B}$ is universal across all ensembles.
- **Microstate probability** follows different forms based on constraints from different thermodynamic potentials.
- **Macrostate probability** always includes an entropy term but is modified by energy, pressure, and chemical potential, depending on the ensemble.



### **Ensemble Equivalence and Fluctuation-Response Relations**

**Smallness of Fluctuations**

The total differential of internal energy $ U $ in a thermodynamic system can be expressed in terms of its conjugate variables:

$$
dU = SdT - VdP + \mu dN + BdM + \dots = \sum_i f_i dX_i
$$

where each pair $ (X_i, f_i) $ represents a conjugate extensive and intensive variable, such as:
- $ (S, T) $ → entropy and temperature,
- $ (V, -P) $ → volume and pressure,
- $ (N, \mu) $ → particle number and chemical potential,
- $ (M, B) $ → magnetization and magnetic field.

### **Fluctuation-Response Relations**
For a given extensive variable $ X $ and its conjugate intensive variable $ Y $, the partition function $ Z $ governs both the **mean value** and **fluctuations** of $ X $. 

- **Mean value of $ X $ at constant $ Y $:**
  $$
  \langle X \rangle = \frac{\partial \log Z}{\partial (\beta f)}
  $$

- **Fluctuations of $ X $ at constant $ Y $:**
  $$
  \sigma^2_X = \langle X^2 \rangle - \langle X \rangle^2 = \frac{\partial^2 \log Z}{\partial (\beta f)^2}
  $$

This relation shows that fluctuations in $ X $ are directly linked to the second derivative of the partition function, a fundamental result of statistical mechanics.

### **Smallness of Fluctuations in the Thermodynamic Limit**
For macroscopic systems, fluctuations in extensive variables are typically small relative to their mean values. Examples include:

- **Energy fluctuations (Canonical Ensemble):**

  $$
  \sigma^2_E = k_B T^2 C_V
  $$
  where $ C_V $ is the heat capacity at constant volume.

- **Particle number fluctuations (Grand Canonical Ensemble):**

  $$
  \sigma^2_N = k_B T \frac{\kappa_T}{V}
  $$
  where $ \kappa_T $ is the isothermal compressibility.

### **Key Insights**

- **Fluctuations decrease as system size increases**, typically scaling as $ 1/\sqrt{N} $.
- **Response functions (e.g., heat capacity, compressibility) determine fluctuation magnitude**.
- **Ensemble equivalence** ensures that for large systems, different ensembles (canonical, grand canonical, etc.) give equivalent macroscopic results, despite differing fluctuation magnitudes.



### **Legendre and Laplace Transforms in Thermodynamics and Statistical Mechanics**


- **The  Legendre transformation** provides a way to reformulate equilibrium conditions (e.g., entropy maximization) in terms of more convenient variables (e.g., free energy minimization). This allows for the introduction of thermodynamic potentials tailored to different ensembles.

- **Free Energies as Legendre Transforms of Internal Energy** The internal energy function $ U(S, V, N, \dots) $ depends on extensive variables (e.g., entropy $ S $, volume $ V $, particle number $ N $). The thermodynamic free energies arise as **Legendre transforms** of $ U $ with respect to these variables:

- **Helmholtz free energy** (Legendre transform over $ S $):
  $$
  F(N, V, T) = U - T S = \mathcal{L}_{S} U(S, V, N)
  $$

- **Gibbs free energy** (Legendre transform over $ S, V $):
  $$
  G(N, P, T) = U - T S + P V = \mathcal{L}_{S, V} U(S, V, N)
  $$

### **General Form of the Legendre Transform**

- A general **Legendre transformation** of an energy function $ U(X_1, \dots, X_N) $ with respect to a subset of its extensive variables $ X_0, \dots, X_n $ is given by:

$$
\mathcal{L}_{X_{1}, \dots, X_{n}} U(X_1,  \dots, X_N) = U - \sum_{k=0}^{n} f_k X_k = \Psi(f_0, \dots, f_{n}, X_{n+1}, \dots, X_{N})
$$

- where $ f_k = \frac{\partial U}{\partial X_k} $ are the conjugate **intensive variables**.

**Partition Functions and Legendre Transforms**

- The **partition function** in statistical mechanics naturally follows the structure of a **Legendre transform**, as it is related to free energy via:

$$
Z(f_0, \dots, f_n,  X_{n+1}, \dots, X_N) = e^{-\beta \Psi(f_0, \dots, f_{n}, X_{n+1}, \dots, X_{N})}
$$

- This reveals a **general pattern**:  **Partition functions are exponential functions of Legendre-transformed energy functions** over the fluctuating quantities.

---

## **Laplace Transform: Free Energies as Laplace Transforms of Energy**
In statistical mechanics, free energies also emerge as **Laplace transforms** of the internal energy function:

$$
Z(\beta, N, V) = \int dE \, e^{-\beta E} \Omega(E)
$$

which, in the thermodynamic limit, simplifies to:

$$
Z(\beta, N, V) = e^{-\beta F(\beta, N, V)}
$$

This shows that the **partition function is the Laplace transform of the density of states** $ \Omega(E) $, and the **free energy is the negative logarithm of this Laplace transform**:

$$
F(\beta, N, V) = -\frac{1}{\beta} \log Z(\beta, N, V)
$$



**Key Insights**
- **Legendre transforms** convert energy functions into free energies by replacing **extensive** variables with their conjugate **intensive** counterparts.
- **Laplace transforms** relate partition functions to energy distributions, providing a statistical interpretation of free energy.
- The **partition function takes the form** $ Z \sim e^{-\beta \Psi} $, where $ \Psi $ is a Legendre-transformed potential.

