class Calculadora:
    def __init__(self):
        pass

    def somar(self, a: float, b: float):
        return a + b
    
    def subtrair(self, a: float, b: float):
        return a - b
    
    def multiplicar(self, a: float, b: float):
        return a * b
    
    def dividir(self, a: float, b: float):
        if b == 0:
            print("Impossivel dividir (divisão por zero)")
            return None
        else:
            return a / b
        
    def potencia(self, a: float, b: float):
        if b % 2 == 0 and a < 0:
            print("Impossivel dividir (divisão por zero)")
            return None
        else:
            return a ** b
    