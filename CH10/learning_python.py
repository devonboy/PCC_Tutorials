# program modified by mike paddison on 27 Jan 2020.
#
# Comments added to clarify the underelying file read and printing
# method.
#
filename = 'learning_python.txt'

# Read in the file and write it as a single entity/varaiable

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

# Read in and write the file one line at a time.
# Open file as an object e.g. (f). Note that 'line' object does
# not exist outside the with block.

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

# Read the file into an object and then create the list accordingly.
# Print the list one line at a time. Note that the 'lines' list exists
# after the printing has been completed.

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())