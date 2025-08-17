from setuptools import find_packages,setup
from typing import List

requirements_list:List[str]=[]
def get_requirements()->List[str]:
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirements_list

setup(
    name="Network Security",
    version="0.0.1",
    author="Yuvraj Bansal",
    author_email="yuvrajbnsl@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)