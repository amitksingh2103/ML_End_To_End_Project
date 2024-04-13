from setuptools import find_packages, setup
from typing import List

EDITABLE_INSTALL_OPTION = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will help in installing the required libraries
    for this project to run'''
    requirements = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line and line != EDITABLE_INSTALL_OPTION:
                requirements.append(line)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Amit',
    author_email='amitksingh2103@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
