# Git Hands on


## Setting up 

- Configure Git:

    ```bash
        git config --global user.name "Your Name"
        git config --global user.email "your.email@example.com"
    ```

- Initialize a Git Repository
  ```bash
  git init
  ```
  
- Clone a Repository:

 ```bash
    git clone <repository_url>
 ```
 Creates a copy of a remote repository on your local machine.

## Working with Changes

- Check Status:

   ```bash
   git status
   ```
   Shows the status of changes as untracked, modified, or staged.

- Stage Changes:

    ```bash
    git add <file(s)>
    ```
 Adds changes to the staging area in preparation for a commit.

- Commit Changes:

    ```bash
        git commit -m "Commit message"
    ```
    Records staged changes with a descriptive commit message.


## Branching and Merging

- Create a Branch:

    ```bash
    git branch <branch_name>
    ```
    Creates a new branch.

- Switch Branch:
    ```bash
    git checkout <branch_name>
    ```
    Switches to the specified branch.

- Merge Branch:
    ```bash
    git merge <branch_name>
    ```
    Combines changes from the specified branch into the current branch.

### Working with Remotes

- Add a Remote Repository:
   ```bash
   git remote add <remote_name> <remote_url>
    ```
    Adds a remote repository.

- Push Changes to a Remote Repository:

    ```bash
    git push <remote_name> <branch_name>
    ```
    Pushes committed changes to a remote repository.

- Pull Changes from a Remote Repository:

    ```bash
    git pull <remote_name> <branch_name>
    ```
    Fetches and merges changes from a remote repository.

### Checking History

- View Commit History:

    ```bash
    git log
    ```
    Displays a log of commits.

- Show Changes in a Commit:

    ```bash
    git show <commit_hash>
    ```
    Displays the changes introduced by a specific commit.
