# Makefile reference: https://www.gnu.org/software/make/manual/html_node/Quick-Reference.html

# simple command
list:
	ls


# another simple command
hello:
	python my_script.py


# call defined commands and add further ones
concatenation: hello list
	pwd


# do not show commands and comments in shell
hiding:
	# This command will be shown and then executed
	echo "test1"   # comment
	
	@# This command will be executed, but the command will not be shown
	@echo "test2"   # comment
	
	# This comment will be shown
	@# This comment will not be shown, but only if it is at the beginning of the line
