class MoleculeParserError(Exception):
    pass


class NotValidElementError(MoleculeParserError):
    pass


class InvalidEntryError(MoleculeParserError):
    pass
