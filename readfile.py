import numpy as np

def readfile(filename):
    file = open(filename, "r")

    # Repeat for each song in the text file
    a = []
    for line in file:
  
        if line.startswith("#"):
            continue
        elif len(line.strip()) == 0:
            continue
        else:
            a.append(line.strip())

    file.close()
    gamma = float(a[1])
    noise = a[2].split(', ')
    grid = a[3:]
    noise_value = np.zeros(4,dtype=float)
    for i,data in enumerate(noise):
        noise_value[i]=  float(data)

    # To generate grid array
    gridworld = []
    for i in range(len(grid)):
        b = []
        c = grid[i].split(',')
        for j in range(len(c)):
            b.append(c[j])
        gridworld.append(b)

    return gamma,noise_value,gridworld

