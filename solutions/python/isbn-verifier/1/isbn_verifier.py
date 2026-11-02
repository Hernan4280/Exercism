def is_valid(isbn):
    cleaned = isbn.replace("-", "")
    if len(cleaned) != 10:
        return False
        
    total_sum = 0
    n = len(cleaned)
    
    for j in range(n):
        if j == 9 and cleaned[j] == 'X':
            digit = 10
        elif cleaned[j].isdigit():
            digit = int(cleaned[j])
        else:
            return False
        total_sum += digit * (n - j)
            
    return (total_sum % 11) == 0
