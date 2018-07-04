# CheatSheet for Git
### 1. reset commit
  - ` git reset HEAD^ --hard ` (discard changes, back to last commit)
### 2. branching and merging  
  - create a branch 
     - `git branch <name>`
     - `git checkout <name>`  (switch to the <name> branch)
     - `git commit -m "blabla"`
     - `git push --set-upstream origin <name>` (first time needed)
  - view something
     - `git branch` (show all branches, current branch in the starred one)
  - merge a branch with master
     - `git checkout master`
     - `git merge <the-branch-to-merge>`
  
  - merge pull request w/ master when there are other modifs
      ```
      git fetch
      git rebase origin/master
      git push -f
      ```
  
### 3. tracking status
  - `git status -- <path>` (only track status specified in <path>)
  
### 4. content manipulation

  - restore code to specific commit 
     
    `git checkout SHA -- file1/to/restore file2/to/restore`
  
  - remove all files not under source control
    
    `git clean -d -f -x` 

### 5. stats of a repo
  - get the total lines of code (in python in this case, if c++ then change py to cpp, and so on)       
    `git ls-files | grep py |xargs wc -l` 
### 6. Misc
   - colorize output of git
     enter the following content in `.gitconfig`
     
     `[color] ` 
  
  
 
 
