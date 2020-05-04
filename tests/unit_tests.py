import pytest
from molecule_parser.molecule import Molecule
from molecule_parser.string_to_list_converter import capital_letter_followed_by_lower_case, \
    replace_parenthesis_with_brackets, string_to_list_converter, consume_items_from_iterator
from molecule_parser.validators import validate_input, validate_elements
from molecule_parser.errors import InvalidEntryError, NotValidElementError


class TestMoleculeShould:

    @staticmethod
    def test_can_extract_elements():
        molecule = Molecule(['H', 2, 'O'])
        expected = {
            'H': 2,
            'O': 1
        }
        assert molecule.elements == expected

    @staticmethod
    def test_can_extract_sub_molecules():
        molecule = Molecule(['H', 2, 'O', ['S', 'O'], 2])
        expected = {
            'S': 1,
            'O': 1
        }
        assert molecule.sub_molecules[0].elements == expected
        assert molecule.sub_molecules[1].elements == expected

    @staticmethod
    @pytest.mark.parametrize("molecule, expected", [
        (Molecule(['H', 2, 'O', ['S', 'O'], 2]),
         {'H': 2, 'O': 3, 'S': 2}),
        (Molecule(['K', 4, ['O', 'N', ['S', 'O', 3], 2], 2]),
         {'K': 4, 'O': 14, 'N': 2, 'S': 4})
    ])
    def test_as_dict_calculates_element_counts(molecule, expected):
        assert molecule.as_dict == expected


class TestStringToListConverterShould:

    @staticmethod
    @pytest.mark.parametrize("molecule, letter, index, expected", [
        ('Mg(OH)2', 'M', 0, True),
        ('Mg(OH)2', 'g', 1, False),
        ('Mg(OH)2', '2', 6, False),

    ])
    def test_identify_two_letter_elements(molecule, letter, index, expected):
        result = capital_letter_followed_by_lower_case(letter, index, molecule)
        assert result == expected

    @staticmethod
    def test_replace_parenthesis_and_curlys_with_brackets():
        molecule_as_string = 'K4{ON(SO3)2}2'
        expected = 'K4[ON[SO3]2]2'
        result = replace_parenthesis_with_brackets(molecule_as_string)
        assert expected == result

    @staticmethod
    @pytest.mark.parametrize('molecule, expected', [
        ('K4[ON[SO3]2]2', ['K', 4, ['O', 'N', ['S', 'O', 3], 2], 2]),
        ('Mg[OH]2', ['Mg', ['O', 'H'], 2])
    ])
    def test_converts_a_string_to_a_list(molecule, expected):
        result = string_to_list_converter(molecule)
        assert result == expected

    @staticmethod
    def test_consumes_an_iterator():
        string = 'ON[SO3]2'
        string_enumerator = enumerate(string)
        expected = '2'
        consume_items_from_iterator(string_enumerator, 7)
        assert next(string_enumerator)[1] == expected


class TestValidatorsShould:

    @staticmethod
    @pytest.mark.parametrize('input_string', [
        'Mg[fdasf',
        'Mg]fdasf',
        'Mg(fdasf',
        'Mg)fdasf',
        'Mg{fdasf',
        'Mg}fdasf'
    ])
    def test_raise_error_for_incorrect_parenthesis(input_string):
        with pytest.raises(InvalidEntryError):
            validate_input(input_string)
