import setuptools
REQUIRED = [
    "numpy>=1.21.4",
    "pandas>=1.3.4",
    "ShopifyAPI>=9.0.0",
    "requests",
    "fastapi>=0.70.0",
    "gspread>=5.0.0",
    "oauth2client>=4.1.3",
    "monday>=1.2.7",
    "python-dotenv>=0.19.2"
]
with open("README.md", "r") as file:
    LONG_DESCRIPTION = file.read()
setuptools.setup(
    name="pypal-api",
    version="0.1.6",
    author="Ivan Campos",
    description="A collection of helper functions to ease API development",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/IvanCampos11/PyPal-API",
    packages=['pypal_api'],
    python_requires=">=3.8",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
