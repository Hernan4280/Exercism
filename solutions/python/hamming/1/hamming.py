def distance(strand_a, strand_b):
    n = len(strand_a)
    
    if n != len(strand_b):
        raise ValueError("Strands must be of equal length.")
        
    return sum(1 for i in range(n) if strand_a[i] != strand_b[i])
