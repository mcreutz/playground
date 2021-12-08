# Pipenv Cheat Sheet

**Check path of current Python interpreter**
```
which python
```
<br>

**Check version of current Python interpreter**
```
python --version
```
<br>

**Check if pipenv venv exists for the current path (and show it's path)**
```
pipenv --venv
```
---
<br><br>


**Activate pipenv venv for current directory**
```
pipenv shell
```
- If directory does not contain a pipfile, one will be created.

- If directory does not have a virtual environment assigned, one will be created.

- To specify the python version when creating a new venv, use `--python 3.7`. Also consider to use [pyenv](https://github.com/pyenv/pyenv).
<br>
<br>

**Delete the currently active virtual environment**
```
pipenv --rm
```
---
<br><br>

**Install a package**
```
pipenv install package1 package2 [--dev]
```
- Use `--dev` for packages only used in development
<br><br>

**Install all packages from pipfile**
```
pipenv install [--dev]
```
- Use `--dev` to inclue packages only used for development
<br><br>

**Uninstall a package**
```
pipenv uninstall package1 package2
```
<br>

**Uninstall all packages that were not installed by user and are not referenced by those**
```
pipenv clean
```
---
<br><br>

**Create 'requirements.txt' file for current venv**
```
pipenv lock -r [-d] > requirements.txt
```
- Use `-d` to include dev packages
<br><br>

**Install all packages from requirements.txt**
```
pipenv install -r ./requirements.txt
```
---
<br><br>

**Check for security vulnerabilities of installed packages**
```
pipenv check
```
<br>

**Check dependency graph**
```
pipenv graph
```
<br>

**Set lockfile - before deploymen**
```
pipenv lock
```
<br>

**Exit the currently active virtualenv**
```
exit
```
<br>

**Run command with pipenv**
```
pipenv run *
```