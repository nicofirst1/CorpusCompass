from setuptools import setup

# common requirements for all packages
common_requirements = ['pandas', 'numpy', "PySide6", 'nltk', 'matplotlib', 'statsmodels', 'scikit-learn', 'tqdm',
                       'nltk']

setup(
    name='CorpusCompass',
    version='3.0',
    description='Utilities tool for linguistic annotation',
    author="Nicolo' Brandizzi",
    author_email='brandizzi@diag.uniroma1.it',
    url='https://github.com/nicofirst1/CorpusCompass',
    install_requires=common_requirements,

)
