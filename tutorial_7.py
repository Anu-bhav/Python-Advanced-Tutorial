# Python Subprocess Module to Execute Shell Commands

import subprocess

# subprocess.run("dir", shell=True)  #windows
p1 = subprocess.run("ls -la", capture_output=True)

# prints supplied arguments
print("Arguments: ", p1.args)

# if returncode == 0, then 0 errors
print("returncode: ", p1.returncode)
print()

# the stdout is captured as bytes
print("Output as bytes")
print(p1.stdout)
print()
# decoding bytes to normal text
print("Decoded output to utf-8")
print(p1.stdout.decode("utf-8"))
print()

# to display output as text without decoding
# text=True will get string instead of bytes
p2 = subprocess.run("ls -la", capture_output=True, text=True)
print("Output using text=True")
print(p2.stdout)
print()

# in background, the capture_output=True sets the stdout and stderr to subprocess.PIPE
# instead of using capture_output=True, we will use stdout=subprocess.PIPE to set stdout directly
print("stdout=subprocess.PIPE instead of capture_output=True")
p3 = subprocess.run("ls -la", stdout=subprocess.PIPE, text=True)
print(p3.stdout)

# redirect stdout to a file directly
filename = "output.txt"
with open(filename, "w") as f:
    # to redirect stdout to file, set stdout=f
    p4 = subprocess.run("ls -la", stdout=f, text=True)

# to read the output.txt file
with open(filename, "r") as f:
    print("Redirect stdout to file and reading the file")
    print(f.read())

# What happens when the command does not execute successfully?
print("When shell commands fail")
p5 = subprocess.run("ls -la doesnotexist", capture_output=True, text=True)
# by default, python does not give an error when a shell command fails
# it just return a non zero error code, returncode 0 means no error
print("returncode: ", p5.returncode)
print("stderr: ", p5.stderr)
# to handle if command was successful or not
if p5.returncode != 0:
    print("command failed because: ", p5.stderr)

# to make python throw an exception error if the external command fails
print("Make python throw exception error when shell commands fail")
# p5 = subprocess.run("ls -la doesnotexist", capture_output=True, text=True, check=True)
# print(p5.stderr)
# comment try except and uncomment above code to see the exception error
try:
    p5 = subprocess.run(
        "ls -la doesnotexist", capture_output=True, text=True, check=True
    )
    print(p5.stderr)
except subprocess.CalledProcessError as err:
    print(err)
    print()

# redirect error to /dev/null
print("Redirect errors to /dev/null")
p6 = subprocess.run("ls -la doesnotexist", stderr=subprocess.DEVNULL)
print(p6.stderr)
print()

# make output of one command be input of the next command
print("make a command output to be the next one input")
# this method is used when data of one command needs to be process before going to the next command
p7 = subprocess.run("cat output.txt", capture_output=True, text=True)
p7 = subprocess.run("grep tutorial", capture_output=True, text=True, input=p7.stdout)
p7 = subprocess.run(
    "awk -F\" \" '{ print $9 }'", capture_output=True, text=True, input=p7.stdout
)
print(p7.stdout)
print()

# pass all shell command at once
print("multiple shell command at once")
# this method is used when no data needs to be processed by python
p8 = subprocess.run(
    "cat output.txt | grep tutorial | awk -F\" \" '{ print $9 }'",
    capture_output=True,
    text=True,
    shell=True,
)
print(p8.stdout)
