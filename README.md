# Chaotic Systems

Python implementation and exprementation with few simplistic chaotic systems.
<!-- Also intended as an scaffold for starting python projects. -->

* Logistic Map: <img src="https://render.githubusercontent.com/render/math?math=x_{t %2B 1}=rx_{t}(x_{t} %2B 1)">  
  <p align="center">
      <img src="https://github.com/saeedghsh/ChaoticSystems/blob/master/animation.gif" width="900">
  </p>

## Usage
```bash
pip install -r requirements.txt
python main.py logisticmap --length 100 --count 500
```
for help:
```bash
python main.py -h
python main.py logisticmap -h
```

## laundry list
* [x] separate parsers for different type of systems (with subparser)

* [x] gererate chaotic processes via logistic maps
  - [ ] reproduce all the plots from [here](https://en.wikipedia.org/wiki/Logistic_map)
    + [x] frequency spectrum
    + [x] [cobweb plot](https://en.wikipedia.org/wiki/Cobweb_plot)
    + [ ] [Bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram)

  - [ ] use [Tent map](https://en.wikipedia.org/wiki/Tent_map) instead of "Logistic map"

* [ ] the 2D plot from the derivative of the process: <img src="https://render.githubusercontent.com/render/math?math=(x,y)=(dX_{t}, dX_{t %2B 1})">

* [ ] List other chaotic systems
  - [ ] [Arnold tongue](https://en.wikipedia.org/wiki/Arnold_tongue)
  - [ ] double-rod pendulum
  - [ ] Lorenz attractor 
  - [ ] Mobility VS time of blue/red cars from [here](https://en.wikipedia.org/wiki/Chaos_theory)


## License
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/ChaoticSystems/blob/master/LICENSE).
```
Copyright (C) Saeed Gholami Shahbandi
```
