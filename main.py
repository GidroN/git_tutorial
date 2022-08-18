#! some module

def sum(x: int, y: int) -> int:
    return x + y


def main():
    x, y = map(int, input('> ').split())
    sum()


if __name__ == '__main__':
    main()