

# create moidifed mandelbrot fractals in 3d
set params manually or get random fractals

![voxel_rotation2](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/af3067ed-9ce8-4885-8452-c5aadae4091a)

![voxel_rotation1](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/53a87138-de26-4702-a5ad-5fdcf8423e0d)



![mandel_N58_pow2_val1_iter124_off 2 1 1](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/3f0e11ef-6052-4574-b879-5da59877c156)
![mandel_N51_pow2_val1_iter23_off 0 0 0](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/eb3b6eed-7ccb-4618-90ca-2deddd676bf4)
![mandel_N32_pow2_val1_iter101_off 2 2 0](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/8f7bb45d-21ac-4ccc-82d3-93c8a90d4bcb)
![mandel_N27_pow2_val1_iter188_off 1 0 0](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/90e04ba9-fe68-41c5-9571-4640e8508e96)
![mandel_N64_pow2_val2_iter16_off 1, 0, 1](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/4bdfc373-26e8-4738-92ae-572c9ad18ed8)
![mandel_N128_pow2_val2_iter8_off 1, 0, 1](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/81614712-5e8c-4c31-9ced-fd0d48f396a0)
![mandel_N34_pow2_val1_iter194_off 1 1 0](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/ae94f056-1eac-4a35-b1a8-32f3552ad110)
![mandel_N64_pow2_val2_iter2_off 0, 1, 1](https://github.com/nicenustian/mandelbrot-3d-fractals/assets/111900566/ce57a2ef-d2e0-441a-b2ea-ab29104dd462)

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


