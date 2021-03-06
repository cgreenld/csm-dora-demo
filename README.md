# cs-dora-demo
Demo for the for csm's and others to simulate the customer experience getting started with LaunchDarkly.  This assumes some knowledge of git and github as a place to store and update code, but tries to walk through the python setup with some specificity.

*Disclosure - the instrucitons for running this have been written using macOS and python10 as a reference point, 
this may result in some mismatch is trying to build on a windows/linux machine or with other software.* 


# Overview
1. Get your environment set up
2. Get your code running WITHOUT a flags
3. Get your code running WITH a flag
4. Expand


# Access Needed
- If you are on mac, make sure you have access to git.  Else run `xcode-select --install`
- You will need launchDarkly github access and the ability to pull down the local repo
    - https://github.com/cgreenld/csm-dora-demo is the link
    - SSO access to github is required through Okta
- An editor, I recommend Visual Studio Code for this
    - https://code.visualstudio.com/download
    - once instlled look for the extensions tab on the left hand side.  Here add the python extension to vscode, this will make developement and management easier
    - There is also an extension for LaunchDarkly that I would recommend adding as well
        - to full utalize this, you will need to add an environment key.  I would do this after completing the inital run and flagging.
- Virtualized Environment Intro: https://towardsdatascience.com/virtual-environments-104c62d48c54
- Python Installed
- NOTE: Tech stacks vary from company to company, not everyone will use python or flask.  However, these tools will help you quickly get to the core of our product - the flag. 


# Running the code
- It is normal to run into issues here, especially the first time.  Don't be afraid to reference the channel: cs-dev-sandbox
- You will want an up to date python version, the following is a gernal template for the steps to get started.  See references for more info
    - Install python 3 (I am using python 3.10 to set this up first)
    - install brew and pyenv
    - validate by running `python --version` and you should see a python 3 version out put
- once you have python set up, you will want to create a "virtual environemtn" this is like a folder you python code can run in
    - cd into the doraProject folder
    - `python -m venv venv `
        - create the environment
    - `source venv/bin/activate`
        - activate the environment
        - at this point you should see something like "python 3.10.1 ('venv':venv) in the lower left hand side of your screen
        - if you are seeing unrelated errors, try another env through vscode 
        - https://techinscribed.com/python-virtual-environment-in-vscode/ in case you get stuck
    - `pip install [your library here]`
    - NOTE: a good way to try and verify this set up, before pip installing everything, is to try and run the code.  You should see an error referencing a module missing, pip install that module, then run again to see if the error is still there.  This will allow you to validate your flow.
- Environment is activated and libraries are installed, you can hit play in the upper right hand corner with the dorah.py open.  This will run your dorah.py
    - pay attention to the output in the terminal below, this will give you a url to see you locally hosted app running!

- References:
    - https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7
    - https://opensource.com/article/20/4/pyenv
    - https://www.macworld.co.uk/how-to/python-coding-mac-3635912/
    - https://code.visualstudio.com/docs/python/environments
    - https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511


# Let's add a Flag and make sure it is initalized
- For reference
    - You will be using the python SDK: https://docs.launchdarkly.com/sdk/server-side/python
- Open dorah.py
    - stop the code if it is still running (ctrl + C)
    - You will find a few comments 
        - inline comments are denoted in python with a "#"
        - Multiline comments are denoted with a """ at the beginning and end
    - These will have the string `STEP #: [Instructions]` with some context on what is going on
    - This will let you know what lines to uncomment, and what the python code is doing to interact with Launchdarkly
    - let's run the code again once you have added LaunchDarkly back into the mix, keep an eye on the terminal to verify implimenenation!
- YOU HAVE GATHERED A FLAG!!
    - congratulations, now it is up to you to find some funcationality to turn on and off, maybe change where a link takes you based on a flag???


# Advanced Topics
- Python management
    - https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7
    - requirments.txt is what is going to keep track of the things we need to run this code
    - this venv will allows us to manage that more or less in a containted space
