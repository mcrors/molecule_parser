from typing import Sequence


class Utils:

    @staticmethod
    def is_last_item(seq: Sequence, index: int) -> bool:
        return index + 1 >= len(seq)

    @staticmethod
    def next_item_is_num(seq: Sequence, index: int) -> bool:
        if not Utils.is_last_item(seq, index):
            return isinstance(seq[index + 1], int)
        return False
