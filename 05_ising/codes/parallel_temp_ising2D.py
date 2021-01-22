import numpy as np
from numpy.random import choice, rand, randint
from numba import jit, njit

######## Main Code ###########

@njit
def mcmc(spins, N, J, B, T, n_steps = 10000, out_freq = 1000):
    
    '''mcmc takes spin configuration and samples with given N,J,B,T 
    for n_steps outputing results every out_freq'''

    confs = [] 
    
    for step in range(n_steps):

        #Pick random spin
        i, j = randint(N), randint(N)

        #Compute energy change
        z  = spins[(i+1)%N, j] + spins[(i-1)%N, j] + spins[i, (j+1)%N] + spins[i, (j-1)%N]
        dE = 2*spins[i,j]*(J*z + B)

        #Metropolis condition
        if dE <= 0 or np.exp(-dE/T) > rand():
            
            spins[i,j] *= -1 

        #Store the spin configuration
        if step % out_freq == 0:
            
            confs.append(spins.copy())
        
    return confs

@njit
def getM(spins):
    
    return np.mean(spins)


@njit
def getE(spins,N,J,B):    
    
    E = 0
    
    for i in range(N):
        for j in range(N):   
            
            z = spins[(i+1)%N, j] + spins[(i-1)%N, j] +spins[i,(j+1)%N] +  spins[i,(j-1)%N]
            
            E += -J*z*spins[i,j]/4 # Since we overcounted interactions 4 times divide by 4.

    return E - B*np.sum(spins) #Field contribution added


@jit
def temper(configs):
    
    '''Randomly pick two adjacent replicas and attempt an exchange'''
    
    i       = np.random.randint(N_repl-1)
    j       = i+1
    
    deltaBeta      = 1/T[i] - 1/T[j]
    
    deltaEnergy    = getE(configs[i][-1],N,J,B) - getE(configs[j][-1],N,J,B)
    
    if deltaBeta*deltaEnergy < 0 or np.exp(-deltaBeta*deltaEnergy) > rand():
        
        configs[i][-1], configs[j][-1] = configs[j][-1], configs[i][-1]
        
    return configs

@jit
def pt_mcmc(N, J, B, T=[1, 0.1], n_exch=1000, n_steps=10000, out_freq=1000):
    
    N_repl     = len(T)
    configs    = [[choice([-1,1], (N,N))] for i in range(N_repl)]
    
    
    for exch_attempt in range(n_exch): #Exchange attemps
    
        configs = temper(configs)
    
        for i in range(N_repl): #mcmc in between exchange attemps
    
            configs_new = mcmc(configs[i][-1],N, J, B, T[i])
    
            configs[i].extend(configs_new)
        
    return configs

        

        

