import  matplotlib.pyplot as plt
import numpy as np

def mandelbrot(width, height, x_lim = (-2.3, 1), y_lim = (-1.4, 1.4), max_iterations = 30) :
    m = height # Height of plot
    n = width # Width of plot
    values_real = np.linspace(x_lim[0], x_lim[1], n).reshape((1,n))
    values_imag = np.linspace(y_lim[0], y_lim[1], m).reshape((m,1))
    initial_values = values_real + values_imag*1j
    initial_values
    values = initial_values
    iterations = np.ones(initial_values.shape) * max_iterations
    for i in range(max_iterations) :
        values = values**2 + initial_values
        divergent = values * np.conjugate(values) > 4
        divergent = divergent & (iterations == max_iterations) # Test that we haven't already found this number
        iterations[divergent] = i
    return iterations

x = mandelbrot(500, 500)

## TODO 
## 1. comment out the line above
## 2. uncomment the the line below : x = mandelbrot(...)
## 3. set the values of the variables, R, X, Y
## using the values from http://www.cuug.ab.ca/dewara/mandelbrot/Mandelbrowser.html
## 4. set the value COLMAP
## using values from https://matplotlib.org/tutorials/colors/colormaps.html
## 5. set the value MAX_ITER. 
## good values are between 100 and 1000
## Bigger number takes longer time but will show more detail
## 7. run the code

R = 6.5E-4
X = -0.7453
Y = 0.1127
MAX_ITER = 500
COLMAP = plt.cm.hsv
## x = mandelbrot_data = mandelbrot(600, 600, (X-R,X+R ), (Y-R,Y+R),max_iter)
plt.imshow( x, cmap=plt.cm.hsv) 
