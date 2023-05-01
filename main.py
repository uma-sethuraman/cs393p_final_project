from problem_generator.problem_generator_kg import run_request_kg
from problem_generator.problem_generator_first import run_request_1
from problem_generator.problem_generator_second import run_request_2
from problem_generator.problem_generator_third import run_request_3
from problem_generator.problem_generator_fourth import run_request_4
from problem_generator.problem_generator_fifth import run_request_5
from problem_generator.problem_generator_sixth import run_request_6
from problem_generator.problem_generator_seventh import run_request_7
from problem_solver import solution_generator
import z3
from z3 import *

def execute_kg():
    print("These are the available topics for the kindergarten grade level: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Mixed Operations (Addition and Subtraction)")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    print("Choose which topics you would like to generate problems for and how many questions you want for each topic.")
    print("You MUST enter your request in this format: number of topic-number of problems for that topic-difficulty level of this set of problems")
    print("For instance, the request 1-10-EASY,2-20-MEDIUM means that the user wants 10 easy addition and 20 medium subtraction problems.")
    request = input("Enter request here: ")
    problems = run_request_kg(request)
    generate_solutions(problems)

def execute_first():
    print("These are the available topics for the 1st grade level: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Mixed Operations (Addition and Subtraction)")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_1(request)
    generate_solutions(problems)

def execute_second():
    print("These are the available topics for the 2nd grade level: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Mixed Operations (Addition and Subtraction)")
    print("4. Multiplication")
    print("5. Division")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_2(request)
    generate_solutions(problems)

def execute_third():
    print("These are the available topics for the 3rd grade level: ")
    print("1. Multiplication")
    print("2. Division")
    print("3. Mixed Operations (Multiplication and Division)")
    print("4. Fraction Addition - Same Denominators")
    print("5. Fraction Subtraction - Same Denominators")
    print("6. Mixed Operations (Fraction Addition and Fraction Subtraction)")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_3(request)
    generate_solutions(problems)

def execute_fourth():
    print("These are the available topics for the 4th grade level: ")
    print("1. Decimal Addition")
    print("2. Decimal Subtraction")
    print("3. Mixed Operations (Decimal Addition and Decimal Subtraction)")
    print("4. Multiplication")
    print("5. Division")
    print("6. Mixed Operations (Multiplication and Division)")
    print("7. Fraction Addition")
    print("8. Fraction Subtraction")
    print("9. Mixed Operations (Fraction Addition and Fraction Subtraction)")
    print("10. Fraction Multiplication")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_4(request)
    generate_solutions(problems)

def execute_fifth():
    print("These are the available topics for the 5th grade level: ")
    print("1. Decimal Multiplication")
    print("2. Decimal Division")
    print("3. Mixed Operations (Decimal Multiplication and Decimal Division)")
    print("4. Percentages")
    print("5. Exponents")
    print("6. Fraction Multiplication")
    print("7. Fraction Division")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_5(request)
    generate_solutions(problems)

def execute_sixth():
    print("These are the available topics for the 6th grade level: ")
    print("1. Fraction Multiplication")
    print("2. Fraction Division")
    print("3. Percentages")
    print("4. Exponents")
    print("5. Inequalities")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_6(request)
    generate_solutions(problems)

def execute_seventh():
    print("These are the available topics for the 6th grade level: ")
    print("1. Inequalities")
    print("2. Percentages")
    print("3. Exponents")
    print("4. Square Roots")
    print("Difficulty Level Options: EASY, MEDIUM, HARD")
    request = input("Enter request here: ")
    problems = run_request_7(request)
    generate_solutions(problems)

def generate_solutions(problems):
    print("Here are the generated problems and solutions for each problem.")
    print("------------------")
    problem_index = 1
    for problem in problems:
        updated_problem = problem
        if "PERCENT:" in problem:
            updated_problem = problem.split(":")[1]
            values = updated_problem.split("*")
            percent = float(values[0])*100
            num = values[1]
            print(str(problem_index) + ". " + "What is " + str(percent) + " percent of" + str(num) + "?")
        elif "√" not in problem:
            print(str(problem_index) + ". " + updated_problem)
        solution = solution_generator(updated_problem)
        if "√" in problem:
            updated_problem = ""
            plus_split = problem.split("+")
            for i in range(len(plus_split)):
                num = plus_split[i].split("√")[0]
                num = float(num)
                if i == (len(plus_split)-1):
                    updated_problem += "√" + str(num)
                else:
                    updated_problem += "√" + str(num) + " + "
            print(str(problem_index) + ". " + updated_problem)
        if isinstance(solution, z3.RatNumRef):
            print("Solution: " + str(solution.as_decimal(3)))
        else:
            print("Solution: " + str(solution))
        print("------------------")
        problem_index += 1

def main():
    grade_level = input("Hello! Enter the grade level (K-7) for which you would like to generate problems: ")
    print("\nExcellent! Next, you MUST enter your request in this format: <number of topic>-<number of problems requested for that topic>-<difficulty level>.")
    print("\nFor instance, the request 1-10-EASY,2-20-MEDIUM means that the user wants 10 easy topic 1 problems and 20 medium topic 2 problems.")
    print("\nFrom the list below, choose which topics, how many questions per topic, and difficulty level per topic and format the request as specified.\n")
    if grade_level == "K":
        execute_kg()
    elif grade_level == "1":
        execute_first()
    elif grade_level == "2":
        execute_second()
    elif grade_level == "3":
        execute_third()
    elif grade_level == "4":
        execute_fourth()
    elif grade_level == "5":
        execute_fifth()
    elif grade_level == "6":
        execute_sixth()
    elif grade_level == "7":
        execute_seventh()
    
if __name__ == '__main__':
    main()