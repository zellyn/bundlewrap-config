"""
Per-user ssh-agent for headless machines.

Installs a global systemd user unit so every user gets an ssh-agent listening
on a fixed socket ($XDG_RUNTIME_DIR/ssh-agent.socket), exports SSH_AUTH_SOCK
for login shells, and sets AddKeysToAgent so a key's passphrase is only typed
once per boot. The fixed socket path keeps working inside long-lived tmux
sessions.

Lingering is enabled for the listed users so their agent (and loaded keys)
survives between logins.

Optional metadata:
  - ssh-agent/linger_users: Users to enable lingering for (default: [node.username])

Example metadata:
    'ssh-agent': {
        'linger_users': ['zellyn'],
    }

After the first apply, log out and back in (or run
`systemctl --user daemon-reload && systemctl --user start ssh-agent`).
"""
