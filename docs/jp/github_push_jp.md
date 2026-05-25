# GitHub に Remote Repository を作成して Push する手順

ローカルで作ったコードを GitHub に公開・バックアップするまでの手順。

---

## リポジトリの種類を理解する

作業を始める前に、2 種類のリポジトリの違いを把握しておく。

| 種類 | 場所 | 説明 |
|------|------|------|
| **ローカルリポジトリ** | 自分の PC | ファイルを実際に編集・コミットする場所 |
| **リモートリポジトリ** | GitHub のサーバー | チームで共有する中央リポジトリ |

```
[自分の PC]                          [GitHub サーバー]
ローカルリポジトリ  ---- push ---->  リモートリポジトリ
                   <--- clone/pull --
```

---

## 事前確認

### Git バージョンの確認

```bash
git --version
# 例：git version 2.45.2
```

### 作業場所の確認

```bash
pwd
# 例：/home/yamamoto
```

---

## Step 1：GitHub でリポジトリを作成する

### 1-1. GitHub にログインする

[https://github.com](https://github.com) にアクセスしてログインする。

### 1-2. 新しいリポジトリを作成する

右上の `+` → `New repository` をクリックして以下を設定する。

| 項目 | 内容 |
|------|------|
| **Repository name** | 例：`example_repo` |
| **Public / Private** | 用途に合わせて選択 |
| **Add a README file** | チェックしなくてOK（空の repo で作る場合） |

設定が終わったら **Create repository** をクリックする。

### 1-3. リポジトリの URL を確認する

作成後に表示されるページで URL をコピーしておく。

| プロトコル | URL の形式 |
|-----------|-----------|
| HTTPS | `https://github.com/USERNAME/example_repo.git` |
| SSH（推奨） | `git@github.com:USERNAME/example_repo.git` |

> **ポイント：** SSH を使うと push のたびにパスワードを入力する必要がなくなる。
> 次の Step 2 で SSH 鍵を登録しておくと便利。

---

## Step 2：SSH 鍵を登録する（推奨）

HTTPS でも動作するが、SSH を使うと認証が自動化されて楽になる。
すでに SSH 鍵を GitHub に登録済みの場合はこの Step をスキップしてよい。

### 2-1. SSH 鍵を生成する

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Enter を 3 回押してデフォルト設定のまま進める。
鍵は `~/.ssh/id_ed25519`（秘密鍵）と `~/.ssh/id_ed25519.pub`（公開鍵）に保存される。

### 2-2. 公開鍵を確認する

```bash
cat ~/.ssh/id_ed25519.pub
```

`ssh-ed25519 AAAA...` から始まる1行が表示される。これをコピーしておく。

### 2-3. GitHub に公開鍵を登録する

**GitHub → Settings → SSH and GPG keys → New SSH key**

「Title」に任意の名前（例：`my-laptop`）を入力し、コピーした公開鍵を「Key」に貼り付けて **Add SSH key** をクリックする。

### 2-4. 接続を確認する

```bash
ssh -T git@github.com
```

成功すると以下のように表示される：

```
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## Step 3：ローカルリポジトリを作成する

### 3-1. 作業ディレクトリを作成する

```bash
mkdir example_repo
cd example_repo
```

### 3-2. Git リポジトリとして初期化する

```bash
git init
```

`.git/` ディレクトリが作成される。これで Git の管理下になった。

```bash
ls -a
# .  ..  .git
```

### 3-3. ファイルを作成する

```bash
echo "# Example Repo" > README.md
```

ファイルが作成されたか確認する：

```bash
ls
# README.md
```

---

## Step 4：コミットしてプッシュする

### 4-1. ファイルをステージに追加する

```bash
git add README.md
```

特定のファイルではなく全ファイルをまとめてステージする場合：

```bash
git add .
```

ステージ状態を確認する：

```bash
git status
# Changes to be committed:
#   new file:   README.md
```

### 4-2. コミットする

```bash
git commit -m "Initial commit"
```

コミット後に履歴を確認する：

```bash
git log --oneline
# a1b2c3d Initial commit
```

### 4-3. リモートリポジトリを登録する

**SSH を使う場合（推奨）：**

```bash
git remote add origin git@github.com:USERNAME/example_repo.git
```

**HTTPS を使う場合：**

```bash
git remote add origin https://github.com/USERNAME/example_repo.git
```

> **ポイント：** HTTPS を使う場合、`git push` 時のパスワードには Personal Access Token（PAT）を入力する必要がある。
> 発行手順は [github_token_https_jp.md](github_token_https_jp.md) を参照。

登録されたか確認する：

```bash
git remote -v
# origin  git@github.com:USERNAME/example_repo.git (fetch)
# origin  git@github.com:USERNAME/example_repo.git (push)
```

### 4-4. ブランチ名を `main` に変更する

```bash
git branch -M main
```

> **ポイント：** `git init` で作られるデフォルトのブランチ名は環境によって `master` になる場合がある。
> GitHub のデフォルトに合わせて `main` に統一しておく。

### 4-5. GitHub へプッシュする

```bash
git push -u origin main
```

プッシュ後にブランチの状態を確認する：

```bash
git branch -v
# * main  a1b2c3d Initial commit
```

> **ポイント：** `-u` は初回のみ必要（`origin/main` を upstream として設定する）。
> 2 回目以降は `git push` だけでOK。

---

## 全体の流れまとめ

```bash
# 1. 作業ディレクトリを作成して初期化
mkdir example_repo
cd example_repo
git init

# 2. ファイルを作成
echo "# Example Repo" > README.md

# 3. ステージしてコミット
git add .
git commit -m "Initial commit"

# 4. リモートを登録してプッシュ
git remote add origin git@github.com:USERNAME/example_repo.git
git branch -M main
git push -u origin main
```

---

## よく使うコマンド早見表

| コマンド | 用途 |
|---------|------|
| `git status` | 変更・ステージ・未追跡ファイルの状態を確認 |
| `git log --oneline` | コミット履歴をコンパクトに確認 |
| `git remote -v` | 登録済みリモートと URL を確認 |
| `git branch` | ローカルブランチ一覧（`*` が現在地） |
| `git push` | 2 回目以降のプッシュ（upstream 設定済みの場合） |

---

## 付録

### 既存フォルダを GitHub 管理する場合

すでにローカルにプロジェクトフォルダがある場合は Step 3-1（ディレクトリ作成）をスキップして以下を実行する：

```bash
cd existing_folder
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:USERNAME/example_repo.git
git branch -M main
git push -u origin main
```

### `.gitignore` の設定（Python の例）

Git に追跡させたくないファイルをあらかじめ除外しておく：

```bash
echo "__pycache__/" >> .gitignore
echo "*.pyc"        >> .gitignore
echo ".venv/"       >> .gitignore
```

### 空フォルダを Git で管理したい場合

Git は空ディレクトリを追跡しないため、プレースホルダーファイルを置く：

```bash
mkdir output
touch output/.gitkeep
git add output/.gitkeep
```
