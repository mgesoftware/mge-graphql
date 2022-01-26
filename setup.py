from setuptools import setup, find_packages


setup(
    name='mge_graphql',
    version='1.0',
    license='BSD 3-Clause "New" or "Revised"',
    author="Alexandru Plesoiu",
    author_email='alexandru@mgesoftware.com',
    packages=find_packages(exclude=["examples*"]),
    url='https://github.com/mgesoftware/mge-graphql',
    keywords='graphene mongodb flask graphql mge_graphql',
    install_requires=[
          'graphene',
      ],
)