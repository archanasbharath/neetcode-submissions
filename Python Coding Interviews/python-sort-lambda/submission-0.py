from typing import List

def get_wlen(word:str):
    return len(word)
def sort_words(words: List[str]) -> List[str]:
    output = sorted(words,key = lambda x : len(x),reverse=True)
    return output


def sort_numbers(numbers: List[int]) -> List[int]:
    output = sorted(numbers, key = lambda x: abs(x))
    return output


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
