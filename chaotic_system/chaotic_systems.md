# Chaotic Systems
Python implementation and exprementation with few simplistic chaotic systems.

* Logistic Map: <img src="https://render.githubusercontent.com/render/math?math=x_{t %2B 1}=rx_{t}(x_{t} %2B 1)">  
  <p align="center">
      <img src="https://github.com/saeedghsh/ChaoticSystems/blob/master/images/logisticmap_animation.gif" width="900">
  </p>

## laundry list

* [x] separate parsers for different type of systems (with subparser)

* [x] gererate chaotic processes via logistic maps
  - [ ] reproduce all the plots from [here](https://en.wikipedia.org/wiki/Logistic_map)
    + [x] frequency spectrum
    + [x] [cobweb plot](https://en.wikipedia.org/wiki/Cobweb_plot)
    + [ ] [Bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram)
    + [ ] "lyapunov exponent" v.s. `r`: In mathematics the Lyapunov
      exponent or Lyapunov characteristic exponent of a dynamical
      system is a quantity that characterizes the rate of separation
      of infinitesimally close trajectories.

    + [ ] Two- and three-dimensional [Poincaré plots](https://en.wikipedia.org/wiki/Poincar%C3%A9_plot)
  - [ ] use [Tent map](https://en.wikipedia.org/wiki/Tent_map) instead of "Logistic map"
  - [ ] use the "[hyperbolic tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions) map" instead of "Logistic map".

* [ ] the 2D plot from the derivative of the process: <img src="https://render.githubusercontent.com/render/math?math=(x,y)=(dX_{t}, dX_{t %2B 1})">

* [ ] List other chaotic systems
  - [ ] [Arnold tongue](https://en.wikipedia.org/wiki/Arnold_tongue)
  - [ ] double-rod pendulum
  - [ ] Lorenz attractor 
  - [ ] Mobility VS time of blue/red cars from [here](https://en.wikipedia.org/wiki/Chaos_theory)
  - [ ] [Three-body problem](https://en.wikipedia.org/wiki/Three-body_problem)

* [ ] [dynamic mode decomposition](https://en.wikipedia.org/wiki/Dynamic_mode_decomposition)

* [ ] ? predicting chaos ("Although, 3-body is rather a simpler chaotic system" -Adam) "[Newton vs the machine: solving the chaotic three-body problem using deep neural networks](https://arxiv.org/abs/1910.07291)"
* [ ] ? stochastic chaos

## References
https://en.wikipedia.org/wiki/Arnold_tongue#Standard_circle_map
