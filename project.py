import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rng

def random_lattice(s,p):
    prob = p
    sites = s

    # %%%%
    n = np.zeros((sites, sites)) #occupied sites
    occupancy = int(prob * (sites - 2) * (sites - 2)) #total clusters
    d = np.zeros((sites, sites))  # number of cluster at each site
    clust = np.zeros(sites * sites) #index tool
    clust_p = np.zeros(sites * sites,dtype=object) #index tool


    # %%%%%%

    # cluster count
    x = 0
    for count in range(occupancy):
        i = int((sites - 2) * rng()) + 1
        j = int((sites - 2) * rng()) + 1
        while n[i, j] > 0:
            i = int((sites - 2) * rng()) + 1 #find an empty site
            j = int((sites - 2) * rng()) + 1

        x = x + 1 #cluster count
        n[i, j] = 1 #mark empty site as now occupied
        d[i, j] = x #assign current cluster count to site
        clust[x] = x #keep order
        clust_p[x] = [i,j]

    #store connected clusters
        if (n[i - 1, j] != 0):
            ind = d[i - 1, j]
            ind = clust[int(ind)] #filled adjacent cluster's assignment value is set to index
            while ind < 0:
                ind = clust[int(-1 * ind)] #find the root index
            if (ind != x):
                clust[int(ind)] = -1 * x #make root value negative of current assignment value

        if (n[i + 1, j] != 0):
            ind = d[i + 1, j]
            ind = clust[int(ind)]
            while ind < 0:
                ind = clust[int(-1 * ind)]
            if (ind != x):
                clust[int(ind)] = -1 * x

        if (n[i, j - 1] != 0):
            ind = d[i, j - 1]
            ind = clust[int(ind)]
            while ind < 0:
                ind = clust[int(-1 * ind)]
            if (ind != x):
                clust[int(ind)] = -1 * x

        if (n[i, j + 1] != 0):
            ind = d[i, j + 1]
            ind = clust[int(ind)]
            while ind < 0:
                ind = clust[int(-1 * ind)]
            if (ind != x):
                clust[int(ind)] = -1 * x

    #making connected values
    clust_f = clust.copy()
    for i in range(len(clust)):
        ind=clust[i]
        while ind < 0:
            ind = clust[int(-1 * ind)]
        ind_f = ind
        ind = clust[i]
        while ind < 0:
            ind = clust[int(-1 * ind)]
            clust_f[int(ind*-1)] = ind_f
        clust_f[i] = ind_f

    v=d.copy()
    for z in range(len(clust_f)):
        ind = clust_p[z]
        if type(ind) == list:
            i,j = ind
            i = int(i)
            j = int(j)
            v[i,j] = int(clust_f[z])
    return v

def e(s, p):
    e_total = int(2 * (s - 1) ** 2 + 2 * (s - 1) - 4 * (s - 1))
    e_occupancy = int(p * (2 * (s - 1) ** 2 + 2 * (s - 1) - 4 * (s - 1)))
    e_list = np.zeros(e_total)
    for count in range(e_occupancy):
        i = int((e_total * rng()))
        while e_list[i] > 0:
            i = int((e_total * rng()))
        e_list[i] = 1
    return e_list

def weighted_average(s):
    total_trials = 50
    occupation_prob_list=np.arange(0.1, 1, 0.01)
    shortest_path_list_f = np.zeros(len(occupation_prob_list))
    percolation_occurence_list_f = np.zeros(len(occupation_prob_list))
    for l in range(total_trials):
        shortest_path_list = []
        percolation_occurence_list = []
        d_weights = rng(2 * (s - 1) ** 2 + 2 * (s - 1) - 4 * (s - 1))
        for j in range(len(occupation_prob_list)):
            Percolation_Occurance = 0
            total_shortest = 0
            for i in range(total_trials):
                e_list = e(s, occupation_prob_list[j])
                rl = random_lattice(s, occupation_prob_list[j])
                rls = s**2
                Common_Elements = set(rl[1, 1:-1]) & set(rl[-2, 1:-1])
                shortest_path = 100
                for n in Common_Elements:
                    if n > 0:
                        for k in range(int(s - 2)):
                            shortest_trial = 100
                            visited = []
                            d_list = [[100]*rls,[-1]*rls]
                            a= int(k+1)
                            b= int(1)
                            c = b*s + a
                            d_list[0][c] = 0
                            queue = [[0,[a,b]]]
                            if rl[a,b] == n:
                                while queue:
                                    if rl[a - 1, b] == n:
                                        temp_c = b*s + a-1
                                        index = int((b - 1) * 2 * (s - 2) + 2 * (a - 1))
                                        if e_list[index] == 1:
                                            if d_list[1][temp_c] == -1:
                                                current_path = d_weights[index] + d_list[0][c]
                                                d_list[0][temp_c] = current_path
                                                d_list[1][temp_c] = c
                                                if [a-1,b] not in visited:
                                                    queue.append([d_list[0][temp_c],[a-1,b]])
                                            else:
                                                prev_node = d_list[1][temp_c]
                                                path = d_list[0][prev_node]
                                                current_path = d_weights[index] + d_list[0][c]
                                                if current_path<path:
                                                    d_list[0][temp_c] = current_path
                                                    d_list[1][temp_c] = c
                                                    if [a - 1, b] not in visited:
                                                        queue.append([d_list[0][temp_c],[a-1,b]])
                                    if rl[a, b + 1] == n:
                                        temp_c = (b + 1) * s + a
                                        index = int((b - 1) * 2 * (s - 2) + 2 * (a - 1) + 1)
                                        if e_list[index] == 1:
                                            if d_list[1][temp_c] == -1:
                                                current_path = d_weights[index] + d_list[0][c]
                                                d_list[0][temp_c] = current_path
                                                d_list[1][temp_c] = c
                                                if [a, b + 1] not in visited:
                                                    queue.append([d_list[0][temp_c], [a, b + 1]])
                                            else:
                                                prev_node = d_list[1][temp_c]
                                                path = d_list[0][prev_node]
                                                current_path = d_weights[index] + d_list[0][c]
                                                if current_path < path:
                                                    d_list[0][temp_c] = current_path
                                                    d_list[1][temp_c] = c
                                                    if [a, b + 1] not in visited:
                                                        queue.append([d_list[0][temp_c], [a, b + 1]])
                                    if rl[a + 1, b] == n:
                                        temp_c = (b) * s + a + 1
                                        index = int((b - 1) * 2 * (s - 2) + 2 * a)
                                        if e_list[index] == 1:
                                            if d_list[1][temp_c] == -1:
                                                current_path = d_weights[index] + d_list[0][c]
                                                d_list[0][temp_c] = current_path
                                                d_list[1][temp_c] = c
                                                if [a + 1, b] not in visited:
                                                    queue.append([d_list[0][temp_c], [a + 1, b]])
                                            else:
                                                prev_node = d_list[1][temp_c]
                                                path = d_list[0][prev_node]
                                                current_path = d_weights[index] + d_list[0][c]
                                                if current_path < path:
                                                    d_list[0][temp_c] = current_path
                                                    d_list[1][temp_c] = c
                                                    if [a + 1, b] not in visited:
                                                        queue.append([d_list[0][temp_c], [a + 1, b]])
                                    if rl[a, b - 1] == n:
                                        temp_c = (b - 1) * s + a
                                        index = int((b - 2) * 2 * (s - 2) + 2 * (a - 1) + 1)
                                        if e_list[index] == 1:
                                            if d_list[1][temp_c] == -1:
                                                current_path = d_weights[index] + d_list[0][c]
                                                d_list[0][temp_c] = current_path
                                                d_list[1][temp_c] = c
                                                if [a, b - 1] not in visited:
                                                    queue.append([d_list[0][temp_c], [a, b - 1]])
                                            else:
                                                prev_node = d_list[1][temp_c]
                                                path = d_list[0][prev_node]
                                                current_path = d_weights[index] + d_list[0][c]
                                                if current_path < path:
                                                    d_list[0][temp_c] = current_path
                                                    d_list[1][temp_c] = c
                                                    if [a, b - 1] not in visited:
                                                        queue.append([d_list[0][temp_c], [a, b - 1]])
                                    queue_list = []
                                    for q in range(len(queue)):
                                        queue_list.append(queue[q][0])
                                        queue_min = min(queue_list)
                                        queue_i = queue_list.index(queue_min)
                                    pop = queue.pop(int(queue_i))
                                    visited.append(pop[1])
                                    a, b = pop[1]
                                    a = int(a)
                                    b = int(b)
                                    c = b*s + a
                                    if b == s - 2:
                                        shortest_trial = d_list[0][c]
                                        if shortest_trial<shortest_path:
                                            shortest_path = shortest_trial
                                            break
                if shortest_path != 100:
                    Percolation_Occurance+=1
                    total_shortest += shortest_path
            avg_shortest = total_shortest/total_trials
            shortest_path_list = np.append(shortest_path_list,avg_shortest)
            Percolation_Probability = Percolation_Occurance/total_trials
            percolation_occurence_list = np.append(percolation_occurence_list, Percolation_Probability)
        max_path = max(shortest_path_list)
        shortest_path_list = shortest_path_list/max_path
        shortest_path_list_f += shortest_path_list
        percolation_occurence_list_f += percolation_occurence_list
    shortest_path_list_f = shortest_path_list_f/total_trials
    percolation_occurence_list_f =percolation_occurence_list_f/total_trials
    return shortest_path_list_f,percolation_occurence_list_f

occupation_prob_list=np.arange(0.1, 1, 0.01)
shortest_path_list = np.zeros(len(occupation_prob_list))
percolation_occurence_list = np.zeros(len(occupation_prob_list))

simulation1 = weighted_average(5)
simulation2 = weighted_average(10)
simulation3 = weighted_average(15)

percolation_occurence_list1 = simulation1[1]
percolation_occurence_list2 = simulation2[1]
percolation_occurence_list3 = simulation3[1]

shortest_path_list1 = simulation1[0]
shortest_path_list2 = simulation2[0]
shortest_path_list3 = simulation3[0]

fig, ax = plt.subplots()
ax.plot(occupation_prob_list,percolation_occurence_list1,label='Lattice Size 5')
ax.plot(occupation_prob_list,percolation_occurence_list2,label='Lattice Size 10')
ax.plot(occupation_prob_list,percolation_occurence_list3,label='Lattice Size 15')
ax.set_xlabel('Occupation Probability')
ax.set_ylabel('Percolation Probability')
ax.set_title('Percolation vs Occupation Probability')
ax.legend()
plt.show()

fig2, ay = plt.subplots()
ay.plot(occupation_prob_list,shortest_path_list1,label='Lattice Size 5')
ay.plot(occupation_prob_list,shortest_path_list2,label='Lattice Size 10')
ay.plot(occupation_prob_list,shortest_path_list3,label='Lattice Size 15')
ay.set_xlabel('Occupation Probability')
ay.set_ylabel('Normalized Path Length')
ay.set_title('Normalized Path Length vs Occupation Probability')
ay.legend()
plt.show()


