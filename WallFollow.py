import gridworld
from gridworld import *
from agent import *

class WallFollow(Agent):

    def __init__(self, gw):
        Agent.__init__(self, gw)
        self.blocked = gw.scan(self.state)

    def turn_left(self):
        self.heading = self.gw.left(self.heading)

    def turn_right(self):
        self.heading = self.gw.right(self.heading)

    def do_step(self, S, act, logfile=None):
        Agent.do_step(self, S, act)
        blocked = self.gw.scan(self.state);

        if (not(blocked[self.gw.left(self.heading)])):
            R, Sp = act(gridworld.LEFT)
        elif not(blocked[self.gw.front(self.heading)]):
            R, Sp = act(gridworld.UP)
        elif not (blocked[self.gw.right(self.heading)]):
            R, Sp = act(gridworld.RIGHT)
        else:
            R, Sp = act(gridworld.DOWN)

        self.G += R
