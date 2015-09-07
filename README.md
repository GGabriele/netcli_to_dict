# NetCLI to Dictionary

The concept of NetCLI to Dictionary is simple. It is a collection of scripts that provide samples of how to iterate through the output of an executed command and return a dictionary, or a list of dictionaries, based on information could be useful in various automation projects. This project itself shouldn't be considered a framework for network automation, but rather a contribution to the netops community, whom are software / devops oriented.

### How to Contribute

+ Fork this repository
+ Clone your fork to your local computer
+ Create a new branch
+ Create a new folder
  - Folders should be in the format of vendor_os_command. Example: cisco_ios_show_version
+ Create a text file with the command output
+ Create the script that iterates through the text file and returns a dictionary of the desired meta data.
+ Commit your changes to your branch
+ Submit a pull request
+ The community should then review the code and merge it to the master branch

The gist of it is to follow the git workflow. 

### Basic Guidelines

1. The scripts can be written in any language that you are comfortable with.
2. An individual of any skill level should feel encouraged to contribute, as the whole goal is a community of sharing.
