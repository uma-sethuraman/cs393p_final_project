import lark
import z3
import math

# DSL/Interpreter/Synthesis Techniques based on:
# https://github.com/lark-parser/lark/wiki/Examples
# https://www.cs.cornell.edu/~asampson/blog/minisynth.html
GRAMMAR = """
?start: sum
  | sum "?" sum ":" sum -> if
?sum: term
  | sum "+" term        -> add
  | sum "-" term        -> subtract
?term: item
  | term "*"  item      -> multiply
  | term "/"  item      -> divide
  | term "^" item       -> exponent
  | term "<" item       -> less
  | term "<=" item      -> less_eq
  | term ">" item       -> greater
  | term ">=" item      -> greater_eq
  | term "√" item       -> sqrt
?item: NUMBER           -> number
  | "-" item            -> negative
  | CNAME               -> variable
  | "(" start ")"
%import common.CNAME
%import common.NUMBER
%import common.WS
%ignore WS
""".strip()

lookup = {}

def interpreter(tree, lookup):
    operator = tree.data
    valid_operations = ['add', 'subtract', 'multiply', 'divide', 'exponent', 'less', 'less_eq', 'greater', 'greater_eq', 'sqrt']
    if operator in valid_operations:
        before_operator_nums = tree.children[0]
        after_operator_nums = tree.children[1]
        before_operator = interpreter(before_operator_nums, lookup)
        after_operator = interpreter(after_operator_nums, lookup)
        return convert_operation(operator, before_operator, after_operator)
    elif operator == 'negative':
        before_operator_nums = tree.children[0]
        return -1 * interpreter(before_operator_nums, lookup)
    elif operator == 'number':
        before_operator_nums = tree.children[0]
        return float(before_operator_nums)
    
def convert_operation(operator, before_operator, after_operator):
    if operator == 'add':
        return before_operator + after_operator
    elif operator == 'subtract':
        return before_operator - after_operator
    elif operator == 'multiply':
        return before_operator * after_operator
    elif operator == 'divide':
        return before_operator / after_operator
    elif operator == 'exponent':
        return pow(before_operator, after_operator)
    elif operator == 'less':
        return before_operator < after_operator
    elif operator == 'less_eq':
        return before_operator <= after_operator
    elif operator == 'greater':
        return before_operator > after_operator
    elif operator == 'greater_eq':
        return before_operator >= after_operator
    elif operator == 'sqrt':
        return math.sqrt(before_operator)

def synthesize_solution(problem):
    converted_problem = interpreter(problem, interpreter_lookup)
    if isinstance(converted_problem, bool):
        s = z3.Solver() # creating the program to solve the problem
        s.add(converted_problem) # constraints based on the expression
        s.check()
        return converted_problem
    else:
        s = z3.Solver() # creating the program to solve the problem
        s.add((z3.Real('output') == (converted_problem))) # constraints based on the expression
        s.check()
        return s.model()

def interpreter_lookup(elem):
    if elem not in lookup:
        width = 20
        lookup[elem] = z3.BitVec(elem, width)
    return lookup[elem]

def solution_generator(problem):
    model = synthesize_solution(lark.Lark(GRAMMAR).parse(problem))
    if isinstance(model, bool):
        return model
    else:
        correct_output = None
        for i in range(len(model.decls())):
            if model.decls()[i].name() == "output":
                correct_output = model[model.decls()[i]]
        return correct_output