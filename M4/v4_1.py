from typing import List, Tuple

def find_sum(target: int, li: List[int]) -> set[int, int]:
    set_a = set()

    for i, numA in enumerate(li):
        for j, numB in enumerate(li):
            if numA + numB == target:
                set_a.add((i,j))
    return set_a

print(find_sum(5, [1, 2, 3, 4, 5]))
print('O(n**2)')