# Stochastic Processes

Python implementation of Simple Stochastic Processes (e.g. Simple Random Walk).
Right now it is mainly a sandbox to play with matplotlib slider.

<p align="center">
	<img src="https://github.com/saeedghsh/SimpleRandomWalk/blob/master/animation.gif" width="900">
</p>

## Usage
Currently only Simple Random Walk:
```bash
pip install -r requirements.txt
python main.py --length 1000 --count 10
```
- `--count` (default: 1) is the number of processess plotted at the same time (3 in the animation above)
- `--length` (default: 100) is the maximum time (100 in the animation above)

<!-- ## Markov chain -->
<!-- A stochastic process where future states only depend on the current state. -->
<!-- More formally, a discrete stochastic process: -->
<!-- ``` -->
<!-- X0, X1, ... -->
<!-- ``` -->
<!-- is a markov chain if -->
<!-- ``` -->
<!-- P(X[t+1]=s | X[0],X[1],...,X[t]) == P(x[t+1]=s|X[t]) \forall t>=0 \and \forall s -->
<!-- ``` -->

<!-- If X[i] has values in S (state space; a fininte set of m members); -->
<!-- ``` -->
<!-- P_{ij} = P(X[t+1]=j | X[t]=i), i,j  \in S -->
<!-- \sum_{j \in S}{P_{ij}} = 1 -->
<!-- ``` -->
<!-- `P_{ij}` construct the "transition probability matrix" A (square, but not symmetric). -->
<!-- Transition probability matrix A has all the information about the process. -->
<!-- For instance, two step probabilities could be computed from A: -->
<!-- Q_{ij} = P(X[t+2]=j | X[t]=i) -->
<!-- [[Q11, Q12, ..., Q1m], -->
<!--  [...], -->
<!--  [Qm1,...]] == A^{2} -->

<!-- If transition probability matrix A has positive entries, by perron frobenius theorem, there exists a vector `v=[p1,p2,...]` satisfying `Av = v`, where `v` is the long term behaviour of the system, i.e. `P(X=i)=p_i` in long term. `v` is called stationary distribution. Note that `v` is the eigenvector of A corresponding the largest eigenvalue of A that is 1.  -->

<!-- ## Simple Random Walk -->
<!-- X[0] = 0 -->
<!-- X[t+1] = (X[t]+1 with probablity 0.5) or (X[t]-1 with probablity 0.5) -->

<!-- * Simple Random Walk is a Markov Chain, but it does not have a "transition probability matrix", because the state space is not finite. -->

<!-- ## Martingale (probability theory) -->
<!-- [Martingale ](https://en.wikipedia.org/wiki/Martingale_(probability_theory)) -->

## Laundary List
* [ ] ...


## License
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/SimpleRandomWalk/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
