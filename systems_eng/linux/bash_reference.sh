#!/bin/bash

# Shebang
# Runs the script in an separate shell when script file is executed.
# Needs to be in the first line of the script file.
#!/bin/bash
#!/bin/sh
#!/usr/bin/bash
#!/bin/bash -ex  # -e: Exit on error, -x: Print each command before executing it
#!/usr/bin/env bash


# Execute a script file
source ./script.sh  # run in current shell
. ./script.sh  # run in current shell, shorthand for 'source'
bash ./script.sh  # run in subshell using bash
sh ./script.sh  # run in subshell using sh
./script.sh  # run in subshell using shebang of script file (e.g. #!/bin/bash as first line in script file). File needs to be executable.


# Manage shell options and positional parameters
set -e  # Exit on error of any command
set -x  # Print each command before executing it
set +x  # Disable printing of each command before executing it
set -u  # Exit on usage of undefined variable
set -o pipefail  # Exit on error of any command in a pipe
set  # Show all shell options and positional parameters


# Accessing command line arguments
$0  # Name of the script
$1  # First argument
$2  # Second argument
$@  # All arguments
"$@"  # All arguments, each one in double quotes
$#  # Number of arguments
# Example: ./myScript.sh foo -b baz
#   $0 -> ./myScript.sh
#   $1 -> foo
#   $2 -> -b
#   $3 -> baz
getopts  # Parsing command line arguments


# Functions
my_function() {
  echo "$1"
  echo "$2"
  local my_local_var="my value"  # local variables are only available in the function
  my_global_var="my value"  # global variables are available in the function and in the calling scope
  return 42  # End function and return exit code 0-255, similar to exit-code. Code is assigned to '$?'.
}
my_function "Hello" "World"  # call function with arguments
echo $?  # print exit code of last command
my_result=$(my_function "Hello" "World")  # call function and store its output (not return value!) in variable


# Variables
## Declaration and assignment
my_var=myvalue  # No spaces around the equal sign. Names are case sensitive. Scope is the current shell, not subshells.
unset MY_VAR  # delete variable

## Naming conventions
# Environment variables and constants are usually UPPER_CASE_WITH_UNDERSCORES
# Local variables are usually lower_case_with_underscores

## Strings
my_var=HelloWorld  # No quotes needed for strings without whitespaces
my_var="my value"  # Double quotes allow whitespaces in strings
my_var="my value"  # Double quotes allow line breaks in strings
my_var='my value'  # Single quotes preserve everything literally. Multiple lines are not possible.

## Integers
my_var=123

## Arrays, slicing
# data types are not enforced, arrays can contain mixed types
my_array=(foo bar baz)  # Create array
echo ${my_array[0]}  # Print first element
echo ${my_array[1]}  # Print second element
echo ${my_array[@]}  # Print all elements
echo ${#my_array[@]}  # Print number of elements
echo ${my_array[@]:1:2}  # Print elements 1 and 2
echo ${my_array[@]:1}  # Print elements 1 to end
echo ${my_array[@]::2}  # Print elements 0 and 1
echo ${my_array[@]::-1}  # Print elements 0 and 1
echo ${my_array[@]:(-1)}  # Print last element
echo ${my_array[@]:(-2)}  # Print last two elements
echo ${my_array[@]:(-2):1}  # Print second last element
echo ${my_array[@]:(-2):2}  # Print second and third last element

## Associative arrays
declare -A my_var=( [foo]=bar [baz]=qux )  # No quotes needed for associative arrays
echo ${my_var[foo]}  # Print value of key 'foo'
echo ${my_var[@]}  # Print all values
echo ${!my_var[@]}  # Print all keys
echo ${#my_var[@]}  # Print number of elements
unset my_var[foo]  # Delete element with key 'foo'
unset my_var  # Delete entire array

## Variable substitution
echo $my_var  # variable substitution (short syntax)
echo "$my_var"  # substitute and use value as string. double quotes preserve whitespaces in strings, substititions are still performed
echo "${my_var}bar"  # curly braces are used to separate variable name from the rest of the string (full syntax)
echo '$my_var'  # single quoting preserves everything literally, no substitutions are performed


# Environment variables
export MY_VAR = "my value"  # Export variable to make it available for all commands executed in the current shell and subshells
printenv  # Show all environment variables for the active user, that have a value set
env EDITOR=vim xterm  # Run a command under modified environment
$HOME  # Home directory of the current user
$PATH  # Colon-separated list of directories to search for commands
$PWD  # Current working directory
$USER  # Current user
$UID  # Current user ID
$GROUPS  # Groups of the current user
$HOSTNAME  # Hostname of the current machine
$SHELL  # Current shell
$HISTFILE  # History file


# Command execution
## Command substitution
my_date=$(date)  # executes the command in a subshell and substitutes the command with its output (command substitution)
my_date=`date`  # equivalent to $(date), but deprecated

## Redirecting a command's in- and output
mycommand_1 | mycommand_2  # Pipe output of mycommand_1 to input of mycommand_2, mycommand_2 runs in a subshell
mycommand > file  # Write to file (replace previous content or create if file does not exist)
mycommand >> file  # Append to file
mycommand > /dev/null  # Discard output
mycommand 2> file  # Write error output to file
mycommand 2>&1  # Redirect error output to standard output
mycommand 2>/dev/null  # Discard error output
mycommand &> file  # Write standard and error output to file
mycommand < file  # Read from file
mycommand <<< "my input"  # Pass string as input to command

## Concatenation of commands
command_1 && command_2  # && only executes the second command, if the first one exited with code 0 (means successful)
command_1 || command_2  # || only executes the second command, if the first one exited with a non-zero code (means failed)
command_1 ; command_2  # ; runs both commands in the given order, regardless of the exit codes

## Command grouping
{ command_1; command_2; }  # executes the commands in the current shell
( command_1; command_2; )  # executes the commands in a subshell

## Aliases
alias myalias="mycommand --option"  # create alias
alias  # list all aliases
myalias  # execute command with alias
command myalias  # ignore alias and execute command
unalias myalias  # delete alias

## Check if a command is available
if command -v some_command &> /dev/null; then
    echo "some_command is available"
else
    echo "some_command is not available"
fi


# Working with strings
## Concatenation of strings
my_var="foo"
my_var+="bar"  # my_var is now "foobar"

## Counting in strings
my_var="foo bar baz"
${#my_var}  # length of string
${my_var//[^ ]}  # number of spaces in string

## Multiline string literals
cat <<EOF > file  # to a file. EOF is a delimiter, can be any string
line 1
line 2
EOF

read -r -d '' my_var <<EOF  # to a variable.
line 1
line 2
EOF

cat <<EOF | grep foo  # to a command
line 1
line 2
EOF

## String manipulation
${my_var:0:3}  # Get first 3 characters
${my_var:3}  # Get characters 3 to end
${my_var: -3}  # Get last 3 characters
${my_var: -3:2}  # Get last 3 characters
${#my_var}  # Get length of string
${my_var/foo}  # Remove first occurence of 'foo'
${my_var//foo}  # Remove all occurences of 'foo'
${my_var/#foo}  # Remove prefix 'foo'
${my_var/%foo}  # Remove suffix 'foo'
${my_var/foo/bar}  # Replace first occurence of 'foo' with 'bar'
${my_var//foo/bar}  # Replace all occurences of 'foo' with 'bar'
${my_var/#foo/bar}  # Replace prefix 'foo' with 'bar'
${my_var/%foo/bar}  # Replace suffix 'foo' with 'bar'
${my_var^}  # Uppercase first character
${my_var^^}  # Uppercase all characters
${my_var,}  # Lowercase first character
${my_var,,}  # Lowercase all characters

## String formatting with printf
%[flags][width][.precision]specifier  # conversion specification

### Flags
-  # Left align the printed text within the field. By default, the text is right-aligned.
+  # Prefix the numbers with a + or - signs. By default, only negative numbers are prefixed with a negative sign.
0  # Pads numbers with leading zeros rather than space.
blank  # Prefix the positive numbers with a blank space and negative numbers with a minus (-).
#  # An alternative format for numbers.

### Width
# Minimum number of characters the conversion should result in,  padded with spaces

### Precision
# For integer specifiers (d, i, o, u, x, X): minimum number of digits to be written. If the value to be written is shorter than this number, the result is padded with leading zeros. The value is not truncated even if the result is longer.
# For floating point specifiers (e, E, f, g, G): number of digits to be printed after the decimal point. If the value to be written is shorter than this number, the result is padded with trailing zeros. The value is not truncated even if the result is longer.
# For the string specifier (s): maximum number of characters to be printed. Characters in excess of this number are not printed.

### Specifiers
%d, %i  # Print the argument as a signed decimal integer.
%u  # Print the argument as an unsigned decimal integer.
%f  # Print the argument as a floating-point number.
%s  # Print the argument as a string.
%%  # Print a literal % symbol.

### Examples
printf "%s %d %f\n" "Hello" 123 456.789  # Print string, integer and float with newline
printf "%+10s %+10d %+10f\n" "Hello" 123 456.789  # Print string, integer and float with newline, left-aligned, padded with spaces, prefixed with signs
printf "%010s %010d %010f\n" "Hello" 123 456.789  # Print string, integer and float with newline, left-aligned, padded with zeros
printf "%-10s %-10d %-10f\n" "Hello" 123 456.789  # Print string, integer and float with newline, left-aligned, padded with spaces


# Arithmetic operations
## Arithmetic substitution
$((2 + 3))  # evaluates the given arithmetic expression and substitutes the expression with its result
$[2 + 3]  # equivalent to the above, but deprecated

## Incrementing and decrementing
my_var=0
my_var+=1  # my_var is now 1
my_var-=1  # my_var is now 0
((my_var++))  # my_var is now 1
((my_var--))  # my_var is now 0


# Constrol structures
## Conditional execution
if [ $foo == "bar" ]; then  # single brackets are a shorthand for the 'test' command
  date
elif [[ $foo == "bar" && $bar == "baz" ]]; then  # double brackets allow more advanced conditionals
  pwd
else
  whoami
fi

## Loops
while [ $foo == "bar" ]; do
  mycommand_1
  mycommand_2
done

until [ $foo == "bar" ]; do
  mycommand_1
  mycommand_2
done

for color in "Red Green Blue"; do
  echo $color
done


# Comparisons
## Equality for strings
=, ==, !=  # Expressions need to be enclosed in double brackets

## Equality for integers
-eq, -ne  # Expressions need to be enclosed in double brackets

## Size for srings
<, >, -z, -n  # Expressions need to be enclosed in double brackets

## Size for integers
<=, >=, <, >  # Expressions need to be enclosed in double brackets
-lt, -le, -gt, -ge  # Expressions need to be enclosed in double parentheses


## Pattern matching for strings
=~  # Expressions need to be enclosed in double brackets

## Bitwise
&, |, ^, ~, <<, >>, &=, |=, ^=, ~=, <<=, >>=  # bitwise AND, OR, XOR, NOT, left shift, right shift, assignments

## Logical opeartors
&&, ||, !  # logical AND, OR, NOT, can be used in double brackets and double parentheses


# Trapping
trap my_function EXIT  # Run 'my_function' on event 'EXIT'. Can also run a command or semicolon-separated list on commands.
# Some possible events:
#   EXIT: Run when the shell exits (regardless of exit status)
#   ERR: Run on error
#   0: Run when a command returns a zero exit status
#   DEBUG: Run before every command
#   RETURN: Run when a shell function or a script executed with the . or source commands finishes executing
#   SIGINT: Run when the shell receives a SIGINT signal (generated by the Ctrl-C key sequence)
#   SIGTERM: Run when the shell receives a SIGTERM signal (usually generated with the kill command)
#   SIGKILL: Run when the shell receives a SIGKILL signal (usually generated with the kill command)
#   SIGSTOP: Run when the shell receives a SIGSTOP signal (usually generated with the kill command)


# Exiting
set -e  # Exit on error of any command
exit 0  # Exit with code 0 (means successful)
exit 1  # Exit with code != 0 (means failed)
# If no exit command is given at the end and last command was successful, the script will exit with code 0


# misc
exec sh  # Switch to a different shell.
exec bash -c "echo Hello World"  # Run command in a different shell
cd .. \  # Line break in command
    && cd ..
REPO_ROOT_DIR = "${CI_DIR}/.."  # Select parent directory of a given directory
test -z "$TARGET_DIR" && { echo "Fatal Error: No TARGET_DIR set" ; exit 1 ; }  # Test for availability of features / vars


# References
https://tldp.org/LDP/abs/html/index.html

