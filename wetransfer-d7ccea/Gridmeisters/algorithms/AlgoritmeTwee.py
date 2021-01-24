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

# cable_coordinates

def second_algorithm():
    """
    Schrijf hier je code voor tweede algoritme, je hoeft niks te printen
    of returnen, zorg er alleen voor dat de huizen geappend worden aan alle batterijen
    """

    # shuffle houses
    random.shuffle(houses)

    # initialize
    total_costs = 0
    cables_coordinates = []
    count_houses = 0

    batterijen_lijst = []
    for battery in batteries:
        battery_dict ={"location": battery.coordinates, "capacity": battery.capacity, "houses":[]}
        batterijen_lijst.append(battery_dict)


    # for house in houses: 

        # battery_dict["capacity"] = battery_dict["capacity"] - house.maxoutput
        # print (battery_dict["capacity"])

    # print(batterijen_lijst)
    

    # for battery in batteries:

    #     for house in houses:

    #         battery_dict["capacity"] - house.maxoutput
    #         if battery_dict["capacity"] - house.maxoutput < 0:
    #             battery_dict["capacity"] - house.maxoutput
    #             battery_dict["houses"].append(house.id)

        # print(battery_dict["capacity"])

list_of_lists = []

for battery in batteries:

    cables_coordinates.append(batteries[4].coordinates)
    print(cables_coordinates)
    # loop for house in houses
    for house in houses:
        
        # empty list for connect options 
        connect_options = []

        # keep track of distances between each house and battery
        dist_dict = {}

        # for all connect options calculate distance to house and save in list
        for cable_point in cables_coordinates:
            distance = int(abs(house.coordinates[0] - cable_point[0]) + abs(house.coordinates[1] - cable_point[1]))
            connect_options.append(distance)

            # print(cable_point)

            # add all connect options to distance dictionary
            dist_dict[cable_point] = distance 
            # print(dist_dict[cable_point])
        
        # return closest distance of a house to all connect optionss
        closest_distance = min(dist_dict.items(), key=lambda x: x[1])
        closest_connection = closest_distance[0]
        connection = closest_connection
        
        x_dist = abs(house.x - connection[0])
        y_dist = abs(house.y - connection [1])
        
        
        house_costs = (x_dist + y_dist) * 9

        total_costs += house_costs 

        # print(f"costs for this house cable: {house_costs}")

        # start is house, end is connection coordinates
        current_x = house.x
        end_x= connection[0]
        current_y = house.y
        end_y = connection [1]
        
        # only if house isn't already connected, append first coordinate
        if house.coordinates != connection: 
            house.cables.append((current_x, current_y))

        # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
        if current_y < end_y:
            while current_y < end_y:
                current_y += 1
                house.cables.append((current_x, current_y))
        elif current_y > end_y:
            while current_y > end_y:
                current_y -= 1
                house.cables.append((current_x, current_y))
        if current_x < end_x:
            while current_x < end_x:
                current_x += 1
                house.cables.append((current_x, current_y))
        elif current_x > end_x:
            while current_x > end_x:
                current_x -= 1
                house.cables.append((current_x, current_y))
        
        # if there is already a connection for this house
        if house.coordinates == connection:
            battery.connect_house(house)
            # print("verbind2")

        # loops through dictionary and cables, to compare
        for cable_point in house.cables:
                
            # find connection point in dictionary 
            if cable_point == connection:
                    
                # connect battery
                battery.connect_house(house)

                # waar dit niet staat gaat het dus fout....
                # print("verbonden4")

        # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
        for tuple in house.cables:
            if tuple not in cables_coordinates:
                cables_coordinates.append(tuple)

        battery.capacity = battery.capacity - house.maxoutput
        if battery.capacity - house.maxoutput < 0:
            break

    print (battery.capacity)
    # return total_costs


def plot_second_algorithm():
    """
    Hier kan je tweede algoritme plotten
    """
    pass

    ax = plt.subplot(111)

    for battery in batteries:
        batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')
    for house in houses:
        houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')

    for house in houses:
        plt.plot(*zip(*house.cables), color='k')

    fig = plt.savefig("figure2.png")
    return fig

    # i = -1

    # for battery in batteries:
    #     i += 1
    
    #     for house in battery.houses_to_battery:

    #         colors = ['c', 'k', 'b', 'g', 'r']

    #         cutt_point_x = house.x
    #         cutt_point_y = battery.y

    #         x = [house.x, cutt_point_x, battery.x]
    #         y = [house.y, cutt_point_y, battery.y]

    #         plt.plot(x,y, color= colors[i])

    #         ax = plt.subplot()

    #         houses_plt = ax.scatter(house.x, house.y, color='k', marker='*')
    #         batteries_plt = ax.scatter(battery.x, battery.y, color='r', marker='^')

     

def run_sec_output():

    """
    Hier run je output, print dus per regel batterij etc...
    """
    pass     


"""
Loopt over huizen en zoekt dichtsbijzijnde afstand tot aan batterij
"""
# import load_data
# import house
# import battery
# import random
# import cables
# import matplotlib.pyplot as plt

# from matplotlib import style

# # read in all data
# reader = load_data.Load_data()
# batteries = reader.load_batteries()
# houses = reader.load_houses()

# def second_algorithm():
#     """
#     Schrijf hier je code voor tweede algoritme, je hoeft niks te printen
#     of returnen, zorg er alleen voor dat de huizen geappend worden aan alle batterijen
#     """

#     # shuffle houses
#     random.shuffle(houses)

#     cables_coordinates_1 = []
#     cables_coordinates_1.append(batteries[0].coordinates)
#     cables_coordinates_2 = []
#     cables_coordinates_2.append(batteries[1].coordinates)
#     cables_coordinates_3 = []
#     cables_coordinates_3.append(batteries[2].coordinates)
#     cables_coordinates_4 = []
#     cables_coordinates_4.append(batteries[3].coordinates)
#     cables_coordinates_5 = []
#     cables_coordinates_5.append(batteries[4].coordinates)

#     batterijen_lijst = []
#     for battery in batteries:
#         battery_dict ={"location": battery.coordinates, "capacity": battery.capacity, "houses":[]}
#         batterijen_lijst.append(battery_dict)

#     cables_coordinates.append(cables_coordinates_1)
#     cables_coordinates.append(cables_coordinates_2)


# # initialize houses count
# count_houses = 0

#     # for house in houses: 

# # first add the batteries as connect option and add as first items in dictionary
# for battery in batteries:
#     cables_coordinates.append(battery.coordinates)
        
# # loop for house in houses
# for house in houses:
    
#     # empty list for connect options 
#     connect_options = []
#         # battery_dict["capacity"] = battery_dict["capacity"] - house.maxoutput
#         # print (battery_dict["capacity"])

#     # print(batterijen_lijst)
    

#     # for battery in batteries:

#     cable = cables.Cable(house.x, house.y)
#     house.cables.append(cable)

#     temp_x = house.x
#     temp_y = house.y

#     while temp_x != connection[0] or temp_y != connection[1]:
#         if temp_x < connection[0]:
#                 cable = cables.Cable(temp_x + 1, temp_y)
#                 temp_x += 1
#                 house.cables.append(cable)

#         elif temp_x > connection[0]:
#             cable = cables.Cable(temp_x - 1, temp_y)
#             temp_x -= 1
#             house.cables.append(cable)

#         elif temp_y > connection[1]:
#             cable = cables.Cable(temp_x, temp_y - 1)
#             temp_y -= 1
#             house.cables.append(cable)

#         elif temp_y < connection[1]:
#             cable = cables.Cable(temp_x, temp_y + 1)
#             temp_y += 1
#             house.cables.append(cable)         

#     # start is house, end is connection coordinates
#     current_x = house.x
#     end_x= connection[0]
#     current_y = house.y
#     end_y = connection [1]
    
    
#     # only if house isn't already connected, append first coordinate
#     if house.coordinates != connection: 
#         house.cables.append((current_x, current_y))

#     # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
#     if current_y < end_y:
#         while current_y < end_y:
#             current_y += 1
#             house.cables.append((current_x, current_y))
#     elif current_y > end_y:
#         while current_y > end_y:
#             current_y -= 1
#             house.cables.append((current_x, current_y))
#     if current_x < end_x:
#         while current_x < end_x:
#             current_x += 1
#             house.cables.append((current_x, current_y))
#     elif current_x > end_x:
#         while current_x > end_x:
#             current_x -= 1
#             house.cables.append((current_x, current_y))
    
#      # if there is already a connection for this house
#     if house.coordinates == connection:
#         battery.connect_house(house)
#         print("verbind2")

#     #         battery_dict["capacity"] - house.maxoutput
#     #         if battery_dict["capacity"] - house.maxoutput < 0:
#     #             battery_dict["capacity"] - house.maxoutput
#     #             battery_dict["houses"].append(house.id)

#         # print(battery_dict["capacity"])


#     # first add the batteries as connect option and add as first items in dictionary
#     # for battery in batteries:
#     #     cables_coordinates.append(battery.coordinates)
#     #     print(cables_coordinates)

#     for battery in batteries:

#         cables_coordinates.append(batteries[4].coordinates)
#         print(cables_coordinates)
#         # loop for house in houses
#         for house in houses:
            
#             # empty list for connect options 
#             connect_options = []

#             # keep track of distances between each house and battery
#             dist_dict = {}

#             # for all connect options calculate distance to house and save in list
#             for cable_point in cables_coordinates:
#                 distance = int(abs(house.coordinates[0] - cable_point[0]) + abs(house.coordinates[1] - cable_point[1]))
#                 connect_options.append(distance)

#                 # print(cable_point)

#                 # add all connect options to distance dictionary
#                 dist_dict[cable_point] = distance 
#                 # print(dist_dict[cable_point])
            
#             # return closest distance of a house to all connect optionss
#             closest_distance = min(dist_dict.items(), key=lambda x: x[1])
#             closest_connection = closest_distance[0]
#             connection = closest_connection
            
#             x_dist = abs(house.x - connection[0])
#             y_dist = abs(house.y - connection [1])
            
            
#             house_costs = (x_dist + y_dist) * 9

#             total_costs += house_costs 

#             # print(f"costs for this house cable: {house_costs}")

#             # start is house, end is connection coordinates
#             current_x = house.x
#             end_x= connection[0]
#             current_y = house.y
#             end_y = connection [1]
            
#             # only if house isn't already connected, append first coordinate
#             if house.coordinates != connection: 
#                 house.cables.append((current_x, current_y))

#             # make the route, while the coordinates of the route aren't the coordinates of the right battery: move
#             if current_y < end_y:
#                 while current_y < end_y:
#                     current_y += 1
#                     house.cables.append((current_x, current_y))
#             elif current_y > end_y:
#                 while current_y > end_y:
#                     current_y -= 1
#                     house.cables.append((current_x, current_y))
#             if current_x < end_x:
#                 while current_x < end_x:
#                     current_x += 1
#                     house.cables.append((current_x, current_y))
#             elif current_x > end_x:
#                 while current_x > end_x:
#                     current_x -= 1
#                     house.cables.append((current_x, current_y))
            
#             # if there is already a connection for this house
#             if house.coordinates == connection:
#                 battery.connect_house(house)
#                 # print("verbind2")

#             # loops through dictionary and cables, to compare
#             for cable_point in house.cables:
                    
#                 # find connection point in dictionary 
#                 if cable_point == connection:
                        
#                     # connect battery
#                     battery.connect_house(house)

#                     # waar dit niet staat gaat het dus fout....
#                     # print("verbonden4")

#             # if it is a new coordinate add to dictionary with right connected battery and add to cables_Coordinates
#             for tuple in house.cables:
#                 if tuple not in cables_coordinates:
#                     cables_coordinates.append(tuple)

#             battery.capacity = battery.capacity - house.maxoutput
#             if battery.capacity - house.maxoutput < 0:
#                 break

#     print (battery.capacity)
#     return total_costs