# Coordinate Transformations
A playground for conversion and visualization of spatial transformations.

## Usage
```bash
pip install -r requirements.txt
python main.py -h
```

## Road Map
* tracer code - iteration 0 - visualizer backbone:
    ```
    original   | rotation   | trans
    full tform | similarity | rigid
    ```

* tracer code - iteration 1 - vanilla transformation:
    - draw a reference coordinate frame (RCF)
    - construct a coordinate frame w.r.t RCF representing a 6DOF pose (pose coordinate frame PCF)
    - draw PCF w.r.t RCF
    - construct an affinity matrix object (AMO) from (t,r,s) 
    - illustrate the motion of PCF under AMO (in one frame to two frames?)

* extend transformations:
  test each time it by visualizing the transformation of PCF/PCO
    - construct an unit quaternion rotation object,
    - rotation format conversion: euler, axis angle, and unit quaternion
    - construct an unit double quaternion transformation object
    - transformation format conversion: matrix to unit dual quaternion

* tracer code - iteration 2 - extend object of transform from coordinate frame to data:
    - synthesize a point cloud object (PCO) with a recognizable shape that can uniquely be expressed with 6D pose (like a bunny or a pot?)
    - draw PCO w.r.t RCF
    - construct an affinity matrix object
    - illustrate the motion of PCF under AMO

## Laundry list:
* [ ] data vs frame transformation
* [ ] transformation composition
* [ ] A2B : C2B x A2C
* [ ] quaternion can be interpolated, draw transformation as a "trajectory"
* [ ] intrinsic vs extrinsic rotation
      see General rotations in [Rotation_matrix](https://en.wikipedia.org/wiki/Rotation_matrix)
* [ ] implicit (T after R) and explicit (T and R together) transformation?

* [ ] https://en.wikipedia.org/wiki/3D_rotation_group
* [ ] Lie algebra correspondence
* [ ] nonlinear piece-wise transformation?
* [ ] 2D?

