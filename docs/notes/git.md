
# Git & GitOps for Telecom Engineers

## What is Git

Git is a distributed version control system (DVCS) designed to handle everything from small to very large projects with speed and efficiency. It was created by Linus Torvalds in 2005 to manage the development of the Linux kernel. Git is widely used for source code management (SCM) and is the most popular version control system in the world.

Here are some key concepts and features of Git:

- **Version Control**: Git allows developers to track changes in their codebase over time. Each change is recorded, and developers can navigate through different versions of the code.

- **Distributed**: Git is a distributed version control system, meaning that every developer has a complete copy of the repository on their local machine. This allows for offline work and faster operations.

- **Branching and Merging**: Git makes it easy to create branches for parallel development and merge them back into the main codebase. This is crucial for collaborative development, enabling multiple developers to work on different features simultaneously.

- **History Tracking**: Git maintains a detailed history of changes, making it possible to trace back and understand how the code evolved. This is valuable for debugging and auditing purposes.

- **Staging Area**: Git uses a staging area, also known as the index, where changes can be reviewed and selectively committed before making them a permanent part of the project history.

## What is GitOps
GitOps is a set of practices that use Git as the single source of truth for managing infrastructure and application delivery. It extends the principles of Git to operations, promoting a declarative approach to infrastructure and application management. The core idea is to use Git repositories not only for source code but also as the source of truth for the desired state of the entire system.

Key concepts of GitOps:

- **Declarative Configuration**: In GitOps, the desired state of the system is declared in a Git repository. This includes both application code and infrastructure configuration. Changes to the system are made by updating the Git repository with the desired changes.
- **Versioned Configuration**: Git provides version control for the entire system configuration. This allows for easy rollback to a previous state and provides an audit trail of changes over time.
- **Automation**: GitOps relies heavily on automation to continuously monitor the Git repository for changes and automatically apply those changes to the target environment. Continuous Deployment (CD) pipelines are often used to automate the deployment process.
- **Reconciliation**: The actual state of the system is continuously compared with the declared state in the Git repository, and any deviations are automatically corrected. This ensures that the system is always in the desired state.



## Infrastructure as Code

Infrastructure as Code (IaC) for Network Ops refers to the practice of using code to automate the provisioning, configuration, and management of network infrastructure in a telecom environment. This approach brings several benefits to the telecom industry, improving efficiency, reliability, and scalability. Here's how IaC for Network Ops helps in the telecom sector:

- Automation and Efficiency:
  - Rapid Deployment: IaC allows for the rapid and consistent deployment of network infrastructure. Telecom operators can automate the provisioning of networking components, reducing the time it takes to set up new services or make changes to existing ones.
  - Consistency: IaC ensures that the network configuration is consistent across different environments. This reduces the chances of errors caused by manual configuration and enhances overall network reliability.

- Scalability:
   - Elasticity: Telecom networks often need to scale up or down based on demand. IaC enables dynamic scaling by automatically adjusting the network infrastructure to accommodate changes in traffic or service requirements.

- Version Control and Rollbacks:
   - Versioning: IaC tools enable version control for network configurations. This means that changes to the network can be tracked over time, and different versions can be managed.
   - Rollback Capabilities: In case of issues or failures, IaC allows for easy rollback to a previous version of the network configuration. This helps in quickly reverting to a known and working state.

- Collaboration and Documentation:
   - Collaboration: IaC facilitates collaboration among network operations teams by allowing them to work on the same codebase. This promotes better communication and coordination in managing network infrastructure.
   - Documentation: The code itself serves as documentation for the network configuration. This makes it easier for teams to understand how the network is set up and configured, improving knowledge sharing and troubleshooting.

- Policy Compliance:
   - Enforcement of Policies: IaC can be used to enforce network policies and compliance standards. This ensures that the network configurations adhere to security, regulatory, and operational requirements.

- Testing and Validation:
    - Automated Testing: IaC allows for the creation of automated tests to validate network configurations before deployment. This helps catch potential issues early in the development process, reducing the likelihood of errors in the live network.

- Cost Optimization:
    - Resource Optimization: IaC can help optimize resource usage by dynamically adjusting network resources based on demand. This can lead to cost savings by ensuring that resources are allocated efficiently.


## GitOps in Telecom

- **Repository Structure**:
    - Create a Git repository to store configuration files for network equipment. This repository becomes the single source of truth for the desired state of the network.
    - Organize the repository with directories for different types of equipment, such as routers, switches, and firewalls.

- **Infrastructure as Code (IaC)**:
    - Represent network configurations as code using Infrastructure as Code (IaC) principles. This means defining network configurations in a declarative format that can be version-controlled in Git.

- **Version Control**:
    - Leverage Git's version control capabilities to track changes to network configurations over time. Each commit should represent a specific configuration state, making it easy to roll back to previous configurations if needed.

- **Branching Strategy**:
    - Implement a branching strategy in Git to manage different environments or stages of the network (e.g., development, testing, production). This allows for parallel development and testing of configurations.

- **Continuous Integration/Continuous Deployment (CI/CD)**:
    - Set up CI/CD pipelines to automate the testing and deployment of network configurations. Changes pushed to the Git repository trigger these pipelines, ensuring that configurations are tested before being applied to the actual network equipment.

- **Git Hooks for Automation**:
    - Use Git hooks to trigger automation scripts whenever changes are pushed to the repository. These scripts can validate configurations, generate documentation, and initiate deployment processes.

- **Secrets Management**:
    - Implement secure handling of sensitive information, such as device credentials and access keys. Use tools or practices for managing secrets securely within the GitOps workflow.

- **Reconciliation**:
    - Employ reconciliation mechanisms to continuously compare the actual state of network equipment with the declared state in the Git repository. Automated tools can be used to detect and correct any discrepancies.

- **Monitoring and Auditing**:
    - Integrate monitoring tools to keep track of the network's operational status. Implement logging and auditing mechanisms to trace changes and activities related to network configurations.

- **Collaboration and Code Review**:
        Facilitate collaboration among network engineers by enabling them to review and comment on proposed changes through Git pull requests. This helps ensure that configurations are thoroughly reviewed before being merged.

- **Documentation**:
        Use the Git repository not only for configurations but also for storing documentation related to network equipment. This documentation can include network diagrams, change logs, and other relevant information.
 
## Working with Git

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
``
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

> If you are working on Windows, It is highly recommended to use Git Bash which is installed with the Git package, so that you can follow along with the facilitator who will be using Bash.If you are working on macOS or another Unix-like system, you can use the built-in Terminal application


2. Clone the following repository

Open your chosen shell, and type:

```bash
git clone https://github.com/mohitkr05/TelcoBootcamp.git
```

If the clone is successful you'll see:

```bash
$ git clone https://github.com/mohitkr05/TelcoBootcamp.git
Cloning into 'TelcoBootcamp'...
remote: Counting objects: 6, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (6/6), done.
```



3. Assignment
- [Excercise -  Git](../excercises/git-handson.md)
- Read the Pro Git Ebook
- Watch the Linux command line video