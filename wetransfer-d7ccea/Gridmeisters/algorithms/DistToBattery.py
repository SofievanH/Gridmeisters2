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

def first_algorithm():
    """
    Connects each house to the closest battery based on distance
    """
   
    # houses that are currently not being used because the battery is full
    unused_houses = []

    random.shuffle(houses)

    # total costs for the cables
    total_costs = 0

    for house in houses:

        # keeps track of distances between each house and battery
        dist_dict = {}

        # keeps track on wether battery has sufficient capacity
        keep_track = []

        for battery in batteries:

            # costs for all cables connected to the current battery
            battery_costs = 0

            # battery has sufficient capacity
            if battery.status(house) == True:

                # calculate distance between house and battery
                distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])

                # stores distance in dictionary
                dist_dict[battery] = distance

                keep_track.append(1)

            else:
                keep_track.append(0)

        # full battery move on to the next one
        if keep_track.count(1) == 0:
            unused_houses.append(house)

        else:

            # return closest distance of a house to the battery
            closest_distance = min(dist_dict.items(), key=lambda x: x[1])
            closest_battery= closest_distance[0]
            battery = closest_battery

            # define cutting point between battery and house
            route = (house.x, battery.y)

            # connects house to battery and vice versa
            house.connect_to_battery(battery)
            battery.connect_house(house)

            # adds costs of cables for this house to the battery
            house.add_costs(battery)
            battery.add_house_info(house)
            house.route_calc(battery)
            battery_costs += house.costs
            total_costs += battery_costs

            # no unused houses left, applies hillclimber to optimalize connections
            if len(unused_houses) == 0:
                helper.hillclimber(batteries, houses)
                

    return total_costs


def plot_first_algorithm():
    """
    Plots the cables, houses and batteries for the Hillclimber algorithm
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

            fig = plt.savefig("figure.png")
    return fig
 
def run_output():

    for curr_batt in batteries:
        print(curr_batt)

        for curr_house in curr_batt.houses_to_battery:
            print(curr_house)

            for cable_point in curr_house.cables:
                print(cable_point)