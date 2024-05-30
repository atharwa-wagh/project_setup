from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements.txt
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements] # we write each library on a new line, so while reading \n gets added, so we are replacing it with blank

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
name = 'Project setup',
version = '0.0.1',
author = 'Atharwa',
packages = find_packages(),
install_requires = get_requirements('requirements.txt') # take packages from the requirements.txt file
)