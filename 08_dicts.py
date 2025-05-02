# 08_dicts - Python by Example

def main():
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print(f"Person's name: {person['name']}")

    person["job"] = "Engineer"
    del person["age"]
    print(f"Updated person: {person}")

if __name__ == "__main__":
    main()
