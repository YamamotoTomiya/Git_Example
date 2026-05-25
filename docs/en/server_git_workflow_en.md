# Git Workflow Using a Bare Repository on the Server

Steps for cloning, creating a branch, and pushing on the vaccine server (vaccine-00).

---

## Understanding Repository Types

Before you start, understand the difference between the three types of repositories.

| Type | Location | Description |
|------|----------|-------------|
| **Local repository** | Your home directory | Where you actually edit files and create commits |
| **Remote repository** | GitHub or similar server | Central repository shared with the team (e.g., GitHub) |
| **Bare repository** | Shared area on the server | A repository with no working tree — receives pushes only |

```
[Your home directory]               [Shared area on vaccine server]
Local repository  <-- clone/pull -- Bare repository (/home/repository/)
                  ---- push ------>
```

**Characteristics of a bare repository:**
- Contains only the contents of `.git/` — files cannot be edited directly
- By convention, the folder name ends with `.git` (e.g., `vaccine_example.git`)
- GitHub and GitLab also use bare repositories internally

---

## Prerequisites

### Check Git version

```bash
git --version
# e.g., git version 2.45.2
```

### Check your working location

```bash
# Confirm you are in your home directory
cd ~
pwd
# e.g., /home/yamamoto
```

---

## Step 1: Clone from the Bare Repository

### 1-1. Create a working directory

```bash
cd ~
mkdir example    # any name is fine
cd example
```

Your prompt should read `<username>@vaccine-00:~/example$`.

### 1-2. Locate the bare repository

On the vaccine server, bare repositories are stored under `/home/repository/`.

```bash
ls /home/repository/tyamamoto/server/
# e.g., vaccine_example.git
```

### 1-3. Clone

```bash
git clone /home/repository/tyamamoto/server/vaccine_example.git
```

> **Note:** For GitHub you would specify `https://...` or `git@github.com:...`,
> but a bare repository on the server can be cloned using its local path directly.

### 1-4. Verify the clone succeeded

```bash
ls
# vaccine_example should appear

cd vaccine_example
ls -a
# .  ..  .git  .gitignore  README.md  docs  job_scripts  src  ...
```

If the `.git/` directory is present, the folder is under Git management.

---

## Step 2: Create a Branch and Push

### 2-1. Check the current branch

```bash
git branch
# * main  ← the branch marked with * is where you currently are
```

### 2-2. Create and switch to a new branch

```bash
git checkout -b feature/add_<username>
# e.g., git checkout -b feature/add_yamamoto
```

**Branch naming conventions:**

Branch names are commonly structured as **category/description** separated by `/`.
The slash is treated as part of the name, not a directory separator.

```
feature/add_yamamoto      # adding a new file or feature
feature/fix_typo          # fixing a typo or minor mistake
feature/update_readme     # updating documentation or an existing file
bugfix/issue_42           # bug fix (some teams prefer the bugfix/ prefix)
```

| Prefix | When to use |
|--------|-------------|
| `feature/` | Regular work: new features, adding files |
| `bugfix/` | Bug fixes |
| `hotfix/` | Emergency fixes for production |
| `docs/` | Documentation-only changes |

> **Why use slashes:** In larger projects, `git branch -a` groups branches by category, making the output easier to read. It is not required, but consistent naming across the team simplifies management.

Confirm you are on the new branch:

```bash
git branch
#   main
# * feature/add_yamamoto   ← * should have moved here
```

### 2-3. Create your folder and files

```bash
cd student_6th
mkdir <username>          # e.g., mkdir yamamoto
cd <username>
touch ex.py               # create an empty file
```

There are several ways to write content to the file:

**Option 1: Write a line with echo (simple)**

```bash
echo "print('hello')" > ex.py        # overwrite (create new or replace)
echo "print('world')" >> ex.py       # append (add to the end)
```

> `>` overwrites; `>>` appends. Using the wrong one can erase the file contents.

**Option 2: Edit with vi**

```bash
vi ex.py
```

Basic vi commands:

| Key | Action |
|-----|--------|
| `i` | Switch to insert mode |
| `Esc` | Return to command mode |
| `:wq` | Save and quit |
| `:q!` | Quit without saving |

### 2-4. Check the change status

```bash
git status
# Newly created files should appear under "Untracked files"
```

### 2-5. Stage and commit

```bash
git add .
git commit -m "Add ex.py for yamamoto"
```

Example commit messages:

```bash
git commit -m "Add yamamoto directory and example script"
```

### 2-6. Push the branch

```bash
git push origin feature/add_<username>
# e.g., git push origin feature/add_yamamoto
```

After pushing, the branch is reflected in the bare repository. Use `git branch -v` to list local branches and their latest commits:

```bash
git branch -v
#   main                    a1b2c3d Merge pull request #8 from YamamotoTomiya/feature/add_hayashi
# * feature/add_yamamoto    f4e5d6c Add yamamoto directory and example script
```

| Column | Description |
|--------|-------------|
| `*` | The branch you are currently on |
| Branch name | Branches that exist locally |
| Commit ID | Shortened hash of the latest commit on that branch |
| Commit message | First line of the latest commit |

To see remote branches as well:

```bash
git branch -av
# * feature/add_yamamoto              f4e5d6c Add yamamoto directory and example script
#   main                              a1b2c3d Merge pull request #8 ...
#   remotes/origin/main               a1b2c3d Merge pull request #8 ...
#   remotes/origin/feature/add_yamamoto f4e5d6c Add yamamoto directory and example script
```

---

## Summary

```bash
# 1. Clone
cd ~/example
git clone /home/repository/tyamamoto/server/vaccine_example.git
cd vaccine_example

# 2. Create branch
git checkout -b feature/add_<username>

# 3. Create files
cd student_6th
mkdir <username>
cd <username>
touch ex.py

# 4. Commit
git add .
git commit -m "Add <username> directory"

# 5. Push
git push origin feature/add_<username>
```

---

## Quick Command Reference

| Command | Description |
|---------|-------------|
| `git branch` | List branches (`*` marks current branch) |
| `git status` | Check changed files |
| `git log --oneline` | View commit history in one line per commit |
| `git diff` | Show detailed diff of changes |
| `git push origin <branch>` | Push a specified branch to the remote |

---

## Removing a Cloned Repository

### Check before deleting

Deleting a cloned directory is just a folder deletion, but **changes that have not been pushed cannot be recovered**. Verify the following before deleting.

**1. Check for uncommitted changes**

```bash
git status
# "nothing to commit, working tree clean" means it is safe to delete
# If changes remain, commit or discard them before deleting
```

**2. Check for unpushed commits**

```bash
git log origin/main..HEAD --oneline
# No output means there are no local-only commits

# If you have a feature branch, check it too
git log origin/feature/add_<username>..HEAD --oneline
```

> Pushed commits are preserved in the bare repository, so deleting the clone does not lose them.
> Local-only commits will be gone along with the directory.

---

### Delete

Once you have confirmed it is safe, delete the local clone directory.

```bash
# Move one level up from the cloned directory, then delete
cd ~/example
rm -rf vaccine_example
```

Confirm the deletion:

```bash
ls
# vaccine_example should no longer appear
```

> **Warning about `rm -rf`:**
> - `-r` (recursive) deletes the directory and all contents; `-f` (force) skips confirmation
> - Deleted files do **not** go to the trash — they are gone immediately with no undo
> - Never run this against broad paths like `/` or `~`

---

### Impact on the bare and remote repositories

| What you deleted | Impact on the bare repository |
|-----------------|-------------------------------|
| Local clone (`~/example/vaccine_example`) | **No impact.** The bare repository on the server remains intact |
| The bare repository itself (`/home/repository/...`) | Everyone is affected. **Do not touch it** |

You can re-clone at any time:

```bash
git clone /home/repository/tyamamoto/server/vaccine_example.git
```

---

## Related Documents

- [Git Basic Command Reference](git_workflow_en.md)
- [Git Workflow Step by Step](git_workflow_steps_en.md)
