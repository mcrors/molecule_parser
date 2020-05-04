from functools import wraps
from molecule_parser.errors import InvalidEntryError, NotValidElementError
from molecule_parser.elements import ELEMENTS


def validate_input(molecule: str):
    molecule = [item for item in molecule]
    if molecule.count('[') != molecule.count(']'):
        raise InvalidEntryError(f"Some brackets in the input string {molecule} "
                                f"were left unopened or unclosed")
    if molecule.count('{') != molecule.count('}'):
        raise InvalidEntryError(f"Some curlies in the input string {molecule} "
                                f"were left unopened or unclosed")
    if molecule.count('(') != molecule.count(')'):
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
