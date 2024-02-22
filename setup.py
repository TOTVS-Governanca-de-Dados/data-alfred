from setuptools import setup, find_packages

setup(
    name='data-alfred',
    version='0.1.0',
    author='Alestan Alves',
    author_email='alestan.silva@totvs.com.br',
    description='This is a package for creating a data science project structure',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TOTVS-Privacidade-de-Dados/data-alfred',
    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
