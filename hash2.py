import os
import hashlib

def generate_sha256(file_path):
    """Generate SHA-256 hash for a file."""
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

# List of files to check
files_to_check = ["test.txt", "all codes.txt","money.txt"]

for file_path in files_to_check:
    if os.path.isfile(file_path):
        print(f"{file_path}: {generate_sha256(file_path)}")
    else:
        print(f"{file_path} does not exist.")