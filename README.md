# Git & GitHub 入門リポジトリ

Git および GitHub の使い方を学ぶためのオープンなリポジトリです。
日本語・英語のドキュメントを収録しており、初めて Git を使う方から、GitHub との連携や応用的な運用を学びたい方まで活用できます。

> English version: [README_en.md](README_en.md)

## リポジトリ構成

```
Git_Example/
├── docs/
│   ├── jp/                                         # 日本語ドキュメント
│   │   ├── 01_server_git_workflow_jp.md            # ① ベアリポジトリからのクローンと push
│   │   ├── 02_server_bare_repo_create_jp.md        # ② ベアリポジトリを自分で作って push
│   │   ├── 03_github_push_jp.md                    # ③ GitHub リモートリポジトリ作成と push
│   │   ├── 04_multi_remote_jp.md                   # ④ GitHub とベアリポジトリを両方 remote で管理（応用）
│   │   ├── git_workflow_jp.md                      # Git コマンドリファレンス
│   │   ├── git_workflow_steps_jp.md                # Git ワークフロー ステップバイステップ
│   │   ├── github_token_https_jp.md                # HTTPS 用 Personal Access Token の登録
│   │   └── vscode_ssh_agent_jp.md                  # VSCode GitHub 連携用 SSH エージェント設定
│   └── en/                                         # English documents
│       ├── 01_server_git_workflow_en.md            # ① Clone from bare repository and push
│       ├── 02_server_bare_repo_create_en.md        # ② Create a bare repository and push
│       ├── 03_github_push_en.md                    # ③ Create GitHub remote repo and push
│       ├── 04_multi_remote_en.md                   # ④ Manage GitHub and bare repo as remotes (advanced)
│       ├── git_workflow_en.md                      # Git command reference
│       ├── git_workflow_steps_en.md                # Git workflow step-by-step
│       ├── github_token_https_en.md                # Personal Access Token for HTTPS
│       └── vscode_ssh_agent_en.md                  # SSH agent setup for VSCode GitHub integration
├── README.md
└── README_en.md
```

## ドキュメント一覧

### サーバー運用ワークフロー（推奨読む順）

| # | タイトル | 日本語 | English |
|---|---------|--------|---------|
| 1 | ベアリポジトリからのクローンと push | [JP](docs/jp/01_server_git_workflow_jp.md) | [EN](docs/en/01_server_git_workflow_en.md) |
| 2 | ベアリポジトリを自分で作って push | [JP](docs/jp/02_server_bare_repo_create_jp.md) | [EN](docs/en/02_server_bare_repo_create_en.md) |
| 3 | GitHub リモートリポジトリ作成と push | [JP](docs/jp/03_github_push_jp.md) | [EN](docs/en/03_github_push_en.md) |
| 4 | GitHub とベアリポジトリを両方 remote で管理（応用） | [JP](docs/jp/04_multi_remote_jp.md) | [EN](docs/en/04_multi_remote_en.md) |

### リファレンス・補足

| タイトル | 日本語 | English |
|---------|--------|---------|
| Git コマンドリファレンス | [JP](docs/jp/git_workflow_jp.md) | [EN](docs/en/git_workflow_en.md) |
| Git ワークフロー ステップバイステップ | [JP](docs/jp/git_workflow_steps_jp.md) | [EN](docs/en/git_workflow_steps_en.md) |
| HTTPS 用 Personal Access Token の登録 | [JP](docs/jp/github_token_https_jp.md) | [EN](docs/en/github_token_https_en.md) |
| VSCode GitHub 連携用 SSH エージェント設定 | [JP](docs/jp/vscode_ssh_agent_jp.md) | [EN](docs/en/vscode_ssh_agent_en.md) |
