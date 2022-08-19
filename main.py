#! some module

class Calculator:
    
    def add(x: int, y: int) -> int:
        return x + y

    def sub(x: int, y: int) -> int:
        return x - y

    def mult(x: int, y: int) -> int:
        return x * y

    def div(x: int, y: int) -> int:
        if y == 0:
            raise ZeroDivisionError()
        return x // y

def main():
    x, y = map(int, input('> ').split())
    calc = Calculator()
    calc.sub(x, y)
    calc.add(x, y)
    calc.mult(x, y)
    calc.div(x, y)

if __name__ == '__main__':
    main()
