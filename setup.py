from setuptools import setup, find_packages

DESCRIPTION = 'Lib que facilita a vida de quem trabalham com Nota Fiscal de Serviços Eletrônica (NFS-e)'

LONG_DESCRIPTION = '''
A PyNFSe realiza todos os passos para quem trabalha com NFS-e:

- Cria os XMLs de RPS (Recibo Provisório de Serviço) e dos Lotes RPS. Tudo devidamente assinado :)

- Realiza a comunicação com o webservice da respectiva prefeitura, enviando lotes RPSs, consultando e cancelando NFS-es...

Enfim, a PyNFSe faz todo o trabalho duro :)

Prefeituras suportadas:
- Curitiba/PR
- Mais em breve :)
'''

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Other Audience',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Natural Language :: Portuguese (Brazilian)',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.5',
    'Topic :: Office/Business :: Financial',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities',
]

INSTALL_REQUIREMENTS = [
    'PyXB>=1.2.5',
    'lxml',
    'zeep',
    'signxml',
]

setup(
    name='PyNFSe',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license='GNU General Public License v3 or later (GPLv3+)',
    platforms='any',
    version='0.1.0',
    url='https://github.com/marcelobelli/PyNFSe',
    author='Marcelo Belli',
    author_email='marcelo@belli.me',
    packages=find_packages(exclude=['test*']),
    install_requires=INSTALL_REQUIREMENTS,
    test_suite='tests',
    classifiers=CLASSIFIERS,
)
