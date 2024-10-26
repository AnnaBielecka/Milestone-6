def is_balanced(s: str) -> bool:
    balance = 0
    
    for char in s:
        if char == '(':
            balance += 1  # Increment for an opening parenthesis
        elif char == ')':
            balance -= 1  # Decrement for a closing parenthesis
            
        # If at any point balance goes negative, there's a closing parenthesis without a match
        if balance < 0:
            return False
    
    # The string is balanced if all opening parentheses have been matched
    return balance == 0
    

# Example usage
print(is_balanced('()'))    # True
print(is_balanced('())'))   # False
print(is_balanced('(()'))   # False
print(is_balanced(')())'))  # False