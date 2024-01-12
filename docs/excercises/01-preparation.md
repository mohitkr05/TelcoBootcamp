# System preparation

Suggest method is to use Virtual Machine with VirtualBox on your local PC, if you have resource constraints you can use WSL as well.



## Software to be installed
- **VirtualBox**: VirtualBox is a powerful open-source virtualization tool that allows you to run multiple operating systems on a single machine. Ideal for development, testing, and experimentation.
- **Python 3**: Python is a versatile and easy-to-learn programming language. Python 3 is the latest version, offering improvements in performance and syntax over its predecessors.
- **Notepad++**: Notepad++ is a feature-rich, free source code editor and Notepad replacement that supports various programming languages. It offers a clean and efficient interface.
- **Kubernetes CLI**: The Kubernetes Command Line Interface (kubectl) allows you to interact with Kubernetes clusters. Manage applications, deploy containers, and troubleshoot your cluster from the command line.
- **Kubernetes Helm**: Helm is a package manager for Kubernetes applications. It simplifies the deployment and management of complex applications on Kubernetes clusters
- **Wireshark**: Wireshark is a powerful network protocol analyzer. It lets you capture and examine the data traveling back and forth on your network, helping with troubleshooting and analysis.
- **PuTTY**: PuTTY is a lightweight and reliable terminal emulator for Windows. It supports various network protocols, including SSH, Telnet, and more.
- **Git**: Git is a distributed version control system used for tracking changes in source code during software development. It facilitates collaboration and code management.
- **Visual Studio Code (VSCode)**: VSCode is a free, open-source code editor with excellent support for various programming languages. It features a wide range of extensions for customization and additional functionality.
- **Docker Desktop**:  Docker Desktop simplifies the deployment and management of containerized applications. It provides an easy-to-use interface for building, testing, and running Docker containers.
- **AWS Command Line Interface (AWS CLI)**:  AWS CLI is a unified tool to manage AWS services directly from the command line. It simplifies script automation and interaction with various AWS resources.

## Installing software on Windows

In this chapter, we guide you through the essential steps of installing the required software for your Windows system. The list of softwares to be installed are as follows.

You can either directly download from the exe files that are provided or you can use chocolatey to download and install it.

### To use chocolatey

To install Chocolatey, simply open PowerShell and run the following command:
`Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))`




### Chocolatey Script
```
# Install Chocolatey packages for DevOps tools
choco install virtualbox -y
choco install git -y
```

Going forward we are going to install following softwares as well.
```
choco install python3 -y
choco install notepadplusplus -y
choco install kubernetes-cli -y
choco install kubernetes-helm -y
choco install wireshark -y
choco install putty -y
choco install vscode -y
choco install docker-desktop -y
choco install awscli -y
choco install terraform -y
choco install packer -y
choco install jenkins -y
```

## Linux VM Configuration

We are going to use the Virtual Machine as our NMS (Network Management Server)

### Configure SSH port forwarding

1. Add yourself into the `sudoers` file 
    1. Login as root with - `su - root`
    2. Add yourself to the `sudoers` file - `echo "<username> ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers`
    3. Exit the terminal and test it using - `sudo whoami`
2. Install OpenSSH 
    1. Perform the apt-get update using - `sudo apt update`
    2. Install OpenSSH - `sudo apt install openssh-server`
3. Configure OpenSSH for Password login
    1. Start the OpenSSH service - `sudo systemctl start ssh`
    2. Enable the OpenSSH service - `sudo systemctl enable ssh`
    3. Check the status of the OpenSSH service - `sudo systemctl status ssh`
    4. Enable port 22 in UFW - `sudo ufw allow 22`
4. Configure the Port forwarding the VM 
    1. Port forwarding from local port to the server ports
5. Connect using the SSH terminal
    1. Login with - `ssh <username>@<hostname>`


### System Configuration
- Set the system name   - `sudo hostnamectl set-hostname nms`
- Configure the hostnames - `sudo vi /etc/hosts`


### Installing Git

- Update the system - `sudo apt-get update`
- Install Git - `sudo apt-get install git`


## Configure Git

- Configure Git 
  - `git config --global user.name "Your Name"`
  - `git config --global user.email "Your Email"`

## Download the Repository

- Fork the repository `https://github.com/mohitkr05/TelcoBootcamp`
- Clone the Repository 
  - `git clone https://github.com/your-username/TelcoBootcamp.git`

