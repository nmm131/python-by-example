# 17_pathlib_os - Python by Example
from pathlib import Path
import os

def main():
    current = Path.cwd()
    print(f"Current directory: {current}")

    test_dir = current / "data" / "test_folder"
    test_dir.mkdir(exist_ok=True)

    file_path = test_dir / "info.txt"
    file_path.write_text("This file was created with pathlib!")

    print(f"\nCreated file: {file_path}")
    print(f"File exists? {file_path.exists()}")
    print(f"List in test_folder: {os.listdir(test_dir)}")

if __name__ == "__main__":
    main()
