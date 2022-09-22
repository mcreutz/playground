# Homebrew helpers

## Show user istalled formulae
```
$ brew leaves
```

## Show dependencies of user installed formulae
```
$ brew deps --tree $(brew leaves)
```

## Remove unused dependencies
```
$ brew autoremove
```