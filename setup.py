from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
  long_description = f.read()

setup(
  name="py-carbone-connect",
  version="1.1.2", # This will be automatically updated by bump2version
  author="Raul B. Netto",
  author_email="raulbeni@gmail.com",
  description="A Python client for the Carbone API",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/Piuliss/py-carbone-connect",
  packages=find_packages(),
  classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Programming Language :: Python :: 3.10",
      "Programming Language :: Python :: 3.11",
  ],
  python_requires=">=3.7",
  install_requires=[
      "requests>=2.25.0",
  ],
  extras_require={
      "dev": [
          "pytest>=6.0",
          "pytest-cov>=2.0",
          "pytest-mock>=3.6",
          "black>=22.0",
          "isort>=5.0",
          "mypy>=0.900",
          "flake8>=3.9",
      ],
  },
  project_urls={
      "Bug Reports": "https://github.com/Piuliss/py-carbone-connect/issues",
      "Source": "https://github.com/Piuliss/py-carbone-connect",
  },
)