# Use Sops with Helmfile
## Install
```bash
brew install gnupg sops
helm plugin install https://github.com/jkroepke/helm-secrets --version v4.6.3
```

## List existing GPG keys
```bash
gpg --list-keys
gpg --list-secret-keys
```

## Import further GPG key
```bash
gpg --import <key>  # omit key to import from stdin, use ctrl-d to enter EOF
gpg --keyring secring.gpg --export-secret-keys > ~/.gnupg/secring.gpg  # if necessary
gpg --keyring pubring.gpg --export > ~/.gnupg/pubring.gpg  # if necessary
```

## Make Sops available in terminal session
```bash
GPG_TTY=$(tty)
export GPG_TTY
```