import time
#Courses is a dictionary containing all the courses and the corresponding sections for each course,
#there are multiple sections for each course and days are defined by letters, time of day is defined 
# by the amount of minutes from midnight 12:00am, for example, 510/60 = 8+30, which means 8:30 in the 
# morning, by using this format, it is easy to compare different courses and check for time conflicts. 
COURSES1 = { #5 courses 3 sections each, 15 sections
    "ANT100": [
        {"id": "ANT100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "ANT100-B", "meetings": [("T",540,615),("R",540,615)]},
        {"id": "ANT100-C", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "BIO101": [
        {"id": "BIO101-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "BIO101-B", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "BIO101-C", "meetings": [("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "CHM112": [
        {"id": "CHM112-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "CHM112-B", "meetings": [("T",540,615),("R",540,615)]},
        {"id": "CHM112-C", "meetings": [("T",600,675),("R",600,675)]},
    ],
    "MAT109": [
        {"id": "MAT109-A", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "MAT109-B", "meetings": [("T",600,675),("R",600,675)]},
        {"id": "MAT109-C", "meetings": [("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "PSY100": [
        {"id": "PSY100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "PSY100-B", "meetings": [("T",660,735),("R",660,735)]},
        {"id": "PSY100-C", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
    ],
}

COURSES1a = { #5 courses 2 sections each, 10 sections
    "ANT100": [
        {"id": "ANT100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "ANT100-B", "meetings": [("T",540,615),("R",540,615)]},
    ],
    "BIO101": [
        {"id": "BIO101-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "BIO101-B", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "CHM112": [
        {"id": "CHM112-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "CHM112-B", "meetings": [("T",540,615),("R",540,615)]},
    ],
    "MAT109": [
        {"id": "MAT109-A", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "MAT109-C", "meetings": [("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "PSY100": [
        {"id": "PSY100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "PSY100-B", "meetings": [("T",660,735),("R",660,735)]},
    ],
}

COURSES1b = { #5 courses 4 sections each, 20 sections
    "ANT100": [
        {"id": "ANT100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "ANT100-B", "meetings": [("T",540,615),("R",540,615)]},
        {"id": "ANT100-C", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "ANT100-C", "meetings": [("M",690,740),("W",690,740),("F",690,740)]},
    ],
    "BIO101": [
        {"id": "BIO101-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "BIO101-B", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "BIO101-C", "meetings": [("M",660,710),("W",660,710),("F",660,710)]},
        {"id": "BIO101-C", "meetings": [("M",680,730),("W",680,730),("F",680,730)]},
    ],
    "CHM112": [
        {"id": "CHM112-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "CHM112-B", "meetings": [("T",540,615),("R",540,615)]},
        {"id": "CHM112-C", "meetings": [("T",600,675),("R",600,675)]},
        {"id": "CHM112-A", "meetings": [("M",640,690),("W",640,690),("F",640,690)]},
    ],
    "MAT109": [
        {"id": "MAT109-A", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "MAT109-B", "meetings": [("T",600,675),("R",600,675)]},
        {"id": "MAT109-C", "meetings": [("M",660,710),("W",660,710),("F",660,710)]},
        {"id": "MAT109-B", "meetings": [("T",620,695),("R",620,695)]},
    ],
    "PSY100": [
        {"id": "PSY100-A", "meetings": [("M",540,590),("W",540,590),("F",540,590)]},
        {"id": "PSY100-B", "meetings": [("T",660,735),("R",660,735)]},
        {"id": "PSY100-C", "meetings": [("M",600,650),("W",600,650),("F",600,650)]},
        {"id": "PSY100-B", "meetings": [("T",600,675),("R",600,675)]},
    ],
}

COURSES2 = { # 6 courses 3 sections each 18 sections
    "ANT100":[
        {"id":"ANT100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"ANT100-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"ANT100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "BIO101":[
        {"id":"BIO101-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"BIO101-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"BIO101-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "CHM112":[
        {"id":"CHM112-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"CHM112-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"CHM112-C","meetings":[("T",600,675),("R",600,675)]},
    ],
    "MAT109":[
        {"id":"MAT109-A","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"MAT109-B","meetings":[("T",600,675),("R",600,675)]},
        {"id":"MAT109-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "PSY100":[
        {"id":"PSY100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"PSY100-B","meetings":[("T",660,735),("R",660,735)]},
        {"id":"PSY100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "ECO100":[
        {"id":"ECO100-A","meetings":[("M",720,770),("W",720,770),("F",720,770)]},
        {"id":"ECO100-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"ECO100-C","meetings":[("M",620,670),("W",620,670),("F",620,670)]},
    ],
}

COURSES3 = { # 7 courses 3 sections each 21 sections
    "ANT100":[
        {"id":"ANT100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"ANT100-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"ANT100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "BIO101":[
        {"id":"BIO101-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"BIO101-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"BIO101-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "CHM112":[
        {"id":"CHM112-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"CHM112-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"CHM112-C","meetings":[("T",600,675),("R",600,675)]},
    ],
    "MAT109":[
        {"id":"MAT109-A","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"MAT109-B","meetings":[("T",600,675),("R",600,675)]},
        {"id":"MAT109-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "PSY100":[
        {"id":"PSY100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"PSY100-B","meetings":[("T",660,735),("R",660,735)]},
        {"id":"PSY100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "ECO100":[
        {"id":"ECO100-A","meetings":[("M",720,770),("W",720,770),("F",720,770)]},
        {"id":"ECO100-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"ECO100-C","meetings":[("M",620,670),("W",620,670),("F",620,670)]},
    ],
    "CPS111":[
        {"id":"CPS111-A","meetings":[("M",780,830),("W",780,830),("F",780,830)]},
        {"id":"CPS111-B","meetings":[("T",600,675),("R",600,675)]},
        {"id":"CPS111-A","meetings":[("M",730,780),("W",730,780),("F",730,780)]},
    ],
}

COURSES4 = { # 8 courses 24sections {'ANT100': 'ANT100-B', 'BIO101': 'BIO101-C', 'CHM112': 'CHM112-A', 'MAT109': 'MAT109-A', 'PSY100': 'PSY100-B', 'ECO100': 'ECO100-A', 'HIS120': 'HIS120-A', 'CPS111': 'CPS111-A'}
    "ANT100":[
        {"id":"ANT100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"ANT100-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"ANT100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "BIO101":[
        {"id":"BIO101-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"BIO101-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"BIO101-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "CHM112":[
        {"id":"CHM112-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"CHM112-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"CHM112-C","meetings":[("T",600,675),("R",600,675)]},
    ],
    "MAT109":[
        {"id":"MAT109-A","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"MAT109-B","meetings":[("T",600,675),("R",600,675)]},
        {"id":"MAT109-C","meetings":[("M",660,710),("W",660,710),("F",660,710)]},
    ],
    "PSY100":[
        {"id":"PSY100-A","meetings":[("M",540,590),("W",540,590),("F",540,590)]},
        {"id":"PSY100-B","meetings":[("T",660,735),("R",660,735)]},
        {"id":"PSY100-C","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
    ],
    "ECO100":[
        {"id":"ECO100-A","meetings":[("M",720,770),("W",720,770),("F",720,770)]},
        {"id":"ECO100-B","meetings":[("M",600,650),("W",600,650),("F",600,650)]},
        {"id":"ECO100-C","meetings":[("M",620,670),("W",620,670),("F",620,670)]},
    ],
    "CPS111":[
        {"id":"CPS111-A","meetings":[("M",780,830),("W",780,830),("F",780,830)]},
        {"id":"CPS111-B","meetings":[("T",600,675),("R",600,675)]},
        {"id":"CPS111-A","meetings":[("M",730,780),("W",730,780),("F",730,780)]},
    ],
    "HIS120":[
        {"id":"HIS120-A","meetings":[("M",840,890),("W",840,890),("F",840,890)]},
        {"id":"HIS120-B","meetings":[("T",540,615),("R",540,615)]},
        {"id":"HIS120-B","meetings":[("T",890,940),("R",890,940)]},
    ],
}

courses1_costsa = {
    "ANT100-A":1,
    "BIO101-B":1,
    "CHM112-C":1,
    "MAT109-C":1,
    "PSY100-B":1
}
courses1_costsb = {
    "ANT100-A": 1,
    "BIO101-B": 2,
    "CHM112-C": 1,
    "MAT109-C": 2,
    "PSY100-B": 1,
}
courses1_costsc = {
    "ANT100-A": 1,
    "BIO101-B": 3,
    "CHM112-C": 1,
    "MAT109-C": 3,
    "PSY100-B": 1,
}

#uniform cost test:
course_coststest = {}

#the order of registering for courses is fixed because order does not matter when we register for courses,
#this also greatly shortens the amount of states that we need to explore for each course that we need to register.
COURSES1_ORDER = ["ANT100", "BIO101", "CHM112", "MAT109", "PSY100"]
COURSES2_ORDER = ["ANT100", "BIO101", "CHM112", "MAT109","PSY100", "ECO100"]
COURSES3_ORDER = ["ANT100", "BIO101", "CHM112", "MAT109","PSY100", "ECO100", "CPS111"]
COURSES4_ORDER = ["ANT100", "BIO101", "CHM112", "MAT109","PSY100", "ECO100", "HIS120", "CPS111"]

# this function returns all the sections of a given course id code, retrieved from the dictionary
def find_section(sec_id, courses):
    for course, section_list in courses.items():
        for section in section_list:
            if section["id"] == sec_id:
                return section
    return None

#this function checks and returns TRUE if two course sections have time conflicts 
def sections_conflict(sec_id1, sec_id2, courses):
    sec1 = find_section(sec_id1, courses)
    sec2 = find_section(sec_id2, courses)

    for (day1, start1, end1) in sec1["meetings"]:
        for (day2, start2, end2) in sec2["meetings"]:
            # if two classes are not even on the same day, there shouldnt be any conflicts
            if day1 != day2: 
                continue
            # if a class starts before another ends, there is a conflict
            latest_start = max(start1, start2)
            earliest_end = min(end1, end2)
            if latest_start < earliest_end:
                return True

    return False


#For a partial schedule like {"ANT100": "ANT100-A", "BIO101": "BIO101-B"}, this function
#checks if there are any conflicts in the current schedule.
def has_conflict(state, courses):
    section_ids = list(state.values())

    for i in range(len(section_ids)):
        id1 = section_ids[i] # the first section in the pair
        for j in range(i + 1, len(section_ids)):
            id2 = section_ids[j] # the second section in the pair
            # Check whether this pair conflicts
            if sections_conflict(id1, id2, courses):
                # If any pair overlaps in time, the whole schedule is invalid
                return True
    return False

#Checks the course cost list and adds them to the total cost for the state
def path_cost(state, course_costs):
    total = 0
    for course, sec_id in state.items():
        total += course_costs.get(sec_id, 0)
    return total

#this function generates all the schedules based on the current schedule for the next course
def possible_next_classes(state, course_order, courses):
    # if all courses are already assigned, no successors
    if len(state) == len(course_order):
        return []
    # if the current state is incomplete, the next course should be the length of the state,
    # for example, if we only have 2 items in the current state, the next course in the order
    # should be index 2, same as the length of the incomplete state. 
    next_course = course_order[len(state)]
    new_schedule = []
    for sec in courses[next_course]:
        sec_id = sec["id"]
        # make a copy of the current schedule and add new classes 
        new_state = state.copy()
        new_state[next_course] = sec_id

        # if not has_conflict(new_state, courses):
        new_schedule.append(new_state)

    return new_schedule

# since all courses are added in the same order, if the total number of courses is correct,
# then we have all the courses needed. If there are no conflicts, we have achieved our goal.
def is_goal(state, course_order, courses):
    if len(state) != len(course_order):
        return False

    if has_conflict(state, courses):
        return False
    
    return True

# Standard BFS search with added preference 
def BFS(courses, course_order,course_costs):
    start_state = {}
    t0 = time.time()
    # BFS uses a FIFO queue. We begin by putting the empty schedule inside it.
    queue = [start_state]
    nodes_explored = 0
    # later added a best solution state to store the schedule with the highest preference score
    best_solution = None
    best_cost = None
     # continue searching while there are still schedules to explore
    while queue:
        state = queue.pop(0)
        nodes_explored += 1
        # Check if we have assigned all courses AND have no time conflicts
        if is_goal(state, course_order, courses):
            cost = path_cost(state, course_costs)
            if best_solution is None or cost < best_cost:
                best_solution = state
                best_cost = cost
            continue
        # add each valid successor state to the queue for later exploration
        for state in possible_next_classes(state, course_order, courses):
            queue.append(state)

    if best_solution is not None:
        print("Nodes explored:", nodes_explored)
        print("Time Taken:", time.time() - t0)
        print("BFS Success!")
    else:
        print("Nodes explored:", nodes_explored)
        print("Time Taken:", time.time() - t0)
        print("BFS did not find any valid schedule.")

    return best_solution

# helper function for A* search to calculate the heuristic value
def f(state, course_order, courses, heuristic, course_costs):
    g = path_cost(state, course_costs)
    h = heuristic(state, course_order, courses)
    return g + h


#all paths are equal cost, adding classes to schedule is equal cost, so we can assume
#number of assigned courses is the cost.
def A_Star(courses, course_order, heuristic,course_costs):
    nodes_explored = 0
    # Initial state: empty schedule (no courses assigned yet)
    start_state = {}
    # Frontier is just a list of states
    frontier = [start_state]
    nodes_explored = 0
    t0 = time.time()

    while frontier:
        #Choose the state in frontier with smallest f(n)
        best_index = 0
        best_state = frontier[0]
        best_f = f(best_state, course_order, courses, heuristic,course_costs)

        #loops through the heuristic function to find the best heuristic value
        for i in range(1, len(frontier)):
            state_i = frontier[i]
            f_i = f(state_i, course_order, courses, heuristic,course_costs)
            if f_i < best_f:
                best_f = f_i
                best_index = i
                best_state = state_i

        # Remove the best state from the frontier
        state = frontier.pop(best_index)
        nodes_explored += 1

        if is_goal(state, course_order, courses):
            print("A* Success!")
            print("Nodes explored:", nodes_explored)
            print("Time Taken:", time.time() - t0)
            return state
                
        # Generate all the possible schedules
        schedules = possible_next_classes(state, course_order, courses)
        for state in schedules:
            g_new = len(state)    
            frontier.append((state))

    # If frontier is empty, no solution exists
    return None

# this heuristics function never over estimates because there can only be 4 classes in a schedule,
# and the number of classes remaining to add is the shortest way to finishing the calendar.
def heuristic_unassigned(state, course_order, courses):
    return len(course_order) - len(state)

# this heuristics checks the number of conflicts in the current schedule, the less courses assigned with 
# time conflicts, the closer to the goal it is. 
def heuristic_conflicts(state, course_order, courses):
    section_ids = list(state.values())
    conflicts = 0

    # for sections in a course state, check if there are conflicts in the code and returns the number of conflicts.
    for i in range(len(section_ids)):
        for j in range(i + 1, len(section_ids)):
            if sections_conflict(section_ids[i], section_ids[j], courses):
                conflicts += 1

    return conflicts


#For testing the code, just un-comment any section below and run!
def main():
    print("Hi, thank you for reviewing my project! ")
#====================================================================================
    # #For different number of courses:
    # print("Courses 1 Results:")
    # print(BFS(COURSES1, COURSES1_ORDER,course_coststest))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_conflicts,course_coststest))

    # print("Courses 2 Results:")
    # print(BFS(COURSES2, COURSES1_ORDER,course_coststest))
    # print(A_Star(COURSES2, COURSES2_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES2, COURSES2_ORDER, heuristic_conflicts,course_coststest))

    # print("Courses 3 Results:")
    # print(BFS(COURSES3, COURSES3_ORDER,course_coststest))
    # print(A_Star(COURSES3, COURSES3_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES3, COURSES3_ORDER, heuristic_conflicts,course_coststest))

    # print("Courses 4 Results:")
    # print(BFS(COURSES4, COURSES4_ORDER,course_coststest))
    # print(A_Star(COURSES4, COURSES4_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES4, COURSES4_ORDER, heuristic_conflicts,course_coststest))

#====================================================================================

    # #For different number of sections:
    # print("5 Courses, 10 sections  Results:")
    # print(BFS(COURSES1a, COURSES1_ORDER,course_coststest))
    # print(A_Star(COURSES1a, COURSES1_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES1a, COURSES1_ORDER, heuristic_conflicts,course_coststest))

    # print("5 Courses, 15 sections  Results:")
    # print(BFS(COURSES1, COURSES1_ORDER,course_coststest))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_conflicts,course_coststest))

    # print("5 Courses, 20 sections  Results:")
    # print(BFS(COURSES1b, COURSES1_ORDER,course_coststest))
    # print(A_Star(COURSES1b, COURSES1_ORDER, heuristic_unassigned,course_coststest))
    # print(A_Star(COURSES1b, COURSES1_ORDER, heuristic_conflicts,course_coststest))

#====================================================================================

    # #For different preferences:
    # print("5 Courses, 15 sections, uniform preference  Results:")
    # print(BFS(COURSES1, COURSES1_ORDER,courses1_costsa))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_unassigned,courses1_costsa))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_conflicts,courses1_costsa))

    # print("5 Courses, 15 sections, 1-2 preference  Results:")
    # print(BFS(COURSES1, COURSES1_ORDER,courses1_costsb))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_unassigned,courses1_costsb))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_conflicts,courses1_costsb))

    # print("5 Courses, 15 sections, 1-3 preference  Results:")
    # print(BFS(COURSES1, COURSES1_ORDER,courses1_costsc))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_unassigned,courses1_costsc))
    # print(A_Star(COURSES1, COURSES1_ORDER, heuristic_conflicts,courses1_costsc))
#====================================================================================

main()
