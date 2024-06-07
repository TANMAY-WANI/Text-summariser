from setuptools import setup, find_packages

setup(
    name='textSummarizer',
    version='0.1.0',
    author='Tanmay Wani',
    author_email='tanmaywani145@gmail.com',
    description='A text summarizer NLP project',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    url="https://github.com/TANMAY-WANI/Text-summarizer"
)
