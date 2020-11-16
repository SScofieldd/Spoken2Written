#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
	  name = 'spoken2written',
      packages = ['spoken2written'],
      version='0.1',
      description='Convert Spoken English given as text to Written English ',
      author='Roshan Singh',
      author_email='roshansingh82333@gmail.com',
      url='https://github.com/SScofieldd/Spoken2Written',
      classifiers = [
     					 'Intended Audience :: Developers',
      					'Programming Language :: Python'
  				]

     )


# In[ ]:




