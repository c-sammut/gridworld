from gridworld import *
from agent import *

class WallFollow(Agent):

    def __init__(self, state_count):
        Agent.__init__(self, state_count)
        self.dirn = gridworld.N
        self.blocked = GridWorld.scan(GridWorld)

    def do_step(self, S, act, logfile=None):
        Agent.do_step(self, S, act)
        blocked = GridWorld.scan(GridWorld);

        if (not(blocked[self.left(self.dirn)])):
            R, Sp = act(GridWorld.turn(GridWorld.left(self.dirn)))
        elif not(blocked[self.front(self.dirn)]):
            R, Sp = act(GridWorld.move(GridWorld.front(self.dirn)))
        else:
            R, Sp = act(GridWorld.turn(GridWorld.right(self.dirn)))

        self.G += R
