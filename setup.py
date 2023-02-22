from setuptools import setup

# common requirements for all packages
common_requirements = ['pandas', 'numpy']

setup(
    name='CorpusCompass',
    version='2.0',
    description='Utilities tool for linguistic annotation',
    author="Nicolo' Brandizzi",
    author_email='brandizzi@diag.uniroma1.it',
    url='https://github.com/nicofirst1/CorpusCompass',
    install_requires=common_requirements,
    packages=[
        'annotation_fixer',
        'dataset_analyzer',
        'dataset_creator',
    ],
    extras_require={
        'annotation_fixer': ['PySide6'],
        'dataset_analyzer': ['nltk', 'matplotlib', 'statsmodels', 'scikit-learn'],
        'dataset_creator': ['tqdm', 'nltk']
    }
)
