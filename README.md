# cs-dora-demo
Demo for the for csm's and others to simulate the customer experience.  This assumes some knowledge of git and github as a place to store and update code, but tries to walk through the python set up with some specificity.

*Disclosure - the instrucitons for running this have been written using macOS as a reference point, 
this may result in some mismatch is trying to build on a windows or linux machine.* 


# Access Needed
- You will need launchDarkly github access and the ability to pull down the local repo
    - https://github.com/launchdarkly/cs-dora-demo is the link
    - SSO access to github is required through Okta
- An editor, I recommend Visual Studio Code for this
    - https://code.visualstudio.com/download
    - once instlled look for the extensions tab on the left hand side.  Here add the python extension to vscode, this will make developement and management easier
    - There is also an extension for LaunchDarkly that I would recommend adding
- Virtualized Environment Intro
- Python Installed


# Running the code
- You will want an up to date python experience, depending on your OS this can vary the following is a gernal template.  See references for more info
    - Install python 3 (I am using python 3.10 to set this up first)
    - install brew and pyenv
    - validate by running `python --version` and you should see a python 3 version out put
- once you have python set up, you will want to create a "virtual environemtn" this is like a folder you python code can run in
    - cd into the doraProject folder
    - `python -m venv venv `
    - `source venv/bin/activate`
        - at this point you should see something like "python 3.10.1 ('venv':venv) in the lower left hand side of your screen
        - if you are seeing unrelated errors, try another env through vscode 
        - https://techinscribed.com/python-virtual-environment-in-vscode/ in case you get stuck
    - `pip install [your library here]`
    https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511

- References:
    - https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7
    - https://opensource.com/article/20/4/pyenv
    - https://www.macworld.co.uk/how-to/python-coding-mac-3635912/
    - https://code.visualstudio.com/docs/python/environments


# Let's add a Flag and make sure it is initalized
- For reference
    - You will be using the python SDK: https://docs.launchdarkly.com/sdk/server-side/python
- Open dorah.py
    - You will find a few comments 
        - inline comments are denoted in python with a "#"
        - Multiline comments are denoted with a """ at the beginning and end
    - These will have the string `STEP #: [Instructions]` with some context on what is going on
    - This will let you know what lines to uncomment, and what the python code is doing to interact with Launchdarkly


# Advanced Topics
- Python management
    - https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7
    - requirments.txt is what is going to keep track of the things we need to run this code
    - this venv will allows us to manage that more or less in a containted space
