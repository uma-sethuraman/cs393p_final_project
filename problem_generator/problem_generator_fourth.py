import random
from utils import convert_difficulty

def decimal_add_problem(difficulty_trace_level):
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
            problem += str(nums[i]) + " + "

    return problem

def decimal_subtract_problem(difficulty_trace_level):
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
            problem += str(nums[i]) + " - "

    return problem

def decimal_mixed_operations_problem(difficulty_trace_level):
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
            if (i%2) == 0:
                problem += str(nums[i]) + " - "
            else:
                problem += str(nums[i]) + " + "

    return problem

def multiplication_problem(difficulty_trace_level):
    nums = []
    while difficulty_trace_level > 0:
        num = random.randrange(1000)
        nums.append(num)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " * "

    return problem

def division_problem(difficulty_trace_level):
    nums = []
    result = -1
    modified_trace_level = difficulty_trace_level-1
    while result != 0:
        num1 = random.randint(100*modified_trace_level, 300*modified_trace_level)
        num2 = random.randint(100*modified_trace_level, 300*modified_trace_level)
        nums = [num1, num2]
        result = num1 % num2

    problem = ""
    for i in range(len(nums)):
        if i == (len(nums) - 1):
            problem += str(nums[i])
        else:
            problem += str(nums[i]) + " / "
    
    return problem

def multiple_operations_problem_mul_div(difficulty_trace_level):
    nums = []
    modified_trace_level = difficulty_trace_level + 1
    while modified_trace_level > 0:
        num = random.randrange(1000)
        nums.append(num)
        modified_trace_level -= 1

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

def fraction_add_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1, 100)
        numerators.append(random.randint(1, denominator))
        denominators.append(denominator)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(numerators)):
        if i == (len(numerators) - 1):
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")"
        else:
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " + "
    
    return problem

# intro to negative numbers
def fraction_sub_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1, 100)
        numerators.append(random.randint(1, denominator))
        denominators.append(denominator)
        difficulty_trace_level -= 1

    problem = ""
    for i in range(len(numerators)):
        if i == (len(numerators) - 1):
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")"
        else:
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " - "
    
    return problem

def multiple_operations_problem_frac_add_sub(difficulty_trace_level):
    denominators = []
    numerators = []
    modified_trace_level = difficulty_trace_level + 1
    while modified_trace_level > 0:
        denominator = random.randint(1, 100)
        numerators.append(random.randint(1, denominator))
        denominators.append(denominator)
        modified_trace_level -= 1

    problem = ""
    for i in range(len(numerators)):
        if i == (len(numerators) - 1):
            problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")"
        else:
            if (i%2) == 0:
                problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " + "
            else:
                problem += "(" + str(numerators[i]) + "/" + str(denominators[i]) + ")" + " - "

    return problem

def fraction_multiply_problem(difficulty_trace_level):
    denominators = []
    numerators = []
    while difficulty_trace_level > 0:
        denominator = random.randint(1, 100)
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

# returns a list of problem strings 
def run_request_4(request):
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
        return decimal_add_problem(difficulty)
    elif (type_of_problem == "2"):
        return decimal_subtract_problem(difficulty)
    elif (type_of_problem == "3"):
        return decimal_mixed_operations_problem(difficulty)
    elif (type_of_problem == "4"):
        return multiplication_problem(difficulty)
    elif (type_of_problem == "5"):
        return division_problem(difficulty)
    elif (type_of_problem == "6"):
        return multiple_operations_problem_mul_div(difficulty)
    elif (type_of_problem == "7"):
        return fraction_add_problem(difficulty)
    elif (type_of_problem == "8"):
        return fraction_sub_problem(difficulty)
    elif (type_of_problem == "9"):
        return multiple_operations_problem_frac_add_sub(difficulty)
    else:
        return fraction_multiply_problem(difficulty)

