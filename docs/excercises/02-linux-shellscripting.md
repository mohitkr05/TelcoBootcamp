# Linux and Shell scripting

## Linux excercise
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



## Shell scripting hands on

