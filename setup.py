from setuptools import find_packages,setup

HYPEN_E_dot  = '-e .'
def get_req(filename):
    req = []
    with open (filename,'r') as file:
        line = file.readlines()
        for i in line:
            l = i.strip()
            if(l==HYPEN_E_dot):
                pass
            else:
                req.append(l)
    return req



setup(
    name='student Life Cycle',
    author='Deepraj',
    author_email='work.deepraj@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
)