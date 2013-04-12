# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import Polybius

properties = {'script': "Polybius.py",
              'icon_resources': [(0, "encryption.ico")],
              'version': Polybius.__version__,
              'company_name': "labs @ PUT",
              'copyright': "Copyright 2013 Lukasz Banasiak. All rights reserved.",
              'name': "Polybius square demo",
              'description': "In cryptography, the Polybius square is a device for fractionating plaintext characters.",
              'author': "Lukasz Banasiak",
              'author_email': "lukasz@banasiak.me",
              'url': "http://banasiak.me",
              'license': "GPL"}

setup(options={'py2exe': {"compressed": 1,
                          "optimize": 2,
                          "bundle_files": 1}},

      console=[properties],
      zipfile=None,)
