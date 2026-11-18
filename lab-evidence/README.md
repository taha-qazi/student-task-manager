# Lab Evidence

Screenshots and logs captured while building this project. Capture each
screenshot at the moment it happens — several of these states (especially
the conflict markers and the failed CI run) cannot be recreated afterwards
without redoing the work.

## Checklist

- [ ] Git log / commit graph showing the progressive history (`git log --graph --oneline --all`)
- [ ] Branch list on GitHub showing the 3 feature branches
- [ ] GitHub Issues list (4+ issues, with labels)
- [ ] Pull Request page for a feature branch, showing the review comment and `Closes #…` link
- [ ] Merged Pull Requests list (5 merged PRs)
- [ ] Merge conflict **before** resolution — README.md showing `<<<<<<<`, `=======`, `>>>>>>>` markers
- [ ] Merge conflict **after** resolution — the clean resolved line and the merge commit
- [ ] GitHub Actions — the **failed** run (red) from the first tests push
- [ ] GitHub Actions — the **passed** run (green) after the fix commit
- [ ] GitHub Release page for **v1.0.0**
- [ ] The console app running (add, display, complete, delete in one session)

Text logs in this folder (commit graph, test output) are supporting evidence,
not a replacement for the screenshots above.
