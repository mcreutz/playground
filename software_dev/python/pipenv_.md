# Pipenv Cheat Sheet
## General
### Check path of current Python interpreter
```
which python
```

### Check version of current Python interpreter
```
python --version
```

### Check if pipenv venv exists for the current path (and show its path)
```
pipenv --venv
```

## Environments
### Activate pipenv venv for current directory
```
pipenv shell
```
- If directory does not contain a pipfile, one will be created.
- If directory does not have a virtual environment assigned, one will be created.
- To specify the python version when creating a new venv, use `--python 3.7`. Also consider to use [pyenv](https://github.com/pyenv/pyenv).

### Exit the currently active venv
```
exit
```

### Delete the currently active venv
```
pipenv --rm
```

## Dependencies
### Install a package
```
pipenv install package1 package2 [--dev]
```
- Use `--dev` for packages only used in development

### Install all packages from pipfile
```
pipenv install [--dev]
```
- Use `--dev` to inclue packages only used for development

### Uninstall a package
```
pipenv uninstall package1 package2
```

### Uninstall all packages that were not installed by user and are not referenced by those
```
pipenv clean
```

## Dependencies files
### Create 'requirements.txt' file for current venv
```
pipenv lock -r [-d] > requirements.txt
```
- Use `-d` to include dev packages

### Install all packages from requirements.txt
```
pipenv install -r ./requirements.txt
```

## Misc
### Check for security vulnerabilities of installed packages
```
pipenv check
```

### Check dependency graph
```
pipenv graph
```

### Set lockfile - before deployment
```
pipenv lock
```

### Run command with pipenv
```
pipenv run *
```