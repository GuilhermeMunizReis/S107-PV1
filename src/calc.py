class Calculadora:
    def __init__(self):
        self.__run()
    
    def __run(self):
        flag = True
        
        while flag:
            print('Escolha uma opção:')
            print('1 - Somar')
            print('2 - Subtrair')
            print('3 - Multiplicar')
            print('4 - Dividir')
            print('5 - Potência')
            print('6 - Sair')
            
            op = int(input())
            
            match op:
                case 1:
                    x = float(input())
                    y = float(input())
                    print(self.somar(x, y))
                case 2:
                    x = float(input())
                    y = float(input())
                    print(self.subtrair(x, y))
                case 3:        
                    x = float(input())
                    y = float(input())
                    print(self.multiplicar(x, y))
                case 4:
                    x = int(input())
                    y = int(input())
                    print(self.dividir(x, y))
                case 5:
                    x = int(input())
                    y = int(input())
                    print(self.potencia(x, y))
                case 6:
                    op = 6
                    flag = False
                case _:
                    print('Opção inválida. Tente novamente.')
            
            print()
            
            
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
    