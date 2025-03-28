class Calculadora:
    def __init__(self):
        pass

    def somar(self, float: a, float: b):
        return a + b
    
    def subtrair(self, float: a, float: b):
        return a - b
    
    def multiplicar(self, float: a, float: b):
        return a * b
    
    def dividir(self, float: a, float: b):
        if b == 0:
            print("Impossivel dividir (divisão por zero)")
            return None
        else:
            return a / b