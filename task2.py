'''
The program is written to take an input from a user and write and append to the file
'''
file = "output.txt"
s1 = input("Enter text to write to file: ")
with open(file, "wt") as f:
    f.write(s1)
    print(f"Data successfully written to {file}")
s2 = input("Enter additional text to append : ")
with open(file, "at") as f:
    f.write(f"\n{s2}")
    print(f"Data successfully appended: ")
print(f"Final content of {file}")
with open(file, "rt") as f:
    content = f.readlines()
    for line in content:
        print(line.rstrip())