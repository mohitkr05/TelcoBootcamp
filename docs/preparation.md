# Preparation

Suggest method is to use Virtual Machine with VirtualBox on your local PC, if you have resource constraints you can use WSL as well.


## Installing software on Windows

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

