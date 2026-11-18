# GitHub Actions — CI Runs

Workflow: **Python CI Tests** (`.github/workflows/python-ci.yml`)
Command run in CI: `python -m unittest discover -s tests -v`
Triggers: push to `main`, and pull requests to `main`.

## Failed run (red) — the deliberate failure

- **Run ID:** 44259915921
- **When:** 2026-11-18 07:34 UTC
- **Event:** pull_request, branch `feature/tests-ci` (PR #11, first push)
- **Result:** failure — one test expectation was intentionally wrong
  (the completed-task checkbox casing), so the suite failed in CI exactly
  as it would for a real bug.

**Screenshot to add:** this run's page in the Actions tab, saved in this folder.

## Passing run (green) — after the fix

- **Fix commit:** `Fix expected checkbox casing in completed task unit test`
- **Run ID:** 44260372178
- **When:** 2026-11-18 07:37 UTC
- **Event:** pull_request, branch `feature/tests-ci` (PR #11, after the fix push)
- **Result:** success — all 6 tests passed

A further successful run (ID 44260592347) fired on the push to `main` when
PR #11 was merged.

**Screenshot to add:** the passing run's page in the Actions tab, saved in this folder.

All runs: https://github.com/taha-qazi/student-task-manager/actions
