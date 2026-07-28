### worktrees / sandboxes
- are created per agent instance. originally thought as disposable, setting them up in vscode is too many clicks for the user, so we keep them over mutlitple tasks per agent instance
- we create them with a detached main branch to not conflict with the main clone or other worktrees
- are located within the repos main clone at .worktrees/
- we mount the repos main clone into the sandbox and run the coding agent cli within the worktree folder


**shell alias to setup**
- create the new worktree, use `git worktree add --detach <path-to-worktree> origin/main` to solve the branch conflict
- if an .env file exists, copy it over
- cd into worktree dir
- setup sandbox
- within sandbox, cd into the worktree folder
- setup git user and token
- run agent cli in sandbox

**shell alias to delete**
- quit with error if pwd is not a worktree
- if sand box container is present, delete it and its volume
- cd to main clone
- user confirmation if uncommitted or unpushed changes exist, then delete with `--force`
- delete worktree with `git worktree remove <path>`

**slash command to cleanup worktree**
- ```sh
	git fetch origin
	git switch --detach origin/main
	git branch | grep -v " main$" | xargs --no-run-if-empty git branch -D
	git clean -fd --exclude .env
	```
- clear context

### issues

**slash command to check for open and unassigned issues**

**slash command to create issue  (param: issue description)**
- exit if an github issue for that request/topic/problem already exists in the repo
- create new issue on github
- add issue description

**slash command to plan issue (param: issue number)**
- if assigned to someone else, exit with error
- if unassigned, self assign to issue and doublecheck assignment
- read repo instructions
- read issue description and comments
- create implementation plan

**slash command to post implementation plan as issue comment (param: issue number)**
- if no plan for the issue exists locally, exit
- post existing plan as issue comment
- /worktree-cleanup

**slash command to implement issue (param: issue number)**
- /worktree-cleanup
- if assigned to someone else, exit with error
- if unassigned, self assign to issue and doublecheck assignment
- /worktree-cleanup
- if issue or comment with implementation plan does not exist, exit with error
- if linked branch or linked PR already exist for the issue, exit with error.
- create linked branch on github
- fetch and switch to branch
- implement the plan until verifications / tests succeed (max iterations?)
- add, commit and push to branch
- create PR with reference to issue and description of solution
- self-assign to PR as owner
- /worktree-cleanup 

### pull requests

**slash command to check for open and unassigned pull requests**

**slash command to review pull request (param: PR number)**
- /worktree-cleanup
- if PR reviewer assigned to someone else, exit with error
- if PR reviewer unassigned, self assign to issue and doublecheck assignment
- read repo instructions
- read issue description and comments
- read PR description and comments
- fetch and switch to branch
- if branch has merge conflicts with main branch, comment and exit
- review
	- issue plan matched
	- code style and quality
	- running the tests
	- docs
- when not ok:
	- post problems as line comments
	- post declining review comment
	- exit
- post approving review comment with description of review procedure
- /worktree-cleanup 


**slash command to update PR (param: PR number)**
- /worktree-cleanup 
- exit, if PR owner not assigned to me
- read repo instructions
- read issue description and comments
- read PR description and comments
- fetch and switch to branch
- if not based on latest commit in main branch, rebase and solve merge conficts. `git push --force-with-lease`
- if declining comments exist, solve the problems or remarks. verifications / tests need to pass. (max iterations?)
- add, commit and push all changes
- comment your changes in the pull request
- /worktree-cleanup 


**slash command to merge PR (param: PR number)**
- /worktree-cleanup
- exit, if PR owner not assigned to me
- exit, if PR not approved by at least one reviewer
- read repo instructions
- read issue description and comments
- read PR description and comments
- exit, if declining comments exist
- fetch and switch to branch
- if cannot be merged without conflicts, comment and exit
- if not based on latest commit in main branch, rebase. `git push --force-with-lease`
- merge PR on github and delete branch
- /worktree-cleanup 
- remove local branch if it still exists


### general

**slash command (or alias?) to get next task**
- get all declined PRs assigned to me
- sort by priority descending
- get all open and unassigned PRs
- sort by priority descending and add to bottom of the list
- get all open and unassigned issues
- sort by priority descending and add to bottom of the list
- suggest the top item of the list