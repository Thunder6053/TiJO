from collections import Counter

def lottery(numbers, count):
    if not isinstance(numbers, list) or not isinstance(count, int):
        return []

    frequency = Counter(numbers)
    return [num for num, freq in frequency.items() if freq == count]


def generate_results():
    test_cases = [
        ([1, 1, 3, 2, 2, 2, 4, 5], 2),
        ([1, 1, 2, 2, 2, 3, 4, 5], 3),
        ([1, 2, 2, 2, 3, 4, 5, 5, 1], 2),
        (None, 1),
        ([1, 2, 3], None),
        (None, None),
        ([1, 1, 2, 2, 2, 3, 4, 5], 7)
    ]
    print(f"| {'PARAMETRY FUNKCJI LOTTERY':<30} | {'EFEKT DZIAŁANIA':<18} | {'REZULTAT':<10} |")
    print(f"|{'-'*32}|{'-'*20}|{'-'*12}|")

    for numbers, count in test_cases:
        result = lottery(numbers, count)
        print(f"| {str(numbers):<30} | {str(count):<18} | {str(result):<10} |")

if __name__ == "__main__":
    generate_results()