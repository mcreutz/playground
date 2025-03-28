Create files and folders structure for a new project
```shell
poetry new <project name>
```

Initialize a pre-existing project
```shell
cd <pre-existing-project>
poetry init
```

Activate environment for current directory (create if not exists)
```shell
poetry shell [--group <name>]
```

Add dependency to active environment
```shell
poetry add <dependency> [--group <name>]
```

Install dependencies for active environment
```shell
poetry install [--with <name>]
```

Remove dependency from active enviroment
```shell
poetry remove <dependency> [--group <name>]
```

Lock depencies to a specific version
```shell
poetry lock
```
Will pin the dependencies to the latests version that matches the constraints in pyproject.toml.
To only refresh the lock file, use the --no-update option.
Usually not necessary, as the lockfile is automatically updated when adding or removing dependencies.

Create requirements.txt file
```shell
poetry export --format requirements.txt --output requirements.txt [--with <name>]
```

Show a list of all dependencies
```bash
poetry show [--tree] [--with dev]
```