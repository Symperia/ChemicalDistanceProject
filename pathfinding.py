import numpy as np
from numpy.random import random as rng
import lattice

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
                e_list = lattice.e(s, occupation_prob_list[j])
                rl = lattice(s, occupation_prob_list[j])
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