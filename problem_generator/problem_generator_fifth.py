import random
from utils import convert_difficulty

def decimal_multiply_problem(difficulty_trace_level):
    nums = []
    while difficulty_trace_level > 0:
        num = round(random.uniform(1.0, 100.0), 2)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " * "

    return problem

def decimal_divide_problem(difficulty_trace_level):
    nums = []
    while difficulty_trace_level > 0:
        num = round(random.uniform(1.0, 100.0), 2)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " / "

    return problem

def decimal_mixed_operations_problem(difficulty_trace_level):
    nums = []
    difficulty_trace_level += 1
    while difficulty_trace_level > 0:
        num = round(random.uniform(1.0, 100.0), 2)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            if (i%2) == 0:
                problem += str(nums[i]) + " * "
            else:
                problem += str(nums[i]) + " / "

    return problem

def percents_problem(difficulty_trace_level):
    percent = round(random.random(), 2)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(10*modified_trace_level, 100*modified_trace_level)
    problem = "PERCENT:" + str(percent) + " * " + str(num)
    return problem

def exponents_problem(difficulty_trace_level):
    exponent = random.randint(0, 10)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(1*modified_trace_level, 10*modified_trace_level)
    problem = str(num) + " ^ " + str(exponent)
    return problem

def fraction_multiply_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1, 1000)
        numerators.append(random.randint(1, denominator))
        denominators.append(denominator)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(numerators)):
        if i == (len(numerators) - 1):
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")"
        else:
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " * "
    
    return problem

def fraction_divide_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1, 1000)
        numerators.append(random.randint(1, denominator))
        denominators.append(denominator)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(numerators)):
        if i == (len(numerators) - 1):
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")"
        else:
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " / "
    
    return problem

def run_request_5(request):
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
        return decimal_multiply_problem(difficulty)
    elif (type_of_problem == "2"):
        return decimal_divide_problem(difficulty)
    elif (type_of_problem == "3"):
        return decimal_mixed_operations_problem(difficulty)
    elif (type_of_problem == "4"):
        return percents_problem(difficulty)
    elif (type_of_problem == "5"):
        return exponents_problem(difficulty)
    elif (type_of_problem == "6"):
        return fraction_multiply_problem(difficulty)
    else:
        return fraction_divide_problem(difficulty)
