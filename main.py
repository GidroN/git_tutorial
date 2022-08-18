#! some module

def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y

def main():
    x, y = map(int, input('> ').split())
    sub()
    add()

if __name__ == '__main__':
    main()
