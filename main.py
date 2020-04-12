import numpy as np
from gridworld import grid_mat, print_policy ,print_values, all_actions_ingrid, all_rewards_ingrid
from value_iteration_p3 import value_iteration
from policy_iteration_p3 import policy_iteration
from readfile import readfile
import time


if __name__ == '__main__':

    # Enter the file name for which you want to excute value and policy iteration.
    gamma, noise, gridworld = readfile("Input/i3.txt")
    gridworld = np.asarray(gridworld)
    all_actions = all_actions_ingrid(gridworld)
    all_rewards = all_rewards_ingrid(gridworld)
    grid = grid_mat(all_actions, all_rewards)


    #Value Iteration
    start = time.time()
    V,policy = value_iteration(grid,gamma,noise)
    end = time.time()

    print("Values:")
    print_values(V, gridworld.shape)
    print("Policy:")
    print_policy(policy, gridworld.shape)
    print("Runtime of Value iteration", end-start)

    #Policy Iteration
    start = time.time()
    V, policy = policy_iteration(grid, gamma, noise)
    end = time.time()

    print("Values:")
    print_values(V, gridworld.shape)
    print("Policy:")
    print_policy(policy, gridworld.shape)
    print("Runtime of Policy iteration",end-start)