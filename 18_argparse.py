# 18_argparse - Python by Example
import argparse

def main():
    parser = argparse.ArgumentParser(description="Demo for argparse.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greeting", default="Hello", help="Custom greeting")

    args = parser.parse_args()
    print(f"{args.greeting}, {args.name}!")

if __name__ == "__main__":
    main()
