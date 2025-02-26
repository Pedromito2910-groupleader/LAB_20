'''
   Programador...: (C) 2025 Pedro Sousa
   Data..........: 17/02/2025
   Observações...: Estudo e análise acerca do scope das variáveis.

'''

x = 98

def procedimento1():
    x = 40
    print(x)

def procedimento2():
    x = 60 
    print(x)
   
procedimento1()
procedimento2()
print(x)