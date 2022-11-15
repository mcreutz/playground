Initialize the module
```console
$ go mod init <appname>
```

Run application
```console
$ go run <appname>
```

Build application
```console
$ go build <appname>
```

Tools
- go install -v github.com/ramya-rao-a/go-outline@latest  
- go install -v github.com/go-delve/delve/cmd/dlv@latest
- go install -v github.com/rogpeppe/godef@latest
- go install -v github.com/stamblerre/gocode@latest
- go install -v golang.org/x/tools/gopls@latest  # Go Language Server
- go install -v golang.org/x/tools/cmd/goimports@latest
- go install -v honnef.co/go/tools/cmd/staticcheck@latest