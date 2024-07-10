from collections import deque

def solution(bridge_length, weight, truck_weights):

    time = 0
    truck_weights = deque(truck_weights)
    enter = deque([0]*bridge_length)
    current_weight = 0

    while len(truck_weights) != 0:

        time += 1
        out_truck = enter.popleft()
        current_weight -= out_truck

        if current_weight + truck_weights[0] <= weight :
            in_truck = truck_weights.popleft()
            enter.append(in_truck)
            current_weight += in_truck
        else:
            enter.append(0)

    return time + bridge_length


# bridge_length_, weight_, truck_weights_ =		100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# 1) 2, 10, [7, 4, 5, 6]
# 2) 100, 100, [10]
# 3) 100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# solution(bridge_length_, weight_, truck_weights_)