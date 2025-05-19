# UV

## Managing Python interpreters
```sh
# List all available Python interpreters
uv python list
```

## Initializing a new project
```sh
# Initialize a new project
uv init --no-workspace
# Initialize a new project with a specific Python version
uv init --no-workspace --python 3.10
```

## Managing virtual environments
```sh
# Create a new virtual environment
uv venv .venv

# Create a new virtual environment with a specific Python version
uv venv .venv --python 3.10

# Activate the virtual environment
source .venv/bin/activate

# Deactivate the virtual environment
deactivate

# Remove the virtual environment
rm -rf .venv
```

## Managing dependencies
### ... of the project
```sh
# List all dependencies of the project
uv tree

# Add a dependency to the project
uv add requests

# Add a dependency with a specific version to the project
uv add requests==2.25.1

# Add a dependency to a group of the project
uv add requests --group dev

# Export the dependencies of the project to a requirements file
uv export > requirements.txt

# Remove a dependency from the project
uv remove requests
```

### ... of the virtual environment
```sh
# Install all dependencies from the lockfile to the environment
uv sync
```
