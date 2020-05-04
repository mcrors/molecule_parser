from molecule_parser.molecule import Molecule
from molecule_parser.string_to_list_converter import string_to_list_converter
from molecule_parser.validators import validate_input
from . import MoleculeParserError


def molecule_parser(molecule: str) -> dict:
    """
    For a given chemical formula represented by a string,
    count the number of atoms of each element contained in the molecule
    and return a dict.

    :param molecule:
    :return: dict
    :raises: MoleculeParserError, NotValidElementError, InvalidEntryError
    """
    try:
        validate_input(molecule)
        molecule_as_list = string_to_list_converter(molecule)
        m = Molecule(molecule_as_list)
        return m.as_dict
    except MoleculeParserError:
        raise
