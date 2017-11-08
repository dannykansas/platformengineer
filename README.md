# Platform Engineer Training 
This is a *very* simplified, basic repo intended to help introduce git, Vagrant, and local development environment concepts as the first phase of a Platform Engineer training course.

## Contents:
- Vagrantfile with nginx for rapid visual feedback on:
    -  git branching
    -  git workflow
    -  git merges
- Lessons plans (sort of)
- In-class exercises

## Initial Setup:
- From your Terminal.app run `git clone https://github.com/dannykansas/platformengineer.git`
- `cd` to the new `platformengineer` directory
- Run a `vagrant up`
- vagrant will provision your environment, wait...
- When completed, the contents of `platformengineer/www` will be available:
    - [Here!](http://localhost:9999), or 
    - By running `open http://localhost:9999` from the CLI 
