#!/bin/bash

# Shebangs
# Needs to be in the first line of the script, runs the script in an separate
# shell when script file is executed. Use 'source' command to execure a script 
# file in the current shell.
# #!/bin/bash
# #!/bin/sh
# #!/usr/bin/bash
# #!/bin/bash -ex
# #!/usr/bin/env bash


# Output a string
echo Hello World  # Actually two variables
echo 'Hello World'  # Single quotes PREVENT variable substitution ($<varname>) and escaping of special characters
echo "Hello World"  # Double quotes ALLOW variable substitution ($<varname>) and escaping of special characters


# Variables
MY_VAR = myvalue
MY_VAR = "my value"
echo $MY_VAR  # "variable substitution", short syntax
echo ${MY_VAR}  # full syntax
echo "$MY_VAR"  # double quoting preserves whitespaces in strings
echo '$MY_VAR'  # -> $MY_VAR
cd "$HOME"/Documents
cd ${HOME}/Document


# Execute command
<command>
$(<command>)  # “command substitution”, substitutes the given command with its output

# Variable scope
export


# Conditional execution
if [ <condition> ]; then
  <commands>
fi


# Loops
while [<condition>]; do
  <commands>
done

until [condition]; do
  <commands>
done

for var in <list>; do  # <list> is a series of strings, separated by spaces: "Red Green Blue"
  <commands>
done


# Concatenation of commands
command_1 && command_2  # && only executes the second command, if the first one exited with code 0 (means successful)
command_1 || command_2  # || only executes the second command, if the first one exited with a non-zero code (means failed)
command_1 ; command_2  # ; runs both commands in the given order, regardless of the exit codes


# Line break
cd .. \
    && cd ..


# Available variables
$HOME


# comparisons
## equality
==, !=

## size
<=, >=, <, >

## bitwise
&, |, ^  # AND, OR, XOR

## logical
&&, ||  # AND, OR

## strings
-z  # resolves to true, if following string has length zero:  foo=""; [ -z "$foo" ]
-n  # resolves to false, if following string has length zero:  foo="bar"; [ -n "$foo" ]


# evaluations
(command)  # run command in a subshell
((arithmetic expression))  # evaluate arithmetic expression
$(command)  # command substitution, substitute command with its output


# Slicing


# Exit with code
exit 1  # If no exit command is given at the end and last command was successful, the script will exit with code 0 (means successful)


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
yq


# shortcuts
!nnn  # Run command no nnn from command history
!!  # Last command
-  # Previous directory
.  # Current directory
..  # Parent directory
~  # Current users home directory
Esc, Esc  # Re-run last command with sudo, zsh only


# parameters
$@ delivers all parameters, ./someScript.sh foo bar, $@ -> foo bar
"$@" delivers all parameters, each one in double quotes


# misc
exec



# References
https://tldp.org/LDP/abs/html/index.html
