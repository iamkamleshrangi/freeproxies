import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="freeproxies",
    version="0.0.1",
    author="Kamlesh Kumar Rangi",
    author_email="iamkamleshrangi@gmail.com",
    description="free proxies for humans",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamkamleshrangi/freeproxies",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
