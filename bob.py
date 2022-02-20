def response(hey_bob):
    if hey_bob.endswith("?") == True or hey_bob.endswith("?   ") :
        if hey_bob.isupper() == True:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif  hey_bob.isupper() == True:
        return "Whoa, chill out!"
    elif (not (hey_bob and not hey_bob.isspace())):
        return "Fine. Be that way!"
    else:
        
        return "Whatever."