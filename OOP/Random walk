import random
from math import *
from Particle import *


def cekTotalInside(arr_particle):
    jum = 0
    for i,particle in enumerate(arr_particle):
        if(particle.isInside==1):
            jum = jum + 1
    return jum

def raise_random():
    arr_r = []
    for i in range(5):
        arr_r.append( random.uniform(0,1) )
    return arr_r

def initialize_position(r1,r2,r3,a):
    x = r1 * a
    y = r2 * a
    z = r3 * a
    return Position(x,y,z)

def next_position(particle,delta_t):
    x = particle_position.x +  particle.velocity.vx * delta_t
    y = particle_position.y + particle.velocity.vy * delta_t
    z = particle_position.z + particle.velocity.vz * delta_t
    return Position(x,y,z)

def update_position(particle,delta_t,a,ring):

    isStop = 0
    isOut = 0
    new_position = next_position(particle,delta_t)

    while(isStop==0 and isOut==0):

        [new_position_old, delta_position_new ] = checkBoundary(new_position.x,new_position.y,new_position.z,a)

        if(abs(delta_position_new.x) + abs(delta_position_new.y )+ abs(delta_position_new.z) > 0 ):
            # Wall Hit
            cek_wall_flag = [0,0,0]
            if(delta_position_new.x > 0):
                

                new_position_old.x = new_position_old.x - abs(delta_position_new.x)
                cek_wall_flag[0] = 1

            if(delta_position_new.y > 0 ):
                # hit wall perpendicuar to y
                cek_wall_flag[1] = 1

            if(delta_position_new.z > 0):
                # hit wall perpendicuar to z
                new_position_old.z = new_position_old.z - abs(delta_position_new.z)
                cek_wall_flag[2] = 1

            if( cek_wall_flag[1] == 1 and new_position_old.y ==a):
               
                if(isInHole(ring,new_position_old)==1):
                    # if in the hole
                    particle.isInside = 0
                    isOut = 1

                new_position_old.y = new_position_old.y - abs(delta_position_new.y)

            new_position = new_position_old

        else:
            isStop = 1

    particle.position = new_position

def update_position2(particle,delta_t,a,ring):
    candidate_new_position = next_position(particle, delta_t)
    [new_position_temp, wall_flag,wall_hit] = checkBoundary(candidate_new_position.x, candidate_new_position.y, candidate_new_position.z, a)

    if(wall_hit==1):

        if( wall_flag[0]==1 or wall_flag[0]==2):
            # hit wall perpendicuar to x
            particle_position = particle_position.x
            position_temp = new_position_temp.x
            particle_speed = particle.velocity.vx
            axis_update = 'x'
        elif(wall_flag[1]==1 or wall_flag[1]==2):
            # hit wall perpendicuar to y
            particle_position = particle_position.y
            position_temp = new_position_temp.y
            particle_velocity = particle.velocity.vy
            axis_update = 'y'
        elif(wall_flag[2]==1 or wall_flag[2]==2):
            # hit wall perpendicuar to z
            particle_position = particle_position.z
            position_temp = new_position_temp.z
            particle_velocity = particle.velocity.vz
            axis_update = 'z'

        if (isInHole(ring, new_position_temp) == 1 and wall_flag[1]==2):
            # is it in the hole?
            particle.isInside = 0
        else:
            # its in the wall
            delta_t_to_wall = (position_temp - particle_position) / particle_velocity
            remainder_delta_t = delta_t - delta_t_to_wall
            position_in_wall = next_position(particle, delta_t_to_wall)
            v_baru = particle_velocity * -1

            if(axis_update=='x'):
                vbaru = Velocity(v_baru, particle.velocity.vy, particle.velocity.vz)
            elif(axis_update=='y'):
                vbaru = Velocity(particle.velocity.vx, v_baru, particle.velocity.vz)
            elif(axis_update=='z'):
                vbaru = Velocity(particle.velocity.vx, particle.velocity.vy, v_baru)

            particle_position = position_in_wall
            particle.velocity = vbaru
            new_position = next_position(particle, remainder_delta_t)
            particle_position = new_position

    else:
        particle_position = candidate_new_position


def generate_Velocity(v,r1,r2):
    m = 2 * pi * r1
    kos_t = 1 - 2 * r2
    sin_t = sqrt( 1 - kos_t**2 )

    vx = v * sin_t * cos(m)
    vy = v * sin_t * sin(m)
    vz = v * kos_t
    return Velocity(vx,vy,vz)

def iinitialize_particle(N,a,v,arr_r):
    arr_particle = []
    for i in range(N):
        position = initialize_position( arr_r[0], arr_r[1],arr_r[2],a )
        Velocity = generate_velocity(v,arr_r[3],arr_r[4])
        p = Particle(position,velocity)
        arr_particle.append(p)
    return arr_particle


def checkBoundary(x, y, z, a):
    xnew = x
    ynew = y
    znew = z
    wall_flag = [0,0,0]
    isHitwall = 0

    if (x < 0):
        xnew = 0
        wall_flag[0] = 1
        isHitwall = 1

    if (x > a):
        xnew = a
        wall_flag[0] = 2
        isHitwall = 1

    if (y < 0):
        ynew = 0
        wall_flag[1] = 1
        isHitwall = 1

    if (y > a):
        ynew = a
        wall_flag[1] = 2
        isHitwall = 1

    if (z < 0):
        znew = 0
        wall_flag[2] = 1
        isHitwall = 1

    if (z > a):
        znew = a
        wall_flag[2] = 2
        isHitwall = 1

    return [Posisi(xnew, ynew, znew), wall_flag, isHitwall ]

def isInHole(ring,position):
    r = ring.r
    px = position.x
    pz = position.z

    dist_l_to_position = sqrt( (px-ring.a)**2 + (pz-ring.b)**2  )
    if( dist_l_to_position <= r ):
        return 1
    else:
        return 0






