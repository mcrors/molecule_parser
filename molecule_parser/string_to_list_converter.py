from itertools import islice
import collections
from typing import List
from molecule_parser.utils import Utils


def replace_parenthesis_with_brackets(orginal: str) -> str:
    return orginal.replace('(', '[').\
        replace(')', ']').\
        replace('{', '[').\
        replace('}', ']')


def string_to_list_converter(convert_from: str) -> List:
    convert_from = replace_parenthesis_with_brackets(convert_from)
    convert_from_enumerator = enumerate(convert_from)
    result = []
    for index, item in convert_from_enumerator:
        if item.isalpha():
            if capital_letter_followed_by_lower_case(item, index, convert_from):
                result.append(item + convert_from[index+1])
            else:
                if item.islower():
                    continue
                result.append(item)
        if item.isdigit():
            result.append(int(item))
        if item == '[':
            end_index = convert_from.rfind(']')
            sub_string = convert_from[index+1:end_index]
            result.append(string_to_list_converter(sub_string))
            consume_items_from_iterator(convert_from_enumerator, len(sub_string))
    return result


def consume_items_from_iterator(iterator, n):
    if n is None:
        collections.deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def capital_letter_followed_by_lower_case(letter: str, index: int, word: str) -> bool:
    if Utils.is_last_item(word, index) or Utils.next_item_is_num(word, index):
        return False
    if letter.isupper() and word[index + 1].islower():
        return True
    return False


