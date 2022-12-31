# Commands that can be useful to install wsl in windows, configure it and launched using Visual Studio Code

## Step 1: Install WSL and the desired Linux distro (I always use Debian)


## Step 2: Connect Visual Studio Code to the WSL distro


## Step 3: Install and set up Git in WSL
sudo apt update
sudo apt install git
git config --global user.name "Douglas Figueroa"
git config --global user.email "douglasr.figueroa@gmail.com"
git config --list
git clone https://myrepo.github.com

## Step 4: How to manage the project folders within wsl
To open the wsl folders using the windows explorer (in case you dont want to use the console), just enter: explorer.exe . in the wsl console, this will open a new Explorer already in the wsl folder from within the command was runned. 

You can also use the command: \\wsl$\

For more information you can check the following link[https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password].
