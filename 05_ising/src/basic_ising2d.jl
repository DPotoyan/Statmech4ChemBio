using Random
using Statistics
using PyPlot

######## Main Code ###########
function ising2d_mcmc(N,J,B,T; n_steps = 10^7, out_freq = 5000)

    #Initialize
    spins    = ones((N,N))        #rand([-1,1], (N,N))

    # Empty array/matrix for recording
    confs    = []
    M, E     = [], []

    for step in 1:n_steps

        #Pick random spin
        i, j = rand(1:N), rand(1:N)

        #Compute energy change
        z = spins[mod1(i+1,N), j] + spins[mod1(i-1,N), j] + spins[i, mod1(j+1,N)] + spins[i, mod1(j-1,N)]
        dE = 2*spins[i,j]*(J*z + B)

        #Metropolis condition
        if dE <= 0  ||  exp(-dE/T) > rand()

            spins[i,j] *= -1 # flip spin

        end

        #Store the spin configuration
        if step % out_freq ==0

            push!(confs,  copy(spins))
            push!(M,      getM(spins))
            push!(E,      getE(spins,N,J,B))

        end

    end
    return confs, M, E

end

######## Thermo output ###########

# Compute M
function getM(spins)

    return mean(spins)

end

# Compute E
function getE(spins,N,J,B)

    E = 0

    for i in 1:N
        for j in 1:N

            z = spins[mod1(i+1,N), j] + spins[mod1(i-1,N), j] + spins[i, mod1(j+1,N)] + spins[i, mod1(j-1,N)]
            E += -J*z*spins[i,j]/4

        end
    end

    return E-B*sum(spins)

end


##### Print info #####

println("Julia MC loaded\n 2 functions are availible:\n ising2d_mcmc(N,J,B,T, n_steps, out_freq) and getE(spins,N,J,B)\n Default number of steps is 10^7 with output frequency 5000.")
