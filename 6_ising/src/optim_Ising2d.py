import numpy  as np
import pandas as pd
#from numba import jit, njit

def compute_thermo(spins, J, B):
  '''Computes thermodynamic variables given the spin lattice'''
  
  N = len(spins)

  # Energy 
  z = np.roll(spins, 1, axis = 0) + np.roll(spins, -1, axis = 0) + np.roll(spins, 1, axis = 1) + np.roll(spins, -1, axis = 1)
  E = np.sum(-J*spins*z/4) - B*np.sum(spins)

  # Magnetization
  M   = np.mean(spins)

  return M, E  

def run_ising2d(spins, J, B, T, n_steps, out_freq):

    #Initialize data arrays
    M, E, traj = [], [], []
    N = len(spins)

    for step in range(n_steps):

        #Pick random spin
        i, j = np.random.randint(N), np.random.randint(N)

        #Compute energy change due to a flip of spin at i,j
        z  = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N] 
        dE = 2*spins[i,j]*(J*z + B)

        #Metropolis condition
        if dE <= 0 or np.exp(-dE/T) > np.random.rand():
          
            spins[i,j] *= -1 

        #Compute and store data
        if step % out_freq == 0:

            M_t, E_t = compute_thermo(spins, J, B)
            
            M.append(M_t)
            E.append(E_t)
            traj.append(spins.copy())

    return traj, E, M

if __name__ == "__main__":

    traj, E, M = ising2d_mcmc(spins=np.ones((20,20)), J=1, B=0, T=3, n_steps=1e7, out_freq = 1e4);

    thermo = pd.DataFrame({'E': E, 'M': M})