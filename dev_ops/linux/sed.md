# sed Syntax Overview

## Usage

```bash
sed [OPTIONS] [SCRIPT] [INPUTFILE]
```

## Options

- `-n` - suppress automatic printing of pattern space
- `-e script` - add the script to the commands to be executed
- `-f script-file` - add the contents of script-file to the commands to be executed
- `-i[SUFFIX]` - edit files in place (makes backup if SUFFIX supplied)
- `-r` - use extended regular expressions in the script
- `-s` - treat the files as separate files (i.e., do not reset line numberings between files)
- `-u` - disable output buffering
- `-l N` - specify the line wrap length
- `-b` - make a backup of each file that is modified
- `-p` - print the pattern space


## Scripts  

- `s/regexp/replacement/` - replace the first occurrence of the regexp with the replacement
- `s/regexp/replacement/g` - replace all occurrences
- `s/regexp/replacement/2` - replace the second occurrence
- `s/regexp/replacement/3` - replace the third occurrence
- `s/regexp/replacement/i` - case-insensitive replacement
- `s/regexp/replacement/ig` - case-insensitive replacement of all occurrences
- `s/regexp/replacement/igp` - case-insensitive replacement of all occurrences with print
- `s/regexp/replacement/igpw` - case-insensitive replacement of all occurrences with print and write


## Examples

- `sed 's/hello/world/' input.txt > output.txt` - read input.txt, replace the first occurrence of 'hello' with 'world' and write to output.txt
- `sed 's/hello/world/' < input.txt > output.txt` - same as above
- `cat input.txt | sed 's/hello/world/' - > output.txt` - same as above
- `sed -i 's/old-text/new-text/g' input.txt` - replace all occurrences of 'old-text' with 'new-text' in input.txt
- `sed -n '10,20p' input.txt`  - print lines 10 to 20 from input.txt
- `sed -i '10,20d' input.txt`  - delete lines 10 to 20 from input.txt
- `sed -n '/pattern/p' input.txt`  - print lines that contain the pattern in input.txt
- `sed -i '$a\appended text' input.txt` - append 'appended text' to the end of input.txt
- `sed -i '10i\inserted text' input.txt`  - insert 'inserted text' before line 10 in input.txt
- `sed -i '10c\replaced text' input.txt`  - replace line 10 with 'replaced text' in input.txt


