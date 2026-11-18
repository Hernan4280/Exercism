def is_paired(input_string: str) -> bool:
    
    clean_str = "".join([i for i in input_string if i in "[]{}()"])
    
    while "()" in clean_str or "[]" in clean_str or "{}" in clean_str:
        clean_str = clean_str.replace("()", "")
        clean_str = clean_str.replace("[]", "")
        clean_str = clean_str.replace("{}", "")
        
    return clean_str == ""
