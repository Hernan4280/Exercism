def slices(series: str, length: int) -> list[str]:
    
    n: int = len(series)
    
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if n == 0:
        raise ValueError("series cannot be empty")
    if n < length:
        raise ValueError("slice length cannot be greater than series length")
        
    return [series[i:i + length] for i in range(n - (length - 1))]
