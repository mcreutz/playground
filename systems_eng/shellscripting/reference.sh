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
## equality
==, !=

## comparison
<=, >=, <, >

## bitwise
&, |, ^(XOR)

## logical
&&, ||


# evaluations
(command)
((arithmetic expression))


# Slicing


# Exit with code
exit 1  # If no exit command is given at the end and last command was successful, the script will exit with code 1 (means successful)


# Environment variables
printenv  # Show all environment variables for the active user, that have a value set
env  # Run a command under modified environment: $ env EDITOR=vim xterm


# Test for availability of features / vars
test -z "$TARGET_DIR" && { echo "Fatal Error: No TARGET_DIR set" ; exit 1 ; }


# Select parent dir
REPO_ROOT_DIR = "${CI_DIR}/.."


# Files handling
cat  # print a files content. If multiple files are given, print concatenated contents 
chmod
chown
cp
mkdir
mv
rm
rmdir
touch  # create files. If file exists, modification timestamp is updated


# Redirecting standartd output
command_1 | command_2
command > file  # Write to file (replace previous content or create if file does not exist)
command >> file  # Append to file


# Useful commands and programs
curl / wget
echo  # create output from string
grep  # filter lines for text or regex
history  # Command history
jq
less / more
mount | column -t  # Column formatted table of active mounts
passwd
printenv
pushd / popd
pwd
sed
tail -f  # Open textfile and stream file updates
tar
tee
test
truncate -s 0 filename  # Remove content of file up to given size is reached. Good to clear a file without deleting it.


# shortcuts
!nnn  # Run command no nnn from command history
!!  # Last command
-  # Previous directory
.  # Current directory
..  # Parent directory
~  # Current users home directory
Esc, Esc  # Re-run last command with sudo, zsh only

