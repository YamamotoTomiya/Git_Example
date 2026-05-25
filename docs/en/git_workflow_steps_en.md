# Git Workflow Step-by-Step Guide

A practical guide covering the full Git workflow from cloning a repository to deleting a merged branch.

---

## 1. Clone the Remote Repository

Download a remote repository to your local machine.

```bash
git clone <REMOTE_URL>
cd <REPOSITORY_NAME>
```

Example:

```bash
git clone git@github.com:<username>/my_project.git
cd my_project
```

---

## 2. Update the Local main Branch

Synchronize your local `main` with the latest remote version before starting any work.

```bash
git checkout main
git pull origin main
```

---

## 3. Create a Feature Branch

Create a new branch for your changes so that `main` stays clean.

```bash
git checkout -b feature/add_xxx
```

Branch naming conventions:

```
feature/add_xxx       # adding something new
feature/fix_bug       # fixing a bug
feature/update_docs   # updating documentation
```

---

## 4. Edit Files

Open and modify the files you need to change.

```bash
vim main.py
```

or open the project folder in VS Code:

```bash
code .
```

---

## 5. Check Changes

Verify which files have been modified before staging them.

```bash
# Show which files changed
git status

# Show the exact line-level differences
git diff
```

---

## 6. Stage and Commit Changes

Add the changed files to the staging area, then commit them.

```bash
git add .
git commit -m "Add new feature"
```

Example:

```bash
git commit -m "Delete example.py"
```

---

## 7. Push the Branch to the Remote Repository

Upload your local branch to GitHub. GitHub will usually display a Pull Request URL after pushing.

```bash
git push origin feature/add_xxx
```

---

## 8. Compare the Branch with main

Switch to `main`, pull the latest changes, then inspect the differences.

```bash
git checkout main
git pull origin main
```

| Command | Description |
|---------|-------------|
| `git diff main..feature/add_xxx` | Full diff between main and the feature branch |
| `git diff --name-only main..feature/add_xxx` | Show only changed file names |
| `git log --oneline main..feature/add_xxx` | List commits in feature branch not yet in main |
| `git log --oneline --graph main..feature/add_xxx` | Same as above, with a graph view |

---

## 9. Merge the Branch into main

Merge your feature branch into `main` locally.

```bash
git merge feature/add_xxx
```

If there are no conflicts, the merge completes automatically.

---

## 10. Push the Updated main Branch

Upload the merged `main` to the remote repository.

```bash
git push origin main
```

If using another remote:

```bash
git push server main
```

---

## 11. Delete the Merged Branch

Remove the branch both locally and on the remote once the merge is complete.

Delete the local branch:

```bash
git branch -d feature/add_xxx
```

Delete the remote branch:

```bash
git push origin --delete feature/add_xxx
```

For another remote:

```bash
git push server --delete feature/add_xxx
```

---

## 12. Remove Stale Remote-Tracking Branches Locally

Clean up local references to remote branches that have already been deleted.

```bash
git fetch origin --prune
```

---

## Useful Commands

### Branch Listing

| Command | Description |
|---------|-------------|
| `git branch` | Show local branches |
| `git branch -r` | Show remote-tracking branches |
| `git branch -a` | Show all branches (local + remote-tracking) |
| `git status` | Show current branch and working tree status |

---

## Notes

- `.gitignore` only affects **untracked** files. Files already tracked by Git will continue to be committed even if added to `.gitignore`.
- To stop tracking an already-tracked file:

```bash
git rm --cached <FILE_NAME>
```

Example:

```bash
git rm --cached path/to/file.txt
```

---

## See Also

- [Git Command Reference (English)](git_workflow_en.md)
- [Git Command Reference (Japanese)](git_workflow_jp.md)
