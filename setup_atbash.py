# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

properties = {'script': "AtBash.py",
              'icon_resources': [(0, "encryption.ico")],
              'version': "1.1",
              'company_name': "labs @ PUT",
              'copyright': "Copyright 2013 Lukasz Banasiak. All rights reserved.",
              'name': "AtBash Cipher demo",
              'description': "Atbash is a simple substitution cipher for the Hebrew alphabet.",
              'author': "Lukasz Banasiak",
              'author_email': "lukasz@banasiak.me",
              'url': "http://banasiak.me",
              'license': "GPL"}

setup(options={'py2exe': {"compressed": 1,
                          "optimize": 2,
                          "bundle_files": 1}},

      console=[properties],
      zipfile=None,)
