"""
The janitor of a high school is extremely efficient. 
By the end of each day, all of the school's waste is in plastic bags weighing between 1.01 pounds and 3.00 pounds. 
All plastic bags are then taken to the trash bins outside. 
One trip is described as selecting a number of bags which together do not weigh more than 3.00 pounds, 
dumping them in the outside trash can and returning to the school. 
Given the number of plastic bags n, and the weights of each bag, 
determine the minimum number of trips the janitor has to make.
"""

MIN_BAG_WEIGHT = 1.01
MAX_BAG_WEIGHT = 3
MAX_WEIGHT_IN_ONE_TRIP = MAX_BAG_WEIGHT-MIN_BAG_WEIGHT

def get_min_trips(garbage_bag_list):
    trips = 0

    number_of_bags = len(garbage_bag_list)

    right_index = number_of_bags-1
    garbage_bag_list.sort(reverse=True)

    for left_index in range(number_of_bags):
        if left_index >= right_index:
            break

        if garbage_bag_list[left_index] + garbage_bag_list[right_index] <= MAX_BAG_WEIGHT:
           right_index -= 1

        trips +=1

    return trips

input_list = [1.01 ,1.02, 1.5, 1.98 ,2.5]
print(get_min_trips(input_list))

# Left index moves every loop
# Right index moves only if small bag can be taken in addition to big one
#   L                      R
# [2.5,  1.98, 1.5, 1.02, 1.01]

