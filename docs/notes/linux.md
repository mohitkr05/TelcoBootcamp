# Linux

## Linux command Line hands on

This tutorial is for a quick hands on demo for the class. A detailed hands on is based on the Linux Command Line handbook.

## Getting to know the system
- `uname -a`: Display system information including kernel version, hostname, and architecture.
- `hostname`: Show or set the system's hostname.
- `lsb_release -a`: Display distribution-specific information.
- `cat /etc/os-release`: View information about the operating system.
- `cat /proc/version`: Show Linux kernel version and information.
- `uptime`: Display how long the system has been running.
- `date`: Show the current date and time.
- `cal`: Display a calendar.
- `w`: Show who is logged in and what they are doing.
- `whoami`: Display the username of the current user.
- `id`: Display user and group information.


## Understanding the filesystem

### Basic Filesystem Structure:

  - / (Root Directory): The top-level directory of the filesystem hierarchy.
  - /bin: Essential system binaries (commands) needed for system repair and recovery.
  - /sbin: System binaries specifically used for system administration tasks.
  - /etc: Configuration files and directories.
  - /home: Home directories for users.
  - /var: Variable data, such as logs, spool files, and temporary files.
  - /tmp: Temporary files.
  - /usr: User-related programs and files.
  - /lib and /lib64: Essential shared libraries needed for system boot.
  - /dev: Device files representing hardware devices.
  - /proc: A virtual filesystem that provides information about processes and kernel parameters.


### File system navigation

- `pwd`: Print the current working directory.
- `ls`: List directory contents.
- `cd`: Change directory.
- `cp`: Copy files or directories.
- `mv`: Move or rename files or directories.
- `rm`: Remove files or directories.
- `file`: Determine file type.
- `stat`: Display detailed file or filesystem status.
- `du`: Estimate file space usage.
- `df`: Display disk space usage.
- `cat`: Concatenate and display file content.



## File permissions and ownerships

File permissions and ownership are crucial aspects of Linux file system security. They determine who can access, modify, or execute files and directories. Each file and directory has an associated owner, group, and a set of permissions for three categories of users: owner, group, and others.

### File Permissions:

- Read (r): Allows the reading of a file's contents or viewing a directory's listing.
- Write (w): Permits the modification of a file's contents or the creation and deletion of files within a directory.
- Execute (x): Grants the ability to execute a file or traverse a directory.

### File Ownership:

- Owner: The user who owns the file. This user has special permissions to read, write, and execute the file.
- Group: A set of users who share the same permissions on the file. Files can belong to a user and a group.

### Commands for File Permissions and Ownership:

- `chmod` -  Change Mode - Used to change file or directory permissions.
    - `chmod permissions filename`
    - `chmod u+rw filename`
    - `chmod o-w filename`
- `chown` - Change Owner - Used to change the owner of a file or directory. 
    - `chown user:group filename`
    - `chown john filename`
- `chgrp` - Change Group - Used to change the group ownership of a file or directory.
    - `chgrp groupname filename`
    - `chgrp staff filename`

## Checking the hardware

- `df -h`: Display disk space usage in a human-readable format.
- `free -m`: Display the amount of free and used memory in megabytes.
- `lscpu`: Display CPU information.
- `lsblk`: List block devices (disks and partitions).
- `lshw`: List hardware information.
- `lspci`: Display PCI devices.
- `lsusb`: Display USB devices.
- `ifconfig` or `ip a`: Show network interfaces and their configurations.
- `route -n`: Display the routing table.
- `cat /etc/resolv.conf`: View DNS configuration.


## Processes


- `ps aux`: Display information about all running processes.
- `top`: Display dynamic real-time information about running processes.
- `systemctl list-units --type=service`: List all active services.


## Understanding users and Groups

- `useradd` - To add a user - e.g. `sudo useradd username` 
- `userdel` - To delete a user - e.g. `sudo userdel username`
- `groupadd` - To add a group - e.g.`sudo groupadd groupname`
- `groupdel` - To delete a group - e.g. `sudo groupdel groupname`
- `usermod` -  Add user to group - e.g. `sudo usermod -a -G groupname username`
- `su`- Switch user - e.g. `su username`



## Project

### Basic Linux system administrator

The objective of this excercise is to understand how system administrators work in Linux

1. Change the hostname of the system `nms01`.
2. Validate the system configuration using command line commands.
    - Hostname
    - Type of shell
    - Home directory
    - List of users defined
    - List of groups defined
    - List of users in each group
    - Disk space
    - Memory usage
    - Hardware attached
    - Type of distribution and version
    - Linux kernel version
    - IP address
    - Reachability to internet
    - Timezone

3. Check the root directory and print out the nested directory structure
4. What is the type of package manager used?
5. Update the system to latest version.

### Command Line excercise

The objective of this excercise is to understand how command line works in Linux

1. Check which shell you are using.
2. Repeat the above command with a short cut key.
3. Create a directory `hello` and create a file `hello.txt` in it.
4. Edit the file `hello.txt` and write `Hello World` in it.
5. Manipulate the file and perform the folloing
    - Open the file -  `cat hello.txt`
    - Count the lines in the file - `wc -l hello.txt`
    - Count the first 5 lines in the file - `head -n 5 hello.txt`
    - Count the last 5 lines in the file - `tail -n 5 hello.txt`
6. Use the input and output redirection in two of the commands.
7. Use a pipe operator with two commands.
8. Print out the root directory structure in a file with a single line command.
9. Instal wireshark on the system.
10. Remove the package wireshark from the system.



### Linux as a Multi-user Environment

The objective of this excercise is to understand how multiuser environment works in Linux

1. You are a system administrator. Create the following permission scopes
    1. Create 3 Groups - `sysadmins`, `netengineers` and `users` 
    2. Create 4 Users - `john`, `paul`,`ajay` , `george` and `ringo`
    3. Add users to groups - 
        - `john` in `sysadmins`
        - `paul` & `ajay` in `netengineers` 
        - `george` & `ringo` in `users`

2. Add the user `john` to sudoers list.

3. Switch user with each of the above user and validate the following
    - Type of shell 
    - home directory

4. Create the following directories in `/opt/project`.  Use only a single line command to do this.
    1. `/opt/project/sysadmin`
    2. `/opt/project/netengineers`
    3. `/opt/project/users`

5. Change the ownership of both directories to the following groups 
    1. owner sysadmin -  /opt/project/sysadmin
    2. owner netengineers - /opt/project/netengineers
    3. owner users -  /opt/project/users

6. Validate that both `ajay` and `paul` are able to access the documents in the directory `/opt/project/netengineers` & not able to access any documents in `/opt/project/sysadmin`.

7. Validate that `george` and `ringo` are able to access the documents in the directory `/opt/project/users` & not able to access any documents in `/opt/project/sysadmin`.

8. Create a new file in `/opt/project/netengineers` with the user `ajay`. Switch to `paul` - Can you write to this file? How can you do this?


