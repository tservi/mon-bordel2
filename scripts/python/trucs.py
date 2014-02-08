# fonction factorielle sur une ligne
fact = lambda x: x>0 and x * fact(x-1) or 1

