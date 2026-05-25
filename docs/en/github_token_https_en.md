# Registering a Personal Access Token (Classic) for GitHub HTTPS Access

When using `git push` over HTTPS, you must use a Personal Access Token (PAT) instead of a password.
GitHub discontinued password authentication in 2021, so pushing without a PAT will result in an authentication error.

---

## Prerequisites

### Check Git version

```bash
git --version
# e.g., git version 2.45.2
```

---

## Step 1: Generate a Personal Access Token

### 1-1. Open GitHub settings

Log in to GitHub, then click your avatar in the top-right corner → **Settings**.

### 1-2. Navigate to the token page

Click **Developer settings** at the bottom of the left sidebar.

```
Settings
└── Developer settings
    └── Personal access tokens
        └── Tokens (classic)
```

Select **Personal access tokens → Tokens (classic)**.

### 1-3. Start generating a new token

Click **Generate new token → Generate new token (classic)**.

### 1-4. Configure the token

| Field | Value |
|-------|-------|
| **Note** | Describe the token's purpose (e.g., `my-laptop`) |
| **Expiration** | Set an expiry date (e.g., 90 days). `No expiration` is not recommended |
| **Select scopes** | Check at least `repo` |

**Operations enabled by the `repo` scope:**

| Scope | Description |
|-------|-------------|
| `repo` | Read and write access to private and public repositories |
| `repo:status` | Read and write commit statuses |
| `public_repo` | Sufficient if you only need to access public repositories |

### 1-5. Generate and copy the token

Click **Generate token** to display the token.

> **Important:** The token is shown only once. Copy and save it before leaving this page.

```
ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## Step 2: Push Using the Token

### 2-1. Register the remote with HTTPS

```bash
git remote add origin https://github.com/USERNAME/example_repo.git
```

If already registered, just verify:

```bash
git remote -v
# origin  https://github.com/USERNAME/example_repo.git (fetch)
# origin  https://github.com/USERNAME/example_repo.git (push)
```

### 2-2. Run the push

```bash
git push -u origin main
```

When prompted for credentials, enter the following:

| Field | What to enter |
|-------|--------------|
| **Username** | Your GitHub username |
| **Password** | Paste the token directly (not your login password) |

> **Note:** Although the prompt says "Password", you must paste the token you generated —
> not your GitHub account password.

---

## Step 3: Cache the Token to Avoid Repeated Input

Entering the token on every push is tedious. Cache your credentials to skip it.

### Option 1: Temporary cache (recommended — more secure)

```bash
git config --global credential.helper cache
```

Credentials are cached for 15 minutes by default. To extend the duration (e.g., 1 hour):

```bash
git config --global credential.helper 'cache --timeout=3600'
```

### Option 2: Permanent storage (convenient but stores token in plaintext)

```bash
git config --global credential.helper store
```

> **Warning:** Using `store` saves the token in plaintext to `~/.git-credentials`.
> Do not use this on shared servers or machines accessible by others.

Check the current credential helper setting:

```bash
git config --global credential.helper
# cache  or  store
```

---

## Managing Your Token

### Review existing tokens

You can view a list of issued tokens at:

**GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**

The token string cannot be displayed again, but you can see its **Note**, **expiration date**, and **last used date**.

### Revoke a token

Click **Delete** next to the token on the page above to revoke it immediately.
Revoke the token right away if you suspect it has been leaked.

### When a token has expired

Running `git push` produces an error like:

```
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/...'
```

Generate a new token, clear the credential cache, then push again:

```bash
# Clear the cache (when using the cache helper)
git credential-cache exit

# Push again — you will be prompted for credentials
git push
```

---

## Summary

```bash
# 1. Generate a token on GitHub (browser)
#    Settings → Developer settings → Personal access tokens → Tokens (classic)
#    → Generate new token (classic) → check repo → Generate token → copy

# 2. Register the remote with HTTPS
git remote add origin https://github.com/USERNAME/example_repo.git

# 3. Push (enter GitHub username and token when prompted)
git push -u origin main

# 4. Cache the token (optional)
git config --global credential.helper cache
```

---

## Quick Command Reference

| Command | Purpose |
|---------|---------|
| `git remote -v` | Check registered remotes and their URLs |
| `git config --global credential.helper` | Check the current credential helper setting |
| `git credential-cache exit` | Clear the credential cache |
| `git push -u origin main` | First push (sets upstream) |
| `git push` | Subsequent pushes |

---

## Related Documents

- [Creating a Remote Repository on GitHub and Pushing Code](github_push_en.md)
