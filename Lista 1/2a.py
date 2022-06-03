memory = {
    "A": True,
    "C": True,
    "D": True,
    "E": True,
    "G": True,
    "H": True,
    "K": True
}

objective = {
    "Q": True
}

def verify(rules):
    for i in rules:
        if (not(i in memory)):
            return False
    # Se saiu do For todo mundo ta na memoria
    
    for i in rules:
        if(not (memory[i])):
            return False
    # E se sai desse for todo mundo e true

    return True
    

def rules():
    if verify(["K", "L", "M"]):
        memory["I"] = True
        return
    if (verify(["I", "L", "J"])):
        memory["Q"] =  True
        return
    if (verify(["C", "D", "E"])):
        memory["B"] = True
        return
    if(verify(["A", "B"])):
        memory["Q"] = True
        return
    if(verify(["L", "N", "O", "P"])):
        memory["Q"] = True
        return
    if(verify(["C", "H"])):
        memory["R"] = True
        return
    if(verify(["R","J","M"])):
        memory["S"] = True
        return
    if(verify(["F","H"])):
        memory["B"] = True
        return
    if(verify(["G"])):
        memory["F"] = True
        return

    