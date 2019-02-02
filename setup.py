import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Sastrawize",
    version="1.0.1-F",
    author="Guedho Augnifico Mahardika",
    author_email="edho08@gmail.com",
    description="FAST Library for stemming Indonesian (Bahasa) text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)