# Homebrew helpers

## Show user istalled formulae
```bash
brew leaves
```

## Show installed versions of formulae
```bash
brew list --formulae --versions
```

## Show dependencies of user installed formulae
```bash
brew deps --tree $(brew leaves)
```

## Remove unused dependencies
```bash
brew autoremove
```