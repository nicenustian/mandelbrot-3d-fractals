import numpy as np
from numba import jit
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import animation
import numba as nb


font = {'family' : 'serif', 'weight' : 'normal','size' : 34}
matplotlib.rc('font', **font)


@jit(nopython=True)
def mandel(c, power, abs_value, max_iters=10):
    """
    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a fixed number of iterations.
    """
    i = 0
    z = 0.0j
    for i in range(max_iters):
        z = z**power + c
        if np.abs(z) >= abs_value:
            return i

    return 0

@jit(nopython=True)
def mandelbrot_set(grid, off, power, abs_value, max_iter, val=1):
    """
    Create a 3D Mandelbrot set.
    """
    
    width, height, depth = grid, grid, grid
    xmin, xmax, ymin, ymax, zmin, zmax, = -val,val,-val,val,-val,val
    
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    z = np.linspace(zmin, zmax, depth)
    
    mandelbrot_data = np.zeros((width, height, depth))
    
    
    for i in range(width):
        for j in range(height):
            for k in range(depth):
                cx = x[i] + off[0]
                cy = y[j] + off[1]
                cz = z[k] + off[2]
                
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
                

    return mandelbrot_data


# Function to update the azimuth angle
def update_azimuth(frame):
    ax.view_init(elev=30, azim=frame)

if __name__ == "__main__":
    
    make_animation = False

    # # Uncomment if you wan to generate fractals with constant params
    # # provide lists one value for each fractal
    # # size of grid for given fractal
    # grids = [64]
    # # max tieration for a given pixel
    # max_iters = [8]
    # # power of the complex number
    # powers = [1]
    # #abs values for cut off for fractals 
    # abs_values = [2]
    # # offset in the real space x,y,z
    # off = [[0,0,0]]
    # # offset in the plotting the fractal
    # offset = [[0,0,0]]
    # num_voxels = len(grids)

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

    # Create Mandelbrot fractals with random shifts
    fractals = []

    for si, origin in enumerate(grids):
        print("fractal #", si+1)
        frac = mandelbrot_set(grids[si], off[si], powers[si], abs_values[si], max_iters[si])
        fractals.append(frac)
        print("done fractal #", si+1)
    
    # Plotting
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')    
    
    for si, grid in enumerate(grids):
    
        print("plotting fractal #", si+1)
        
        # Custom coordinates for grid
        x,y,z = np.indices((grid+1,grid+1,grid+1))
        x += offset[si][0]
        y += offset[si][1]
        z += offset[si][2]
        
        fractals_colors = fractals[si].astype(np.float32) / np.max(fractals[si])
        #colors = plt.cm.plasma(fractals_colors)
        colors = plt.cm.magma(fractals_colors)
        ax.voxels(x,y,z, fractals[si], facecolors=colors,
                  shade=True, rasterized=True, alpha=.8)
        
        print("done plotting fractal #", si+1)
    
        # Remove the axes
        ax.set_axis_off()
        # Set background color to black
        ax.set_facecolor('black')
        # Adjust layout to make plot elements fit within the figure without overlapping
        plt.tight_layout()  
        
        # # Save frames as images
        filename = 'mandel_N'+str(grids[si])+'_pow'+str(powers[si])+'_val'+str(abs_values[si])+'_iter'+str(max_iters[si])+'_off'+str(off[si])
        
    if make_animation:
        # Animation
        ani = animation.FuncAnimation(fig, update_azimuth, frames=np.arange(0, 360, 5), interval=50)
        ani.save(filename+'voxel_rotation.gif', writer='pillow')
    
    plt.savefig(filename+'.jpg', format='jpg')
    plt.show()
