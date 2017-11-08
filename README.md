# Platform Engineer Training 
This is a *very* simplified, basic repo intended to help introduce git, Vagrant, and local development environment concepts as the first phase of a Platform Engineer training course.

## Contents:
- Auto-deploying, encapsulated dev environment 
    - uses nginx
    - based on vagrant
    - uses not-Docker on purpose
- Lessons plans
- In-class work
- Homework

## Outline:
- Intro to git
    -  git branching
    -  git workflow
    -  git merges
    -  "gitting along" with other committers (zing!)
- Intro to Object-Oriented Programming (OOP) with Python
    - classes
    - class instances
    - instance methods
    - class methods
    - alternative costructors
    - static methods
    - magic methods/"dunders"
    - decorators
- The Pythonic Approach to Programming (OOP Extended)
    - duck-typing
    - EAFP

## Quick Setup:
- From your Terminal.app run `git clone https://github.com/dannykansas/platformengineer.git`
- `cd` to the new `platformengineer` directory
- Run a `vagrant up`
- vagrant will provision your environment, wait...
- When completed, the contents of `platformengineer/www` will be available:
    - [Here!](http://localhost:9999), or 
    - By running `open http://localhost:9999` from the CLI 
