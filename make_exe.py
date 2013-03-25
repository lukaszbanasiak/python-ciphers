from distutils.core import setup
import py2exe

setup(name = "Caeser Cipher",
      version = "0.1",
      options = {"py2exe" : {"compressed" : 1,
                             "optimize" : 2,
                             "bundle_files" : 1 }},

      console=[{'script': 'caesar.py',
               "icon_resources": [(0, "encryption.ico")]
               }],
      zipfile = None,
      description = "Szyfr Cezara",
      author = "Lukasz Banasiak",
      author_email ="lukasz@banasiak.me",
      license = "GPL",
      url = "http://banasiak.me"
      )
