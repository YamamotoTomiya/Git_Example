# GitHub HTTPS 接続用 Personal Access Token (Classic) の登録手順

HTTPS で `git push` するとき、パスワードの代わりに Personal Access Token（PAT）を使う必要がある。
GitHub は 2021 年以降、パスワード認証を廃止しており、PAT を使わないと認証エラーになる。

---

## 事前確認

### Git バージョンの確認

```bash
git --version
# 例：git version 2.45.2
```

---

## Step 1：Personal Access Token を発行する

### 1-1. GitHub の設定画面を開く

GitHub にログインし、右上のアイコン → **Settings** をクリックする。

### 1-2. Token 発行ページに移動する

左側メニューの一番下にある **Developer settings** をクリックする。

```
Settings
└── Developer settings
    └── Personal access tokens
        └── Tokens (classic)
```

**Personal access tokens → Tokens (classic)** を選択する。

### 1-3. 新しい Token を生成する

**Generate new token → Generate new token (classic)** をクリックする。

### 1-4. Token の設定をする

| 項目 | 内容 |
|------|------|
| **Note** | Token の用途を書く（例：`my-laptop`） |
| **Expiration** | 有効期限を設定する（例：90 days）。`No expiration` は非推奨 |
| **Select scopes** | 最低限 `repo` にチェックを入れる |

**`repo` スコープで有効になる操作：**

| スコープ | 内容 |
|---------|------|
| `repo` | プライベート・パブリックリポジトリへの読み書き |
| `repo:status` | コミットステータスの読み書き |
| `public_repo` | パブリックリポジトリのみ操作したい場合はこちらだけでもOK |

### 1-5. Token を生成してコピーする

**Generate token** をクリックすると Token が表示される。

> **注意：** Token はこのページを離れると二度と表示されない。必ずこの場でコピーしてメモしておく。

```
ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

## Step 2：Token を使って Push する

### 2-1. リモートを HTTPS で登録する

```bash
git remote add origin https://github.com/USERNAME/example_repo.git
```

すでに登録済みの場合は確認だけ行う：

```bash
git remote -v
# origin  https://github.com/USERNAME/example_repo.git (fetch)
# origin  https://github.com/USERNAME/example_repo.git (push)
```

### 2-2. Push を実行する

```bash
git push -u origin main
```

認証を求められたら以下を入力する：

| 項目 | 入力する内容 |
|------|------------|
| **Username** | GitHub のユーザー名 |
| **Password** | Token をそのまま貼り付ける（パスワードではない） |

> **ポイント：** 「Password」と表示されるが、ここには GitHub のログインパスワードではなく
> 発行した Token を貼り付ける。

---

## Step 3：Token をキャッシュして毎回の入力を省略する

Push のたびに Token を入力するのは手間なので、資格情報をキャッシュしておく。

### 方法 1：一時キャッシュ（推奨・セキュリティ重視の場合）

```bash
git config --global credential.helper cache
```

デフォルトで 15 分間キャッシュされる。時間を延ばす場合（例：1 時間）：

```bash
git config --global credential.helper 'cache --timeout=3600'
```

### 方法 2：恒久的に保存（簡便だが Token がファイルに平文保存される）

```bash
git config --global credential.helper store
```

> **注意：** `store` を使うと Token が `~/.git-credentials` に平文で保存される。
> 共有サーバーや他人が触れる環境では使わないこと。

キャッシュ設定を確認する：

```bash
git config --global credential.helper
# cache  または  store
```

---

## Token の管理

### Token を再確認する

発行済み Token の一覧は以下から確認できる：

**GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)**

Token の文字列は再表示できないが、**Note**・**有効期限**・**最終使用日** は確認できる。

### Token を失効させる

上記ページで Token の **Delete** をクリックすると即座に無効化される。
Token が漏洩した疑いがある場合はすぐに削除する。

### Token の有効期限が切れた場合

`git push` 時に以下のようなエラーが出る：

```
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/...'
```

新しい Token を発行して、キャッシュをクリアしてから再度 Push する：

```bash
# キャッシュをクリアする（cache の場合）
git credential-cache exit

# 再度 Push すると認証を求められる
git push
```

---

## 全体の流れまとめ

```bash
# 1. GitHub で Token を発行する（ブラウザ操作）
#    Settings → Developer settings → Personal access tokens → Tokens (classic)
#    → Generate new token (classic) → repo にチェック → Generate token → コピー

# 2. リモートを HTTPS で登録する
git remote add origin https://github.com/USERNAME/example_repo.git

# 3. Push する（Username: GitHubユーザー名、Password: Token を入力）
git push -u origin main

# 4. Token をキャッシュする（任意）
git config --global credential.helper cache
```

---

## よく使うコマンド早見表

| コマンド | 用途 |
|---------|------|
| `git remote -v` | 登録済みリモートと URL を確認 |
| `git config --global credential.helper` | 現在のキャッシュ設定を確認 |
| `git credential-cache exit` | キャッシュをクリアする |
| `git push -u origin main` | 初回プッシュ（upstream を設定） |
| `git push` | 2 回目以降のプッシュ |

---

## 関連ドキュメント

- [GitHub Remote Repository の作成と Push](github_push_jp.md)
