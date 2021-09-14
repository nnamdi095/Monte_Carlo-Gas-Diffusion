from random_walk import *
import matplotlib.pyplot as plt

N = 100
a = 12
v = 6
arr_r = raise_random()
arr_particle = initialize_particle(N,a,v,arr_r)
delta_t = 0.1
t_sim = 5000
step = t_sim / delta_t
z_center = 1/2 * a
x_center = 1.2 * a
r = 3
i = 0
ring = Hole(x_center,z_center,r) 
result = []
t = []

while(i <= step):
    print('t = ' + str(delta_t*(i)) + " ----------")
    for j in range(N):
        if(arr_particle[j].isInside==1):

            update_position2(arr_particle[j],delta_t,a,ring)
            arr_r = raise_random()
            arr_particle[j].velocity = generate_velocity(v,arr_r[3],arr_r[4])
            result.append(cekTotalInside(arr_particle))
            t.append(delta_t*(i))
    # print("remainder: " + str(cekTotalInside(arr_particle))  + " partickle")
    i = i + 1
print(result)
plt.plot(t,result)
plt.show()