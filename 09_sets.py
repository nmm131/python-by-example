# 09_sets - Python by Example

def main():
    fruits = {"apple", "banana", "cherry"}
    print(f"Fruits set: {fruits}")

    fruits.add("orange")
    fruits.remove("banana")
    print(f"Updated fruits set: {fruits}")

if __name__ == "__main__":
    main()
