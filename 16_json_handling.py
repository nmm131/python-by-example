# 16_json_handling - Python by Example
import json

def main():
    data = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Linux", "Ansible"]
    }

    json_str = json.dumps(data, indent=4)
    print("Serialized JSON:")
    print(json_str)

    parsed = json.loads(json_str)
    print("\nDeserialized data:")
    print(parsed["skills"])

if __name__ == "__main__":
    main()
