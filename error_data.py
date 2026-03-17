error_database = {

    "map_undefined": {
        "keywords": ["map", "undefined"],
        "why": "You are trying to use .map() on something that is undefined or null.",
        "causes": ["API data hasn't loaded yet", "Variable was never initialized", "Typo in variable name"],
        "fix": "Add a guard: array?.map(...) or initialize with an empty array: const items = data ?? []"
    },

    "index_error": {
        "keywords": ["indexerror", "index out of range", "list index out of range"],
        "why": "You are trying to access a position in a list that doesn't exist.",
        "causes": ["Loop iterating one step too many", "The list is empty", "Hardcoded index is wrong"],
        "fix": "Check the list length before accessing: if index < len(my_list): ..."
    },

    "key_error": {
        "keywords": ["keyerror"],
        "why": "You're accessing a dictionary key that doesn't exist.",
        "causes": ["Misspelled key name", "Key was never added to the dictionary", "API response changed structure"],
        "fix": "Use dict.get('key', default) to safely access keys, or check with 'key' in dict."
    },

    "syntax_error": {
        "keywords": ["syntaxerror", "unexpected eof", "invalid syntax"],
        "why": "Python can't understand your code because of a writing mistake.",
        "causes": ["Missing closing parenthesis, bracket, or quote", "Bad indentation", "Using Python 2 syntax in Python 3"],
        "fix": "Look at the line number in the error. Check for unclosed brackets or quotes above that line."
    },

    "type_error": {
        "keywords": ["typeerror", "unsupported operand", "not subscriptable", "object is not callable"],
        "why": "You're performing an operation on the wrong type of value.",
        "causes": ["Adding a string and integer together", "Calling something that isn't a function", "Passing wrong type to a function"],
        "fix": "Check variable types with type(variable) and convert if needed: int(x) or str(x)."
    },

    "name_error": {
        "keywords": ["nameerror", "is not defined"],
        "why": "You're using a variable or function name that Python doesn't recognize.",
        "causes": ["Typo in the variable name", "Variable used before it was created", "Forgot to import a module"],
        "fix": "Check spelling of the variable. Make sure it's defined before use. Add missing import statements."
    },

    "attribute_error": {
        "keywords": ["attributeerror", "has no attribute"],
        "why": "You're trying to access a property or method that doesn't exist on this object.",
        "causes": ["Typo in the attribute name", "Using the wrong type of object", "Variable is None when you expect an object"],
        "fix": "Use dir(object) to see available attributes. Check for None with: if obj is not None:"
    },

    "value_error": {
        "keywords": ["valueerror", "invalid literal", "could not convert"],
        "why": "The value you provided is the right type, but an inappropriate value.",
        "causes": ["Converting a non-numeric string to int/float", "Passing an out-of-range value", "Wrong format for parsing"],
        "fix": "Validate input before converting. Wrap in try/except: try: int(x) except ValueError: ..."
    },

    "import_error": {
        "keywords": ["importerror", "modulenotfounderror", "no module named"],
        "why": "Python can't find the module you're trying to import.",
        "causes": ["Package not installed", "Typo in the module name", "Wrong Python environment active"],
        "fix": "Install the package: pip install package-name. Make sure you're in the right virtual environment."
    },

    "none_type_error": {
        "keywords": ["nonetype", "attributeerror: 'nonetype'"],
        "why": "You're trying to use a variable that is None as if it has a value.",
        "causes": ["Function returned None instead of a value", "Variable was never assigned", "Failed DB/API call returned nothing"],
        "fix": "Add a None check: if result is not None: before using the variable."
    },

    "recursion_error": {
        "keywords": ["recursionerror", "maximum recursion depth", "stack overflow"],
        "why": "A function is calling itself too many times without stopping.",
        "causes": ["Missing base case in a recursive function", "Circular references between objects", "Infinite loop disguised as recursion"],
        "fix": "Make sure your recursive function has a clear base case that stops the recursion."
    },

    "zero_division": {
        "keywords": ["zerodivisionerror", "division by zero"],
        "why": "Your code is trying to divide a number by zero.",
        "causes": ["Denominator variable is 0", "User input was 0 without validation", "Calculation resulted in 0 unexpectedly"],
        "fix": "Check before dividing: if divisor != 0: result = a / divisor"
    },

    "file_not_found": {
        "keywords": ["filenotfounderror", "no such file", "errno 2"],
        "why": "Python can't find the file you're trying to open.",
        "causes": ["Wrong file path or filename", "File is in a different directory", "File was deleted or never created"],
        "fix": "Print the path with os.path.abspath(path) to see where Python is looking."
    },

    "indentation_error": {
        "keywords": ["indentationerror", "unexpected indent", "expected an indented block"],
        "why": "Your code's indentation is inconsistent or wrong.",
        "causes": ["Mixing tabs and spaces", "Missing indented block after if/for/def", "Extra or missing spaces"],
        "fix": "Use only spaces (4 per level) consistently. Configure your editor to show whitespace."
    },

    "connection_error": {
        "keywords": ["connectionerror", "connection refused", "connection timed out", "timeout"],
        "why": "Your code couldn't connect to a server or network resource.",
        "causes": ["Server is not running", "Wrong URL or port", "Firewall blocking the connection"],
        "fix": "Check the server is running and the URL/port is correct. Add proper timeout handling."
    }
}