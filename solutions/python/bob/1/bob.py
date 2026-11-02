def response(hey_bob):
    #Remove spaces at the beginning and at the end of the string
    current = hey_bob.strip()
    
    if current == "":
        return "Fine. Be that way!"
    if current[-1] == "?" and current.isupper():
        return "Calm down, I know what I'm doing!"
    if current[-1] == "?":
        return "Sure."
    if current.isupper():
        return "Whoa, chill out!"
    return "Whatever."
