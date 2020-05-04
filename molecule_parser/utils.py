from typing import Sequence


class Utils:

    @staticmethod
    def is_last_item(seq: Sequence, index: int) -> bool:
        return index + 1 >= len(seq)
