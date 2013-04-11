# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

properties = {'script': "Caesar.py",
              'icon_resources': [(0, "encryption.ico")],
              'version': "1.0",
              'company_name': "labs @ PUT",
              'copyright': "Copyright 2013 Lukasz Banasiak. All rights reserved.",
              'name': "Caeser Cipher demo",
              'description': "In cryptography a Caesar cipher is one of the simplest and most widely known encryption techniques",
              'author': "Lukasz Banasiak",
              'author_email': "lukasz@banasiak.me",
              'url': "http://banasiak.me",
              'license': "GPL"}

setup(options={'py2exe': {"compressed": 1,
                          "optimize": 2,
                          "bundle_files": 1}},

      console=[properties],
      zipfile=None,)
