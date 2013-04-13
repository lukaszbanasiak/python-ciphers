# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import Bifid

properties = {'script': "Bifid.py",
              'icon_resources': [(0, "encryption.ico")],
              'version': Bifid.__version__,
              'company_name': "labs @ PUT",
              'copyright': "Copyright 2013 Lukasz Banasiak. All rights reserved.",
              'name': "Bifid cipher demo",
              'description': "Bifid cipher is a cipher which combines the Polybius square with transposition, and uses fractionation to achieve diffusion.",
              'author': "Lukasz Banasiak",
              'author_email': "lukasz@banasiak.me",
              'url': "http://banasiak.me",
              'license': "GPL"}

setup(options={'py2exe': {"compressed": 1,
                          "optimize": 2,
                          "bundle_files": 1}},

      console=[properties],
      zipfile=None,)
