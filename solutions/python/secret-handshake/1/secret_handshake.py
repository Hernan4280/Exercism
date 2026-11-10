def commands(binary_str):
    secret_handshake = []
    actions = ["wink", "double blink", "close your eyes", "jump"]
    reversed_str = binary_str[::-1]
    
    for i in range(4):
        if reversed_str[i] == "1":
            secret_handshake.append(actions[i])
            
    if reversed_str[4] == "1":
        secret_handshake.reverse()
        
    return secret_handshake
