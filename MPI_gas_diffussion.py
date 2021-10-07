from random_walk import *
import time
from mpi4py import MPI


def main_parallel(N, a, v, delta_t, t_sim, z_centre, x_centre, r):
    start = time.time()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        N_parallel = (N // (size - 1))
        N_remainder = (N % (size - 1))
        arr_r = make_random()
        step = t_sim / delta_t
        ring = Hole(x_centre, z_centre, r)  
        result = []
        t = []
        p_hist = []
        data = [N, N_parallel, N_remainder, a, v, arr_r, delta_t, t_sim, step, ring, result, t, p_hist]
    else:
        data = None

    data = comm.bcast(data, root=0)
    N = data[0]
    N_parallel = data[1]
    N_remainder = data[2]
    a = data[3]
    v = data[4]
    arr_r = data[5]
    delta_t = data[6]
    t_sim = data[7]
    step = data[8]
    ring = data[9]
    result = data[10]
    t = data[11]
    p_hist = data[12]
    i = 0

    N_particle = None
    if rank == 0:
        N_particle = N_remainder
    else:
        N_particle = N_parallel

    arr_particle = init_particle(N_particle, a, v, arr_r)

    while (i < step):
        for j in range(N_particle):

            if (arr_particle[j].isInside == 1):
                update_position2(arr_particle[j], delta_t, a, ring)
                arr_r = make_random()
                arr_particle[j].velocity = generate_velocity(v, arr_r[3], arr_r[4])

        result.append(TotalInside(arr_particle))
        t.append(delta_t * (i))
        p_hist.append(arr_particle.copy())
        i = i + 1

    result = comm.gather(result, root=0)
    t = comm.gather(t, root=0)
    p_hist = comm.gather(p_hist, root=0)
    end = time.time()
    elapsed = end - start
    if (rank == 0):
        temp = result[0][:]
        for i_ in range(1, len(result)):
            for j_ in range(0, len(result[i_])):
                temp[j_] = temp[j_] + result[i_][j_]
        print('=============== Parallel Result ============')
        print('N initial = ' + str(N))
        print('remainder particle= ' + str(temp[len(temp) - 1]))
        print('time parallel = ' + str(elapsed) + ' s')
        print('=========================================')


# ======================= Parameter sim =======================================================
N = 1000
a = 12
v = 6
delta_t = 0.1
t_sim = 1000
z_centre = 1 / 2 * a
x_centre = 1/2 * a
r = 3
# ==================================================================================================
main_parallel(N, a, v, delta_t, t_sim, z_centre, x_centre, r)