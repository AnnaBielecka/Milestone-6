from typing import List, Tuple

def find_sum_fast(target: int, li: List[int]) -> Tuple[int, int]:
    seen = {}  # Словник для збереження чисел та їхніх індексів
    
    for i, num in enumerate(li):
        difference = target - num
        
        if difference in seen:
            return (seen[difference], i)  # Якщо різниця вже була, повертаємо пару індексів
        
        seen[num] = i  # Додаємо поточний елемент у словник

# Приклад виклику функції
assert find_sum_fast(5, [1, 2, 3, 4, 5]) in {(0, 3), (1, 2)}

print(find_sum_fast(5, [1, 2, 3, 4, 5]))
print('O(n)')