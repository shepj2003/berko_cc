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
t = np.arange(0.0, 40, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th11 = 120.0
w11 = 0.0
th12 = -10.0
w12 = 0.0

## TODO adjust the starting positions of the 2nd & 3rd pendulum 
## very very slightly from pendulum 1 
## to see if the 2 diverge
th21 = 120.0 ## starting point of 1st weight
w21 = 0.1 ## speed of 1st weight
th22 = -10.0 ## starting point of 2nd wieght
w22 = 0.0 ## speed of 2nd weight

th31 = 120.0
w31 = 0.0
th32 = -10.0
w32 = 0.5


# initial state
state1 = np.radians([th11, w11, th12, w12])
state2 = np.radians([th21, w21, th22, w22])
state3 = np.radians([th31, w31, th32, w32])

# integrate your ODE using scipy.integrate.
y1 = integrate.odeint(derivs, state1, t)
y2 = integrate.odeint(derivs, state2, t)
y3 = integrate.odeint(derivs, state3, t)

x11 = L1*sin(y1[:, 0])
y11 = -L1*cos(y1[:, 0])
x12 = L2*sin(y1[:, 2]) + x11
y12 = -L2*cos(y1[:, 2]) + y11

x21 = L1*sin(y2[:, 0])
y21 = -L1*cos(y2[:, 0])
x22 = L2*sin(y2[:, 2]) + x21
y22 = -L2*cos(y2[:, 2]) + y21
                 
x31 = L1*sin(y3[:, 0])
y31 = -L1*cos(y3[:, 0])
x32 = L2*sin(y3[:, 2]) + x31
y32 = -L2*cos(y3[:, 2]) + y31

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

## TODO 
## instead of showing the pendulum .. trace the path of 
## the ends of each arm of the pendulum
## line_p1 is for the first arm, line_p2 is for the 2nd arm 

line_p12, = ax.plot([], [], '-', lw=2)
line_p12.set_color(colors[30])

line_p22, = ax.plot([], [], '-', lw=2)
line_p22.set_color(colors[10])

line_p32, = ax.plot([], [], '-', lw=2)
line_p32.set_color(colors[40])

time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
#    line.set_data([], [])
#    line_p1.set_data(], []))
#    line_p2.set_data([], [])
    
    time_text.set_text('')
    return line, time_text


def animate(i):
    
    
    p12_x = [x12[max(0, i-10):i]]
    p12_y = [y12[max(0,i-10):i]]
    line_p12.set_data(p12_x, p12_y)
    
    p22_x = [x22[max(0, i-10):i]]
    p22_y = [y22[max(0,i-10):i]]
    line_p22.set_data(p22_x, p22_y)
                 
    p32_x = [x32[max(0, i-10):i]]
    p32_y = [y32[max(0,i-10):i]]
    line_p32.set_data(p32_x, p32_y)

    
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
interval=200, blit=True, init_func=init)
