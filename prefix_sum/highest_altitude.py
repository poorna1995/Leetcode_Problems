
# gain = [-5,1,5,0,-7]
gain = [-4,-3,-2,-1,4,3,2]

def highest_altitude(gain):
    current_altitude = 0
    max_altitude = float('-inf')
    for num in gain:
        current_altitude= current_altitude + num
        max_altitude = max(current_altitude,max_altitude)

    return max(0,max_altitude)

print(highest_altitude(gain))



