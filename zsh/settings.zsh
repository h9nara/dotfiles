# Initialize completion
autoload -Uz compinit && compinit -i
zstyle ':completion:*' menu select=4
zmodload zsh/complist
# Use vim style navigation keys in menu completion
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history

# If a command is issued that can’t be executed as a normal command, and the command is the name of a directory, perform the cd command to that directory.
setopt AUTO_CD

# Nicer history
HISTSIZE=1048576
HISTFILE="$HOME/.zsh_history"
SAVEHIST=$HISTSIZE
setopt appendhistory
setopt sharehistory
setopt extendedhistory

# If a command is issued that can’t be executed as a normal command, and the command is the name of a directory, perform the cd command to that directory.
setopt AUTO_CD

# Use vim as the editor
export EDITOR=vim

# bash-like help for zsh
# unalias run-help
autoload run-help
HELPDIR=/usr/share/zsh/"${ZSH_VERSION}"/help
alias help=run-help

#zoxide
eval "$(zoxide init zsh)"

# Set up fzf key bindings and fuzzy completion
# Uncomment this to use fzf default key bindings
source <(fzf --zsh)

# # 1. 禁用 fzf 默认的快捷键绑定
# export FZF_CTRL_R_COMMAND=""
# export FZF_CTRL_T_COMMAND=""

# # 2. 加载 fzf 的 Shell 集成
# source <(fzf --zsh)

# # 3. 手动将 fzf 的内部功能绑定到 Alt+R 和 Alt+T (此部分为外部知识)
# # 在终端中，Alt 键通常用 ^[ 表示
# bindkey '^[r' fzf-history-widget  # 将 Alt+R 绑定到 fzf 历史搜索
# bindkey '^[t' fzf-file-widget     # 将 Alt+T 绑定到 fzf 文件搜索

# # 4. 可选：如果你想把 Ctrl+R 恢复为 zsh 自带的、没有 fzf 的默认历史搜索
# bindkey '^R' history-incremental-search-backward
