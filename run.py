import sys
from os import path
import A

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    if not path.exists(input_file):
        print("File not found")
        sys.exit(1)
    A.main(input_file)