from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of walk"""
        self.num_points = num_points

        #walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        
        direction = choice([1, -1])
        distance = choice([1,2,3,4])

        return distance * direction

        
    def fill_walk(self):
        """Calculate all points in a walk"""

        #Keep taing steps until the walk reaches the desired legth
        while len(self.x_values) < self.num_points:
            
            #decide which direction to go to and how far to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject non motion

            if x_step == 0 and y_step == 0:
                continue
            
            # Calc the new pos
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            

# Make random walk
while True: 
    rw = RandomWalk(50_00)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)

    ax.plot(rw.x_values, rw.y_values, linewidth = 1)
    ax.plot(0, 0, c='green')
    ax.plot(rw.x_values[-1], rw.y_values[-1])
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (yn)?')
    if keep_running == 'n':
        break