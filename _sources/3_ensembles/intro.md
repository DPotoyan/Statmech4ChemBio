Statistical ensembles
=======================

In this module we are going to learn the essence of equilibrium statistical mechanics the statistical ensembles which will serve as a bridge connecting the probablistic world with the deterministic world of thermodynamics. 

![](./03_ensembles/figs/ensembl.png)


## NVE 

### Statistical picture

$$\Omega(N,V,E) = \sum^{number\, of\, microstates,}_{i} 1$$

$$S(N,V,E) = k_B log \Omega(N, V, E)$$

- Computing a weight of a microstate $E_i$ 

$$p(E_i) = \frac{1}{\Omega(N, V, E_i)}$$

- Computing a weight of sub-sytem macrostate $E=E_1+E_2$

$$p(E_1, E-E_1) = \frac{\Omega(E_1) \Omega(E-E_1)}{\sum_{E_1} \Omega(E_1) \Omega(E-E_1)} = \frac{e^{S_1(E_1)+S_2(E-E_1)}}{e^{S(E)}}$$

### Thermodynamic picture

- First and second law

$$dU = TdS-pdV+\mu dN$$

- Irreversible vs reversible process

$$dS_{tot}\geq 0$$ 

$$dE\leq 0$$


## NVT 

### Statistical picture

$$Z(N,V,T) = \sum^{number\, of\, microstates,}_{i} e^{-E_i/k_B T} = \sum_E \Omega(E) e^{-E/k_B T}$$

$$F=-k_BT log Z$$

- Computing a weight of a microstate $E_i$ 

$$p(E_i) = \frac{e^{-E_i/k_BT}}{Z}$$

- Computing a weight of a sub-sytem macrostate $E_1$ 

$$p(E_1) = \frac{\Omega(E) e^{-E_1/k_BT}}{Z} = \frac{e^{-F_1/k_BT}}{Z}$$

### Thermodynamic picture

- First and second law

$$dF_{T} = d(U-TS) = -pdV+\mu dN$$

- Irreversible vs reversible process

$$dS_{tot}\geq 0$$ 

$$dF\leq 0$$


## $\mu$VT 

### Statistical picture

$$Z_G(\mu,V,T) = \sum^{number\, of\, microstates,}_{i, N_i} e^{-E_i/k_B T} \cdot e^{\mu N_i/k_B T} = \sum_E \Omega(E, N) e^{-E/k_B T} e^{\mu N/k_B T}$$

$$Z_G(\mu, V, T) =-k_BT log Z_G$$

- Computing a weight of a microstate $E_i$ 

$$p(E_i) = \frac{e^{-E_i/k_BT} e^{\mu N_i/k_BT}}{Z_G}$$

- Computing a weight of a sub-sytem macrostate $E_1$ 

$$p(E_1, N_1) = \frac{\Omega(E, N) e^{-E_1/k_BT} e^{\mu N/k_BT}}{Z_G} = \frac{e^{-\Phi_1/k_BT}}{Z_G}$$

### Thermodynamic picture

- The First and the second law

$$d\Phi_{\mu, T} = d(U-TS - \mu N) = -pdV$$

- Irreversible vs reversible process

$$dS_{tot}\geq 0$$ 

$$d\Phi\leq 0$$


## Ensemble equivalence

### Smallness of fluctuations

Consider the extensive variable X and intensive variable Y where X (fluctuating) and Y (fixed) form a pair of conjugate variables. The sign will depend on the specific definitions of the variables X and Y. An example would be X = volume and Y = pressure.

$$\langle X \rangle  = \frac{\partial log Z}{\partial \beta Y}$$

$$\sigma^2_X = \langle X^2 \rangle - \langle X \rangle^2  = \frac{\partial^2 log Z}{\partial (\beta Y)^2}$$

 - $\sigma^2_E = k_B T^2 C_v(T) \sim O(N)$
 - $\sigma^2_N = \frac{k_B T}{v} \kappa_T \sim O(N)$
 
Ensembles with flcutuating extensive variables still end up being dominanted by averages hence being effectively in microcanonical regime with constant values repalced by aveages:

$$S = k_B log \Omega(\bar{E}, \bar{N}, \bar{V})$$

### Legendre transform

$$Z(X_0, ... X_n | X_{n+1}, ... X_{t}) = exp \big(-\beta \mathcal{L_{x_{0}, ... x_{n}}} E (x_0, ... x_t) \big)$$


