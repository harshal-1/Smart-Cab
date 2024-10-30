# cab_allocation.py
import heapq

cabs = {
    "cab1": (10, 20),
    "cab2": (15, 25),
    "cab3": (30, 35),
}

def find_nearest_cab(cabs, location):
    nearest_cabs = []
    for cab_id, cab_location in cabs.items():
        distance = ((cab_location[0] - location[0]) ** 2 + 
                    (cab_location[1] - location[1]) ** 2) ** 0.5
        heapq.heappush(nearest_cabs, (distance, cab_id))
    return heapq.heappop(nearest_cabs)[1]  # Return nearest cab ID

def allocate_cab(employee_location):
    # This function allocates a cab based on nearest cab to the employee's location
    employee_location = tuple(map(int, employee_location.split(',')))
    return find_nearest_cab(cabs, employee_location)

def search_nearby_cabs(employee_location):
    employee_location = tuple(map(int, employee_location.split(',')))
    return [cab for cab in cabs if find_nearest_cab(cabs, employee_location)]
