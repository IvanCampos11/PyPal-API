import setuptools
REQUIRED = [
    "numpy",
    "pandas",
    "ShopifyAPI",
    "fastapi",
    "gspread",
    "oauth2client",
    "monday",
    "requests",
    "python-dotenv"
]
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
setuptools.setup(
    name="pypal-api",
    version="0.1.1",
    author="Ivan Campos",
    description="A collection of helper functions to ease API development",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/IvanCampos11/PyPal-API",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)