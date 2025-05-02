# 07_lists - Python by Example

def main():
    fruits = ["apple", "banana", "cherry"]
    print(f"List of fruits: {fruits}")

    fruits.append("orange")
    fruits.remove("banana")
    print(f"Updated fruits: {fruits}")

    print(f"First two fruits: {fruits[:2]}")

if __name__ == "__main__":
    main()
