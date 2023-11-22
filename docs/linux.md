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


