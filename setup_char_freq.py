# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

properties = {'script': "char_freq.py",
              'icon_resources': [(0, "char_freq.ico")],
              'version': "1.0",
              'company_name': "labs @ PUT",
              'copyright': "Copyright 2013 Lukasz Banasiak. All rights reserved.",
              'name': "Character frequency analysis demo",
              'description': "In cryptanalysis, frequency analysis is the study of the frequency of letters or groups of letters in a ciphertext.",
              'author': "Lukasz Banasiak",
              'author_email': "lukasz@banasiak.me",
              'url': "http://banasiak.me",
              'license': "GPL"}

setup(options={'py2exe': {"compressed": 1,
                          "optimize": 2,
                          "bundle_files": 1}},

      console=[properties],
      zipfile=None,)
