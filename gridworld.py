import numpy as np


class Grid:  # Environment
    def __init__(self,start_i,start_j):

        self.i = start_i
        self.j = start_j

    def set(self, rewards, actions):
        self.rewards = rewards
        self.actions = actions

    def get_ajacent_move(self, dir,index):

        self.i = index[0]
        self.j = index[1]

        if dir in self.actions[(self.i, self.j)]:
            if dir == 'U':
                self.i -= 1
            elif dir == 'D':
                self.i += 1
            elif dir == 'R':
                self.j += 1
            elif dir == 'L':
                self.j -= 1

        current_state = (self.i, self.j)
        if self.rewards.get((self.i, self.j)) == None:
            return 0,current_state
        else:
            return self.rewards.get((self.i, self.j)),current_state


    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())


#For getting all possible legal actions
def all_actions_ingrid(gridworld):
    all_actions = {}
    x_coor, y_coor = np.where(gridworld == 'X')
    for index in range(0, len(x_coor)):
        a = []
        if y_coor[index] + 1 < len(gridworld):
            a.append("R")
        if y_coor[index] - 1 >= 0:
            a.append("L")
        if x_coor[index] - 1 >= 0:
            a.append("U")
        if x_coor[index] + 1 < len(gridworld):
            a.append("D")
        all_actions[(x_coor[index], y_coor[index])] = tuple(a)

    return all_actions

#For getting all  Terminal state
def all_rewards_ingrid(gridworld):
    all_rewards = {}
    x_coor, y_coor = np.where(gridworld != 'X')
    for index in range(0, len(x_coor)):
        all_rewards[(x_coor[index], y_coor[index])] = int(gridworld[x_coor[index]][y_coor[index]])

    return all_rewards

#Initialising a gridworld
def grid_mat(all_actions,all_rewards):

    g = Grid(0,2)
    g.set(all_rewards, all_actions)
    return g

def initialise_grid(grid):
    V = {}
    states = grid.all_states()
    for index in states:
        # V[s] = 0
        if index in grid.actions:
            V[index] = 0
        else:
            # terminal state
            V[index] = grid.rewards.get(index)

    return V

def initialise_policy(grid,directions):
    policy = {}
    states = grid.all_states()
    for s in states:
        if s in grid.actions:
            policy[s] = np.random.choice(directions)
        else:
            policy[s] = grid.rewards.get(s)
    return policy

#To print values and policy
def print_values(V, g):
    for i in range(g[0]):
        print("----------------------------------------------")
        for j in range(g[1]):
            v = V.get((i, j))
            if v >= 0:
                print(" %.2f|" % v, end="")
            else:
                print("%.2f|" % v, end="")
        print("")

def print_policy(P, g):
  for i in range(g[0]):
    print("----------------------------------------------")
    for j in range(g[1]):
      a = P.get((i,j), ' ')

      if a == 'R':
          print("  \u2192   |", end="")
      elif a == 'L':
          print("  \u2190   |", end="")
      elif a == 'U':
          print("  \u2191   |", end="")
      elif a == 'D':
          print("  \u2193   |", end="")
      else:
          print("  %s  |" % a, end="")

    print("")

