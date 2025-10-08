# 🐙 A Visual Guide to Git Commands

> Your ultimate interactive cheatsheet for mastering Git.  

---

## 🌀 The Daily Git Workflow

This is the fundamental process every developer follows.  
It's a simple loop of checking the status of your project, adding your changes to a "staging area," and then permanently saving them with a descriptive commit message.


| Stage | Command | Description |
|:------|:---------|:-------------|
| **Workspace** | `git status` | View changed files |
| **Staging Area** | `git add .` | Add all modified files |
| **Local Repository** | `git commit -m "message"` | Save snapshot permanently |

---

## 📊 Command Category Breakdown

Git has a rich command set.  
Below is how commands are distributed across different functions — collaboration (Branching & Remotes) plays a major role.

| Category | Description |
|:----------|:-------------|
| **Basic Setup** | Configuration and user setup |
| **Starting a Repository** | `git init`, `git clone` |
| **Staging & Committing** | `git add`, `git commit` |
| **Branching & Merging** | `git branch`, `git merge` |
| **Remotes** | `git push`, `git pull`, `git fetch` |
| **Viewing History** | `git log`, `git show`, `git diff` |
| **Undoing Changes** | `git revert`, `git reset`, `git restore` |
| **Tagging** | `git tag` |
| **Stashing** | `git stash`, `git stash pop` |

---

## 🧠 Core Command Loop

These are the **most commonly used Git commands** — your daily toolkit as a developer:

| Command | Use |
|:---------|:----|
| `git add .` | Stage all changes |
| `git commit -m "..."` | Save staged changes |
| `git push` | Upload commits to remote repo |
| `git pull` | Get updates from remote repo |
| `git checkout -b branch_name` | Create and switch to a new branch |
| `git merge branch_name` | Combine branches |

---

## 📥 Stashing: A Lifesaver

Need to switch branches but aren’t ready to commit?  
Use `git stash` to temporarily shelve your changes.

```bash
git stash      # Save current uncommitted changes
git stash pop  # Bring them right back
