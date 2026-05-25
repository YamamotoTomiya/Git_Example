# SSH Agent Setup for GitHub Integration in VSCode

When using VSCode's Git features (push / pull / clone) over SSH,
you need to register your private key with the SSH agent first.
Without this, VSCode cannot find the SSH key and authentication will fail.

---

## What is the SSH Agent?

The SSH agent is a program that holds your private key in memory.
Once registered, you no longer need to enter your passphrase on every push.
VSCode accesses the key through the OS SSH agent, which is why registration is required.

```
VSCode Git operation
  → SSH agent (holds the key)
    → GitHub (authentication)
```

---

## Prerequisites

Check that an SSH key already exists:

```bash
ls ~/.ssh/
# id_ed25519     ← private key
# id_ed25519.pub ← public key
```

If no key exists, create one first (see Step 2 in [03_github_push_en.md](03_github_push_en.md)).

---

## Step 1: Start the SSH Agent

Check whether the agent is already running:

```bash
echo $SSH_AGENT_PID
# A number means it is running
# Nothing means it needs to be started
```

If it is not running, start it:

```bash
eval "$(ssh-agent -s)"
# Agent pid 12345  ← this output means the agent started successfully
```

---

## Step 2: Add the Private Key to the Agent

```bash
ssh-add ~/.ssh/id_ed25519
```

If you set a passphrase when creating the key, you will be prompted to enter it.
If no passphrase was set, the key is registered immediately.

Confirm the key was added:

```bash
ssh-add -l
# 256 SHA256:XXXX... your_email@example.com (ED25519)
```

If key information appears, the key is registered.

---

## Step 3: Test the Connection to GitHub

```bash
ssh -T git@github.com
# Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

If you see this message, push and pull from VSCode will work.

---

## Step 4: Try Git Operations in VSCode

Open the Source Control panel in VSCode (the branch icon in the left sidebar)
and run a push or pull. Authentication should succeed without a passphrase prompt.

> **Note:** Keys registered with the SSH agent are cleared on logout.
> After logging back into the server or restarting your PC, repeat Steps 1–2.

---

## Auto-register on Login (Optional)

If running `ssh-add` manually each time is inconvenient, add it to your shell config file.

```bash
vi ~/.bashrc
```

Append the following at the end:

```bash
# Auto-start SSH agent and register key
if [ -z "$SSH_AGENT_PID" ]; then
    eval "$(ssh-agent -s)" > /dev/null
    ssh-add ~/.ssh/id_ed25519 2>/dev/null
fi
```

Apply the changes:

```bash
source ~/.bashrc
```

> **Note:** This setting attempts to start the agent every time a shell is opened.
> If you set a passphrase on your key, you will be prompted to enter it at each login.

---

## Summary

```bash
# Start the agent
eval "$(ssh-agent -s)"

# Register the key
ssh-add ~/.ssh/id_ed25519

# Test the connection
ssh -T git@github.com

# → VSCode push / pull now works without authentication prompts
```

---

## Quick Command Reference

| Command | Purpose |
|---------|---------|
| `eval "$(ssh-agent -s)"` | Start the SSH agent |
| `ssh-add ~/.ssh/id_ed25519` | Register the private key with the agent |
| `ssh-add -l` | List registered keys |
| `ssh-add -D` | Remove all registered keys |
| `ssh -T git@github.com` | Test the SSH connection to GitHub |

---

## Related Documents

- [Creating a Remote Repository on GitHub and Pushing Code](03_github_push_en.md)
