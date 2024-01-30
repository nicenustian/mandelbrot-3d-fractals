

# create moidifed mandelbrot fractals in 3d
set params manually or get random fractals
![Uploading voxel_rotation1.gif…]()
![voxel_rotation2](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/af3067ed-9ce8-4885-8452-c5aadae4091a)



# manual

```python
    # Uncomment if you wan to generate fractals with constant params
    # provide lists one value for each fractal
    # size of grid for given fractal
    grids = [64]
    # max tieration for a given pixel
    max_iters = [8]
    # power of the complex number
    powers = [1]
    #abs values for cut off for fractals 
    abs_values = [2]
    # offset in the real space x,y,z
    off = [[0,0,0]]
    # offset in the plotting the fractal
    offset = [[0,0,0]]
    num_voxels = len(grids)
```
# random

```python
    # Uncomment if you wan to generate fractals with random params
    # number of fractals, all fractals would be stack 
    # together with offets provided
    num_voxels = 4
    # size of grid for given fractal
    grids = np.sort(np.random.randint(8, 64, size=num_voxels))
    max_iters = np.random.randint(8, 256, size=num_voxels)
    powers = np.sort(np.random.randint(1, 3, size=num_voxels))
    offset = np.random.randint(0, np.max(grids), size=(num_voxels, 3))
    off = np.random.randint(0, 3, size=(num_voxels, 3))
    abs_values = np.random.randint(1, 2, size=num_voxels)
```

# change Equations

```python
                # valcanic type shapes
                mandelbrot_data[i, j, k] = \
                    mandel(complex(cz*cx*cz, cz*cy*cz), power, max_iter)
                
                # valcanic type shapes
                mandelbrot_data[i, j, k] = \
                    mandel(complex(cz*cx*cz*cz, cz*cy*cz*cz), power, max_iter)

                #symmteric shapes
                #mandelbrot_data[i, j, k] = \
                #    mandel(complex(cx*cy*cz, cz*cx*cy), power, max_iter)
    
                #mandelbrot_data[i, j, k] = \
                #    mandel(complex(cz*cx*cx, cz*cx*cx), power, max_iter)
                
```


