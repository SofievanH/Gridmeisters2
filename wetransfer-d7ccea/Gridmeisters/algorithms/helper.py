import random
import models.load_data

def hillclimber(batteries, houses):

    for battery in batteries:

        curr_battery = battery

        for next_house in houses:

            for curr_house in curr_battery.houses_to_battery:

                if next_house not in curr_battery.houses_to_battery:

                    # if curr_house is not next_house and curr_house.calc_costs(curr_battery) > next_house.calc_costs(curr_battery):
                        
                    next_battery = next_house.connected_to

                    if logic_swap(curr_battery, curr_house, next_battery, next_house) == True:

                        # if curr_house.maxoutput + curr_battery.capacity > next_house.maxoutput and next_house.maxoutput + next_battery.capacity > curr_house.maxoutput:
                        if output_swap(curr_battery, curr_house, next_battery, next_house) == True:

                            # STAP 1:
                            # if curr_house in curr_battery.houses_to_battery:
                            # remove current house van current battery
                            curr_battery.remove_house(curr_house)
                            curr_house.deconnect_to_battery(curr_battery)

                            # connect next house aan current battery
                            curr_battery.connect_house(next_house)
                            next_house.connect_to_battery(curr_battery)

                            # STAP 2:
                            # remove next house van next battery
                            next_battery.remove_house(next_house)
                            next_house.deconnect_to_battery(next_battery)

                            # connect current house aan next battery
                            next_battery.connect_house(curr_house)
                            curr_house.connect_to_battery(next_battery)


def output_swap(curr_battery, curr_house, next_battery, next_house):
    """
    Check to see if swap is possible based on output
    """

    if curr_house.maxoutput + curr_battery.capacity > next_house.maxoutput and next_house.maxoutput + next_battery.capacity > curr_house.maxoutput:
        return True
    else:
        return False

def logic_swap(curr_battery, curr_house, next_battery, next_house):

    if curr_house and curr_battery and next_house and next_battery is not None:

        dist10 = abs(curr_house.coordinates[0] - next_battery.coordinates[0]) + abs(curr_house.coordinates[1] - next_battery.coordinates[1])  
        dist11 = abs(next_house.coordinates[0] - curr_battery.coordinates[0]) + abs(next_house.coordinates[1] - curr_battery.coordinates[1])  

        dist12 = abs(curr_house.coordinates[0] - curr_battery.coordinates[0]) + abs(curr_house.coordinates[1] - curr_battery.coordinates[1])
        dist13 = abs(next_house.coordinates[0] - next_battery.coordinates[0]) + abs(next_house.coordinates[1] - next_battery.coordinates[1])    

        dist2 = dist10 + dist11
        dist1 = dist12 + dist13

        if dist2 < dist1:
            return True
        else:
            return False    

def calc_shared_costs(houses):

    tot = 0

    for battery in batteries:

        pass