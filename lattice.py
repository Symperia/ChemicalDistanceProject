import numpy as np
from numpy.random import random as rng

def random_lattice(s,p):
    prob = p
    sites = s

    n = np.zeros((sites, sites)) #occupied sites
    occupancy = int(prob * (sites - 2) * (sites - 2)) #total clusters
    d = np.zeros((sites, sites))  # number of cluster at each site
    clust = np.zeros(sites * sites) #index tool
    clust_p = np.zeros(sites * sites,dtype=object) #index tool

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