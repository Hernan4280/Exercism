def classify(number):
    
    # if a number to be classified is less than 1.
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    aliquot_sum = sum(i for i in range(1, number) if number % i == 0)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"
