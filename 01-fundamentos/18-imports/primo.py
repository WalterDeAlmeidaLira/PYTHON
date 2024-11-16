
''' 
    verifica se um númeor é primo!
'''

def primo(numero):
    if numero > 1:
        for x in range(2,numero):
            if(numero % x) == 0:
                return "Esse numero não é primo!"
        
        return "Esse número é primo!"
    else:
        return "Esse número não é primo!"