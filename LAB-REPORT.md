# Lab Report — Student Task Manager Development and Version Control Using Git and GitHub

**Course:** CSC418 — DevOps for Cloud Computing (BSE 7th Semester, Batch FA23)
**Instructor:** Dr. M. Hasanain Ch
**Student:** Taha Bin Yousuf
**Repository:** https://github.com/taha-qazi/student-task-manager

---

## Q1. What is the difference between Git and GitHub? Explain `add`, `commit` and `push`.

Git and GitHub are not the same thing. **Git** is a distributed version control system that runs on my own machine. It records the history of my project as a series of snapshots called commits, lets me create branches, and lets me undo or compare changes — all of this works completely offline. **GitHub** is a hosting service on the internet where a Git repository can be stored and shared. On top of storage it adds collaboration tools that Git itself does not have: Issues, Pull Requests, code review, GitHub Actions for CI, and Releases. So Git is the tool that tracks my code, and GitHub is the place where that tracked code lives so a team (and my instructor) can see and work on it.

The three commands form a pipeline. `git add` moves changes from my working folder into the **staging area** — it is me choosing exactly which changes belong in the next snapshot. `git commit` takes everything staged and permanently records it in the local repository's history, with a message explaining the change. At this point the work exists only on my machine. `git push` uploads my local commits to GitHub, so the remote repository catches up with my local one. In short: add selects, commit records, push publishes.

## Q2. How do branches, Pull Requests and merge conflicts work?

A **branch** is an independent line of development that points at a commit. When I created `feature/add-task` I could experiment and commit freely without touching the stable code on `main`; if the feature had failed, `main` would never have been affected. This is why branches are useful: several features (or several people) can progress in parallel without overwriting each other.

A **Pull Request (PR)** is how work on a branch is proposed for merging into another branch, usually `main`. On GitHub a PR shows exactly which files changed, allows reviewers to comment on specific lines, runs automated checks, and records the discussion before anything is merged. In this project every PR was linked to an Issue (for example with `Closes #1`), so merging the PR automatically closed the Issue it implemented.

A **merge conflict** happens when two branches change the *same lines* of the *same file* in different ways and Git cannot decide which version is correct. Git stops the merge and marks the disputed area with `<<<<<<<`, `=======` and `>>>>>>>` markers. A human must edit the file to the correct combined result, delete the markers, then `add` and `commit` to complete the merge. Conflicts are not errors — they are Git asking for a decision it should not make alone.

## Q3. `fetch` vs `pull`, and `merge` vs `rebase`.

`git fetch` downloads new commits and branches from the remote into my local repository, but it **does not change my working files or my current branch**. It is a safe way to inspect what others have pushed before deciding what to do. `git pull` is fetch *plus* merge: it downloads the remote changes and immediately merges them into my current branch, updating my working files. So fetch is "show me what's new", pull is "bring me up to date now".

`merge` and `rebase` are two ways to combine branches. **Merge** joins two branches with a merge commit that has two parents; the history shows exactly what happened, including when branches diverged and came back together, but the graph can look busy. **Rebase** replays my branch's commits one by one on top of the target branch, producing a clean, straight-line history — as if I had started from the latest code all along. The trade-off is that rebase rewrites commit history, so it should not be used on commits that have already been pushed and shared with others. I used merge in this project because the Pull Request workflow is built around it and because keeping the true history was better evidence of the workflow.

## Q4. How do GitHub Issues and GitHub Actions help a team?

**Issues** are the team's shared to-do list and discussion space. A feature request, a bug, or a documentation task becomes an Issue with a description, labels (such as `enhancement`, `bug` or `documentation`) and an assignee, so everyone can see what needs doing, what is in progress, and why decisions were taken. Because Pull Requests can reference and close Issues, the work and the code that implements it stay connected — months later you can trace a change back to the discussion that requested it.

**GitHub Actions** is the team's automated checker. A workflow file in `.github/workflows/` defines jobs that run on GitHub's servers whenever something happens — in this project, on every push and every Pull Request to `main`, Actions installs Python and runs the unit tests. This helps a team because no one has to remember to run the tests or trust that "it works on my machine": a red (failed) run blocks careless merges and catches a bug within minutes of it being pushed, and a green (passed) run is shared proof that the code passes the same checks for everyone.

## Q5. One difficulty I faced, and how I solved it

The difficulty I remember most clearly was the deliberate merge conflict on the "Project status" line of the README — and it taught me why the accidental ones used to feel so confusing. When I merged the second status branch into `main`, Git stopped and left `<<<<<<< HEAD`, `=======` and `>>>>>>>` markers inside README.md, and at first the file looked broken. What solved it was slowing down and reading the markers literally: the section between `<<<<<<< HEAD` and `=======` was the version already on `main`, and the section between `=======` and `>>>>>>>` was the incoming branch's version. Once I understood that a conflict is just both versions written into one file, the fix was simple: edit that line to the final wording I actually wanted, delete all three marker lines, check with `git status` that nothing else was unmerged, then `git add README.md` and commit to complete the merge. The same experience helped in the CI part of the lab: my first Actions run failed on a wrong test expectation, and instead of guessing, I read the failing test name in the Actions log, fixed the assertion, pushed again, and the run went green.

---

*Screenshots of each stage (commits, branches, Issues, Pull Requests, the conflict before and after resolution, the failed and passed Actions runs, and the v1.0.0 Release) are collected in the `lab-evidence/` folder.*
