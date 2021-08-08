from setuptools import setup
setup(
    name = 'typercli',
    version = '0.0.1',
    packages = ['typerclitest'],
    #url='python repo url'
    install_requires=[
        'typer == 0.3.2'
        #'click==7.1.1'
    ],
    entry_points = {
        'console_scripts': [
            'typerclitest = typerclitest.__main__:app'
        ]
    })
        
    #pip install wheel
    #python setup.py sdist bdist_wheel
        
   
    #pip3 install typercli
    
