from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='mge_graphql',
    version='1.1.0',
    license='BSD 3-Clause "New" or "Revised"',
    author="Alexandru Plesoiu",
    author_email='alexandru@mgesoftware.com',
    description="GraphQL support with data validations, error handle and permission support built on top of graphene.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["examples*"]),
    url='https://github.com/mgesoftware/mge-graphql',
    keywords='api graphene mongodb flask graphql mge_graphql mge-graphql rest relay mgesoftware mge',
    install_requires=[
          'graphene',
      ],
    project_urls= {
        "Documentation": "https://mge-graphql.readthedocs.io/en/latest/",
        "Source": "https://github.com/mgesoftware/mge-graphql",
        "Tracker": "https://github.com/mgesoftware/mge-graphql/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)