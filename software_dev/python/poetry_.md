Create files and folders structure for a new project
```console
poetry new <project name>
```

Initialize a pre-existing project
```console
cd <pre-existing-project>
poetry init
```

Activate environment for current directory (create if not exists)
```console
poetry shell [--group <name>]
```

Add dependency to active environment
```console
poetry add <dependency> [--group <name>]
```

Install dependencies for active environment
```console
poetry install [--with <name>]
```

Create requirements.txt file
```console
poetry export --format requirements.txt --output requirements.txt [--with <name>]
```