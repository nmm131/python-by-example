# 05_loops - Python by Example

def main():
    for i in range(5):
        print(f"Iteration {i}")
    
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(f"I love {fruit}")
    
    count = 0
    while count < 3:
        print(f"Count is {count}")
        count += 1

if __name__ == "__main__":
    main()
