# Git vs. GitHub, and Understanding Repository Types

An introductory document for anyone touching Git or GitHub for the first time. Get the basic picture here, then move on to the hands-on steps starting with [01](01_server_bare_repo_create_en.md) for a smoother learning curve.

---

## What You'll Learn Here

- What the difference between Git and GitHub actually is
- What "local repository," "remote repository," and "bare repository" each mean

---

## 1. Git vs. GitHub

### What Is Git?

Git is a piece of software called a "version control system." You install it on your own computer and use it locally.

- Records the history of changes to files
- Lets you go back to any past state at any time
- Can integrate (merge) changes made by multiple people
- Works entirely offline — no internet connection required

### What Is GitHub?

GitHub is a web service (a hosting service) for storing repositories that are managed with Git.

- Stores your Git repository on the internet so it can be shared with others
- Provides collaboration features that Git itself doesn't have, such as Pull Requests, Issues, and GitHub Actions
- Similar services include GitLab and Bitbucket

### Summary

| | Git | GitHub |
|---|---|---|
| What it is | Version control software | Web hosting service |
| Where it runs | Your own computer (local) | On the internet (cloud) |
| Can you skip it? | No — nothing works without Git | Yes — you can run Git-only workflows without GitHub (e.g., an in-house server) |
| Main features | History tracking, diffs, branches, merging | Repository sharing, PRs, Issues, CI/CD, etc. |

> **Analogy:** Git is the mechanism that records a document's change history. GitHub is the place and service that stores and shares that document online. GitHub can't exist without Git, but Git can be used entirely on its own without GitHub — [01](01_server_bare_repo_create_en.md) and [02](02_server_git_workflow_en.md) in this repository are exactly that kind of GitHub-free example.

---

## 2. Types of Repositories: Local / Remote / Bare

### Local Repository

A repository that lives on your own computer and has both the actual files you edit (the working tree) and a `.git` folder. This is where you edit files and build up history with `git add` → `git commit`.

### Remote Repository

"Remote" is a general term for **whatever your local repository pushes to and pulls from** — it does not describe a specific kind of repository. It doesn't matter what the other end actually is:

- A bare repository you set up yourself on a server
- A repository hosted on GitHub
- A repository on a colleague's computer

Any of these becomes a "remote" the moment you register it locally with `git remote add`. In other words, "remote repository" describes a relationship — "the other end you sync with via push/pull" — not a type of repository.

### Bare Repository

A repository that has no working tree (no actual editable files), consisting only of the contents of `.git`. You create one with `git init --bare`.

- It's not a place where anyone edits files directly
- It exists purely as a shared drop-off point that multiple people push to and pull from
- A repository on GitHub is, internally, managed with this same bare-repository mechanism

So it helps to think of "a GitHub repository" as "a bare repository hosted in the cloud, plus collaboration features like PRs and Issues" on top.

### The Three, as a Diagram

```
[Local repository]                        [Remote repository]
~/example/  (has a working tree)           One of two things:
  ex.py                                    ① A bare repository you create yourself
  .git/                                       on a server (covered in 01, 02)
        -- git push -->                    ② A repository hosted on GitHub
        <-- git pull --                       (covered in 03, 04)
```

| Type | Working tree | Main purpose | Related documents |
|---|---|---|---|
| Local repository | Yes | Where you actually edit files and commit | - |
| Bare repository (self-hosted) | No | A shared push/pull location you set up yourself | [01](01_server_bare_repo_create_en.md), [02](02_server_git_workflow_en.md) |
| GitHub repository | No (browsable on the web) | A shared push/pull location plus PR/Issue features | [03](03_github_push_en.md), [04](04_multi_remote_en.md) |

> **Note:** Because "remote" is just a role, a single local repository can register both an in-house bare repository and GitHub as two separate remotes at the same time. This advanced pattern is covered in [04](04_multi_remote_en.md).

---

## Documents to Read Next

- [Creating a Bare Repository on the Server and Pushing](01_server_bare_repo_create_en.md)
- [Create GitHub Remote Repo and Push](03_github_push_en.md)
