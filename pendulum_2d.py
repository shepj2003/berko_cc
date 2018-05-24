"""
copied from matplotlib animation examples
https://matplotlib.org/gallery/animation/double_pendulum_sgskip.html
"""


from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from matplotlib.colors import cnames

## need the line below tomake the animation work in jupyter
%matplotlib nbagg

## TODO 
## investigate the effect of changing the lengths & weights of each part of the pendulum
## investigate changing gravity

G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg

## TODO 
## change the colour scheme 
## https://matplotlib.org/users/colormaps.html
colors = plt.cm.jet(np.linspace(0, 1, 50))

def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1

    dydx[2] = state[3]

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2

    return dydx

# create a time array from 0..100 sampled at 0.05 second steps
dt = 0.05
t = np.arange(0.0, 20, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate your ODE using scipy.integrate.
y = integrate.odeint(derivs, state, t)

x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

## TODO 
## instead of showing the pendulum .. trace the path of 
## the ends of each arm of the pendulum
## line_p1 is for the first arm, line_p2 is for the 2nd arm 

line, = ax.plot([], [], 'o-', lw=2)
#line_p2, = ax.plot([], [], '-', lw=1)
#line_p1, = ax.plot([], [], '-', lw=1)

time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
#    line.set_data([], [])
#    line_p1.set_data(], []))
#    line_p2.set_data([], [])
    
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    
    p2_x = [x2[:i]]
    p2_y = [y2[:i]]
    
    p1_x = [x1[:i]]
    p1_y = [y1[:i]]
    

    line.set_data(thisx, thisy)
    line.set_color(colors[i%50])
    
#    line_p2.set_data(p2_x, p2_y)
#    line_p2.set_color(colors[30])
    
#    line_p1.set_data(p1_x, p1_y)
#    line_p1.set_color(colors[20])


    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
interval=200, blit=True, init_func=init)

