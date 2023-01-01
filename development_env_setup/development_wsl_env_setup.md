# Configure dev environment using WSL in Windows and launch it using Visual Studio Code

## Step 1: Install WSL and the desired Linux distro (I always use Debian)
Open Powershell as Administrator and run the following commands:

Installing WSL:
```
wsl --install
```

If you want to first list the available distros, you can run this command:
```
wsl --list --online
```

Now, install the distro
```
wsl --install -d <Distribution Name> 
```

If you want to setup a distro as the default distro for WSL, run this command:
```
wsl --setdefault <DistributionName>
```

For more information you can check the documentation [here](https://learn.microsoft.com/en-us/windows/wsl/install).

## Step 2: Connect Visual Studio Code to the WSL distro
Click on the left bottom corner in Visual Studio Code, and in the prompt box select:
*New WSL Window* then, select the distro installed.

This will open a new window and the console will be in the WSL. So you can start developing and installing everything you need for Linux.

## Step 3: Install and set up Git in WSL
Enter the console and run the following commands:

```
sudo apt update
sudo apt install git
git config --global user.name "Name Lastname"
git config --global user.email "yourmail@gmail.com"
git config --list
git clone https://myrepo.github.com
git checkout yourbranch
```

## Step 4: How to manage the project folders within wsl
To open the wsl folders using the windows explorer (in case you dont want to use the console), just enter in the wsl console this command: 
```
explorer.exe . 
````
It will open a new Explorer already in the wsl folder from within the command was runned. 

You can also use the command: \\wsl$\

For more information you can check the following [link](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#set-up-your-linux-username-and-password).
