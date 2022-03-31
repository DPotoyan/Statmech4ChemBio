
# Overview of ensembles

![](./figs/ensembl.png)

## NVE 

### Thermodynamics

- **Fundamental relation**

$$dE = TdS-pdV+\mu dN$$

- **Derivatives of energy**

$$T = \Big(\frac{\partial E}{\partial S}\Big)_{V,N}\,\,\,\,\,\, p = -\Big(\frac{\partial E}{\partial V}\Big)_{S,N} \,\,\,\,\,\, \mu = \Big(\frac{\partial E}{\partial N}\Big)_{S,V}$$

- **Second law**

$$dS(E,V,N)\geq 0\,\,\,\,\,\,\,\,\, dE(S,V,N)\leq 0$$ 

### Statistical mechanics 

- **Bridge equation**

$$\Omega(N,V,E) = \sum^{}_{i} 1$$

$$S(N,V,E) = k_B log \Omega(N, V, E)$$

- **Probability of a microstate**

$$p(E) = \frac{1}{\Omega(N, V, E)}$$

- **Probability of a macrostate**

$$p(E_1, E-E_1) = \frac{\Omega(E_1) \Omega(E-E_1)}{\sum_{E_1} \Omega(E_1) \Omega(E-E_1)} = \frac{e^{S_1(E_1)+S_2(E-E_1)}}{e^{S(E)}}$$


## NVT 

### Thermodynamics

- **Fundamental relation**

$$dF = d(E-TS) = -SdT -pdV + \mu dN$$

- **Derivatives of free energy**

$$S = -\Big(\frac{\partial F}{\partial T}\Big)_{V,N}\,\,\,\,\,\, p = -\Big(\frac{\partial F}{\partial V}\Big)_{T,N} \,\,\,\,\,\, \mu = \Big(\frac{\partial F}{\partial N}\Big)_{T,V}$$

- **Second law**

$$dF(T,V,N)\leq 0$$ 

### Statistical mechanics

- **Bridge equation**

$$Z(N,V,T) = \sum^{}_{i} e^{-E_i/k_B T} = \sum_E \Omega(E) e^{-E/k_B T}$$

$$F=-k_BT log Z$$

- **Probability of a microstate**

$$p(E_i) = \frac{e^{-E_i/k_BT}}{Z}$$

- **Probability of a macrostate**

$$p(E') = \frac{\Omega(E^{'}) e^{-E^{'}/k_BT}}{Z} = \frac{e^{-\beta F^{'}}}{Z}$$




## $\mu$VT 


### Thermodynamics

- **Fundamental relation**

$$d\Phi_{\mu, T} = d(U-TS - \mu N) = -SdT-pdV-Nd\mu$$

- **Derivatives of free energy**

$$S = -\Big(\frac{\partial \Phi}{\partial T}\Big)_{V,N}\,\,\,\,\,\, p = -\Big(\frac{\partial \Phi}{\partial V}\Big)_{T,\mu} \,\,\,\,\,\, N = - \Big(\frac{\partial \Phi}{\partial \mu}\Big)_{T,V}$$


- **Second law**

$$d\Phi\leq 0$$

### Statistical mechanics

- **Bridge equation**

$$Z_G(\mu,V,T) = \sum^{}_{i, N} e^{-E_i/k_B T} \cdot e^{\mu N/k_B T} = \sum_E \Omega(E, N) e^{-E/k_B T} e^{\mu N/k_B T}$$

$$\Phi(\mu, V, T) =-k_BT log Z_G$$

- **Probability of a microstate**

$$p(E_i) = \frac{e^{-E_i/k_BT} e^{\mu N_i/k_BT}}{Z_G}$$

- **Probability of a macrostate**

$$p(E', N') = \frac{\Omega(E', N') e^{-E'/k_BT} e^{ \beta \mu N'}}{Z_G} = \frac{e^{-\beta \Phi'}}{Z_G}$$


## Ensemble equivalence

### Smallness of fluctuations

$$dU = SdT -VdP +\mu dN + BdM +... = \sum_i Y_i dX_i$$

Consider a conjucate pair of extensive $X_i$ and intensive $Y_i$ variables. For instnace $(1, E)$, $(S, T)$ or $(V, -p)$. The average and fluctuations of extensive variable $X$ for constant $Y$ is given by derivatives of parition function:

$$\langle X \rangle  = \frac{\partial log Z}{\partial \beta Y}$$

$$\sigma^2_X = \langle X^2 \rangle - \langle X \rangle^2  = \frac{\partial^2 log Z}{\partial (\beta Y)^2}$$

- **Smallness of fluctuations**

 $$\sigma^2_E = k_B T^2 C_v(T) $$

 $$\sigma^2_N = \frac{k_B T}{v} \kappa_T$$

### Legendre and Laplace transforms

Legendre transformation enables expressing the condition of equilibrium (e.g. maximium of entropy function) in terms of convenient variables (e.g minimum of some free eneergy function). 

- **Free energies are Legedre transforms of internal energy function $E(S,V,N,...)$**

$$\mathcal{L}_{S} E(S,V,N) = U - T\cdot S = F(N, V, T)$$ 

$$\mathcal{L}_{S, V} E(S,V,N) = U - T\cdot S + pV = G(N, p, T)$$

**General expression of Legendtre transform**

A general expression for legendre transform of energy $U(X_0, X_1, ...X_n, X_n+1, ... X_t)$ with respect to its extensive variables can be written down as:

$$\mathcal{L}_{X_{0}, ... X_{n}} U = U - \sum Y_k X_k = \Psi(Y_0,... Y_{n}, X_{n+1}, ...X_{t})$$

The various **partion functions** can then be seen to be of general form $e^{\beta \Psi}$ where the free energy function is a **Legendre transform over fluctuating quantities.**

$$Z(X_0, ... X_n | X_{n+1}, ... X_{t}) = exp \big(-\beta \mathcal{L_{X_{0}, ... X_{n}}} E (X_0, ... X_t) \big)$$

- Free energies as Laplace transform of internal energy function $E(S,V,N,...)$

$$Z(\beta, N, V) = e^{-\beta F(\beta, N, V)}$$
