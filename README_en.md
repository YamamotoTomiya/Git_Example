# vaccine_example

A sample project for running SLURM jobs on the **vaccine** and **itc** clusters.

## Repository Structure

```
vaccine_example/
├── src/
│   ├── main.py                    # Simple test script
│   └── machin_like_formula.py     # Pi calculation using Machin-like formula
├── job_scripts/
│   ├── vaccine/                   # Job scripts for the vaccine server
│   │   ├── job_example.sh         # Runs src/main.py
│   │   ├── job_machin.sh          # Runs src/machin_like_formula.py
│   │   └── output/                # SLURM log output directory
│   └── itc25/                     # Job scripts for the itc server
│       └── output/                # SLURM log output directory
│           ├── job_example.sh     # Runs src/main.py
│           └── job_machine.sh     # Runs src/main.py
├── docs/
│   ├── jp/                                      # Japanese documents
│   │   ├── git_workflow_jp.md                   # Git command reference
│   │   ├── git_workflow_steps_jp.md             # Git workflow step-by-step
│   │   ├── github_push_jp.md                    # Create GitHub remote repo and push
│   │   ├── github_token_https_jp.md             # Personal Access Token for HTTPS
│   │   ├── server_bare_repo_create_jp.md        # Create a bare repository and push
│   │   ├── server_git_workflow_jp.md            # Clone from bare repository and push
│   │   ├── vscode_ssh_agent_jp.md               # SSH agent setup for VSCode GitHub integration
│   │   └── multi_remote_jp.md                   # Manage GitHub and bare repo as remotes (advanced)
│   └── en/                                      # English documents
│       ├── git_workflow_en.md                   # Git command reference
│       ├── git_workflow_steps_en.md             # Git workflow step-by-step
│       ├── github_push_en.md                    # Create GitHub remote repo and push
│       ├── github_token_https_en.md             # Personal Access Token for HTTPS
│       ├── server_bare_repo_create_en.md        # Create a bare repository and push
│       ├── server_git_workflow_en.md            # Clone from bare repository and push
│       ├── vscode_ssh_agent_en.md               # SSH agent setup for VSCode GitHub integration
│       └── multi_remote_en.md                   # Manage GitHub and bare repo as remotes (advanced)
└── student_6th/              # Student example script
```

## Usage

### vaccine server

```bash
cd job_scripts/vaccine
sbatch job_example.sh      # submit main.py job
sbatch job_machin.sh       # submit machin_like_formula.py job
```

#### SLURM options (`job_scripts/vaccine/job_example.sh`)

| Option | Value | Description |
|---|---|---|
| `-p` | `GPU-S` | Partition to use |
| `--gres` | `gpu:1` | Number of GPUs |
| `-n` | `1` | Number of tasks |
| `-t` | `72:00:00` | Maximum runtime |
| `-J` | `example` | Job name |
| `-o` | `output/%x-%j.out` | Log output path |

---

### itc server

```bash
cd job_scripts/itc25/output
sbatch job_example.sh      # submit main.py job
sbatch job_machine.sh      # submit main.py job
```

#### SLURM options (`job_scripts/itc25/output/job_example.sh`)

| Option | Value | Description |
|---|---|---|
| `-p` | `gpu_short` | Partition (queue) to use |
| `--gres` | `gpu:1` | Number of GPUs |
| `-N` | `1` | Number of nodes |
| `-n` | `8` | Number of tasks (processes) |
| `-c` | `1` | CPUs per task (`OMP_NUM_THREADS`) |
| `-t` | `4:00:00` | Maximum runtime |
| `--output` | `output/%x-%j.out` | Log output path |

---

## Checking Job Status

```bash
# List your running/pending jobs
squeue -u $USER

# Check the output log
cat output/example-<jobid>.out
```

## Documentation

| Title | English | Japanese |
|-------|---------|----------|
| Git command reference | [EN](docs/en/git_workflow_en.md) | [JP](docs/jp/git_workflow_jp.md) |
| Git workflow step-by-step | [EN](docs/en/git_workflow_steps_en.md) | [JP](docs/jp/git_workflow_steps_jp.md) |
| Create GitHub remote repo and push | [EN](docs/en/github_push_en.md) | [JP](docs/jp/github_push_jp.md) |
| Personal Access Token for HTTPS | [EN](docs/en/github_token_https_en.md) | [JP](docs/jp/github_token_https_jp.md) |
| Create a bare repository and push | [EN](docs/en/server_bare_repo_create_en.md) | [JP](docs/jp/server_bare_repo_create_jp.md) |
| Clone from bare repository and push | [EN](docs/en/server_git_workflow_en.md) | [JP](docs/jp/server_git_workflow_jp.md) |
| SSH agent setup for VSCode GitHub integration | [EN](docs/en/vscode_ssh_agent_en.md) | [JP](docs/jp/vscode_ssh_agent_jp.md) |
| Manage GitHub and bare repo as remotes (advanced) | [EN](docs/en/multi_remote_en.md) | [JP](docs/jp/multi_remote_jp.md) |
