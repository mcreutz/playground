#1 /bin/bash

non_existing_command &> /dev/null
# echo $?
if (($? != 0)); then exit 1; fi
