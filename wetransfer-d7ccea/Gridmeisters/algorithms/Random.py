import models.battery
import models.cables
import models.house
import models.load_data
from . import helper
import random
import matplotlib.pyplot as plt
from matplotlib import style

# read in all data
reader = models.load_data.Load_data()
batteries = reader.load_batteries()
houses = reader.load_houses()

def random_algorithm():
    """
    Connects each house randomly to a battery
    """

    random.shuffle(houses)
    random.shuffle(batteries)

    total_costs = 0

    for house in houses:

        for battery in batteries:

            curr_batt = random.choice(batteries)

            if house not in curr_batt.houses_to_battery:

                if house.maxoutput <= curr_batt.capacity:

                    battery.connect_house(house)
                else:
                    continue


def plot_random_algorithm():
    """
    Plots the cables, houses and batteries for the Random algorithm
    """
    
    i = -1

    for battery in batteries:
        i += 1
    
        for house in battery.houses_to_battery:

            colors = ['c', 'k', 'b', 'g', 'r']

            cutt_point_x = house.x
            cutt_point_y = battery.y

            x = [house.x, cutt_point_x, battery.x]
            y = [house.y, cutt_point_y, battery.y]

            plt.plot(x,y, color= colors[i])

            ax = plt.subplot()

            houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
            batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

            fig = plt.savefig("randomfigure.png")
    return fig


