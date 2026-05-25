# vaccine_example

**vaccine** サーバーおよび **itc** サーバーで SLURM ジョブを実行するためのサンプルプロジェクトです。

## リポジトリ構成

```
vaccine_example/
├── src/
│   ├── main.py                    # シンプルなテストスクリプト
│   └── machin_like_formula.py     # Machin-like formula による円周率計算
├── job_scripts/
│   ├── vaccine/                   # vaccine サーバー用ジョブスクリプト
│   │   ├── job_example.sh         # src/main.py を実行
│   │   ├── job_machin.sh          # src/machin_like_formula.py を実行
│   │   └── output/                # SLURM ログ出力ディレクトリ
│   └── itc25/                     # itc サーバー用ジョブスクリプト
│       └── output/                # SLURM ログ出力ディレクトリ
│           ├── job_example.sh     # src/main.py を実行
│           └── job_machine.sh     # src/main.py を実行
├── docs/
│   ├── jp/                                      # 日本語ドキュメント
│   │   ├── git_workflow_jp.md                   # Git コマンドリファレンス
│   │   ├── git_workflow_steps_jp.md             # Git ワークフロー ステップバイステップ
│   │   ├── github_push_jp.md                    # GitHub リモートリポジトリ作成と push
│   │   ├── github_token_https_jp.md             # HTTPS 用 Personal Access Token の登録
│   │   ├── server_bare_repo_create_jp.md        # ベアリポジトリを自分で作って push
│   │   ├── server_git_workflow_jp.md            # ベアリポジトリからのクローンと push
│   │   ├── vscode_ssh_agent_jp.md               # VSCode GitHub 連携用 SSH エージェント設定
│   │   └── multi_remote_jp.md                   # GitHub とベアリポジトリを両方 remote で管理（応用）
│   └── en/                                      # English documents
│       ├── git_workflow_en.md                   # Git command reference
│       ├── git_workflow_steps_en.md             # Git workflow step-by-step
│       ├── github_push_en.md                    # Create GitHub remote repo and push
│       ├── github_token_https_en.md             # Personal Access Token for HTTPS
│       ├── server_bare_repo_create_en.md        # Create a bare repository and push
│       ├── server_git_workflow_en.md            # Clone from bare repository and push
│       ├── vscode_ssh_agent_en.md               # SSH agent setup for VSCode GitHub integration
│       └── multi_remote_en.md                   # Manage GitHub and bare repo as remotes (advanced)
└── student_6th/              # 学生向けサンプルスクリプト
```

## 使い方

### vaccine サーバー

```bash
cd job_scripts/vaccine
sbatch job_example.sh      # main.py のジョブを投入
sbatch job_machin.sh       # machin_like_formula.py のジョブを投入
```

#### SLURM オプション（`job_scripts/vaccine/job_example.sh`）

| オプション | 値 | 説明 |
|---|---|---|
| `-p` | `GPU-S` | 使用するパーティション |
| `--gres` | `gpu:1` | GPU 数 |
| `-n` | `1` | タスク数 |
| `-t` | `72:00:00` | 最大実行時間 |
| `-J` | `example` | ジョブ名 |
| `-o` | `output/%x-%j.out` | ログ出力パス |

---

### itc サーバー

```bash
cd job_scripts/itc25/output
sbatch job_example.sh      # main.py のジョブを投入
sbatch job_machine.sh      # main.py のジョブを投入
```

#### SLURM オプション（`job_scripts/itc25/output/job_example.sh`）

| オプション | 値 | 説明 |
|---|---|---|
| `-p` | `gpu_short` | 使用するパーティション（キュー） |
| `--gres` | `gpu:1` | GPU 数 |
| `-N` | `1` | ノード数 |
| `-n` | `8` | タスク数（プロセス数） |
| `-c` | `1` | タスクあたりの CPU 数（`OMP_NUM_THREADS`） |
| `-t` | `4:00:00` | 最大実行時間 |
| `--output` | `output/%x-%j.out` | ログ出力パス |

---

## ジョブ状態の確認

```bash
# 自分のジョブ一覧を表示
squeue -u $USER

# ログを確認
cat output/example-<jobid>.out
```

## ドキュメント

| タイトル | 日本語 | English |
|---------|--------|---------|
| Git コマンドリファレンス | [JP](docs/jp/git_workflow_jp.md) | [EN](docs/en/git_workflow_en.md) |
| Git ワークフロー ステップバイステップ | [JP](docs/jp/git_workflow_steps_jp.md) | [EN](docs/en/git_workflow_steps_en.md) |
| GitHub リモートリポジトリ作成と push | [JP](docs/jp/github_push_jp.md) | [EN](docs/en/github_push_en.md) |
| HTTPS 用 Personal Access Token の登録 | [JP](docs/jp/github_token_https_jp.md) | [EN](docs/en/github_token_https_en.md) |
| ベアリポジトリを自分で作って push | [JP](docs/jp/server_bare_repo_create_jp.md) | [EN](docs/en/server_bare_repo_create_en.md) |
| ベアリポジトリからのクローンと push | [JP](docs/jp/server_git_workflow_jp.md) | [EN](docs/en/server_git_workflow_en.md) |
| VSCode GitHub 連携用 SSH エージェント設定 | [JP](docs/jp/vscode_ssh_agent_jp.md) | [EN](docs/en/vscode_ssh_agent_en.md) |
| GitHub とベアリポジトリを両方 remote で管理（応用） | [JP](docs/jp/multi_remote_jp.md) | [EN](docs/en/multi_remote_en.md) |
