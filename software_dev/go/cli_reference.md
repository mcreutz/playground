## Cli
Initialize the module
```console
$ go mod init <module name>
```

Download a package and add it to go.mod
```console
$ go get <example.com/packagename>[@version]
```

Install all dependencies from source code and add them to go.mod (also remove unused dependencies from go.mod)
```console
$ go mod tidy
```

Run tests
```console
$ go test
```

Run application
```console
$ go run <module name> | <main file>
```

Build application
```console
export GOOS=linux  # or darwin, windows, etc.
export GOARCH=amd64  # or 386, arm, arm64, etc.
$ go build <module name>
```

Install the application (builds and installs the application to where exactly?)
```console
$ go install
```


## Tools
- go install -v github.com/ramya-rao-a/go-outline@latest  
- go install -v github.com/go-delve/delve/cmd/dlv@latest
- go install -v github.com/rogpeppe/godef@latest
- go install -v github.com/stamblerre/gocode@latest
- go install -v golang.org/x/tools/gopls@latest  # Go Language Server
- go install -v golang.org/x/tools/cmd/goimports@latest
- go install -v honnef.co/go/tools/cmd/staticcheck@latest