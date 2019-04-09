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


"""

import docopt



if __name__ == '__main__':
    run()
