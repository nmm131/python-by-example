# 11_comprehensions - Python by Example

def main():
    numbers = [x for x in range(10)]
    print(f"Numbers: {numbers}")

    even_numbers = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")

    squares = {x: x**2 for x in range(5)}
    print(f"Squares: {squares}")

if __name__ == "__main__":
    main()
