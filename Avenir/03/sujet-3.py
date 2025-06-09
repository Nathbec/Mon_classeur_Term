def fibonacci(n):
    if n>=2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] 
    for i in range(len(eleves)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i] 
            meilleurs_eleves = [eleves[i]] 
    return (note_maxi, meilleurs_eleves)


