#! -*- coding: utf-8 -*-

"""
releaseinator is a quick but hopefully useful script to 
help pushout and release python packages. It needs to work with mkrepo
and somehow 'validate and clean up' packages to meet best practise, and
will need to use twine to push code up to pypi and push changes to git.

Validation checks
-----------------

[ ] Series of validation checks 
[ ] do docs exist in readthedocs.org?
[ ] LICENCE, AUTHORS, etc etc


Versions and releases
[ ] Handle updating the VERSION file for a 'bump'
[ ] each commit builds a version x.x.x-RevisionNumber but we only do public releases on x.x.y
[ ] generate release notes and add them to docs
[ ] build a new wheel and push to pypi 

How to release a pacakge (ie todoinator)

* have git repo clean 
* bump version
* push to pypi


"""

import docopt
import semver
import os
import subprocess

def bump_version(repopath):
    """Visit `repopath` and find a VERSION file, 
    increase that semver by one.

    """
    versionpath = os.path.join(repopath, "VERSION")
    try:
        with open(versionpath) as fo:
            ver = fo.read()
    except:
        print("Unable to find / open VERSION file {}".format(versionpath))
    try:
        nextver = semver.bump_patch(ver)
    except ValueError:
        print("The version in {} {} is not valid semver".format(versionpath, ver))
        
    print("TO bump patch use {}".format(nextver))

def push_to_pypi(repopath):
    """
* sudo pip install twine
 Install to test location
 sudo python setup.py bdist_wheel 
 python -m twine upload --repository-url=https://test.pypi.org/legacy/ dist/<nameofwheel>

 (username and password - ignore kde wallet request?)


real repositry is upload.pypi.org


    """
    #bump version ok
    #rm-rf build/ dist/
    #python setup.py bdist_wheel
    #python -m twine upload --repository-url=https://upload.pypi.org/legacy/ dist/<nameofwheel>
    pass

    
if __name__ == '__main__':
    bump_version("/var/projects/todoinator")
