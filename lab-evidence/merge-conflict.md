# Merge Conflict — Before & After

**Part D of the CSC418 lab: a merge conflict created and resolved deliberately.**

## How the conflict was created

1. On `main`, the line `Project status: Planning` was added to README.md and committed
   (`Add project status line to README`).
2. Two branches were created from that commit:
   - `update-status-development` changed the line to `Project status: In Development`
   - `update-status-review` changed the same line to `Project status: Under Review`
3. `update-status-development` was merged into `main` first — cleanly.
4. Merging `update-status-review` into `main` then stopped with:
   `CONFLICT (content): Merge conflict in README.md`

## Before (what Git left in README.md)

```
<<<<<<< HEAD
Project status: In Development
=======
Project status: Under Review
>>>>>>> update-status-review
```

The full conflicted file is saved next to this note as `merge-conflict-before.txt`.

- Between `<<<<<<< HEAD` and `=======`: the version already on `main`
- Between `=======` and `>>>>>>> update-status-review`: the incoming branch's version

**Screenshot to add:** the conflicted README.md in the editor, markers visible —
save it in this folder.

## Resolution

Neither side was simply discarded. The final line combines both intents —
the project *is* in development, and it is also under review:

```
Project status: In Development (under review)
```

The marker lines were deleted, the rest of README.md was left untouched
(no unrelated work was lost), then:

```bash
git add README.md
git commit   # completes the merge: "Merge branch 'update-status-review' into main — resolve status line conflict"
```

**Screenshot to add:** the resolved README.md line and the merge commit in
`git log --graph` — save both in this folder.
