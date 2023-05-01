import random
from utils import convert_difficulty

def addition_problem (difficulty_trace_level):
    nums = []
    while difficulty_trace_level > 0:
        num = random.randrange(10)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " + "

    return problem

def subtraction_problem (difficulty_trace_level):
    result = -1
    nums = []
    modified_trace_level = difficulty_trace_level
    while result < 0:
        nums = []
        while modified_trace_level > 0:
            num = random.randint(1, 9)
            nums.append(num)
            modified_trace_level -= 1
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        modified_trace_level = difficulty_trace_level

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " - "

    return problem
    
def multiple_operations_problem(difficulty_trace_level):
    result = -1
    nums = []
    modified_trace_level = difficulty_trace_level + 1
    while result < 0:
        nums = []
        while modified_trace_level > 0:
            num = random.randint(1, 9)
            nums.append(num)
            modified_trace_level -= 1
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        modified_trace_level = difficulty_trace_level + 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            if (i%2) == 0:
                problem += str(nums[i]) + " - "
            else:
                problem += str(nums[i]) + " + "

    return problem


def run_request_kg(request):
    problems = []
    arr = request.split(",")
    for str in arr:
        arr_2 = str.split("-")
        type_of_problem = arr_2[0]
        num_problems = arr_2[1]
        difficulty = convert_difficulty(arr_2[2])
        for i in range(int(num_problems)):
            problem = return_problem(type_of_problem, difficulty)
            problems.append(problem)
    return problems

def return_problem(type_of_problem, difficulty):
    if (type_of_problem == "1"):
        return addition_problem(difficulty)
    elif (type_of_problem == "2"):
        return subtraction_problem(difficulty)
    else:
        return multiple_operations_problem(difficulty)


