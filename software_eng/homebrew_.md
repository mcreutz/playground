# Homebrew helpers

## Show user istalled formulae
```shell
$ brew leaves
```

## Show dependencies of user installed formulae
```shell
$ brew deps --tree $(brew leaves)
```

## Remove unused dependencies
```shell
$ brew autoremove
```