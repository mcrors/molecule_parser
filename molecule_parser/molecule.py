from typing import List
from collections import Counter
from molecule_parser.utils import Utils
from molecule_parser.validators import validate_elements
from molecule_parser.errors import NotValidElementError


class Molecule:

    def __init__(self, molecule: List):
        self._molecule = molecule
        try:
            self._elements = self._extract_elements()
        except NotValidElementError:
            raise
        self._sub_molecules = self._extract_sub_molecules()

    def __repr__(self):
        return str(self._molecule)

    @property
    def as_dict(self):
        elements = Counter(self.elements)
        for molecule in self.sub_molecules:
            elements += molecule.as_dict
        return dict(elements)

    @property
    def elements(self):
        return self._elements

    @property
    def sub_molecules(self):
        return self._sub_molecules

    @validate_elements
    def _extract_elements(self):
        result = {}
        for index, item in enumerate(self._molecule):
            if isinstance(item, str):
                if Utils.next_item_is_num(self._molecule, index):
                    result[item] = int(self._molecule[index+1])
                else:
                    result[item] = 1
        return result

    def _extract_sub_molecules(self):
        result = []
        for index, item in enumerate(self._molecule):
            if isinstance(item, list):
                if Utils.next_item_is_num(self._molecule, index):
                    for _ in range(self._molecule[index+1]):
                        result.append(Molecule(item))
                else:
                    result.append(Molecule(item))
        return result
