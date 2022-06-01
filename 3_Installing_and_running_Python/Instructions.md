# Let's install python (if you haven't)

We recommend anaconda. It depends on the system but https://docs.anaconda.com/anaconda/install/ are the instructions. Let us help you through it. 

# What is Conda?

By now you have all installed Conda but what IS Conda? Conda is a very useful framework in which to maintain your python working space. It can:
1. install python packages 
2. install non-python dependencies 
3. manage dependencies and compatibilities
4. uninstall the above
5. create environments to manage.

## Installing packages and dependencies

You can install many packages with a simple "conda install (package name)" Try "conda install tqdm" Sometimes you may need to specify the Conda channel for it to identify 
the package of interest, eg "conda install -c conda-forge tqdm" Make sure that tqdm is installed with "conda list" 

If you find that your software requires a certain package, you can google "Conda (package of interest)" to check if you can install it via Conda. Then, it's as simple as 
"conda install (package)" from there! This is not limited to python packages, eg OpenSSL. 

NOTE if you have an M1 mac, this may be extremely useful. Conda installingbasically just downloads pre-installed binaries that works on the specified software+hardware. M1 is new enough that
some packages are really finicky to install. If you are able to conda install that package, it will save you a lot of headache. 

If it gave you a bunch of text about updating packages, removing packages, downgrading packages, etc then you just saw...

## Managing dependencies and compabibilities

You don't actually need to do anything for this. When you installed tqdm, you probably saw messages about installing/upgrading/downgrading/removing some packages
that you didn't know were related. Conda knows all about the intricate web of packages and will automatically tell you when things need updating or downgrading. 
As long as nothing looks incredibly off, just say [y] and your packages' dependencies will be kept track of. 

Note that this is not perfect. Sometimes you will encounter errors that you Google and people will say "Oh you have the wrong version of Numpy." Then you need to get
hands on and change versions manually. So, beware. 

## Uninstalling packages

Try "conda uninstall tqdm" Uninstalling packages is extremely simple. Make sure tqdm is gone with "conda list" Ok now "conda install tqdm" again

## Creating environments 

Probably the most important feature is creating environments. Why would you need to create environments??
- You want to use package A and B, but A wants python 2 and B wants python 3. Then you make an environment with python 2 + A, and another with python 3 + B. 
- You are not the administrator of the machine and can only change your home directory. Then you start an environment where you are free to install/uninstall packages
- You don't know what you are doing with an installation and are likely to mess things up HORRIBLY, so you protect the rest of your working space with a dedicated environment
- much much more

Create your environment with "conda create -n dummy python=3.9" Now you have created an environment called "dummy" based on python 3.9. Check that you have indeed
created this environment with "conda env list" Go to this environment with "conda activate dummy" Whatever you install here is contained within myenv and nowhere else.
Type "conda list" and you should not see tqdm because we never installed it in "dummy". Try "conda deactivate dummy" to leave this environment. Now one can easily delete 
environments with "conda env remove -n dummy" this is useful if your installation of some package goes horribly wrong. 

# What is pip?
Pip is another tool that can help you 
1. install python packages 
2. manage dependencies and compatibilities
3. uninstall python packages

But this time it's python packages only, and you're actually installing them instead of downloading pre installed things. Try "pip install natsort" and try "python > 
import natsort" to check that it has indeed been installed. Now "pip uninstall natsort" to uninstall. 

Note that pip and conda don't necessarily talk to each other in terms of dependency tracking, and I've found conda to be slightly better about these things. So, my suggestion:
stick to conda for installing foundational things (numpy, scipy, astropy etc that other packages may use) and use pip for larger things that other packages will not depend on 
(CAMB, namaster, etc)


# PYTHONPATH

pip and conda know where to install their packages for seamless integration, but sometimes you'll develop a package, or get handed the files for some grad student's
unpublished package that you have to use. Then you'll have to use PYTHONPATH to get python to recognize that package. 

1. "cd" to go to home directory
2. "mkdir pythonpathtest" "cd pythonpathtest" "emacs pythonpathtest.py" "ctrl x ctrl c" (we've made a dummy package at pythonpathtest with a pythonpathtest.py)
3. "cd" to go home, and try "python > import pythonpathtest" It doesn't work because python doesn't know that's there. 
4. "export PYTHONPATH='/Users/minsu/pythonpathtest' " Now we've told python there's something there
5. "echo $PYTHONPATH" should return pythonpathtest. Now your computer knows. 
6. Now try "python > import pythonpathtest" it works because python also knows! 

Note this will only work on this terminal session. For permanent integration of pythonpathtest, you have to add "export PYTHONPATH='/Users/minsu/pythonpathtest' " to .bashrc or .zshrc. Similar philosophy applies with other software as well with PATH. Sometimes you have to tell your computer you have some software worth using by adding "export PATH=(directory)" to the .bashrc. 

# Let's run an actual script! 

Download the script below, test.py. Open your Terminal. Navigate to the directory with test.py and type "python test.py" You just ran a python script from the command line! We will be showing you many many more ways to run python scripts today and tomorrow. 

