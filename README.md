# learnsaxs
This project includes several notebooks and a small library to help you learn SAXS with Python in Jupyter,
which cover the following subjects:
  * viewing electron density voxels of an ellipsoid in 3D real space
  * Fourier transform of the voxel values into the reciprocal space
  * spherically averaging in the reciprocal space
  * which produces a detector image and a scattering curve
as shown in the figure below.

<img src="images/detector.png">

The notebooks are designed to use a minimum number of libraries, i.e.,

  * numpy
  * matplotlib
  * learnsaxs

the last of which, "learnsaxs", is provided here to include following few functions

  * draw_voxles_as_dots
  * get_detector_info
  * draw_detector_image

to make the notebook examples as concise as possible.

You can install the learnsaxs package using pip command as follows.

```
pip install learnsaxs
```

Hoping this may be of any help.
