# ベアリポジトリを自分で作って push する

ローカルでコードを作り、サーバー上にベアリポジトリを自分で用意して push するまでの手順。

---

## 全体の流れ

```
[自分のホームディレクトリ]                    [サーバー共有領域]
~/example/          -- git remote add -->  /path/to/repository/<username>/example.git
  ex.py             -- git push ------->   （ベアリポジトリ）
```

1. ローカルにコードを作る
2. ローカルで Git を初期化する
3. サーバー上にベアリポジトリを作る
4. ローカルにリモートとして登録する
5. コミットして push する

---

## Step 1：ローカルにコードを作る

```bash
cd ~
mkdir example
cd example
```

プロンプトが `<username>@<server>:~/example$` になっていればOK。

ファイルを作成する：

```bash
touch ex.py
```

ファイルに内容を書く方法は複数ある。

**方法 1：echo で書き込む**

```bash
echo "print('hello')" > ex.py        # 上書き（新規作成）
echo "print('world')" >> ex.py       # 追記
```

> `>` は上書き、`>>` は追記。`>` を使うと既存の中身が消えるので注意。

**方法 2：vi で編集する**

```bash
vi ex.py
```

| キー | 操作 |
|------|------|
| `i` | 入力モードに切り替える |
| `Esc` | コマンドモードに戻る |
| `:wq` | 保存して終了 |
| `:q!` | 保存せずに終了 |

ファイルの中身を確認：

```bash
cat ex.py
# print('hello')
# print('world')
```

---

## Step 2：ローカルリポジトリを初期化する

`~/example` を Git で管理できるようにする。

```bash
cd ~/example
git init
# Initialized empty Git repository in /home/<username>/example/.git/
```

`.git/` ディレクトリが作られ、Git 管理下になった。

ディレクトリの中身を確認する：

```bash
ls -a
# .  ..  .git  ex.py
```

`.git/` が表示されれば Git 管理下になっている。`-a` オプションをつけないと `.git/` は表示されない。

ブランチ名を確認する：

```bash
git branch
# * master   ← master になっている場合は main に変更する
# または
# * main     ← すでに main なら変更不要
```

`master` になっていた場合は `main` に変更する：

```bash
git branch -m master main
git branch
# * main
```

> **なぜ `main` にするか：** 近年は `master` から `main` に移行するプロジェクトが増えており、GitHub などのサービスもデフォルトを `main` に変更している。チームで名前を統一しておくと、後で push する際にブランチ名のズレでエラーが起きにくい。

現在の状態を確認：

```bash
git status
# On branch main
# Untracked files:
#   ex.py
```

---

## Step 3：サーバー上にベアリポジトリを作る

**ベアリポジトリの場所は `/path/to/repository/<username>/` 以下に作る。**

```bash
cd /path/to/repository
mkdir <username>          # 例：mkdir yamamoto
cd <username>
```

プロンプトが `<username>@<server>:/path/to/repository/<username>$` になっていればOK。

ベアリポジトリを作成する：

```bash
git init --bare /path/to/repository/<username>/example.git
# Initialized empty Git repository in /path/to/repository/<username>/example.git/
```

> **命名の慣例：** push したいローカルフォルダ名に `.git` をつけた名前にする。
> 今回はローカルが `example` フォルダなので `example.git` とする。

作成されたか確認：

```bash
ls /path/to/repository/<username>/
# example.git

ls /path/to/repository/<username>/example.git/
# HEAD  branches/  config  description  hooks/  info/  objects/  refs/
```

`.git/` の中身だけが存在していればベアリポジトリとして正しく作成されている。

ベアリポジトリが `main` を参照しているか確認する：

```bash
cat /path/to/repository/<username>/example.git/HEAD
# ref: refs/heads/main   ← main になっていればOK
```

`master` になっていた場合は `main` に変更する：

```bash
git --git-dir=/path/to/repository/<username>/example.git symbolic-ref HEAD refs/heads/main
cat /path/to/repository/<username>/example.git/HEAD
# ref: refs/heads/main
```

> ベアリポジトリの `HEAD` はデフォルトブランチを指している。ローカルと名前が一致していないと push 時にブランチ名の不一致エラーが起きるため、ここで揃えておく。

---

## Step 4：ローカルにリモートとして登録する

ローカルの `~/example` に戻る：

```bash
cd ~/example
```

ベアリポジトリをリモートとして追加する：

```bash
git remote add origin /path/to/repository/<username>/example.git
# 例：git remote add origin /path/to/repository/yamamoto/example.git
```

> `origin` はリモートにつける名前（エイリアス）。慣例で `origin` が使われる。別の名前でも動くが、チームでは `origin` に統一するとわかりやすい。

登録されたか確認：

```bash
git remote -v
# origin  /path/to/repository/yamamoto/example.git (fetch)
# origin  /path/to/repository/yamamoto/example.git (push)
```

`fetch`（取得）と `push`（送信）の両方に同じ URL が表示されればOK。

---

## Step 5：コミットして push する

### 5-1. ファイルをステージする

```bash
git add .
```

ステージされたか確認：

```bash
git status
# Changes to be committed:
#   new file: ex.py
```

### 5-2. コミットする

```bash
git commit -m "Add ex.py"
```

コミットされたか確認：

```bash
git log --oneline
# a1b2c3d Add ex.py
```

### 5-3. push する

```bash
git push origin main
# または
git push origin master
# （git init 時のデフォルトブランチ名に合わせる）
```

初回 push 時は `-u` オプションをつけると、次回以降 `git push` だけで済む：

```bash
git push -u origin main
```

> `-u` は `--set-upstream` の略。ローカルの `main` ブランチが `origin/main` を追跡するよう設定する。

push 後の確認：

```bash
git branch -av
# * main                a1b2c3d Add ex.py
#   remotes/origin/main a1b2c3d Add ex.py
```

`remotes/origin/main` が表示されれば、ベアリポジトリに正しく push されている。

---

## 全体の流れまとめ

```bash
# --- ローカルでコードを作る ---
cd ~
mkdir example
cd example
touch ex.py
echo "print('hello')" > ex.py

# --- Git を初期化する ---
git init

# --- ベアリポジトリを作る ---
mkdir /path/to/repository/<username>
git init --bare /path/to/repository/<username>/example.git

# --- リモートとして登録する ---
cd ~/example
git remote add origin /path/to/repository/<username>/example.git

# --- コミットして push する ---
git add .
git commit -m "Add ex.py"
git push -u origin main
```

---

## よく起きるエラーと対処

**`error: src refspec main does not match any`**

```bash
# git init 直後はコミットが1つもないためブランチが存在しない
# → 先に git commit してからpushする
git add .
git commit -m "first commit"
git push origin main
```

**`error: failed to push some refs`**

```bash
# リモートとローカルの状態がずれている場合
# → git pull してからpushする
git pull origin main
git push origin main
```

**push 先のブランチ名が `master` か `main` かわからない**

```bash
# ローカルのブランチ名を確認する
git branch
# * master  ← この名前をpushに使う

git push origin master
```

---

## 関連ドキュメント

- [ベアリポジトリからのクローンと push](server_git_workflow_jp.md)
- [Git 基本操作コマンド集](git_workflow_jp.md)
- [Git ワークフロー ステップバイステップ](git_workflow_steps_jp.md)
