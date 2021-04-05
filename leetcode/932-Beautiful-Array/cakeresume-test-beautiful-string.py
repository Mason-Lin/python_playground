from collections import Counter


def isBeautifulString(inputString):
    counter = Counter(inputString)
    sorted_counter = sorted(counter)
    pre = counter[sorted_counter[0]] if sorted_counter[0] == "a" else 0
    for char in sorted_counter:
        if counter[char] > pre:
            return False
        else:
            pre = counter[char]
    else:
        return True


assert isBeautifulString("bbbaacdafe") is True
assert isBeautifulString("aabbb") is False
assert isBeautifulString("bbc") is False
assert isBeautifulString("zyy") is False
assert isBeautifulString("zaa") is False  # why!?????
