error_database = {

    "map_undefined": {
        "keywords": ["map", "undefined"],
        "why": "You are trying to use .map() on something that is undefined.",
        "causes": [
            "API data not loaded yet",
            "Variable not initialized",
            "Typo in variable name"
        ],
        "fix": "Initialize the variable with an empty list before using map."
    },

    "index_error": {
        "keywords": ["indexerror", "out of range"],
        "why": "You are trying to access an index that does not exist in a list.",
        "causes": [
            "Loop going out of range",
            "List is empty",
            "Wrong index number"
        ],
        "fix": "Check the length of the list before accessing elements."
    },
    "key_error": {
        "keywords": ["keyerror"],
        "why": "You are trying to access a dictionary key that does not exist.",
        "causes": [
            "Misspelled key",
            "Key not present in dictionary"
        ],
        "fix": "Use dictionary.get('key') or check if the key exists."
    },
    "syntax_error": {
    "keywords": ["syntaxerror", "unexpected eof", "invalid syntax"],
    "why": "There is a mistake in how your code is written.",
    "causes": [
        "Missing parenthesis",
        "Missing quotation mark",
        "Improper indentation"
    ],
    "fix": "Carefully check the line mentioned in the error and fix the syntax."
}

}
