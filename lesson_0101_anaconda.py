#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:36:37 2021

@author: fennieliang
"""

#Anaconda installation
    #Windows: https://docs.anaconda.com/anaconda/install/windows/
    #MacOS: https://docs.anaconda.com/anaconda/install/mac-os/
    #Documentation for installation https://docs.anaconda.com/anaconda/
    #Terminal commands: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands  


#Anaconda-Navigator 
    #Home >> include a set of software
    #Environments >> shows a list of created virtual environments 
    #Learning  >>  provides many learning resources
    #Community >> join some of your preferred communities to gather 
    #information, learn new technologies, chat about encountered problems
   
#Home
    #install or launch different software available on the display
    
#Environments 
    #a list of created virtual environments shows on the second column 
    #a virtual environment can be created or removed using the bottom icons
    
    #manually create a VM:
    #    conda create -n NLP
    #    conda activate NLP
    #    deactivate a VM: at current vm type "conda deactivate"
    #    remove a VM: conda env remove -n NLP
    #practice: create a new VM called test and see what happens aftward
    
    
    #the third column shows the packages available for the 
    #newly created virtual environment
    #click the drop-down menu on the top of the third column; 
    #you can view different categories of
    #installed, not installed, updatable, selected and all packages  
    
    #practice: click on the blue arrow on python, which shows version 3.8. 
    #to update the python version to the current 3.9
    
    #for installing a new package, from the search box, type the package's name 
    #if found, then click on the box and click the apply button 
    #on the right bottom 
    
    #practice: install two new packages named numpy then pandas. 
     
    #using the anaconda navigator for installing new packages 
    #is a better way to allow 
    #anaconda collecting suitable dependencies for the current VM
    #after the installation, click on the top "update index" button 
    #to update the index in the current VM
    
    #now check if you have pip, conda, python on the installed list and 
    #let me know the versions
     
    
#Manually create new environment and install packages
    #click Environments >> select base(root) virtual machine 
    #(should be available after anaconda-navigator installation)
    #click the green triangle beside the VM then select "open terminal"
    #from the termial type "pip --help" 
    #from the termial type "conda --help" 
    #conda create -n test (check what happens)
   

