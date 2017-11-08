Basics Overview
===============

- git is a Version Control System:
    - specifically, it is a _Distributed_ Version Control System (DVCS)
    - can be used as the functional equivalent of a CVCS (Centralized VCS), without losing the benefits of the "D"
    - allows changing, staging, and committing your code without a network connection
    - despite these benefits, a team needs a well-defined workflow to:
	- enable automation of CI/CD pipelines 
	- smoothe out the onboarding process for new developers
	- keep things from breaking, and
	- keep things clean

An Example Git Workflow 
==========

We use a modified version of a common git workflow called "git flow"

- Core traits include:
    - central repo of "truth" (usually called a "monorepo")
    - each branch should represent one of:
	- feature or "topic" of work
	- one of several statically-defined release branches
		- `qa`
		- `stage`
		- `master`
	- a hotfix
    - tight control of feature branches 
    - keep `origin/master` as the sole location for safe, reliable, and reviewed commits
    - therefore, feature branches... 
	- are branched from master
	- are merged back into qa
	- move from `qa` to `stage` to master (prod)
