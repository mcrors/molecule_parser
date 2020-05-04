from molecule_parser.errors import InvalidEntryError, NotValidElementError
from molecule_parser.elements import ELEMENTS
from functools import wraps


def validate_input(molecule: str):
    molecule = [item for item in molecule]
    opening_brackets_count = molecule.count('[')
    closing_brackets_count = molecule.count(']')
    opening_curly_count = molecule.count('{')
    closing_curly_count = molecule.count('}')
    opening_parenthesis_count = molecule.count('(')
    closing_parenthesis_count = molecule.count(')')
    if opening_brackets_count != closing_brackets_count:
        raise InvalidEntryError(f"Some brackets in the input string {molecule} "
                                f"were left unopened or unclosed")
    if opening_curly_count != closing_curly_count:
        raise InvalidEntryError(f"Some curlies in the input string {molecule} "
                                f"were left unopened or unclosed")
    if opening_parenthesis_count != closing_parenthesis_count:
        raise InvalidEntryError(f"Some curlies in the input string {molecule} "
                                f"were left unopened or unclosed")


def validate_elements(func):
    @wraps(func)
    def validate_element(*args):
        result = func(*args)
        for element in result.keys():
            if element not in ELEMENTS:
                raise NotValidElementError(f"{element} is not a valid element")
        return result
    return validate_element
