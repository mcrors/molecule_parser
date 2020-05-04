import pytest
from molecule_parser import molecule_parser, NotValidElementError


def test_can_parse_water():
    water = "H2O"
    result = molecule_parser(water)
    expected = {"H": 2, "O": 1}
    assert result == expected


def test_can_parse_nigtrogen():
    nitrogen = "N2"
    result = molecule_parser(nitrogen)
    expected = {"N": 2}
    assert result == expected


def test_can_parse_magnesium_hydride():
    magnesium_hydride = "MgH2OFe"
    result = molecule_parser(magnesium_hydride)
    expected = {
        "Mg": 1,
        "H": 2,
        "O": 1,
        "Fe": 1
    }
    assert result == expected


def test_can_parse_magnesium_hydroxide():
    magnesium_hydroxide = "Mg(OH)2"
    result = molecule_parser(magnesium_hydroxide)
    expected = {
        "Mg": 1,
        "O": 2,
        "H": 2
    }
    assert result == expected


def test_can_parse_fermy_salt():
    fremy_salt = 'K4[ON(SO3)2]2'
    result = molecule_parser(fremy_salt)
    expected = {
        'K': 4,
        'O': 14,
        'N': 2,
        'S': 4}
    assert result == expected


@pytest.mark.parametrize('not_an_element', [
    'Gh', 'Ro', 'Q'
])
def test_raises_error_for_values_that_are_not_elements(not_an_element):
    with pytest.raises(NotValidElementError):
        molecule_parser(not_an_element)
