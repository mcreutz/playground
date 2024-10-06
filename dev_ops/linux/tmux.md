# Tmux

## Sessions
- **Start a new session**: `tmux`
- **Start a new session with a name**: `tmux new -s session_name`
- **List all sessions**: `tmux ls`
- **Attach to a session**: `tmux attach -t session_name`
- **Detach from the current session**: `tmux detach` (`Ctrl-b d`)
- **Rename the current session**: `tmux rename-session` (`Ctrl-b $`)
- **Kill a session**: `tmux kill-session -t session_name`

## Windows and Panes
- **Create a new window**: `tmux new-window` (`Ctrl-b c`)
- **List all windows**: `tmux list-windows` (`Ctrl-b w`)
- **Switch to a specific window**: `tmux select-window -t window_number` (`Ctrl-b window_number`)
- **Switch to the next window**: `tmux next-window` (`Ctrl-b n`)
- **Switch to the previous window**: `tmux previous-window` (`Ctrl-b p`)
- **Rename the current window**: `tmux rename-window` (`Ctrl-b ,`)
- **Move window to another session**: `tmux move-window -t session_name` (`Ctrl-b :move-window -t session_name`)

### Panes
- **Split the window horizontally**: `tmux split-window -h` (`Ctrl-b %`)
- **Split the window vertically**: `tmux split-window -v` (`Ctrl-b "`)
- **Switch between panes**: `tmux select-pane -t :.+` (`Ctrl-b o`)
- **Close the current pane**: `tmux kill-pane` (`Ctrl-b x`)
- **Resize pane**: `tmux resize-pane` (`Ctrl-b` followed by arrow keys)

## Copy Mode
- **Enter copy mode**: `tmux copy-mode` (`Ctrl-b [`)
- **Scroll up/down**: `tmux copy-mode -u` / `tmux copy-mode -d` (`Up/Down arrow keys`)
- **Exit copy mode**: `tmux send-keys q` (`q`)

## Miscellaneous
- **Reload tmux configuration**: `tmux source-file ~/.tmux.conf` (`Ctrl-b :source-file ~/.tmux.conf`)
- **Show current key bindings**: `tmux list-keys` (`Ctrl-b ?`)

## Tips
- Customize your `~/.tmux.conf` file to set up your preferred key bindings and options.
- Use plugins like `tmux-resurrect` to save and restore tmux sessions.

For more detailed information, refer to the [tmux man page](https://man7.org/linux/man-pages/man1/tmux.1.html).

