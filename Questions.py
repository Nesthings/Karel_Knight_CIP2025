import random

questions = [
    {
        "pregunta": "What does CPU stand for?",
        "opciones": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility"],
        "respuesta_correcta": "Central Processing Unit"
    },
    {
        "pregunta": "What does RAM stand for?",
        "opciones": ["Random Access Memory", "Read And Modify", "Rapid Action Module"],
        "respuesta_correcta": "Random Access Memory"
    },
    {
        "pregunta": "Which programming language is known for its simplicity and readability?",
        "opciones": ["C++", "Python", "Assembly"],
        "respuesta_correcta": "Python"
    },
    {
        "pregunta": "Which of the following is a valid variable name in Python?",
        "opciones": ["2variable", "my_variable", "my-variable"],
        "respuesta_correcta": "my_variable"
    },
    {
        "pregunta": "What does HTML stand for?",
        "opciones": ["HyperText Markup Language", "High-Level Text Management", "Hyper Transfer Machine Language"],
        "respuesta_correcta": "HyperText Markup Language"
    },
    {
        "pregunta": "Which symbol is used for single-line comments in Python?",
        "opciones": ["//", "#", "--"],
        "respuesta_correcta": "#"
    },
    {
        "pregunta": "Which of the following is NOT a programming language?",
        "opciones": ["Java", "HTML", "Python"],
        "respuesta_correcta": "HTML"
    },
    {
        "pregunta": "Which function is used to display output in Python?",
        "opciones": ["echo()", "print()", "display()"],
        "respuesta_correcta": "print()"
    },
    {
        "pregunta": "Which of the following is a loop structure in Python?",
        "opciones": ["if", "while", "switch"],
        "respuesta_correcta": "while"
    },
    {
        "pregunta": "What does IDE stand for?",
        "opciones": ["Integrated Development Environment", "Internal Debugging Engine", "Interactive Data Editor"],
        "respuesta_correcta": "Integrated Development Environment"
    },
    {
        "pregunta": "Which of the following is used to store multiple values in Python?",
        "opciones": ["Variable", "List", "Function"],
        "respuesta_correcta": "List"
    },
    {
        "pregunta": "Which operator is used for exponentiation in Python?",
        "opciones": ["^", "**", "^^"],
        "respuesta_correcta": "**"
    },
    {
        "pregunta": "Which of the following is a valid way to declare a function in Python?",
        "opciones": ["function myFunc():", "def myFunc():", "declare myFunc():"],
        "respuesta_correcta": "def myFunc():"
    },
    {
        "pregunta": "Which keyword is used to define a class in Python?",
        "opciones": ["class", "define", "struct"],
        "respuesta_correcta": "class"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python data type?",
        "opciones": ["int", "float", "character"],
        "respuesta_correcta": "character"
    },
    {
        "pregunta": "Which of the following is used to check conditions in Python?",
        "opciones": ["if", "for", "print"],
        "respuesta_correcta": "if"
    },
    {
        "pregunta": "Which data structure follows FIFO (First In, First Out)?",
        "opciones": ["Stack", "Queue", "Linked List"],
        "respuesta_correcta": "Queue"
    },
    {
        "pregunta": "What is the main function of a compiler?",
        "opciones": ["Execute the code", "Translate source code into machine code", "Debug the program"],
        "respuesta_correcta": "Translate source code into machine code"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python module?",
        "opciones": ["math", "random", "system"],
        "respuesta_correcta": "system"
    },
    {
        "pregunta": "Which of the following is used to remove an element from a list in Python?",
        "opciones": ["delete()", "remove()", "erase()"],
        "respuesta_correcta": "remove()"
    },
    {
        "pregunta": "Which of the following is NOT a valid way to iterate over a list in Python?",
        "opciones": ["for item in list:", "while item in list:", "for i in range(len(list)):"],
        "respuesta_correcta": "while item in list:"
    },
    {
        "pregunta": "Which of the following is used to create a dictionary in Python?",
        "opciones": ["{}", "[]", "dict()"],
        "respuesta_correcta": "dict()"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python built-in function?",
        "opciones": ["len()", "sum()", "count()"],
        "respuesta_correcta": "count()"
    },
    {
        "pregunta": "Which of the following is used to check if a key exists in a dictionary?",
        "opciones": ["dict.has_key()", "'key' in dict", "dict.contains('key')"],
        "respuesta_correcta": "'key' in dict"
    },
    {
        "pregunta": "Which of the following is NOT a valid way to concatenate strings in Python?",
        "opciones": ["'Hello' + 'World'", "'Hello'.join('World')", "'Hello' + ' ' + 'World'"],
        "respuesta_correcta": "'Hello'.join('World')"
    },
    {
        "pregunta": "Which of the following is used to convert a string to an integer in Python?",
        "opciones": ["int()", "str()", "float()"],
        "respuesta_correcta": "int()"
    },
    {
        "pregunta": "Which of the following is NOT a valid way to define a lambda function in Python?",
        "opciones": ["lambda x: x * 2", "def lambda(x): return x * 2", "lambda x, y: x + y"],
        "respuesta_correcta": "def lambda(x): return x * 2"
    },
    {
        "pregunta": "Which of the following is used to terminate a loop in Python?",
        "opciones": ["break", "exit", "stop"],
        "respuesta_correcta": "break"
    },
    {
        "pregunta": "Which of the following is used to get user input in Python?",
        "opciones": ["input()", "get()", "read()"],
        "respuesta_correcta": "input()"
    },
    {
        "pregunta": "Which of the following is a valid way to declare a string in Python?",
        "opciones": ["string x = 'Hello'", "x = 'Hello'", "str x = 'Hello'"],
        "respuesta_correcta": "x = 'Hello'"
    },
    {
        "pregunta": "Which keyword is used to define a function in Python?",
        "opciones": ["func", "define", "def"],
        "respuesta_correcta": "def"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python loop?",
        "opciones": ["for", "while", "repeat"],
        "respuesta_correcta": "repeat"
    },
    {
        "pregunta": "Which of the following is used to check equality in Python?",
        "opciones": ["=", "==", "==="],
        "respuesta_correcta": "=="
    },
    {
        "pregunta": "Which of the following is used to create a comment in Python?",
        "opciones": ["//", "#", "/* */"],
        "respuesta_correcta": "#"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python operator?",
        "opciones": ["+", "-", "&&"],
        "respuesta_correcta": "&&"
    },
    {
        "pregunta": "Which function is used to find the length of a list in Python?",
        "opciones": ["size()", "length()", "len()"],
        "respuesta_correcta": "len()"
    },
    {
        "pregunta": "Which of the following is used to convert an integer to a string in Python?",
        "opciones": ["str()", "int()", "convert()"],
        "respuesta_correcta": "str()"
    },
    {
        "pregunta": "Which of the following is NOT a valid Python data type?",
        "opciones": ["list", "array", "tuple"],
        "respuesta_correcta": "array"
    },
    {
        "pregunta": "Which of the following is used to exit a loop in Python?",
        "opciones": ["stop", "exit", "break"],
        "respuesta_correcta": "break"
    },
    {
        "pregunta": "Which of the following is used to check if a value exists in a list?",
        "opciones": ["in", "exists", "contains"],
        "respuesta_correcta": "in"
    },
    {
        "pregunta": "Which of the following is used to create an empty list in Python?",
        "opciones": ["[]", "list()", "both"],
        "respuesta_correcta": "both"
    },
    {
        "pregunta": "Which of the following is used to round a number in Python?",
        "opciones": ["round()", "ceil()", "floor()"],
        "respuesta_correcta": "round()"
    },
    {
        "pregunta": "Which of the following is used to import a module in Python?",
        "opciones": ["import", "include", "require"],
        "respuesta_correcta": "import"
    },
    {
        "pregunta": "Which of the following is NOT a valid way to declare a list in Python?",
        "opciones": ["[1, 2, 3]", "list(1, 2, 3)", "list([1, 2, 3])"],
        "respuesta_correcta": "list(1, 2, 3)"
    },
    {
        "pregunta": "Which of the following is used to remove the last element from a list?",
        "opciones": ["pop()", "remove()", "delete()"],
        "respuesta_correcta": "pop()"
    },
    {
        "pregunta": "Which of the following is used to get the first element of a list?",
        "opciones": ["list[0]", "list.first()", "list.get(0)"],
        "respuesta_correcta": "list[0]"
    },
    {
        "pregunta": "Which of the following is used to check if a number is even?",
        "opciones": ["num % 2 == 0", "num / 2 == 0", "num // 2 == 0"],
        "respuesta_correcta": "num % 2 == 0"
    },
    {
        "pregunta": "Which of the following is used to create a tuple?",
        "opciones": ["()", "[]", "{}"],
        "respuesta_correcta": "()"
    },
    {
        "pregunta": "Which of the following is used to convert a string to lowercase?",
        "opciones": ["lower()", "downcase()", "small()"],
        "respuesta_correcta": "lower()"
    },
    {
        "pregunta": "Which of the following is used to check the type of a variable?",
        "opciones": ["typeof()", "type()", "checktype()"],
        "respuesta_correcta": "type()"
    },
    {
        "pregunta": "Which of the following is used to remove whitespace from a string?",
        "opciones": ["strip()", "trim()", "clean()"],
        "respuesta_correcta": "strip()"
    },
    {
        "pregunta": "Which of the following is used to replace text in a string?",
        "opciones": ["replace()", "sub()", "change()"],
        "respuesta_correcta": "replace()"
    },
    {
        "pregunta": "Which of the following is used to split a string into a list?",
        "opciones": ["split()", "divide()", "cut()"],
        "respuesta_correcta": "split()"
    },
    {
        "pregunta": "Which of the following is used to join elements of a list into a string?",
        "opciones": ["join()", "concat()", "merge()"],
        "respuesta_correcta": "join()"
    },
    {
        "pregunta": "Which of the following is used to check if a string starts with a specific character?",
        "opciones": ["startswith()", "beginswith()", "first()"],
        "respuesta_correcta": "startswith()"
    },
    {
        "pregunta": "Which of the following is used to check if a string ends with a specific character?",
        "opciones": ["endswith()", "finish()", "last()"],
        "respuesta_correcta": "endswith()"
    },
    {
        "pregunta": "Which of the following is used to capitalize the first letter of a string?",
        "opciones": ["capitalize()", "upper()", "title()"],
        "respuesta_correcta": "capitalize()"
    },
    {
        "pregunta": "Which of the following is used to declare a boolean variable in Python?",
        "opciones": ["bool x = True", "x = True", "boolean x = True"],
        "respuesta_correcta": "x = True"
    },
    {
        "pregunta": "Which function is used to take user input in Python?",
        "opciones": ["input()", "get()", "read()"],
        "respuesta_correcta": "input()"
    },
    {
        "pregunta": "Which of the following is used to check if a number is odd?",
        "opciones": ["num % 2 == 1", "num / 2 != 0", "num // 2 == 1"],
        "respuesta_correcta": "num % 2 == 1"
    },
    {
        "pregunta": "Which of the following is used to convert a string to uppercase?",
        "opciones": ["upper()", "capitalize()", "big()"],
        "respuesta_correcta": "upper()"
    },
    {
        "pregunta": "Which of the following is used to find the maximum value in a list?",
        "opciones": ["max()", "highest()", "top()"],
        "respuesta_correcta": "max()"
    },
    {
        "pregunta": "Which of the following is used to find the minimum value in a list?",
        "opciones": ["min()", "lowest()", "bottom()"],
        "respuesta_correcta": "min()"
    },
    {
        "pregunta": "Which of the following is used to remove all elements from a list?",
        "opciones": ["clear()", "delete()", "removeAll()"],
        "respuesta_correcta": "clear()"
    },
    {
        "pregunta": "Which of the following is used to reverse a list?",
        "opciones": ["reverse()", "flip()", "invert()"],
        "respuesta_correcta": "reverse()"
    },
    {
        "pregunta": "Which of the following is used to sort a list in ascending order?",
        "opciones": ["sort()", "order()", "arrange()"],
        "respuesta_correcta": "sort()"
    },
    {
        "pregunta": "Which of the following is used to sort a list in descending order?",
        "opciones": ["sort(reverse=True)", "order(desc)", "arrange(desc)"],
        "respuesta_correcta": "sort(reverse=True)"
    },
    {
        "pregunta": "Which of the following is used to check if a list is empty?",
        "opciones": ["len(list) == 0", "list.isEmpty()", "list == None"],
        "respuesta_correcta": "len(list) == 0"
    },
    {
        "pregunta": "Which of the following is used to copy a list?",
        "opciones": ["list.copy()", "clone(list)", "duplicate(list)"],
        "respuesta_correcta": "list.copy()"
    },
    {
        "pregunta": "Which of the following is used to merge two lists?",
        "opciones": ["list1 + list2", "merge(list1, list2)", "combine(list1, list2)"],
        "respuesta_correcta": "list1 + list2"
    },
    {
        "pregunta": "Which of the following is used to check if a string contains a specific substring?",
        "opciones": ["'substring' in string", "string.contains('substring')", "check(string, 'substring')"],
        "respuesta_correcta": "'substring' in string"
    },
    {
        "pregunta": "Which of the following is used to remove a specific character from a string?",
        "opciones": ["replace('char', '')", "delete('char')", "remove('char')"],
        "respuesta_correcta": "replace('char', '')"
    },
    {
        "pregunta": "Which of the following is used to repeat a string multiple times?",
        "opciones": ["string * 3", "repeat(string, 3)", "string.repeat(3)"],
        "respuesta_correcta": "string * 3"
    },
    {
        "pregunta": "Which of the following is used to check if a string is empty?",
        "opciones": ["len(string) == 0", "string.isEmpty()", "string == None"],
        "respuesta_correcta": "len(string) == 0"
    },
    {
        "pregunta": "Which of the following is used to remove the first element from a list?",
        "opciones": ["list.pop(0)", "list.removeFirst()", "list.delete(0)"],
        "respuesta_correcta": "list.pop(0)"
    },
    {
        "pregunta": "Which of the following is used to check if a number is positive?",
        "opciones": ["num > 0", "num >= 0", "num == positive"],
        "respuesta_correcta": "num > 0"
    },
    {
        "pregunta": "Which of the following is used to check if a number is negative?",
        "opciones": ["num < 0", "num <= 0", "num == negative"],
        "respuesta_correcta": "num < 0"
    },
    {
        "pregunta": "Which of the following is used to check if a number is zero?",
        "opciones": ["num == 0", "num <= 0", "num != 0"],
        "respuesta_correcta": "num == 0"
    },
    {
        "pregunta": "Which of the following is used to swap two variables in Python?",
        "opciones": ["x, y = y, x", "swap(x, y)", "x = y; y = x"],
        "respuesta_correcta": "x, y = y, x"
    },
    {
        "pregunta": "Which of the following is used to check if a list contains a specific value?",
        "opciones": ["value in list", "list.contains(value)", "check(list, value)"],
        "respuesta_correcta": "value in list"
    },
    {
        "pregunta": "Which of the following is used to get the last element of a list?",
        "opciones": ["list[-1]", "list.last()", "list.getLast()"],
        "respuesta_correcta": "list[-1]"
    },
    {
        "pregunta": "Which of the following is used to remove duplicates from a list?",
        "opciones": ["list(set(list))", "removeDuplicates(list)", "list.unique()"],
        "respuesta_correcta": "list(set(list))"
    },
    {
        "pregunta": "Which of the following is used to check if a string is numeric?",
        "opciones": ["string.isdigit()", "string.isnumeric()", "string.isNumber()"],
        "respuesta_correcta": "string.isdigit()"
    },
    {
        "pregunta": "Which of the following is used to convert a list into a set?",
        "opciones": ["set(list)", "convertToSet(list)", "list.toSet()"],
        "respuesta_correcta": "set(list)"
    },
    {
        "pregunta": "Which of the following is used to check if a set contains a specific value?",
        "opciones": ["value in set", "set.contains(value)", "check(set, value)"],
        "respuesta_correcta": "value in set"
    },
    {
        "pregunta": "Which of the following is used to get the length of a set?",
        "opciones": ["len(set)", "set.length()", "size(set)"],
        "respuesta_correcta": "len(set)"
    },
    {
        "pregunta": "Which of the following is used to add an element to a set?",
        "opciones": ["set.add(value)", "set.append(value)", "set.insert(value)"],
        "respuesta_correcta": "set.add(value)"
    },
    {
        "pregunta": "Which of the following is used to remove an element from a set?",
        "opciones": ["set.remove(value)", "set.delete(value)", "set.pop(value)"],
        "respuesta_correcta": "set.remove(value)"
    },
    {
        "pregunta": "Which of the following is used to clear all elements from a set?",
        "opciones": ["set.clear()", "set.empty()", "set.removeAll()"],
        "respuesta_correcta": "set.clear()"
    },
    {
        "pregunta": "Which of the following is used to merge two sets?",
        "opciones": ["set1.union(set2)", "merge(set1, set2)", "set1 + set2"],
        "respuesta_correcta": "set1.union(set2)"
    },
    {
        "pregunta": "Which of the following is used to find the intersection of two sets?",
        "opciones": ["set1.intersection(set2)", "set1 & set2", "set1.common(set2)"],
        "respuesta_correcta": "set1.intersection(set2)"
    },
    {
        "pregunta": "Which of the following is used to find the difference between two sets?",
        "opciones": ["set1.difference(set2)", "set1 - set2", "set1.subtract(set2)"],
        "respuesta_correcta": "set1.difference(set2)"
    },
    {
        "pregunta": "Which of the following is used to check if a set is a subset of another?",
        "opciones": ["set1.issubset(set2)", "set1 < set2", "set1.isSubset(set2)"],
        "respuesta_correcta": "set1.issubset(set2)"
    },
    {
        "pregunta": "Which of the following is used to check if a set is a superset of another?",
        "opciones": ["set1.issuperset(set2)", "set1 > set2", "set1.isSuperset(set2)"],
        "respuesta_correcta": "set1.issuperset(set2)"
    }
]

def obtener_pregunta_aleatoria():
    return random.choice(questions)  # Retorna una pregunta aleatoria