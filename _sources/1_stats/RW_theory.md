# Large N approximations

###  Stirling's approximation  

- This is the crude version of Stirling approximation that works out for $N\gg 1$

$$logN! \approx \sum log N_i = \int log N dN$$

$$\boxed{logN! \approx NlogN-N}$$

$$\boxed{N! \approx N^N e^{-N}}$$

A more accurate version is:

$$\boxed{N! \approx N^N e^{-N} \sqrt{2\pi N}}$$

### Applying Stirling approximation to the Binomial 

$$N = N_1+N_2$$ 

$$\frac{N!}{N_1! \cdot N_2!} \approx \frac{N^N e^{-N}}{N_1^{N_1} e^{-N_1}\cdot N_2^{N_2} e^{-N_2}} =\frac{N^N }{N_1^{N_1} \cdot N_2^{N_2} }$$

$$log\frac{N!}{N_1! \cdot N_2!} \approx NlogN -N_1 log N_1 - N_2log N_2 = \\ = N \Big[ -\frac{N_1}{N} log \frac{N_1}{N} - \frac{N_2}{N} log \frac{N_2}{N} \Big] = N[-p_1 log p_1 -p_2log p_2]$$

> The expression $S =  \sum_i -p_i log p_i$ is significant. We are going to associate it with entropy further down the road.

#### Gamma function: generalizing the factorial

$$\Gamma (n) = \int^{\infty}_0 x^{n-1} e^{-x}dx$$

- The gamma function $\Gamma(n)$ provides an extension of the factorial function to domain of noninteger and complex numbers. 
- The gamma function is defined for all complex numbers except the non-positive integers. 
- For any positive integer gamma function reduces to factorials

$$\Gamma(n)=(n-1)!$$

```python
from scipy.special import gamma

# Plot gamma function 
x = np.linspace(-5, 5, 1000)
plt.plot(x, gamma(x), label='$\Gamma(x)$')

# Plot (x-1)! for x = 1, 2, ..., 6
xint = 1+np.arange(6)
factorials = [np.math.factorial(x-1) for x in xint]
plt.plot(xint, factorials, '*', ms=10, color='red', label='$(x-1)!$')

# Style
plt.ylim(-50,50)
plt.xlim(-5, 5)
plt.xlabel('$x$')
plt.legend()
```
### Gaussian approximation to the Binomial Distribution in the large $N$ limit. 

Binomial distribution for large values of $N$ has a sharply peaked distribution around its maximum (most likely) value $\bar{n}$. This motivates us to seek a continuous approximation by Taylor expanding probability distribution around its max value $\Delta n = n-\bar{n}$ and keeping up to quadratic terms.

$$P_N(n) = \frac{N!}{n! (N-n)!} p^n (1-p)^{(N-n)}$$

Thus from the onset we are aiming for a Gaussian distribution. The task then is to find coefficients and to then justify that third term of Taylor expansion is negligible compared to the second!

$$logP(n) = logP(\bar{n}) + \frac{1}{2}B_2\Delta n^2 + O(\delta n^3)$$

$$log P(n) = log N! - log n! - log(N-n)! + nlog(p) + (N-n)log(1-p)$$

We evaluate derivative of $logn!$ in the limit of $n\gg1$ as: 

$$\frac{d}{dn} log n! = \frac{log(n+1)! - log n!}{n+1-n} \approx log(n+1) \approx log(n)$$

- We could also arrive at the same result by using Stirling approximation $logN! \approx  NlogN -n$
- Taking first derivative of Taylor expansion to Binomial we find the peak of the distribution around which we are making expansion:

$$\frac{d}{dn}log P(n) \Big |_{n=\bar{n}} = - log n + log(n-n) + log(p)  -log(1-p)=0$$

$$log \Big( \frac{N-n}{n} \frac{p}{1-p}\Big)=0\,\, \rightarrow \,\, \bar{n} = Np$$

- We recall that $\bar{n} = Np$ is also mean of the binomial! 
- Having found the peak of distribution and knowing first derivative we now proceed to compute the second derivative:

$$B_2 = \frac{d^2}{d n^2} logP(n) \Big |_{n = \bar{n}} = \frac{d}{dn} log \Big( \frac{N-n}{n} \frac{p}{1-p}\Big) \\ = \Big( - \frac{1}{N-n}-\frac{1}{n} \Big) \Big |_{n = \bar{n}} = - \frac{1}{Npq}$$

- While first derivative gave us the mean of binomial we notice that second derivative produces the variance $\sigma^2 = Npq$
- Now all that remains to do is to plug  the coefficients into our approximated probability distribution and then normalize it. Why normalize? After all Binomial was already properly normalized.  But since we made approximation by leaving our some terms we have to re-normalize again!

$$P(n) \approx P(\bar{n}) e^{-(n-\bar{n})^2/ 2Npq}$$

- Normalizing gaussian distribution is done via the following table integral

$$\int^{+\infty}_{-\infty} e^{-ax^2} = \Big(\frac{\pi}{a} \Big)^{1/2}$$

$$\int P(\bar{n}) e^{-(n-\bar{n})^2/ 2Npq} dn  = P(\bar{n}) (2\pi Npq)^{1/2}=1$$

- At last we have the normalized approximation to Binomial which is a guassian distribution arond mean!

$$P(n) \approx \frac{1}{(2\pi Npq)^{1/2}} e^{-(n-\bar{n})^2/ 2Npq} = \frac{1}{(2\pi \sigma^2)^{1/2}}e^{(n-\mu)^2/2\sigma^2}$$



## An Alternative derivation of Gaussian from Binomial making use of Stirling's approximation

Here we would like to start by choosing as a new independent variable the net right displacement of a random walker $m$  

- $m = n - (N-n) = 2n-N$. 
- Hence the number of moves to the right and left are  $n = \frac{N+m}{2}$ and  $(N - n)=\frac{N-m}{2}$ respectively.
- The left and right moves sum to the total move number $\frac{N-m}{2} + \frac{N-m}{2} = N$
- Let us also assume $p = 1/2$ for the sake of simplicity.

$$P_N(m) = \frac{N!}{(\frac{N+m}{2})! \cdot (\frac{N-m}{2})!} \frac{1}{2^N}$$

- Now we make use of Stirling approximation  valid for $N\gg1$ $N! = N^N e^N$. and start group with common exponents containing N and m respectively. 

$$P_N(m) \approx \frac{N^N e^N}{ (N-m)^{(N-m)/2} (N+m)^{(N+m)/2}  \cdot 2^{-N} e^N } \cdot \frac{1}{2^N}  \\ = \frac{N^N}{ (N-m)^{(N-m)/2} (N+m)^{(N+m)/2}} \\ = \frac{N^N}{ (N-m)^{N/2} (N+m)^{N/2}} \cdot  \Big( \frac{N-m}{N+m}\Big)^{m/2} \\ = \frac{1}{[(1-m/N)(1+m/N)]^{N/2}} \cdot  \Big( \frac{N-m}{N+m}\Big)^{m/2} \\ = \Big[(1-m^2/N^2) \Big]^{-N/2} \Big( \frac{1-m/N}{1+m/N}\Big)^{m/2}  \approx (e^{-m^2/N^2})^{-N/2} (e^{-m/N})^{m/2} (e^{+m/N})^{-m/2} = e^{-m^2/2N}$$

- Notice how factors involving $2^N$ and $e^N$ cancell in the first line.
- We have casted all terms in terms of $m/N$. This allowed us to make use of $(1\pm x)\approx e^{\pm x}$ approximation for small $x$. 


## Deriving Poisson distribution from Binomial in the limit of large $N$ and small $p$ such that $Np=const$.


- This is a situation of rare events like rains in forest or radioactive decay of uranium where each individual event has small chance of happening $p \rightarrow 0$  yet there are large number of samples $N\rightarrow \infty$ such that one has a constant average rate of events $\lambda = pN = const$
- In this limit distirbution is no longer well described by the gaussian as the shape of distribution is heavily skewed due to tiny values of p.

$$P_N(n) = \frac{N!}{n! (N-n)!} p^n (1-p)^{(N-n)}$$

- Writing factorial $N!/(N-n)!$ explicitely we realize that it is dominated $N^n$ and also $N-n \approx N$

$$P_N(n) = \frac{N(N-1)...(N-1+1))}{n!} p^n (1-p)^{(N-n)} \approx \frac{N^n}{n!} p^n (1-p)^{N}$$

- Next let us plug in $\lambda = pN = const$ and recall the definition of exponential $lim_{x\rightarrow \infty }(1-1/x)^x = e^{-x}$


$$P(n) = \frac{N^n}{n!} \Big( \frac{\lambda}{N} \Big)^n \Big( 1-\frac{\lambda}{N} \Big)^{N} = \frac{\lambda^n}{n!} \Big( 1-\frac{\lambda}{N} \Big)^{N} \approx \frac{\lambda^n}{n!} e^{-\lambda}$$

