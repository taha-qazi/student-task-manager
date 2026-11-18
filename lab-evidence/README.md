# Lab Evidence

Screenshots and supporting text logs captured while building **Student Task Manager** for **CSC418 — DevOps for Cloud Computing (Lab Assignment 4)**.

## Evidence Checklist & Index

- [x] **Git log / commit graph** showing progressive history (`git log --graph --oneline --all`) — [`01_git_log_graph.png`](01_git_log_graph.png) | [`git-log-graph.txt`](git-log-graph.txt)
- [x] **Branch list on GitHub** showing all feature branches (`feature/add-task`, `feature/complete-task`, `feature/delete-task`, `feature/documentation`, `feature/tests-ci`) — [`02_github_branches.png`](02_github_branches.png)
- [x] **GitHub Issues list** (6 issues with clear descriptions and labels) — [`03_github_issues.png`](03_github_issues.png)
- [x] **Pull Request page** showing review comment, commits, CI checks, and `Closes #5` link — [`04_pr_review_and_link.png`](04_pr_review_and_link.png)
- [x] **Merged Pull Requests list** (5 merged PRs: #7–#11) — [`05_merged_pull_requests.png`](05_merged_pull_requests.png)
- [x] **Merge conflict BEFORE resolution** — `README.md` showing `<<<<<<< HEAD`, `=======`, `>>>>>>> update-status-review` markers — [`06_merge_conflict_before.png`](06_merge_conflict_before.png) | [`merge-conflict-before.txt`](merge-conflict-before.txt)
- [x] **Merge conflict AFTER resolution** — clean resolved line and merge commit (`addef56`) — [`07_merge_conflict_after.png`](07_merge_conflict_after.png) | [`merge-conflict-after.txt`](merge-conflict-after.txt) | [`merge-conflict.md`](merge-conflict.md)
- [x] **GitHub Actions — FAILED run (red)** from the first tests push (Run #1) — [`08_ci_failed_run.png`](08_ci_failed_run.png) | [`08b_ci_failed_job_logs.png`](08b_ci_failed_job_logs.png) | [`ci-runs.md`](ci-runs.md)
- [x] **GitHub Actions — PASSED run (green)** after the fix commit (Run #2) & workflow history showing failed + passed runs — [`09_ci_passed_run.png`](09_ci_passed_run.png) | [`09b_ci_actions_history.png`](09b_ci_actions_history.png)
- [x] **GitHub Release page for `v1.0.0`** — [`10_release_v1_0_0.png`](10_release_v1_0_0.png)
- [x] **Console app & unit test execution** (`python main.py` interactive run + `python -m unittest discover -s tests -v`) — [`11_app_and_tests_demo.png`](11_app_and_tests_demo.png)
