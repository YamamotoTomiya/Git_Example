# Git 基本操作コマンド集

---

## Git の基本概念

### リポジトリ（repository）

ファイルの変更履歴をまるごと保存する場所。`.git/` フォルダがその正体。

| 種類 | 説明 |
|------|------|
| **ローカルリポジトリ** | 自分の PC 上にある。ここで作業する。 |
| **リモートリポジトリ** | GitHub などのサーバー上にある。チームで共有する。 |

```
[自分のPC]                        [GitHub]
ローカルリポジトリ  <-- pull --  リモートリポジトリ
                   -- push -->
```

---

### ブランチ（branch）

コミット履歴の「分岐」。main を汚さずに作業できる。

```
main:    A --- B --- C
                      \
feature:               D --- E   ← ここで作業
```

- `main` ブランチ：本番・安定版を置く
- `feature/xxx` ブランチ：新機能・修正の作業用に作る
- 作業が終わったら `main` にマージして `feature` ブランチは削除する

---

### ローカルブランチ vs リモートブランチ vs リモート追跡ブランチ

| 種類 | 場所 | 説明 |
|------|------|------|
| **ローカルブランチ** | 自分の PC | `git branch` で見えるもの。自分で自由に操作できる。 |
| **リモートブランチ** | GitHub 上 | `git push` で送ったもの。GitHub の画面で見える。 |
| **リモート追跡ブランチ** | 自分の PC | `origin/main` のような形式。「最後に通信したときのリモートの状態」のコピー。`git fetch` で更新される。 |

```
[自分のPC]
  main                 ← ローカルブランチ（自分が操作）
  origin/main          ← リモート追跡ブランチ（リモートのコピー、読み取り専用）

[GitHub]
  main                 ← リモートブランチ
```

---

### HEAD とは

「今自分がいるコミット」を指すポインタ。
通常は現在のブランチの先頭を指している。

```
main:  A --- B --- C ← HEAD（= mainの先頭にいる）
```

---

### ベアリポジトリ（bare repository）

作業ツリー（ファイルを直接編集できる場所）を持たないリポジトリ。
`.git/` フォルダの中身だけが存在する状態。

| 種類 | 作業ツリー | 用途 |
|------|-----------|------|
| **通常のリポジトリ** | あり | 自分の PC でファイルを編集・コミットする |
| **ベアリポジトリ** | なし | 共有サーバーや GitLab/GitHub のような中央リポジトリ |

```
通常のリポジトリ:            ベアリポジトリ:
  myproject/                   myproject.git/
  ├── .git/  ← Git データ      ├── HEAD
  ├── src/   ← 作業ツリー      ├── objects/
  └── README ← 作業ツリー      └── refs/      ← .git/ の中身だけ
```

ベアリポジトリは**直接ファイルを編集・コミットできない**。
`git push` の受け取り先として使うためのもの。

#### 作り方

```bash
# 新しくベアリポジトリを作る（慣例として末尾に .git をつける）
git init --bare myproject.git

# 既存のリポジトリをベアリポジトリとしてクローンする
git clone --bare https://github.com/user/myproject.git
```

> **いつ使うか？**
> - チームの共有サーバーや NAS に置く中央リポジトリを作るとき
> - GitLab / GitHub のようなサービスは内部的にベアリポジトリを使っている
> - 自分の PC だけで作業するなら通常のリポジトリで十分

---

## コマンドオプションの意味

よく使うオプションの読み方：

| オプション | 意味 |
|-----------|------|
| `-r` | `--remotes` の略。リモート追跡ブランチを対象にする。 |
| `-a` | `--all` の略。ローカル＋リモート追跡ブランチ全てを対象にする。 |
| `-b` | `--branch` の略（`git checkout` 用）。ブランチを新規作成して切り替える。 |
| `-c` | `--create` の略（`git switch` 用）。ブランチを新規作成して切り替える。 |
| `-d` | `--delete` の略。ブランチを削除する（マージ済みのみ）。 |
| `-v` | `--verbose` の略。詳細情報を表示する。 |
| `-m` | `--message` の略。コミットメッセージを指定する。 |
| `--oneline` | ログを1行で表示する。 |
| `--graph` | ブランチの分岐をアスキーアートで表示する。 |
| `--all` | 全ブランチを対象にする。 |
| `--no-ff` | fast-forward を禁止してマージコミットを必ず作る。 |
| `--hard` | ブランチのポインタ・ステージ・作業ツリーを全て指定コミットに戻す。 |
| `--stat` | 差分のファイル名と行数の増減だけ表示する（詳細は出さない）。 |
| `--prune` | リモートに存在しないブランチの追跡情報をローカルから削除する。 |
| `--detach` | HEAD をブランチに紐付けず、コミット単体に直接つける。 |

---

## 状態確認

```bash
# 変更状態を確認（どのファイルが変更・追加・削除されたか）
git status

# ブランチ一覧（ローカルのみ）
git branch

# ブランチ一覧（リモート追跡ブランチのみ）
#   -r = --remotes
git branch -r

# ブランチ一覧（ローカル＋リモート追跡ブランチ、全て）
#   -a = --all
git branch -a
```

---

## 履歴確認

```bash
# シンプルな履歴（1コミット1行）
git log --oneline

# グラフ付きで全ブランチの履歴を見る
#   --graph：分岐をアスキー図で表示
#   --all：全ブランチ対象
git log --oneline --graph --all

# 特定のコミットの内容（変更ファイルと差分）を見る
git show <commit_id>
```

---

## ブランチ操作

```bash
# 新しいブランチを作って切り替える（新しい書き方）
#   -c = --create
git switch -c feature/example

# 新しいブランチを作って切り替える（旧来の書き方、どちらでも同じ結果）
#   -b = --branch
git checkout -b feature/example

# ブランチを切り替える
git switch main
git switch feature/example

# リモートブランチを元にローカルブランチを作る
#   origin/main（リモート追跡ブランチ）に追従するローカルブランチを作成
git switch -c main origin/main

# ブランチを削除する（マージ済みのみ削除できる）
#   -d = --delete
git branch -d feature/example
```

---

## 差分確認

```bash
# main との差分（ファイル名と行数の概要だけ）
#   --stat：詳細な diff は出さず統計だけ表示
git diff --stat main feature/example

# main との差分（詳細）
git diff main feature/example

# feature ブランチにしかないコミットを見る
#   main..feature/example：main から見て feature にしかないコミット
git log --oneline main..feature/example
```

---

## コミット

```bash
# ステージに追加（コミット対象にする）
git add <ファイル名>

# コミット（-m でメッセージを指定）
git commit -m "commit message"

# リモートにプッシュする
git push origin <ブランチ名>
```

> **ステージ（index）とは？** `git add` したファイルを一時的に置く場所。
> `作業ツリー → git add → ステージ → git commit → ローカルリポジトリ → git push → リモートリポジトリ` の流れ。

---

## マージ

```bash
# PR のように merge commit を残してマージする
#   --no-ff：fast-forward を禁止してマージコミットを強制的に作る
git switch main
git pull origin main
git merge --no-ff feature/example -m "Merge branch 'feature/example'"
git push origin main
```

> **fast-forward とは？** main が feature の根元から進んでいない場合、
> Git はマージコミットを作らずポインタだけ移動できる（fast-forward）。
> `--no-ff` をつけると必ずマージコミットが作られ、履歴に「ここでマージした」が残る。

---

## リモート操作

```bash
# リモートの一覧と URL を見る
#   -v = --verbose（URL も表示する）
git remote -v

# リモートからローカルに変更を取得して追跡ブランチを更新（作業ツリーには反映しない）
#   origin を省略するとデフォルトのリモートが対象になる
git fetch
git fetch origin

# fetch 後にリモートとの差分を確認する
#   HEAD..origin/main：まだ自分のブランチに取り込んでいないコミットを表示
git log --oneline HEAD..origin/main

# fetch してからマージする（pull の手動版）
#   pull は fetch + merge を一度にやるが、fetch を先にすると差分を確認できる
git fetch origin
git merge origin/main

# リモートブランチを削除する
git push origin --delete feature/example

# リモートに存在しないブランチの追跡情報をローカルから削除する
#   --prune：origin 上にもうないブランチの origin/xxx をローカルから掃除する
git fetch --prune origin
```

> **`git fetch` と `git pull` の違い:**
> - `git fetch`：リモートの変更を取得して **追跡ブランチ（origin/main）だけ** 更新する。作業ツリーは変わらない。
> - `git pull`：`git fetch` + `git merge` を一度に行う。作業ツリーにも反映される。
> 差分を確認してから取り込みたいときは `fetch → log → merge` の順に行うと安全。

---

## 過去の状態を見る・戻す

```bash
# 過去の状態を一時的に見る（detached HEAD 状態）
#   --detach：HEAD をブランチでなくコミット直接に紐付ける
git switch --detach <commit_id>

# detached HEAD から元のブランチに戻る
git switch main

# ブランチを過去のコミットに戻す（変更が全て消える）
#   --hard：ポインタ・ステージ・作業ツリーを全て書き換える
git reset --hard <commit_id>
```

> **注意:** `git reset --hard` は**コミットしていない変更も含めて全て消える**。
> 取り消せないので慎重に使う。
