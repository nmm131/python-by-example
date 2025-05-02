# 04_if_else - Python by Example

def main():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    
    if age == 21:
        print("Happy 21st birthday!")
    elif age == 50:
        print("Half a century old!")
    else:
        print("Have a great day!")

if __name__ == "__main__":
    main()
