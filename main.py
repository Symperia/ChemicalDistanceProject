import numpy as np
import matplotlib.pyplot as plt
import pathfinding

occupation_prob_list=np.arange(0.1, 1, 0.01)
shortest_path_list = np.zeros(len(occupation_prob_list))
percolation_occurence_list = np.zeros(len(occupation_prob_list))

simulation1 = pathfinding.weighted_average(5)
simulation2 = pathfinding.weighted_average(10)
simulation3 = pathfinding.weighted_average(15)

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
