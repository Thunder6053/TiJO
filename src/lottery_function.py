from collections import Counter

def lottery (numbers,count):
    if not isinstance(numbers,list) or not isinstance(count,int):
        return []

    frequency = Counter(numbers)
    return [num for num,freq in frequency.items() if freq == count]