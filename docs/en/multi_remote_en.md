# Advanced: Managing Both GitHub and a Bare Repository as Remotes

How to manage GitHub (`origin`) and a server-side bare repository (`server`)
as two simultaneous remotes.

---

## Why Use Two Remotes?

| Remote name | Location | Primary use |
|-------------|----------|-------------|
| `origin` | GitHub | Publishing, backup, Pull Requests |
| `server` | Bare repository (`/home/repository/`) | Fast team sharing, running jobs directly on the server |

```
[Local]
    │
    ├── push/pull ──→ origin (GitHub)          publish · PR · backup
    │
    └── push/pull ──→ server (bare repository)  team sharing · server execution
```

This setup lets you keep day-to-day server work fast via `server`,
while using `origin` (GitHub) for public sharing and Pull Requests.

---

## Prerequisites

Check your current remote configuration:

```bash
git remote -v
```

If both remotes are registered, you are ready to go:

```
origin  git@github.com:<username>/my_project.git (fetch)
origin  git@github.com:<username>/my_project.git (push)
server  /home/repository/<username>/server/my_project.git (fetch)
server  /home/repository/<username>/server/my_project.git (push)
```

---

## Step 1: Add a Second Remote

Steps to add `server` when `origin` (GitHub) is already registered.

### 1-1. Add the bare repository as a remote

```bash
git remote add server /home/repository/<username>/server/my_project.git
```

### 1-2. Confirm the registration

```bash
git remote -v
# origin  git@github.com:<username>/my_project.git (fetch)
# origin  git@github.com:<username>/my_project.git (push)
# server  /home/repository/<username>/server/my_project.git (fetch)
# server  /home/repository/<username>/server/my_project.git (push)
```

> **Note:** The name in `git remote add <name> <URL>` is arbitrary.
> `origin` and `server` are just conventions — other names work too.

---

## Step 2: Pushing to Each Remote

### Push to GitHub (origin)

```bash
git push origin main
```

### Push to the bare repository (server)

```bash
git push server main
```

### Push a branch to both remotes

```bash
git push origin feature/add_xxx
git push server feature/add_xxx
```

> **Note:** You can push to just one of the remotes at any time.
> For example, push in-progress branches only to `server`,
> and push `main` to `origin` only after merging.

---

## Step 3: Pulling from Each Remote

### Pull from GitHub (origin)

```bash
git pull origin main
```

### Pull from the bare repository (server)

```bash
git pull server main
```

### Fetch from all remotes (without merging)

Retrieve the latest remote state without modifying your local branch:

```bash
git fetch --all
# Fetching origin
# Fetching server
```

After fetching, inspect all branches:

```bash
git branch -av
# * main                          a1b2c3d Merge pull request #8 ...
#   remotes/origin/main           a1b2c3d Merge pull request #8 ...
#   remotes/server/main           a1b2c3d Merge pull request #8 ...
```

Both `remotes/origin/main` and `remotes/server/main` are now listed separately.

---

## Step 4: Comparing the State of Two Remotes

### Check whether origin and server are in sync

```bash
git log origin/main..server/main --oneline
# No output means server is not ahead of origin

git log server/main..origin/main --oneline
# No output means origin is not ahead of server
```

If both commands produce no output, the two remotes are fully in sync.

### Check whether local is ahead of origin

```bash
git log origin/main..HEAD --oneline
# Commits shown here have not been pushed to origin yet
```

---

## Step 5: Setting the Upstream (Default Push Target)

To enable `git push` without specifying a remote each time, set an upstream:

```bash
git push -u origin main
```

After this, running `git push` alone pushes to `origin main`.

To push to `server` explicitly, always specify it:

```bash
git push server main
```

> **Note:** Only one upstream can be set per branch.
> It is not possible to set both `origin` and `server` as the upstream simultaneously.

---

## Common Workflow Patterns

### Pattern 1: server for daily work, origin for publishing

```bash
# Push to server during active development
git push server feature/add_xxx

# After merging to main, push to GitHub as well
git push origin main
```

### Pattern 2: Always keep both in sync

```bash
# Push to both remotes every time
git push origin main
git push server main
```

### Pattern 3: origin as primary, server as backup

```bash
# Use origin as the main remote (upstream already set)
git push

# Sync to server periodically
git push server main
```

---

## Summary

```bash
# 1. Add the server remote (first time only)
git remote add server /home/repository/<username>/server/my_project.git

# 2. Verify both remotes
git remote -v

# 3. Push to each remote
git push origin main
git push server main

# 4. Fetch from all remotes
git fetch --all

# 5. Compare the state of the two remotes
git log origin/main..server/main --oneline
git log server/main..origin/main --oneline
```

---

## Quick Command Reference

| Command | Description |
|---------|-------------|
| `git remote -v` | List all registered remotes |
| `git remote add <name> <URL>` | Add a new remote |
| `git remote remove <name>` | Remove a remote |
| `git push <remote> <branch>` | Push a branch to a specified remote |
| `git pull <remote> <branch>` | Pull a branch from a specified remote |
| `git fetch --all` | Fetch the latest state from all remotes |
| `git branch -av` | List local and all remote branches |
| `git log A..B --oneline` | Show commits in B that are not in A |

---

## Related Documents

- [Creating a Remote Repository on GitHub and Pushing Code](github_push_en.md)
