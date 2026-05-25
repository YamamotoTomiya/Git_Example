# Git ワークフロー ステップバイステップガイド

リポジトリのクローンからマージ済みブランチの削除まで、Git の基本的な作業フローについて。

---

## 1. リモートリポジトリをクローンする

リモートリポジトリをローカルマシンにダウンロード。

```bash
git clone <REMOTE_URL>
cd <REPOSITORY_NAME>
```

例：

```bash
git clone git@github.com:<username>/my_project.git
cd my_project
```

---

## 2. ローカルの main ブランチを最新にする

作業を始める前に、ローカルの `main` をリモートの最新状態に同期。

```bash
git checkout main
git pull origin main
```

---

## 3. フィーチャーブランチを作成する

`main` を汚さないよう、変更用のブランチを新たに作成。

```bash
git checkout -b feature/add_xxx
```

ブランチ名の例：

```
feature/add_xxx       # 何かを追加するとき
feature/fix_bug       # バグを修正するとき
feature/update_docs   # ドキュメントを更新するとき
```

---

## 4. ファイルを編集する

必要なファイルを開いて変更。

```bash
vim main.py
```

VS Code でフォルダを開く場合：

```bash
code .
```

---

## 5. 変更内容を確認する

ステージに追加する前に、何が変わったかを確認。

```bash
# 変更されたファイルを確認する
git status

# 行レベルの差分を確認する
git diff
```

---

## 6. 変更をステージしてコミットする

変更ファイルをステージングエリアに追加し、コミット。

```bash
git add .
git commit -m "Add new feature"
```

例：

```bash
git commit -m "Delete example.py"
```

---

## 7. ブランチをリモートリポジトリにプッシュする

ローカルブランチを GitHub にアップロード。プッシュ後、GitHub がプルリクエストの URL を表示することがある。

```bash
git push origin feature/add_xxx
```

---

## 8. ブランチを main と比較する

`main` に切り替えて最新状態に更新してから、差分を確認。

```bash
git checkout main
git pull origin main
```

| コマンド | 説明 |
|---------|------|
| `git diff main..feature/add_xxx` | main とフィーチャーブランチの全差分を表示 |
| `git diff --name-only main..feature/add_xxx` | 変更されたファイル名のみ表示 |
| `git log --oneline main..feature/add_xxx` | フィーチャーブランチにあって main にないコミットを一覧表示 |
| `git log --oneline --graph main..feature/add_xxx` | 同上をグラフ付きで表示 |

---

## 9. ブランチを main にマージする

フィーチャーブランチをローカルの `main` にマージ。

```bash
git merge feature/add_xxx
```

コンフリクトがなければ、自動的にマージが完了。

---

## 10. 更新した main ブランチをプッシュする

マージ済みの `main` をリモートリポジトリにアップロード。

```bash
git push origin main
```

別のリモートを使用する場合：

```bash
git push server main
```

---

## 11. マージ済みブランチを削除する

マージが完了したら、ブランチをローカルとリモートの両方から削除。

ローカルブランチを削除する：

```bash
git branch -d feature/add_xxx
```

リモートブランチを削除する：

```bash
git push origin --delete feature/add_xxx
```

別のリモートの場合：

```bash
git push server --delete feature/add_xxx
```

---

## 12. 削除済みリモートブランチの追跡情報をローカルから削除する

リモートで削除されたブランチへのローカル参照を掃除。

```bash
git fetch origin --prune
```

---

## よく使うコマンド

### ブランチの確認

| コマンド | 説明 |
|---------|------|
| `git branch` | ローカルブランチを一覧表示 |
| `git branch -r` | リモート追跡ブランチを一覧表示 |
| `git branch -a` | 全ブランチを一覧表示（ローカル＋リモート追跡） |
| `git status` | 現在のブランチと作業ツリーの状態を表示 |

---

## 注意事項

- `.gitignore` は**未追跡ファイル**にのみ有効です。すでに Git に追跡されているファイルは、`.gitignore` に追加しても引き続きコミット対象になる。
- 追跡済みのファイルを追跡対象から外すには：

```bash
git rm --cached <FILE_NAME>
```

例：

```bash
git rm --cached path/to/file.txt
```

---

## 関連ドキュメント

- [Git コマンドリファレンス（英語）](git_workflow_en.md)
- [Git コマンドリファレンス（日本語）](git_workflow_jp.md)
