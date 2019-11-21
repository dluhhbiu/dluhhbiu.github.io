---
layout: post
title: How to write correctly git commits
date: 2019-11-21 09:38:42 +0300
comments: true
tags: 
 - git 
 - best practices 
---

### Format of the commit message
```bash
<type>(<scope>): [<ticket_id>]<subject>

(<scope>) is optional
[<ticket_id>] is required if a project is related with tasks board
```

### Examples
```bash
feat(article): add new article about git commits
feat(users): [TASK-111] create user endpoint GET /users
fix(users): [TASK-113] fix permissions to return users
test(rspecs): [TASK-112] Cover user endpoint GET /users by tests
```

### Message subject (first line)
The first line cannot be longer than 70 characters, the second line is always blank and other lines should be wrapped at 80 characters. Also, you should use the imperative, present tense: “change” not “changed” nor “changes”.

### Type
Type is a broad level classification of the type of your work. The list of allowed types:

`feat`: (new feature for the user, not a new feature for build script)

`fix`: (bug fix for the user, not a fix to a build script)

`docs`: (changes to the documentation)

`style`: (formatting, missing semi colons, etc; no production code change)

`refactor`: (refactoring production code, eg. renaming a variable)

`test`: (adding missing tests, refactoring tests; no production code change)

`chore`: (updating grunt tasks etc; no production code change)

### Scope
Scope is a specific area under the broad level type which is being worked on. The `(<scope>)` can be empty (e.g. if the change is a global, difficult to assign to a single component or it not needed very small project)


**When writing the article, I used next materials:**
 - [Semantic Commit Messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716){:target="_blank"}
 - [http://karma-runner.github.io](http://karma-runner.github.io/1.0/dev/git-commit-msg.html){:target="_blank"}
