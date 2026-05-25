# VSCode で GitHub 連携するための SSH エージェント設定

VSCode の Git 機能（push / pull / clone）を SSH で使う場合、
SSH エージェントに秘密鍵を登録しておく必要がある。
登録しておかないと、VSCode が SSH 鍵を見つけられず認証エラーになる。

---

## SSH エージェントとは

SSH エージェントは、秘密鍵をメモリに保持しておくプログラム。
一度登録すると、push のたびにパスフレーズを入力しなくて済む。
VSCode は OS のSSHエージェントを介して鍵を使うため、エージェントへの登録が必要になる。

```
VSCode の Git 操作
  → SSH エージェント（鍵を保持）
    → GitHub（認証）
```

---

## 事前確認

SSH 鍵がすでに作成されているか確認する：

```bash
ls ~/.ssh/
# id_ed25519     ← 秘密鍵
# id_ed25519.pub ← 公開鍵
```

鍵がない場合は先に作成する（[github_push_jp.md](github_push_jp.md) の Step 2 を参照）。

---

## Step 1：SSH エージェントを起動する

エージェントが動いているか確認する：

```bash
echo $SSH_AGENT_PID
# 数字が表示されれば起動済み
# 何も表示されなければ起動する
```

起動していない場合は起動する：

```bash
eval "$(ssh-agent -s)"
# Agent pid 12345  ← このように表示されれば起動OK
```

---

## Step 2：秘密鍵をエージェントに登録する

```bash
ssh-add ~/.ssh/id_ed25519
```

パスフレーズを設定している場合は入力を求められる。
設定していない場合はそのまま登録される。

登録されたか確認する：

```bash
ssh-add -l
# 256 SHA256:XXXX... your_email@example.com (ED25519)
```

鍵の情報が表示されれば登録済み。

---

## Step 3：GitHub との接続を確認する

```bash
ssh -T git@github.com
# Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

このメッセージが出れば VSCode からの push / pull も動作する。

---

## Step 4：VSCode で Git 操作を試す

VSCode のソースコントロールパネル（左サイドバーの分岐アイコン）から
push / pull を実行すると、パスフレーズなしで認証が通るようになる。

> **ポイント：** SSH エージェントへの登録はログアウトすると消える。
> サーバーに再ログインしたときや PC を再起動したときは Step 1〜2 を再度実行する必要がある。

---

## ログインのたびに自動登録する設定（任意）

毎回 `ssh-add` を実行するのが手間な場合は、シェルの設定ファイルに追加しておく。

```bash
vi ~/.bashrc
```

以下を末尾に追加する：

```bash
# SSH エージェントの自動起動と鍵の登録
if [ -z "$SSH_AGENT_PID" ]; then
    eval "$(ssh-agent -s)" > /dev/null
    ssh-add ~/.ssh/id_ed25519 2>/dev/null
fi
```

設定を反映する：

```bash
source ~/.bashrc
```

> **注意：** この設定はシェルを起動するたびにエージェントを起動しようとする。
> パスフレーズを設定している場合、ログインのたびに入力を求められる。

---

## 全体の流れまとめ

```bash
# エージェント起動
eval "$(ssh-agent -s)"

# 鍵を登録
ssh-add ~/.ssh/id_ed25519

# 接続確認
ssh -T git@github.com

# → VSCode の push / pull が動作するようになる
```

---

## よく使うコマンド早見表

| コマンド | 用途 |
|---------|------|
| `eval "$(ssh-agent -s)"` | SSH エージェントを起動する |
| `ssh-add ~/.ssh/id_ed25519` | 秘密鍵をエージェントに登録する |
| `ssh-add -l` | 登録済みの鍵を一覧表示する |
| `ssh-add -D` | 登録済みの鍵をすべて削除する |
| `ssh -T git@github.com` | GitHub との SSH 接続を確認する |

---

## 関連ドキュメント

- [GitHub Remote Repository の作成と Push](github_push_jp.md)
