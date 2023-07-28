import os
import sys
import zipfile

# a. Create an array of a, b, c, d, e, f....z
alphabet = [chr(ord('a') + i) for i in range(26)]

# b. Based on this array, create txt files (a.txt, b.txt....)
def create_txt_files():
    for letter in alphabet:
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            file.write("This is a sample text for " + filename)

# c. Make sure all txt files are created and if not - fail the script
def verify_txt_files():
    for letter in alphabet:
        filename = f"{letter}.txt"
        if not os.path.exists(filename):
            print(f"ERROR: File '{filename}' is missing.")
            sys.exit(1)

# d. Create zip files with names based on array + VERSION environment variable, that each one will have one txt file inside
def create_zip_files(version):
    for letter in alphabet:
        filename = f"{letter}.txt"
        zip_filename = f"{letter}_{version}.zip"
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            zip_file.write(filename)

# e. Make sure all zip files are created and if not - fail the script
def verify_zip_files(version):
    for letter in alphabet:
        zip_filename = f"{letter}_{version}.zip"
        if not os.path.exists(zip_filename):
            print(f"ERROR: Zip file '{zip_filename}' is missing.")
            sys.exit(1)

if __name__ == "__main__":
    # f. Log all logs to console (stdout)
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)
    
    # Get the VERSION environment variable
    version = os.getenv("VERSION", "1.0.0")

    print(f"Running zip_job.py with VERSION={version}")

    # b. Based on this array, create txt files (a.txt, b.txt....)
    create_txt_files()

    # c. Make sure all txt files are created
    verify_txt_files()

    # d. Create zip files with names based on array + VERSION environment variable
    create_zip_files(version)

    # e. Make sure all zip files are created
    verify_zip_files(version)

    print("All operations completed successfully.")
