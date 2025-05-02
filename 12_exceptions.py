# 12_exceptions - Python by Example

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"
    finally:
        print("Division attempt completed")

def main():
    print(divide(10, 2))
    print(divide(10, 0))
    print(divide(10, "a"))

if __name__ == "__main__":
    main()
