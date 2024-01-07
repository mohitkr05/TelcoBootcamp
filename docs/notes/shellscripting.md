# Shell Scripting 101

## What is shell scripting?

What would happen if we write all the linux commands in a file and execute it? Well, shell scripting is the art of automating tasks through the command line. It uses a series of commands in a script file. 

## Writing your first shell script

1. Create your first script:

Open your text editor and create a new file. Save it with a descriptive name ending in .sh, like hello_world.sh. Remember, the .sh extension tells the system it's a shell script.

2. Hello, world!:

Inside your script, type the following line:

```bash 
echo "Hello, world!"
```

This line uses the echo command to print the text "Hello, world!" to the terminal.

3. Run your script:

Save your script and open a terminal. Navigate to the directory where you saved the script.

To run the script, type the following:

```bash 
chmod u+x hello_world.sh
bash hello_world.sh 
sh hello_world.sh 
./hello_world.sh
```

If everything went well, you should see "Hello, world!" printed in the terminal! Congratulations, you've written and run your first shell script!


## Using variables

- Creating a Variable:

Think of a variable as a named box holding any value you want: text, numbers, dates, even other variables! To create one, simply assign a value using the = operator:

```bash 
name="Bob"
age=3 
today=$(date +%Y-%m-%d) # Store today's date
```
Note: 
- Variable names are case-sensitive! Name and name are different boxes.
- No Spaces: Ensure there are no spaces around the = sign.

2. Accessing Stored Values:

To use the stored value, add a $ symbol before the variable name:

```bash
echo "Hello, $name!"
echo "I was born in $today."
```

3. Unsetting Variables:

Like cleaning up your room, you can remove variables with the unset command:

```bash
unset name
echo "$name" # Should print nothing
```

4. Special variables

pecial Variables

Shell scripts have several special variables, like:
```bash 
    $0 - The name of the script.
    $1 to $9 - The first to ninth argument passed to the script.
    $# - The number of arguments passed to the script.
    $? - The exit status of the last command executed.
    $$ - The process ID of the current script.
    $USER - The username of the user running the script.
```

### Examples

- Dates

```bash
current_date=$(date)
echo $current_date

```

- Arithmetic

```bash
a=5
b=3
sum=$((a + b))
echo $sum  # Outputs: 8

```

- String 

```bash
greeting="Hello, "
name="Bob"
message=$greeting$name
echo $message  # Outputs: Hello, Bob
```

- Text printing

```bash
#!/bin/bash

# Declare a variable
greeting="Hello, Shell Scripting!"

# Use the variable
echo $greeting
```

- User Input 

```bash
#!/bin/bash

# Ask for user input
echo "What is your name?"
read name

# Greet the user
echo "Welcome, $name!"

```

- Command line substitution

```bash
#!/bin/bash

# Get the current directory
current_directory=$(pwd)

# Display the current directory
echo "You are in the directory: $current_directory"

```
- Arithmetic Operations
```bash
#!/bin/bash

# Declare variables
a=10
b=5

# Arithmetic operations
sum=$((a + b))
difference=$((a - b))
product=$((a * b))
quotient=$((a / b))

# Display the results
echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"

```


## Conditional Statements

1. if Statement: It evaluates a condition and, if true, executes a block of code. Here's the basic structure:

```bash
if condition; then
  # Code to execute if true
fi
```

For example, checking if a file exists:

```bash
if [ -f "myfile.txt" ]; then
  echo "myfile.txt is here!"
fi
```

2. Exploring Comparisons: The condition can be any comparison using operators like ==, !=, <, >, <=, and >=. Let's compare user input to a threshold:

```bash
read -p "Enter your age: " age
if [[ $age -ge 18 ]]; then
  echo "Welcome! You're eligible to enter."
else
  echo "Sorry, you must be 18 or older."
fi
```
 

3. Else and Elif: Add options with else for the opposite condition and elif for additional checks:


```bash
read -p "Enter 1 or 2: " number
if [[ $number -eq 1 ]]; then
  echo "Heads!"
elif [[ $number -eq 2 ]]; then
  echo "Tails!"
else
  echo "It's a draw!"
fi
```
Use code with caution. Learn more

### Examples

- Basic If-Else Statement
```bash 
#!/bin/bash
# Read a number
echo "Enter a number:"
read number

# Check if the number is positive or negative
if [ $number -gt 0 ]; then
    echo "The number is positive."
elif [ $number -lt 0 ]; then
    echo "The number is negative."
else
    echo "The number is zero."
fi
```

- Read if file exists

```bash 
#!/bin/bash

# File name
file="sample.txt"

# Check if the file exists
if [ -f "$file" ]; then
    echo "$file exists."
else
    echo "$file does not exist."
fi

```

- Compare strings

```bash
#!/bin/bash

# String variables
str1="Hello"
str2="World"

# Compare strings
if [ "$str1" == "$str2" ]; then
    echo "Strings are equal."
else
    echo "Strings are not equal."
fi

```
- Using AND (&&) and OR (||) in conditions

```bash
#!/bin/bash
# Variables
a=20

# Check conditions
if [ $a -gt 5 ] && [ $a -lt 15 ]; then
    echo "Number is between 5 and 15."
elif [ $a -lt 5 ] || [ $a -gt 15 ]; then
    echo "Number can be less than 5 or more than 15."
else
    echo "Neither condition is true."
fi
```

- Case statement

```bash
#!/bin/bash

# Ask for user input
echo "Enter your choice (yes/no):"
read choice

# Case statement
case $choice in
    yes|YES|y|Y)
        echo "You chose yes."
        ;;
    no|NO|n|N)
        echo "You chose no."
        ;;
    *)
        echo "Invalid choice."
        ;;
esac
```

## File Reading

1. Basic file reading

This method uses a while loop to iterate through each line of the file.
Use the read command to capture each line within the loop.

```bash
while IFS= read -r line; do
  # Process each line (e.g., echo, store in variable)
done < "filename.txt"
```

2. Read specific lines

```bash
head -n 3 "filename.txt"   # Read first 3 lines
tail -n 2 "filename.txt"   # Read last 2 lines
grep "error" "filename.txt" # Read lines containing "error"

```

3. Read whole file into a variable

```bash
file_content=$(cat "filename.txt")
# Process the entire content stored in the variable
```


### Example

```bash 
#!/bin/bash

# Ask the user for the directory path
echo "Enter the directory path containing text files:"
read directory

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory does not exist."
    exit 1
fi

# Ask for the search keyword
echo "Enter the search keyword:"
read keyword

# Loop through each text file in the directory
echo "Searching for '$keyword' in files in $directory:"
for file in "$directory"/*.txt
do
    echo "Searching in $file:"
    grep "$keyword" "$file"
done
```

References 
1. https://www.shellscript.sh/
