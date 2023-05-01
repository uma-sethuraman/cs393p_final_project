import random
from utils import convert_difficulty

def inequalities_problem(difficulty_trace_level):
    nums = []
    difficulty_trace_level *= 2
    while difficulty_trace_level > 0:
        num = random.randint(25, 75)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = "("
    operations = [" + ", " - ", " * ", " / ", " ^ "]
    inequalities = [" > ", " >= ", " < ", " <= "]
    for i in range(len(nums)):
        if i == (len(nums) - 1) or i == ((len(nums))/2 - 1):
            problem += str(nums[i]) + ")"
        else:
            problem += str(nums[i]) + operations[random.randint(0,4)]

        if i == ((len(nums))/2 - 1):
            problem += inequalities[random.randint(0,3)] + "("

    return problem

def percents_problem(difficulty_trace_level):
    percent = round(random.random(), 2)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(1000*modified_trace_level, 5000*modified_trace_level)
    problem = "PERCENT:" + str(percent) + " * " + str(num)
    return problem

def exponents_problem(difficulty_trace_level):
    exponent = random.randint(0, 10)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(100*modified_trace_level, 1000*modified_trace_level)
    problem = str(num) + " ^ " + str(exponent)
    return problem

def roots_problem(difficulty_trace_level):
    nums = []
    difficulty_trace_level -= 1
    while difficulty_trace_level > 0:
        num = random.randint(1, 100)
        nums.append(num*num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i]) + " √ " + "rhs"
        else:
            problem += str(nums[i]) + " √ " + "rhs" + " + "

    return problem
 
def run_request_7(request):
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
        return inequalities_problem(difficulty)
    elif (type_of_problem == "2"):
        return percents_problem(difficulty)
    elif (type_of_problem == "3"):
        return exponents_problem(difficulty)
    else:
        return roots_problem(difficulty)