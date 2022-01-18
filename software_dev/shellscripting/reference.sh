# Shebangs
# Need to be in the first line of the script, runs the script in an separate
# shell when scrpt file is executed. Use 'source' command to execure a script 
# in the current shell.
#!/bin/sh
#!/bin/bash
#!/usr/bin/bash
#!/bin/bash -ex

# Output a string
echo Hello World
echo "Hello World"

# Variables
MY_VAR = my_value
MY_VAR = "my_value"
echo $MY_VAR
echo $"MY_VAR"
echo ${MY_VAR}
cd "$HOME"/Documents
cd ${HOME}/Document

# Variable scope
export

# Conditional execution
if <condition>; then
  <commands>
fi

# Loops
while [condition]; do
  <commands>
done

until [condition]; do
  <commands>
done

for var in <list>; do  # <list> is a series of strings, separated by spaces: "Red Green Blue"
  <commands>
done

# Concatenation of commands
command_1 && command_2  # && only executes the second command, if the first one exited with code 1 (means successful)
command_1 || command_2  # || only executes the second command, if the first one exited with code 0 (means failed)
command_1 ; command_2  # ; runs both commands in the given order, regardless of the exit codes

# Line break
cd .. \
    && cd ..

# Available varibles
$HOME

# comparisons
-le
&&
||
==

# Slicing



# Exit with code
exit 1  # If no exit command is given at the end and last command was successful, the script will exit with code 1 (means successful)









# Test for availability of features / vars
test -z "$TARGET_DIR" && { echo "Fatal Error: No TARGET_DIR set" ; exit 1 ; }

# Select parent dir
REPO_ROOT_DIR="${CI_DIR}/.."




# Useful commands and programs
cat
chmod
curl / wget
grep
jq
less / more
passwd
pwd
pushd / popd
sed
tar
tee
test
