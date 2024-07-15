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

Create requirements.txt file
```shell
poetry export --format requirements.txt --output requirements.txt [--with <name>]
```

Show a list of all dependencies
```bash
poetry show [--tree] [--with dev]
```