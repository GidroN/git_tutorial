import math
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

    def mod(x: int, y: int) -> int:
        return x % y

    def pi():
        return math.pi

def main():
    x, y = map(int, input('> ').split())
    calc = Calculator()
    print(calc.sub(x, y))
    print(calc.add(x, y))
    print(calc.mult(x, y))
    print(calc.div(x, y))
    print(calc.mod(x, y))
    print(calc.pi())

if __name__ == '__main__':
    main()
