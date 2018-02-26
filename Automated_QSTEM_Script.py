
# coding: utf-8

# In[4]:


"""
Written by Alex Rakowski

"""
# Load Depenendcies 
import glob
import os

# define the function 

def run_qstem_scripts():
    """loads all .qsc files, appends 'stem3 ' prefix and runs them. .cfg file must be in the same folder"""
    files = glob.glob("*.qsc")
    new_files = [("stem3 " + str(i)) for i in files]
    for f in new_files:
        os.system(f)
        print("finished " + f)
    print("done")



# In[ ]:


run_qstem_scripts()

