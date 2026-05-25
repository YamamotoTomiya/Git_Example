# サーバー上のベアリポジトリを使った Git ワークフロー

vaccine サーバー（vaccine-00）でのクローンからブランチ作成・プッシュまでの手順。

---

## リポジトリの種類を理解する

作業を始める前に、3 種類のリポジトリの違いを把握しておく。

| 種類 | 場所 | 説明 |
|------|------|------|
| **ローカルリポジトリ** | 自分のホームディレクトリ | ファイルを実際に編集・コミットする場所 |
| **リモートリポジトリ** | GitHub などのサーバー | チームで共有する中央リポジトリ（例：GitHub） |
| **ベアリポジトリ** | サーバー上の共有領域 | 作業ツリーを持たない、プッシュの受け取り専用リポジトリ |

```
[自分のホームディレクトリ]              [vaccine サーバー上の共有領域]
ローカルリポジトリ  <-- clone/pull --  ベアリポジトリ (/home/repository/)
                   ---- push ------>
```

**ベアリポジトリの特徴：**
- `.git/` の中身だけが存在し、ファイルを直接編集できない
- 慣例でフォルダ名の末尾に `.git` をつける（例：`vaccine_example.git`）
- GitHub / GitLab も内部的にはベアリポジトリを使っている

---

## 事前確認

### Git バージョンの確認

```bash
git --version
# 例：git version 2.45.2
```

### 作業場所の確認

```bash
# 自分のホームディレクトリにいることを確認
cd ~
pwd
# 出力例：/home/yamamoto
```

---

## Step 1：ベアリポジトリからクローンする

### 1-1. 作業用ディレクトリを作成する

```bash
cd ~
mkdir example    # 任意の名前でOK
cd example
```

プロンプトが `<username>@vaccine-00:~/example$` になっていればOK。

### 1-2. ベアリポジトリの場所を確認する

vaccine サーバーでは `/home/repository/` 以下にベアリポジトリが置いてある。

```bash
ls /home/repository/tyamamoto/server/
# 出力例：vaccine_example.git
```

### 1-3. クローンする

```bash
git clone /home/repository/tyamamoto/server/vaccine_example.git
```

> **ポイント：** GitHub の場合は `https://...` や `git@github.com:...` を指定するが、
> サーバー上のベアリポジトリはローカルパスを直接指定できる。

### 1-4. クローンできたか確認する

```bash
ls
# vaccine_example が表示されればOK

cd vaccine_example
ls -a
# .  ..  .git  .gitignore  README.md  docs  job_scripts  src  ...
```

`.git/` ディレクトリがあれば Git 管理下にある。

---

## Step 2：ブランチを作ってプッシュする

### 2-1. 現在のブランチを確認する

```bash
git branch
# * main  ← * がついているのが現在いるブランチ
```

### 2-2. 新しいブランチを作成して切り替える

```bash
git checkout -b feature/add_<username>
# 例：git checkout -b feature/add_yamamoto
```

**ブランチ名の慣例：**

ブランチ名は `/`（スラッシュ）で **カテゴリ/内容** の形に区切るのが一般的。
スラッシュはディレクトリ区切りではなく、名前の一部として扱われる。

```
feature/add_yamamoto      # 新しいファイル・機能を追加するとき
feature/fix_typo          # タイポや軽微なミスを修正するとき
feature/update_readme     # ドキュメントや既存ファイルを更新するとき
bugfix/issue_42           # バグ修正（bugfix/ プレフィックスを使う流儀もある）
```

| プレフィックス | 使いどき |
|--------------|---------|
| `feature/`   | 新機能・ファイル追加など通常の作業 |
| `bugfix/`    | バグ修正 |
| `hotfix/`    | 本番環境の緊急修正 |
| `docs/`      | ドキュメントのみの変更 |

> **スラッシュを入れる理由：** 名前が長くなるプロジェクトでは `git branch -a` の出力がカテゴリごとにグループ表示されて読みやすくなる。強制ではないが、チームで揃えると管理しやすい。

現在いるブランチを確認：

```bash
git branch
#   main
# * feature/add_yamamoto   ← * が移動していればOK
```

### 2-3. 自分のフォルダとファイルを作成する

```bash
cd student_6th
mkdir <username>          # 例：mkdir yamamoto
cd <username>
touch ex.py               # 空ファイルを作成
```

ファイルに内容を書く方法は複数ある：

**方法 1：echo で1行書き込む（簡単）**

```bash
echo "print('hello')" > ex.py        # 上書き（ファイルを新規作成または置き換える）
echo "print('world')" >> ex.py       # 追記（既存の内容の後ろに足す）
```

> `>` は上書き、`>>` は追記。間違えるとファイルの中身が消えるので注意。

**方法 2：vi で編集する**

```bash
vi ex.py
```

vi の基本操作：

| キー | 操作 |
|------|------|
| `i` | 入力モードに切り替える |
| `Esc` | コマンドモードに戻る |
| `:wq` | 保存して終了 |
| `:q!` | 保存せずに終了 |

### 2-4. 変更状態を確認する

```bash
git status
# 新しく作ったファイルが "Untracked files" に表示されるはず
```

### 2-5. ステージしてコミットする

```bash
git add .
git commit -m "Add ex.py for yamamoto"
```

コミットメッセージの例：

```bash
git commit -m "Add yamamoto directory and example script"
```

### 2-6. ブランチをプッシュする

```bash
git push origin feature/add_<username>
# 例：git push origin feature/add_yamamoto
```

プッシュ後、ベアリポジトリにブランチが反映される。`git branch -v` でローカルブランチと最新コミットを一覧確認できる：

```bash
git branch -v
#   main                    a1b2c3d Merge pull request #8 from YamamotoTomiya/feature/add_hayashi
# * feature/add_yamamoto    f4e5d6c Add yamamoto directory and example script
```

| 列 | 説明 |
|----|------|
| `*` | 現在いるブランチ |
| ブランチ名 | ローカルに存在するブランチ |
| コミット ID | そのブランチの最新コミットの短縮ハッシュ |
| コミットメッセージ | 最新コミットの1行目 |

リモートのブランチも含めて見たい場合：

```bash
git branch -av
# * feature/add_yamamoto              f4e5d6c Add yamamoto directory and example script
#   main                              a1b2c3d Merge pull request #8 ...
#   remotes/origin/main               a1b2c3d Merge pull request #8 ...
#   remotes/origin/feature/add_yamamoto f4e5d6c Add yamamoto directory and example script
```

---

## 全体の流れまとめ

```bash
# 1. クローン
cd ~/example
git clone /home/repository/tyamamoto/server/vaccine_example.git
cd vaccine_example

# 2. ブランチ作成
git checkout -b feature/add_<username>

# 3. ファイル作成
cd student_6th
mkdir <username>
cd <username>
touch ex.py

# 4. コミット
git add .
git commit -m "Add <username> directory"

# 5. プッシュ
git push origin feature/add_<username>
```

---

## よく使うコマンド早見表

| コマンド | 説明 |
|---------|------|
| `git branch` | 現在のブランチ一覧（* が現在地） |
| `git status` | 変更ファイルの確認 |
| `git log --oneline` | コミット履歴を1行で確認 |
| `git diff` | 変更内容の詳細確認 |
| `git push origin <branch>` | 指定ブランチをリモートにプッシュ |

---

## クローンしたリポジトリを削除したいとき

### 削除前に必ず確認すること

クローンしたディレクトリを削除するのは単なるフォルダ削除だが、**プッシュしていない変更は元に戻せない**。削除前に以下を確認する。

**1. コミットされていない変更がないか確認する**

```bash
git status
# "nothing to commit, working tree clean" ならOK
# 変更が残っている場合はコミットするか破棄してから削除する
```

**2. プッシュしていないコミットがないか確認する**

```bash
git log origin/main..HEAD --oneline
# 何も表示されなければOK（ローカルにしかないコミットがない）

# ブランチを切っている場合は自分のブランチも確認
git log origin/feature/add_<username>..HEAD --oneline
```

> プッシュ済みのコミットはベアリポジトリ側に残るので、削除しても失われない。
> ローカルにしかないコミットはディレクトリごと消えるので注意。

---

### 削除する

確認が済んだら、ローカルのクローンディレクトリを削除する。

```bash
# クローンしたディレクトリの1つ上に移動してから削除する
cd ~/example
rm -rf vaccine_example
```

削除されたか確認：

```bash
ls
# vaccine_example が消えていればOK
```

> **`rm -rf` の注意点：**
> - `-r`（recursive）でディレクトリごと、`-f`（force）で確認なしに削除する
> - 削除したファイルはゴミ箱に入らず**即座に消える**。取り消しはできない
> - 絶対に `/` や `~` など広いパスに対して実行しないこと

---

### ベアリポジトリ・リモートリポジトリへの影響

| 削除した対象 | ベアリポジトリへの影響 |
|------------|----------------------|
| ローカルのクローン（`~/example/vaccine_example`） | **影響なし**。ベアリポジトリはサーバー上にそのまま残る |
| ベアリポジトリ自体（`/home/repository/...`） | 全員が影響を受ける。**触らない** |

クローンし直したいときはいつでも `git clone` で再取得できる。

```bash
git clone /home/repository/tyamamoto/server/vaccine_example.git
```

---

## 関連ドキュメント

- [Git 基本操作コマンド集](git_workflow_jp.md)
- [Git ワークフロー ステップバイステップ](git_workflow_steps_jp.md)
