# Homebrew helpers

## Show user istalled formulae
```bash
brew leaves
```

## Show dependencies of user installed formulae
```bash
brew deps --tree $(brew leaves)
```

## Remove unused dependencies
```bash
brew autoremove
```