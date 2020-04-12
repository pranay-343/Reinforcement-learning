import numpy as np
from gridworld import initialise_grid, initialise_policy

def policy_iteration(grid,gamma,noise):

  convergence_point = 0.001
  Directions = ['U', 'D', 'L', 'R']

  policy = initialise_policy(grid, Directions)
  V = initialise_grid(grid)

  # repeat until convergence - will break out when policy does not change
  while True:

    # policy evaluation step
    while True:
      biggest_change = 0
      for index in grid.actions:
        old_v = V[index]

        # V(s) only has value if it's not a terminal state
        new_v = 0
        j = policy[index]
        # Noise/probability values for each preferred actions
        if j == 'U':
            p = [noise[0], noise[1], noise[2], noise[3]]
        if j == 'D':
            p = [noise[3], noise[0], noise[1], noise[2]]
        if j == 'L':
            p = [noise[2], noise[3], noise[0], noise[1]]
        if j == 'R':
            p = [noise[1], noise[2], noise[3], noise[0]]
        for i, a in enumerate(Directions):
            p1 = p[i]
            r, current_state = grid.get_ajacent_move(Directions[i], index)
            new_v += p1 * (gamma * V[current_state])
        V[index] = new_v

        biggest_change = max(biggest_change, np.abs(old_v - V[index]))

      # Loop breaking condition when Convergence achieved
      if biggest_change < convergence_point:
        break

    # policy improvement step
    is_policy_converged = True
    for index in grid.actions:
        old_dir = policy[index]
        new_dir = None
        best_value = float('-inf')
        # loop through all possible actions to find the best current action
        for j, dir in enumerate(Directions):  # chosen action
            v = 0
            # Noise/probability values for each preferred actions
            if j == 0:
                p = [noise[0], noise[1], noise[2], noise[3]]
            if j == 1:
                p = [noise[3], noise[0], noise[1], noise[2]]
            if j == 2:
                p = [noise[2], noise[3], noise[0], noise[1]]
            if j == 3:
                p = [noise[1], noise[2], noise[3], noise[0]]
            for i, dir_2 in enumerate(Directions):  # resulting action
                p1 = p[i]
                r, current_state = grid.get_ajacent_move(Directions[i], index)
                v += p1 * (gamma * V[current_state])
            if v > best_value:
                best_value = v
                new_dir = dir
        policy[index] = new_dir
        if new_dir != old_dir:
            is_policy_converged = False

    if is_policy_converged:
      break

  return V,policy