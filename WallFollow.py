from agent import *

FORWARD, FORWARD_RIGHT, RIGHT, BACK_RIGHT, BACK, BACK_LEFT, LEFT, FORWARD_LEFT = range(8)

dirn = [1, 0, 0, 0, 3, 0, 2, 0]

class WallFollow(Agent):

    def reset(self):
        Agent.reset(self)
        self.heading = 0
        self.finding_wall = False
        self.blocked = self.gw.scan(self.state)
        print(f'{self.state}: {self.blocked}', end= '        ')
        self.sonar = self.blocked[self.heading:] + self.blocked[:self.heading]
        print(f'{self.heading}: {self.sonar}')

    def turn_left(self):
        self.heading = self.gw.left(self.heading)

    def turn_right(self):
        self.heading = self.gw.right(self.heading)

    def do_step(self, S, act, logfile=None):
        Agent.do_step(self, S, act)

        if self.sonar[LEFT] > 0 and not self.finding_wall:
            self.heading = (self.heading - 2) % 8       # Turn left
            self.finding_wall = True
            print("Turn left")
        elif self.sonar[LEFT] > 0 and self.sonar[BACK_LEFT] == 0:
            self.heading = (self.heading - 2) % 8       # Turn left
            print("Turn left")
        elif self.sonar[FORWARD] > 0:
            self.heading = self.heading                 # Keep going in same direction
            print("Go straight")
        elif self.sonar[FORWARD] == 0:
            self.heading = (self.heading + 2) % 8       # Turn right
            self.finding_wall = False
            print("Turn right")
        elif self.sonar[LEFT] == 0:
            self.heading = (self.heading + 2) % 8       # Turn right
            print("Turn right")

        R, Sp = act(dirn[self.heading])
        self.G += R

        self.blocked = self.gw.scan(self.state)
        print(f'{S}: {self.blocked}', end='        ')
        self.sonar = self.blocked[self.heading:] + self.blocked[:self.heading]
        print(f'{self.heading}: {self.sonar}')

