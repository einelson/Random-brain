from setuptools import setup

setup(name='random_brain',
    version='0.1.0',
    description='Python Random Brain Module',

    author='Ethan Nelson',
    author_email='ethanisaacnelson@gmail.com',
    url='https://github.com/einelson/Random-brain',
    packages=['random_brain'],
    install_requires=['numpy', 'keras'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved:: MIT License",
        "Operating System :: OS Independent",
        ],
)