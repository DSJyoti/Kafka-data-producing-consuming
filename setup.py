from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME="kafka"
VERSION="0.0.1"
AUTHOR="DSJyoti"
DESCRIPTION="THIS IS A SAMPLE PROJECT TO CONSUME DATA FROM KAFKA"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list()-> List[str]:
    """
    Description: This function is going to return list of requiremnts mention in requirements.txt file"""
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readlines()
        requirements_list=[requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requiremnt_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)            
