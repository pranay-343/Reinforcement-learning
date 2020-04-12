import numpy as np
from gridworld import initialise_grid, initialise_policy


def optimal_policy(grid,gamma,noise,V):
    # find a policy that leads to optimal value function

    Directions = ['U', 'D', 'L', 'R']
    policy = initialise_policy(grid, Directions)

    for index in grid.actions:
        best_dir = None
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
            for i, a2 in enumerate(Directions):  # resulting action
                p1 = p[i]
                r, current_state = grid.get_ajacent_move(Directions[i], index)
                v += p1 * (gamma * V[current_state])
            if v > best_value:
                best_value = v
                best_dir = dir
        policy[index] = best_dir

    return policy

def value_iteration(grid,gamma,noise):

  convergence_point = 0.001
  gamma = gamma
  Directions = ['U', 'D', 'L', 'R']

  V = initialise_grid(grid)
  # repeat until convergence
  while True:
    value_change = 0
    for index in grid.actions:
      prev_v = V[index]
      new_v = float('-inf')
      # V(s) only has value if it's not a terminal state
      for j, a in enumerate(Directions):  # chosen action
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
          for i, a2 in enumerate(Directions):  # resulting action
              p1 = p[i]
              r, current_state = grid.get_ajacent_move(Directions[i], index)
              v += p1 * (gamma * V[current_state])

          new_v = max(new_v,v)

      V[index] = new_v
      value_change = max(value_change, np.abs(prev_v - V[index]))

    # Loop breaking condition when Convergence achieved
    if value_change < convergence_point:
      break

  # Optimal Policy Extraction
  policy = optimal_policy(grid,gamma,noise,V)

  return V,policy

