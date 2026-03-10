'''
The program is written to read content of a file and handles the error while reading
'''
import os
file_list = [
    "sample.txt",
    "sample1.txt",
    ]

for i in file_list:
    if os.path.exists(i):
        with open(i) as f1:
            content = f1.readlines()
        print(f"========================\nThe file {i} exist\n========================")
        print("Printing file content:")
        x = 1
        for i in content:
            print(f'Line {x} : ', i.rstrip('\n'))
            x += 1
    else:
        print(f"========================\nThe file {i} was not found\n========================")

        break
