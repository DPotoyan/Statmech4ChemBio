- Only 1% population has cancer hence we get probability of an inidivual having (not having) cancer as:

$$
P(C)=0.01\,\,\,\,hence\,\,\,\,\,\,\, P(\hat{C})=1-P(C)=0.99
$$

- Accuracy of a test (how ofte positives show up when cancer is certain)

$$
P(+|C) = 0.9 \\ P(-|\hat{C})=0.9
$$

**Solution**
$$
P(C|+) = \frac{P(+|C)p(C)}{p(+)} = \frac{P(+|C)p(C)}{p(+|C)p(C)+p(+|\hat{C})p(\hat{C})} =  \frac{0.9\cdot 0.01}{0.9\cdot 0.01+0.1\cdot 0.99} = 0.083
$$
