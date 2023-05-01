import random
from utils import convert_difficulty

def fraction_multiply_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1000, 3000)
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
        denominator = random.randint(1000, 3000)
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

def percents_problem(difficulty_trace_level):
    percent = round(random.random(), 2)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(100*modified_trace_level, 1000*modified_trace_level)
    problem = "PERCENT:" + str(percent) + " * " + str(num)
    return problem

def exponents_problem(difficulty_trace_level):
    exponent = random.randint(0, 50)
    modified_trace_level = difficulty_trace_level-1
    num = random.randint(10*modified_trace_level, 100*modified_trace_level)
    problem = str(num) + " ^ " + str(exponent)
    return problem

def inequalities_problem(difficulty_trace_level):
    nums = []
    difficulty_trace_level *= 2
    while difficulty_trace_level > 0:
        num = random.randint(1, 10)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = "("
    operations = [" + ", " - ", " * ", " / "]
    inequalities = [" > ", " >= ", " < ", " <= "]
    for i in range(len(nums)):
        if i == (len(nums) - 1) or i == ((len(nums))/2 - 1):
            problem += str(nums[i]) + ")"
        else:
            problem += str(nums[i]) + operations[random.randint(0,3)]

        if i == ((len(nums))/2 - 1):
            problem += inequalities[random.randint(0,3)] + "("

    return problem

def run_request_6(request):
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
        return fraction_multiply_problem(difficulty)
    elif (type_of_problem == "2"):
        return fraction_divide_problem(difficulty)
    elif (type_of_problem == "3"):
        return percents_problem(difficulty)
    elif (type_of_problem == "4"):
        return exponents_problem(difficulty)
    else:
        return inequalities_problem(difficulty)