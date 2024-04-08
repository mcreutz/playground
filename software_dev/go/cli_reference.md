## Cli
Initialize the module
```bash
go mod init <module name>
```

Download a package and add it to go.mod
```bash
go get <example.com/packagename>[@version]
```

Install all dependencies from source code and add them to go.mod (also remove unused dependencies from go.mod)
```bash
go mod tidy
```

Run tests
```bash
go test
```

Run application
```bash
go run <module name> | <main file>
```

Build application
```bash
export GOOS=linux  # or darwin, windows, etc.
export GOARCH=amd64  # or 386, arm, arm64, etc.
go build <module name>
```

Install the application (builds and installs the application to where exactly?)
```bash
go install
```


## Tools
```bash
go install github.com/ramya-rao-a/go-outline@latest  # shows code outline
go install github.com/go-delve/delve/cmd/dlv@latest  # debugger
go install github.com/rogpeppe/godef@latest  # go to definition
go install github.com/stamblerre/gocode@latest  # code completion
go install golang.org/x/tools/gopls@latest  # Language Server
go install golang.org/x/tools/cmd/goimports@latest  # auto add imports
go install honnef.co/go/tools/cmd/staticcheck@latest  # linter
```