# Student Task Manager

A Python console-based Student Task Manager, built for **CSC418 — DevOps for Cloud Computing** (BSE 7th Semester, Batch FA23, COMSATS University Islamabad, Lahore Campus).

The app lets a student add, display, complete and delete study tasks from the terminal. The project was built incrementally to demonstrate a realistic Git & GitHub workflow: progressive commits, feature branches, Issues, Pull Requests, a deliberately created and resolved merge conflict, CI with GitHub Actions, and a tagged release.

## Features

- **Add tasks** — with input validation: empty or whitespace-only titles are rejected
- **Display tasks** — a clear list showing each task's ID and completion status (`[x]` / `[ ]`)
- **Complete tasks** — mark a selected task as completed by its ID, with checks for invalid IDs
- **Delete tasks** — delete a task by a valid ID, with checks for invalid IDs
- **Unit tests** — automated tests for add, complete and delete, run locally and in CI
- **CI** — every push and Pull Request to `main` is tested by GitHub Actions

## Tech

- Python 3 (standard library only — no external dependencies)
- Git & GitHub for version control
- GitHub Actions for CI
- `unittest` for testing

## Setup

```bash
git clone https://github.com/taha-qazi/student-task-manager.git
cd student-task-manager
python3 --version   # Python 3.10 or newer recommended
```

No packages need to be installed — the app uses only the Python standard library.

## Usage

```bash
python main.py
```

Then choose from the menu:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

See [docs/user-guide.md](docs/user-guide.md) for a worked example session.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

## Project structure

```
student-task-manager/
├── main.py                    # Console interface (menu)
├── task_manager.py            # Core logic (Task + TaskManager)
├── tests/
│   └── test_task_manager.py   # Unit tests (add, complete, delete)
├── docs/
│   └── user-guide.md          # Step-by-step user guide
├── .github/workflows/
│   └── python-ci.yml          # GitHub Actions CI workflow
├── lab-evidence/              # Screenshots and evidence of the workflow
├── LAB-REPORT.md              # Assignment report (concept answers)
├── LICENSE                    # MIT
└── README.md
```

## Version control workflow used

`main` holds the released code. Each feature was developed on its own branch
(`feature/add-task`, `feature/complete-task`, `feature/delete-task`), reviewed
in a Pull Request linked to a GitHub Issue, and merged. A merge conflict on the
project status line was created and resolved deliberately, and CI runs on every
push and Pull Request to `main`. Version `v1.0.0` is published as a GitHub Release.

## License

MIT — see [LICENSE](LICENSE).
