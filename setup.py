import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mulberry", # Replace with your own username
    version="0.0.1",
    author="Hunter Damron",
    author_email="hdamron1594@yahoo.com",
    description="Coordinate transformation tree with a focus on efficiency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hdamron17/mulberry",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
    python_requires=">=3.6",
)
