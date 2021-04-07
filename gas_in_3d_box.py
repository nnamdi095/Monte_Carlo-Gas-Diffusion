
import numpy as np
from scipy import random
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d

#Initial Conditions
box_width = 1
P = 1
V = 1
R = 0.082
T = 300
n_particles = int((P*V)/(R*T)*1000)

dt = 1
n_steps = 500



global trajectory

#Get coordinates
def get_initial_coordinate():
    x_coord = np.zeros(n_particles)
    y_coord = np.zeros(n_particles)
    z_coord = np.zeros(n_particles)
    for i in range(n_particles):
        x_coord[i]= random.random()*box_width
        y_coord[i] = random.random()*box_width
        z_coord[i] = random.random()*box_width
    return x_coord, y_coord, z_coord

#Get Velocity
def get_initial_velocity():
    v0 = 10
    r4 = random.random()
    r5 = random.random()

    
    phi = 2*np.pi* r4
    cos_theta = 1-2*r5
    sin_theta = np.sqrt(1 - cos_theta**2)
    
    x_vel = np.zeros(n_particles)
    y_vel = np.zeros(n_particles)
    z_vel = np.zeros(n_particles)
    for i in range(len(x_coord)):
        x_vel[i] = v0*sin_theta
        y_vel[i] = v0*cos_theta*np.sin(phi)
        z_vel[i] = v0*sin_theta
    return x_vel, y_vel, z_vel



x_coord, y_coord, z_coord = get_initial_coordinate()
x_vel, y_vel, z_vel = get_initial_velocity()

# To initialize movement of gas particles with change in time, dt
time = [0]
t0 = 0
for j in range(n_steps):

    for i in range(n_particles):
        x_coord[i] += x_vel[i]*dt
        y_coord[i] += y_vel[i]*dt
        z_coord[i] += z_vel[i]*dt
        
        
        if abs(x_coord[i]) > box_width:
            x_vel[i] = -x_vel[i]
            x_coord[i] += x_vel[i]*dt
            
        
        if abs(y_coord[i]) > box_width:
            y_vel[i] = -y_vel[i]
            y_coord[i] += y_vel[i]*dt
        
        if abs(z_coord[i]) > box_width:
            z_vel[i] = -z_vel[i]
            z_coord[i] += z_vel[i]*dt
            
    t0 += dt
    time.append(t0)
    
# To create a 3D plot of the Gas Particles in the box
fig = plt.figure()

ax = plt.axes(projection="3d")
ax.scatter(x_coord, y_coord, z_coord, c='r', marker = 'o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

#plt.savefig('3d_scatter_plot.jpg')

plt.show()


