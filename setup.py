from setuptools import find_packages,setup
from typing import List


hyphen_e_dot='-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will import requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #when we will add requirements \n will be added 
        # so we make next list comprehension
        requirements=[req.replace("\n","") for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements


setup(
name='ML_Project',
version='0.01',
author='ani',
author_email='itsaniruddha1999@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)