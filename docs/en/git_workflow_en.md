# Git Command Reference

---

## Core Concepts

### Repository

A place that stores the full history of file changes. The `.git/` folder is the actual data store.

| Type | Description |
|------|-------------|
| **Local repository** | Lives on your own PC. This is where you do your work. |
| **Remote repository** | Lives on a server like GitHub. Shared with your team. |

```
[Your PC]                          [GitHub]
Local repository  <-- pull --  Remote repository
                  -- push -->
```

---

### Branch

A "fork" in the commit history. Lets you work without touching `main`.

```
main:    A --- B --- C
                      \
feature:               D --- E   ← work here
```

- `main` branch: holds the stable/production code
- `feature/xxx` branch: created for new features or fixes
- After finishing, merge into `main` and delete the `feature` branch

---

### Local vs Remote vs Remote-tracking Branches

| Type | Location | Description |
|------|----------|-------------|
| **Local branch** | Your PC | Shown by `git branch`. You control these freely. |
| **Remote branch** | GitHub | Pushed with `git push`. Visible on GitHub. |
| **Remote-tracking branch** | Your PC | Looks like `origin/main`. A local snapshot of what the remote looked like last time you communicated. Updated by `git fetch`. |

```
[Your PC]
  main                 ← local branch (you control this)
  origin/main          ← remote-tracking branch (read-only snapshot of remote)

[GitHub]
  main                 ← remote branch
```

---

### What is HEAD?

A pointer to "the commit you are currently on."
Normally it points to the tip of your current branch.

```
main:  A --- B --- C ← HEAD (= tip of main)
```

---

### Bare Repository

A repository with **no working tree** — the directory where you actually edit files does not exist.
Only the raw Git data (the contents of `.git/`) is stored.

| Type | Working tree | Purpose |
|------|-------------|---------|
| **Normal repository** | Yes | Edit files and commit on your local PC |
| **Bare repository** | No | Central shared server (like GitLab/GitHub internally) |

```
Normal repository:               Bare repository:
  myproject/                       myproject.git/
  ├── .git/  ← Git data            ├── HEAD
  ├── src/   ← working tree        ├── objects/
  └── README ← working tree        └── refs/      ← only the .git/ contents
```

A bare repository **cannot be used to directly edit or commit files**.
It is intended purely as a destination for `git push`.

#### Creating a bare repository

```bash
# Initialize a new bare repository (conventionally named with a .git suffix)
git init --bare myproject.git

# Clone an existing repository as a bare repository
git clone --bare https://github.com/user/myproject.git
```

> **When should you use a bare repository?**
> - When setting up a central repository on a shared server or NAS
> - GitLab, GitHub, and similar services use bare repositories internally
> - For local development on your own PC, a normal repository is sufficient

---

## Option Reference

Common option meanings at a glance:

| Option | Meaning |
|--------|---------|
| `-r` | Short for `--remotes`. Targets remote-tracking branches. |
| `-a` | Short for `--all`. Targets local + remote-tracking branches. |
| `-b` | Short for `--branch` (used with `git checkout`). Creates a new branch and switches to it. |
| `-c` | Short for `--create` (used with `git switch`). Creates a new branch and switches to it. |
| `-d` | Short for `--delete`. Deletes a branch (only if already merged). |
| `-v` | Short for `--verbose`. Shows extra detail. |
| `-m` | Short for `--message`. Specifies the commit message. |
| `--oneline` | Shows each log entry on a single line. |
| `--graph` | Draws branch topology as ASCII art. |
| `--all` | Includes all branches. |
| `--no-ff` | Disables fast-forward; always creates a merge commit. |
| `--hard` | Resets branch pointer, staging area, and working tree all at once. |
| `--stat` | Shows only filenames and line-count changes (no full diff). |
| `--prune` | Removes local tracking refs for branches deleted on the remote. |
| `--detach` | Attaches HEAD directly to a commit instead of a branch. |

---

## Checking Status

```bash
# Show which files are modified, added, or deleted
git status

# List local branches only
git branch

# List remote-tracking branches only
#   -r = --remotes
git branch -r

# List all branches (local + remote-tracking)
#   -a = --all
git branch -a
```

---

## Viewing History

```bash
# Compact history (one commit per line)
git log --oneline

# History with branch graph across all branches
#   --graph: draw topology as ASCII art
#   --all: include every branch
git log --oneline --graph --all

# Show the changes introduced by a specific commit
git show <commit_id>
```

---

## Branch Operations

```bash
# Create a new branch and switch to it (modern syntax)
#   -c = --create
git switch -c feature/example

# Create a new branch and switch to it (classic syntax — same result)
#   -b = --branch
git checkout -b feature/example

# Switch to an existing branch
git switch main
git switch feature/example

# Create a local branch that tracks a remote-tracking branch
#   origin/main is the remote-tracking branch; this links your local branch to it
git switch -c main origin/main

# Delete a branch (only works if it has been merged)
#   -d = --delete
git branch -d feature/example
```

---

## Comparing Differences

```bash
# Summary of differences from main (filenames and line counts only)
#   --stat: concise stats, no full diff
git diff --stat main feature/example

# Full diff from main
git diff main feature/example

# Commits that exist in feature but not in main
#   main..feature/example: commits reachable from feature but not from main
git log --oneline main..feature/example
```

---

## Committing

```bash
# Stage a file (mark it for the next commit)
git add <filename>

# Commit with a message (-m specifies the message inline)
git commit -m "commit message"

# Push to the remote
git push origin <branch-name>
```

> **What is the staging area (index)?** A holding area for changes you have `git add`-ed.
> Flow: `working tree → git add → staging area → git commit → local repository → git push → remote repository`

---

## Merging

```bash
# Merge with an explicit merge commit (like a PR)
#   --no-ff: disables fast-forward, forces a merge commit to be created
git switch main
git pull origin main
git merge --no-ff feature/example -m "Merge branch 'feature/example'"
git push origin main
```

> **What is fast-forward?** When `main` has not moved since `feature` branched off,
> Git can simply advance the `main` pointer without creating a merge commit.
> `--no-ff` prevents this, so the history always shows where a merge happened.

---

## Remote Operations

```bash
# List remotes and their URLs
#   -v = --verbose (shows the URL)
git remote -v

# Fetch changes from remote and update remote-tracking branches
# (does NOT touch your working tree)
# Omitting "origin" fetches from the default remote
git fetch
git fetch origin

# After fetching, inspect what arrived before merging
#   HEAD..origin/main: commits on the remote that are not yet in your branch
git log --oneline HEAD..origin/main

# Fetch then merge manually (the safer alternative to git pull)
#   git pull does fetch + merge in one step, but doing it manually lets you review first
git fetch origin
git merge origin/main

# Delete a branch on the remote
git push origin --delete feature/example

# Remove local tracking refs for branches that no longer exist on the remote
#   --prune: cleans up stale origin/xxx entries
git fetch --prune origin
```

> **`git fetch` vs `git pull`:**
> - `git fetch`: downloads remote changes and updates **only the remote-tracking branch** (`origin/main`). Your working tree is untouched.
> - `git pull`: runs `git fetch` + `git merge` in one step. Your working tree is updated immediately.
> When you want to review incoming changes before applying them, use `fetch → log → merge` for a safer workflow.

---

## Viewing and Reverting Past State

```bash
# Temporarily view a past commit (enters detached HEAD state)
#   --detach: HEAD points directly to a commit, not a branch
git switch --detach <commit_id>

# Return to your branch from detached HEAD
git switch main

# Reset a branch to a past commit (all uncommitted changes are lost)
#   --hard: overwrites pointer, staging area, and working tree
git reset --hard <commit_id>
```

> **Warning:** `git reset --hard` **permanently discards all uncommitted changes**,
> including staged and unstaged edits. Use with care — this cannot be undone.
