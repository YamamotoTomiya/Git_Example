# Creating a Remote Repository on GitHub and Pushing Code

Steps to publish and back up locally created code to GitHub.

---

## Understanding Repository Types

Before you start, understand the difference between the two types of repositories.

| Type | Location | Description |
|------|----------|-------------|
| **Local repository** | Your PC | Where you actually edit files and create commits |
| **Remote repository** | GitHub server | Central repository shared with the team |

```
[Your PC]                            [GitHub server]
Local repository  ---- push ---->   Remote repository
                  <--- clone/pull --
```

---

## Prerequisites

### Check Git version

```bash
git --version
# e.g., git version 2.45.2
```

### Check your working location

```bash
pwd
# e.g., /home/yamamoto
```

---

## Step 1: Create a Repository on GitHub

### 1-1. Log in to GitHub

Go to [https://github.com](https://github.com) and log in.

### 1-2. Create a new repository

Click `+` in the top-right corner → `New repository` and configure the following.

| Field | Value |
|-------|-------|
| **Repository name** | e.g., `example_repo` |
| **Public / Private** | Choose based on your needs |
| **Add a README file** | Leave unchecked is fine (when creating an empty repo) |

Click **Create repository** when done.

### 1-3. Copy the repository URL

On the page shown after creation, copy the URL.

| Protocol | URL format |
|----------|-----------|
| HTTPS | `https://github.com/USERNAME/example_repo.git` |
| SSH (recommended) | `git@github.com:USERNAME/example_repo.git` |

> **Note:** Using SSH eliminates the need to enter a password on every push.
> Set up your SSH key in Step 2 below.

---

## Step 2: Register an SSH Key (Recommended)

HTTPS also works, but SSH automates authentication and is more convenient.
Skip this step if you have already registered an SSH key with GitHub.

### 2-1. Generate an SSH key

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Press Enter 3 times to proceed with the default settings.
The keys are saved to `~/.ssh/id_ed25519` (private key) and `~/.ssh/id_ed25519.pub` (public key).

### 2-2. View your public key

```bash
cat ~/.ssh/id_ed25519.pub
```

A single line starting with `ssh-ed25519 AAAA...` will appear. Copy it.

### 2-3. Register the public key on GitHub

**GitHub → Settings → SSH and GPG keys → New SSH key**

Enter a name in "Title" (e.g., `my-laptop`), paste the copied public key into "Key", and click **Add SSH key**.

### 2-4. Test the connection

```bash
ssh -T git@github.com
```

On success, you will see:

```
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## Step 3: Create a Local Repository

### 3-1. Create a working directory

```bash
mkdir example_repo
cd example_repo
```

### 3-2. Initialize as a Git repository

```bash
git init
```

A `.git/` directory is created, placing the folder under Git management.

```bash
ls -a
# .  ..  .git
```

### 3-3. Create a file

```bash
echo "# Example Repo" > README.md
```

Confirm the file was created:

```bash
ls
# README.md
```

---

## Step 4: Commit and Push

### 4-1. Stage files

```bash
git add README.md
```

To stage all files at once instead of a specific file:

```bash
git add .
```

Check the staging status:

```bash
git status
# Changes to be committed:
#   new file:   README.md
```

### 4-2. Commit

```bash
git commit -m "Initial commit"
```

Check the commit history:

```bash
git log --oneline
# a1b2c3d Initial commit
```

### 4-3. Register the remote repository

**Using SSH (recommended):**

```bash
git remote add origin git@github.com:USERNAME/example_repo.git
```

**Using HTTPS:**

```bash
git remote add origin https://github.com/USERNAME/example_repo.git
```

> **Note:** When using HTTPS, you must enter a Personal Access Token (PAT) as the password during `git push`.
> See [github_token_https_en.md](github_token_https_en.md) for how to create one.

Confirm the remote was registered:

```bash
git remote -v
# origin  git@github.com:USERNAME/example_repo.git (fetch)
# origin  git@github.com:USERNAME/example_repo.git (push)
```

### 4-4. Rename the branch to `main`

```bash
git branch -M main
```

> **Note:** The default branch name created by `git init` may be `master` depending on your environment.
> Rename it to `main` to match GitHub's default.

### 4-5. Push to GitHub

```bash
git push -u origin main
```

Check the branch status after pushing:

```bash
git branch -v
# * main  a1b2c3d Initial commit
```

> **Note:** The `-u` flag is only needed the first time (it sets `origin/main` as the upstream).
> From the second push onward, `git push` alone is sufficient.

---

## Summary

```bash
# 1. Create and initialize the working directory
mkdir example_repo
cd example_repo
git init

# 2. Create a file
echo "# Example Repo" > README.md

# 3. Stage and commit
git add .
git commit -m "Initial commit"

# 4. Register remote and push
git remote add origin git@github.com:USERNAME/example_repo.git
git branch -M main
git push -u origin main
```

---

## Quick Command Reference

| Command | Purpose |
|---------|---------|
| `git status` | Check changes, staged files, and untracked files |
| `git log --oneline` | View commit history in compact form |
| `git remote -v` | Check registered remotes and their URLs |
| `git branch` | List local branches (`*` marks current branch) |
| `git push` | Push after the first time (upstream already set) |

---

## Appendix

### Managing an existing folder with GitHub

If you already have a project folder locally, skip Step 3-1 (creating a directory) and run:

```bash
cd existing_folder
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:USERNAME/example_repo.git
git branch -M main
git push -u origin main
```

### Setting up `.gitignore` (Python example)

Exclude files you do not want Git to track:

```bash
echo "__pycache__/" >> .gitignore
echo "*.pyc"        >> .gitignore
echo ".venv/"       >> .gitignore
```

### Tracking an empty folder with Git

Git does not track empty directories. Place a placeholder file inside:

```bash
mkdir output
touch output/.gitkeep
git add output/.gitkeep
```
