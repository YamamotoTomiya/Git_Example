# 応用編：GitHub とベアリポジトリを両方 remote として管理する

GitHub（`origin`）とサーバー上のベアリポジトリ（`server`）を
同時に remote として管理する方法。

---

## なぜ 2 つの remote を使うのか

| remote 名 | 場所 | 主な用途 |
|-----------|------|---------|
| `origin` | GitHub | 公開・バックアップ・Pull Request |
| `server` | ベアリポジトリ（`/home/repository/`） | チーム内での高速なやり取り・サーバー上での直接実行 |

```
[ローカル]
    │
    ├── push/pull ──→ origin（GitHub）        公開・PR・バックアップ
    │
    └── push/pull ──→ server（ベアリポジトリ）  チーム内共有・サーバー実行
```

両方を使い分けることで、サーバー内の作業は `server` で速く済ませ、
公開や Pull Request は `origin`（GitHub）で行うことができる。

---

## 事前確認

現在の remote 登録状況を確認する：

```bash
git remote -v
```

以下のように 2 つ登録されていれば準備完了：

```
origin  git@github.com:<username>/my_project.git (fetch)
origin  git@github.com:<username>/my_project.git (push)
server  /home/repository/<username>/server/my_project.git (fetch)
server  /home/repository/<username>/server/my_project.git (push)
```

---

## Step 1：2 つ目の remote を追加する

すでに `origin`（GitHub）が登録済みの場合に `server` を追加する手順。

### 1-1. ベアリポジトリを remote として追加する

```bash
git remote add server /home/repository/<username>/server/my_project.git
```

### 1-2. 登録を確認する

```bash
git remote -v
# origin  git@github.com:<username>/my_project.git (fetch)
# origin  git@github.com:<username>/my_project.git (push)
# server  /home/repository/<username>/server/my_project.git (fetch)
# server  /home/repository/<username>/server/my_project.git (push)
```

> **ポイント：** `git remote add <名前> <URL>` の `<名前>` は任意。
> `origin` と `server` はあくまで慣例名であり、別の名前でも動作する。

---

## Step 2：push の使い分け

### GitHub（origin）に push する

```bash
git push origin main
```

### ベアリポジトリ（server）に push する

```bash
git push server main
```

### ブランチを両方に push する

```bash
git push origin feature/add_xxx
git push server feature/add_xxx
```

> **ポイント：** どちらか一方だけに push することもできる。
> たとえば作業中のブランチは `server` のみに push して、
> マージ後の `main` だけ `origin` に push する、という運用も可能。

---

## Step 3：pull の使い分け

### GitHub（origin）から pull する

```bash
git pull origin main
```

### ベアリポジトリ（server）から pull する

```bash
git pull server main
```

### 全 remote の最新情報を取得する（fetch）

pull はせずに、リモートの状態だけ手元に取り込む：

```bash
git fetch --all
# Fetching origin
# Fetching server
```

fetch 後に全ブランチの状態を確認する：

```bash
git branch -av
# * main                          a1b2c3d Merge pull request #8 ...
#   remotes/origin/main           a1b2c3d Merge pull request #8 ...
#   remotes/server/main           a1b2c3d Merge pull request #8 ...
```

`remotes/origin/main` と `remotes/server/main` がそれぞれ表示される。

---

## Step 4：2 つの remote の状態を比較する

### origin と server が同じ状態か確認する

```bash
git log origin/main..server/main --oneline
# 何も表示されなければ origin が server より遅れていない

git log server/main..origin/main --oneline
# 何も表示されなければ server が origin より遅れていない
```

両方に何も表示されなければ、2 つの remote は同期している。

### ローカルが origin より進んでいるか確認する

```bash
git log origin/main..HEAD --oneline
# 表示されたコミットがまだ origin に push されていないもの
```

---

## Step 5：upstream（デフォルト push 先）を設定する

`git push` だけで push できるようにするには、upstream を設定する。

```bash
git push -u origin main
```

以降は `git push` だけで `origin main` に push できる。

`server` にも upstream を設定したい場合は、別のブランチを使うか、
push 時に明示的に指定する（`git push server main`）。

> **ポイント：** upstream は 1 つのブランチに 1 つしか設定できない。
> `origin` と `server` を同時に upstream にすることはできない。

---

## よくある運用パターン

### パターン 1：普段は server、公開時に origin

```bash
# 作業中は server に push
git push server feature/add_xxx

# main にマージ後、GitHub にも push
git push origin main
```

### パターン 2：両方に常に同期する

```bash
# push を 2 回実行する
git push origin main
git push server main
```

### パターン 3：origin をメインにして server はバックアップ

```bash
# origin をメインで使う（upstream 設定済み）
git push

# 定期的に server にも同期する
git push server main
```

---

## 全体の流れまとめ

```bash
# 1. server remote を追加する（初回のみ）
git remote add server /home/repository/<username>/server/my_project.git

# 2. 両方の remote を確認する
git remote -v

# 3. それぞれに push する
git push origin main
git push server main

# 4. 全 remote の状態を取得する
git fetch --all

# 5. 2 つの remote の状態を比較する
git log origin/main..server/main --oneline
git log server/main..origin/main --oneline
```

---

## よく使うコマンド早見表

| コマンド | 説明 |
|---------|------|
| `git remote -v` | 登録済み remote の一覧を表示 |
| `git remote add <名前> <URL>` | 新しい remote を追加 |
| `git remote remove <名前>` | remote を削除 |
| `git push <remote> <branch>` | 指定 remote にブランチを push |
| `git pull <remote> <branch>` | 指定 remote からブランチを pull |
| `git fetch --all` | 全 remote から最新情報を取得 |
| `git branch -av` | ローカル・全 remote のブランチを一覧表示 |
| `git log A..B --oneline` | A にはなく B にあるコミットを表示 |

---

## 関連ドキュメント

- [GitHub Remote Repository の作成と Push](github_push_jp.md)
