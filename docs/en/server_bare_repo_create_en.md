# Creating a Bare Repository on the Server and Pushing

Steps to create code locally, set up a bare repository on the server yourself, and push to it.

---

## Overview

```
[Your home directory]                        [Server shared area]
~/example/          -- git remote add -->   /home/repository/<username>/example.git
  ex.py             -- git push ------->    (bare repository)
```

1. Create code locally
2. Initialize Git locally
3. Create a bare repository on the server
4. Register it as a remote on your local machine
5. Commit and push

---

## Step 1: Create Code Locally

```bash
cd ~
mkdir example
cd example
```

Your prompt should read `<username>@vaccine-00:~/example$`.

Create a file:

```bash
touch ex.py
```

There are several ways to write content to the file.

**Option 1: Write with echo**

```bash
echo "print('hello')" > ex.py        # overwrite (create new)
echo "print('world')" >> ex.py       # append
```

> `>` overwrites; `>>` appends. Using `>` on an existing file erases its contents.

**Option 2: Edit with vi**

```bash
vi ex.py
```

| Key | Action |
|-----|--------|
| `i` | Switch to insert mode |
| `Esc` | Return to command mode |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |

Verify the file contents:

```bash
cat ex.py
# print('hello')
# print('world')
```

---

## Step 2: Initialize the Local Repository

Place `~/example` under Git management.

```bash
cd ~/example
git init
# Initialized empty Git repository in /home/<username>/example/.git/
```

A `.git/` directory is created, indicating the folder is now Git-managed.

Check the directory contents:

```bash
ls -a
# .  ..  .git  ex.py
```

If `.git/` is shown, Git management is active. The `-a` flag is required to show hidden entries.

Check the branch name:

```bash
git branch
# * master   ← rename to main if this shows master
# or
# * main     ← no change needed if already main
```

If the branch is named `master`, rename it to `main`:

```bash
git branch -m master main
git branch
# * main
```

> **Why use `main`:** More projects are moving from `master` to `main`, and services like GitHub now use `main` as the default. Keeping names consistent across the team prevents branch-name mismatches during push.

Check the current state:

```bash
git status
# On branch main
# Untracked files:
#   ex.py
```

---

## Step 3: Create a Bare Repository on the Server

**Create the bare repository under `/home/repository/<username>/`.**

```bash
cd /home/repository
mkdir <username>          # e.g., mkdir yamamoto
cd <username>
```

Your prompt should read `<username>@vaccine-00:/home/repository/<username>$`.

Create the bare repository:

```bash
git init --bare /home/repository/<username>/example.git
# Initialized empty Git repository in /home/repository/<username>/example.git/
```

> **Naming convention:** Append `.git` to the local folder name you want to push.
> Since the local folder is `example`, the bare repository is named `example.git`.

Confirm the repository was created:

```bash
ls /home/repository/<username>/
# example.git

ls /home/repository/<username>/example.git/
# HEAD  branches/  config  description  hooks/  info/  objects/  refs/
```

If only the contents of `.git/` are present (no working tree), the bare repository was created correctly.

Check that the bare repository points to `main`:

```bash
cat /home/repository/<username>/example.git/HEAD
# ref: refs/heads/main   ← OK if this shows main
```

If it shows `master`, update it to `main`:

```bash
git --git-dir=/home/repository/<username>/example.git symbolic-ref HEAD refs/heads/main
cat /home/repository/<username>/example.git/HEAD
# ref: refs/heads/main
```

> The `HEAD` of a bare repository points to the default branch. If the local and remote branch names differ, you will get a branch-name mismatch error during push, so align them here.

---

## Step 4: Register the Bare Repository as a Remote

Return to your local `~/example`:

```bash
cd ~/example
```

Add the bare repository as a remote:

```bash
git remote add origin /home/repository/<username>/example.git
# e.g., git remote add origin /home/repository/yamamoto/example.git
```

> `origin` is the alias (name) given to the remote. `origin` is the convention. Other names work too, but using `origin` consistently across the team makes things clearer.

Confirm the remote was registered:

```bash
git remote -v
# origin  /home/repository/yamamoto/example.git (fetch)
# origin  /home/repository/yamamoto/example.git (push)
```

Both `fetch` (download) and `push` (upload) should show the same URL.

---

## Step 5: Commit and Push

### 5-1. Stage files

```bash
git add .
```

Confirm files are staged:

```bash
git status
# Changes to be committed:
#   new file: ex.py
```

### 5-2. Commit

```bash
git commit -m "Add ex.py"
```

Confirm the commit:

```bash
git log --oneline
# a1b2c3d Add ex.py
```

### 5-3. Push

```bash
git push origin main
# or
git push origin master
# (use whichever matches your branch name from git init)
```

Adding `-u` on the first push lets you run just `git push` from then on:

```bash
git push -u origin main
```

> `-u` is short for `--set-upstream`. It configures the local `main` branch to track `origin/main`.

Verify after pushing:

```bash
git branch -av
# * main                a1b2c3d Add ex.py
#   remotes/origin/main a1b2c3d Add ex.py
```

If `remotes/origin/main` appears, the push to the bare repository was successful.

---

## Summary

```bash
# --- Create code locally ---
cd ~
mkdir example
cd example
touch ex.py
echo "print('hello')" > ex.py

# --- Initialize Git ---
git init

# --- Create the bare repository ---
mkdir /home/repository/<username>
git init --bare /home/repository/<username>/example.git

# --- Register as remote ---
cd ~/example
git remote add origin /home/repository/<username>/example.git

# --- Commit and push ---
git add .
git commit -m "Add ex.py"
git push -u origin main
```

---

## Common Errors and Fixes

**`error: src refspec main does not match any`**

```bash
# Immediately after git init there are no commits, so the branch does not exist yet
# → Create at least one commit before pushing
git add .
git commit -m "first commit"
git push origin main
```

**`error: failed to push some refs`**

```bash
# The remote and local are out of sync
# → Pull first, then push
git pull origin main
git push origin main
```

**Unsure whether the push target branch is `master` or `main`**

```bash
# Check your local branch name
git branch
# * master  ← use this name in the push command

git push origin master
```

---

## Related Documents

- [Cloning from a Bare Repository and Pushing](server_git_workflow_en.md)
- [Git Basic Command Reference](git_workflow_en.md)
- [Git Workflow Step by Step](git_workflow_steps_en.md)
