
# Git Hands on

## Excercises

- [ ] Create a new GitHub profile
- [ ] Configure git on your system
- [ ] Create a new repository in GitHub
- [ ] Clone the repository
- [ ] Change some files
- [ ] Push the code onto the remote repository
- [ ] Pull the code from the remote repository
- [ ] Create a branch and switch to it
- [ ] Fork the code from TelcoBootcamp
- [ ] Add a branch
- [ ] Submit a PR 


## Solution

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


1. Downloading and installing Git : If you don't already have Git installed, you can download Git at www.git-scm.com.
    > If you need additional assistance installing Git, you can find more information in the ProGit chapter on installing Git.

Now is a good time to create a shortcut to the command-line application you will want to use with Git:

    If you are working on Windows, It is highly recommended to use Git Bash which is installed with the Git package, so that you can follow along with the facilitator who will be using Bash
    If you are working on macOS or another Unix-like system, you can use the built-in Terminal application


2. Clone the following repository

Open your chosen shell, and type:

`git clone https://github.com/mohitkr05/TelcoBootcamp.git`

If the clone is successful you'll see:

```
$ git clone https://github.com/mohitkr05/TelcoBootcamp.git
Cloning into 'TelcoBootcamp'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.
```


  