# Command line and BASH 

Analysis machines (including clusters) that you will use for research will typically be running some flavor of Linux (this will be true for many servers and dedicated devices you might encounter as well).  In particular, you will probably interact with these machines primarily via ssh (maybe with some ftp/sftp).  So, it is useful to be able to navigate using the command-line interface, which will in almost all cases default to a bash shell (though you can sometimes choose to use similar alternatives, eg zsh).  There are also a set of common to universal tools that you will regularly call upon in this sell (eg, grep).

There exist many command-line/bash guides, so rather than try to recreate another one here, I will list a few that I thought were useful (feel free to search for more!).  

- https://github.com/RehanSaeed/Bash-Cheat-Sheet
- https://devhints.io/bash
- https://oit.ua.edu/wp-content/uploads/2020/12/Linux_bash_cheat_sheet-1.pdf
- https://devdojo.com/bobbyiliev/the-only-bash-scripting-cheat-sheet-that-you-will-ever-need

I found the following [text](http://mywiki.wooledge.org/BashGuide) helpful for orienting oneself.

> BASH is an acronym for Bourne Again Shell. It is based on the Bourne shell and is mostly compatible with its features.

> Shells are command interpreters. They are applications that provide users with the ability to give commands to their operating system interactively, or to execute batches of commands quickly. In no way are they required for the execution of programs; they are merely a layer between system function calls and the user.

> Think of a shell as a way for you to speak to your system. Your system doesn't need it for most of its work, but it is an excellent interface between you and what your system can offer. It allows you to perform basic math, run basic tests and execute applications. More importantly, it allows you to combine these operations and connect applications to each other to perform complex and automated tasks. 

> Most users that think of BASH think of it as a prompt and a command line. That is BASH in interactive mode. BASH can also run in non-interactive mode, as when executing scripts. We can use scripts to automate certain logic. Scripts are basically lists of commands (just like the ones you can type on the command line), but stored in a file. When a script is executed, all these commands are (generally) executed sequentially, one after another. 

# Helpful Tips
Most commands are modified with flags, which are specified using either a single dash and a letter/symbol, or a double-dash and a word.  Almost every command will print some useful information in response to the `--help` flag, try eg `ls --help`.

Similarly, the `man` command will provide the more full ocumentation for whatever command follows it, eg `man ls`, or even `man man`. 

Generally, (depending on how you set things up, see the `.bashrc` section below), you can use `tab` to complete commands you are typing, including the names of relevant directories/files.

Finally, as there is more already written on all these topics (by people more knowledgeable than me), I have included helpful links.  Many of these are the result of a quick google.  While it's helpful knowing what to google and knowing that certain helpful resources like the arch-linux wiki exists, you can definitely find a lot of this information pretty readily by searching on your own!

## Exercise Setup
We will provide you with the ip address of a linux-based computer to ssh into, and a username/password for you to use.  Use that account/connection for the rest of these exercises. We will go over ssh-ing into clusters later. 

Go to part (2) for details on how to ssh.

# Directories
As with most operating systems you are likely familiar with, Linux organizes things into directories and sub-directories.  The root-level directory is just `/`, and everything else will live under this.  Moreover, pretty much every Linux system will have a set of [standard system directories](https://www.howtogeek.com/117435/htg-explains-the-linux-directory-structure-explained/) under root, like

- /home
- /bin
- /dev
- /mnt
- ...

When you connect to a system (eg via ssh), you will begin in your user's home directory `/home/[username]`.  This is also usually denoted with a `~`.


## Exercise

A few things to try:

- Check your current location with `pwd`
- cd into some other place -- eg `cd /`
- `ls` to see what's there, explore a bit.  Remember you can always see where you are with `pwd`.  Don't worry, you can't break anything as you don't have write access except in your home directory.
- Go back to your home directory with `cd ~` (usually, `cd` by itself will have the same effect)

Now, in your home directory, and looking up commands you need as you go:

- make a file
- make a directory
- move the file into the directory

# Editors
Say you want to edit a file on this remote machine.  Broadly speaking there are two ways to do it.  The first is to use a command-line text editor, such as `vi`, `vim`, or `nano`.  (A sub-category of this, though I've rarely seen anyone do this, is to use x-forwarding to open a gui text editor on the remote machine.  I would not generally expect there to be many installed on analysis machines you will use.)

Alternatively, you can use ftp/scp to remotely retrieve the file, change it on your computer using the text editor of your choice, then send it back to the remote machine.  This sounds clunky, but various software will automate the process for you.  Examples of this include:

- winscp
- Some fancier text editors that include ftp, like [Atom](https://atom.io/) (eg. use locally by doing "atom /path/to/file". See next section for remote usage) or Sublimetext
- Any sort of FUSE filesystem navigator (Gnome's Nautilus file explorer does this well natively)

While the GUI / ftp options can be more aesthetic, I **strongly recommend** you pick a command-line editor like vim or nano and become fluent in it. It will work on all machines - yours and remote ones, and is the fastest and most fail-safe option. 

## Exercise
Add some text to the file!

# Permissions
Unsurprisingly, your user doesn't have the ability to access everything on the computer.  By default, most system directories (those under `/`) will be a least partially readable by all users, but not writable.  Thus, you can see what's there (which can be useful), but not unintentionally (or maliciously) break anything.  Users generally only have write access (the ability to modify) things they own, like their home directory.  

Which brings us to ownership. Each directory/file is owned by a user and group, which controls who has access to it (and who can set the permissions).  You can own a file and not have write permission to it (which you might want to do to keep yourself from changing it), but since you own it you can change that if you need to.

For more about how permissions and groups work, you can look many places, including:

- https://www.guru99.com/file-permissions.html
- https://linuxfoundation.org/blog/classic-sysadmin-understanding-linux-file-permissions/
- https://wiki.archlinux.org/title/users_and_groups
- https://wiki.archlinux.org/title/File_permissions_and_attributes

Note that using the `-l` flag on `ls`, eg `ls -l`, will show you the permissions and ownership of all the files and sub-directories.

One user `root`, has control of everything on the system.  The `su` command lets you switch users (eg `su root`) to become the root user, for doing administrative things.  Alternatively, `sudo [command]` will let you run just one command with root privileges.  Unless you own or become involved in maintaining the system, you are unlikely to use either of these, but should know they exist.  If for some reason, someone set up a system where no password is needed for either (or you know the password), be careful as you *can* break things using this (for example, the infamous `rm -rf /`).

## Exercise
Partner up.  First, figure out together how to read the permissions printed when you `ls -l`, using the resources above or whatever else you find.

Now, take the file you made before, and make it readable to other users.  See if you can read each other's file!  Can you write to them?


# Wildcards
The `*` symbol means something special.  It is a wildcard, and can stand in for all or part of the name of any file or directory.  Say you want to see only the fits files in a directory, you might run `ls *.fits`.

There are other wildcard symbols, which work similarly to regex: https://linuxhint.com/bash_wildcard_tutorial/

# Variables
Bash is a full-fledged language, and so of course you can use variables.

```
STR="Hello World!"
echo $STR  
```

The `$` marks a character as a variable (to replace with it's corresponding value).  `$(some stuff)` similarly will run the `some stuff` in a subshell and replace the parens with the result.  Thus, `echo ls` just prints `ls`, but `echo $(ls)` prints the text that `ls` would output.

- https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-5.html

# Pipe
You can chain multiple commands together by redirecting the output of one command to another, using the pipe symbol `|`.  `A | B` will take whatever the output of A is and 'pipe' it as input to B.  This can be chained arbitrarily many times. \

You can also redirect output to a file using `>`, or `>>` to append to the file.

- https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html
- https://stackoverflow.com/questions/9834086/what-is-a-simple-explanation-for-how-pipes-work-in-bash
- https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file


## Exercise
Make `file_generator.sh` executable.  Run it.  Make a file containing the names of each file in `~/test_files` that starts with the number 3 -- eg `31415` would have to be included, but `12345` would not -- or that contain a 7 at all.


# top, htop
The top command is a useful way to check what's running on the system (similar to the task manager on Windows), and how many resources are being used.  Processes you control that are causing issues can then be killed with some version of the `kill` command (either separately or from within top).  htop is essentially a prettier version of top. Hit `q` to exit. 

Give it a go so you see what it looks like!


# bashrc
Go to your home directory and run `ls -a`.  You should see some files `.*` -- these are hidden files, which ls ignores by default.  Among these is `.bashrc`.  This file is run at the start of each bash shell session you start, and can be used to define the bash environment you want to work in.  In particular you can define quality of life features that might be useful to you, and set environment variables.

<!-- ## QOL
Take a look at the `.bashrc` in `stuent0`'s home directory.  The first hundred or so lines just set up what the shell prompt looks like, in a way I happen to like. 

Then, there are around 50 lines setting up tab completion, and using the up-arrows.  Instead of just showing the most recent command, this changes the up-arrow to do a reverse search using what you have typed so far.   

There are then some lines defining aliases.  These are basically shortcut commands that run longer commands.  These can save a lot of time setting up common ssh connections you use, making `ls` us the `-a` flag by default if that's something you prefer, etc.

Feel free to copy this to the `.bashrc` in your home folder and modify it as you like! -->

## Aliases 

Aliases are way to make your life easier and your command line faster. You can define shorthands for commands that you often use as 

`alias ls='ls -G'`

Note the lack of spaces around the `=`. Depending on your terminal, this example will print the output of `ls` with nice colours that denote what is a file vs a directory vs an executable. 
I use it to define clusters I `ssh` into, executables I often call and even directories I most navigate to. Here's a snippet from an [MIT computing resource](https://missing.csail.mit.edu/2020/command-line/) about aliases that I found useful: 

    # Make shorthands for common flags
    alias ll="ls -lh"

    # Save a lot of typing for common commands
    alias gs="git status"
    alias gc="git commit"
    alias v="vim"

    # Save you from mistyping
    alias sl=ls

    # Overwrite existing commands for better defaults
    alias mv="mv -i"           # -i prompts before overwrite
    alias mkdir="mkdir -p"     # -p make parent dirs as needed
    alias df="df -h"           # -h prints human readable format

    # Alias can be composed
    alias la="ls -A"
    alias lla="la -l"

    # To ignore an alias run it prepended with \
    \ls
    # Or disable an alias altogether with unalias
    unalias la

    # To get an alias definition just call it with alias
    alias ll
    # Will print ll='ls -lh'

## Environment Variables
There are also a number of (generally in allcaps) [environment variables](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux), which can be important in determining how your bash shell operates.

[One that you should know about](https://linuxhint.com/path_in_bash/) is `PATH`.  Run `echo $PATH` to see it.  It should include things like `/usr/local/bin`.  When you try to run a command -- `ls`, `grep`, `nano`, `python`, or anything else -- bash knows that this program exists by looking in all the directories specified in `PATH`.  Thus, the default `PATH` locations are the standard places that software binaries (or at least links to it) are placed upon installation.

However, you may find that you want to install something on your user account rather than system-wide.  This is common if you are installing your own copy some analysis pipeline you are actively working on.  You 1) don't have root access, but more importantly 2) don't want the system-wide installation to be the version you are actively editing!  To do this, you will generally have to add a new directory to your `PATH` (eg, `~/my_software`), where you will also link/copy compiled versions of your code.

[There is similarly](https://www.tutorialspoint.com/What-is-PYTHONPATH-environment-variable-in-Python) a `PYTHONPATH` variable that tells python where to look for modules (beyond the standard locations, which already includes a user-folder like `~/.local/lib/python3.10/site-packages`).

Make sure that you are only *appending* to your `PATH` and *not replacing* it. This can be done by

`export PATH="/path/to/additional/directory:$PATH"

This appends the contents (`$`) of your current `PATH` to the end of your new `PATH`. The command `export` redefines the variable. 

# Summary of generally useful commands 

- `pwd` print current working directory 
- `cd /path/to/directory/` change directory 
- `ls` list all contents of current working directory. You can also ask for the contents of a specific directory with `ls /path/to/dir` 
- `mkdir /path/to/directory/XX` make a directory at the specified location with the name `XX`
- `touch XX` update the time stamp of file `XX` or create it if it doesn't exist 
- `mv XX YY` move or rename files. To move, `XX` and `YY` should be the `/path/to/file/` and `/new/path/to/file/dir` respectively. 
- `chmod u+x,g+w,o+r XX` change permissions of file `XX`, specifically here, give you, the user, execute permissions, give the group writing permissions and all others reading permissions 
- `XX --help` or `man XX` print documentation for any command `XX`. To get out of the manual page, hit `q`
- `echo XX` prints `XX` to the screen. But `echo` can also be used to print the contents of a variable by adding a dollar sign as `echo $XX`
- `$PATH` tells you all the directories your shell will look for executables in. Unless the command you are trying to execute is in one of these locations, the shell will not recognise it. 
- `which XX` tells you the location of the executable `XX` if your shell recognises it. Very useful to ensure for eg. that you are using the correct python / C++ / etc distribution 
- `vi XX` open the file `XX` in the text editor vim. Replace `vi` with the command for your favourite editor.

### Aesthetic recommendations 

- Get iTerminal 
- Get zsh
- Get oh-my-zsh 
