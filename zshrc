# 6.S081 Labs environment setup
PATH=/usr/local/bin:$PATH
PATH=$PATH:/usr/local/opt/riscv-gnu-toolchain/bin

# For pretty printing logs for 6.824 labs
PATH=$PATH:~/dev/courses/6.824/2022-labs/src

# https://stackoverflow.com/questions/71468590/env-python-no-such-file-or-directory-when-building-app-with-xcode
PATH=$PATH:/opt/homebrew/opt/python@3.9/libexec/bin

# https://stackoverflow.com/questions/64126942/malloc-nano-zone-abandoned-due-to-inability-to-preallocate-reserved-vm-space
# export MallocNanoZone=0

# External plugins (initialized before)
source ~/.zsh/plugins_before.zsh

# Settings
source ~/.zsh/settings.zsh

# Aliases
source ~/.zsh/aliases.sh

# spaceship prompt
autoload -U promptinit; promptinit
prompt spaceship

# External plugins
source ~/.zsh/plugins.zsh
# export PATH="/opt/homebrew/opt/go@1.16/bin:$PATH"
export PATH="/opt/homebrew/opt/node@20/bin:$PATH"
