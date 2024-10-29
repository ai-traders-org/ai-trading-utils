from setuptools import setup, find_packages

setup(
    name="ai_trading_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'boto3~=1.35.0',
        'pandas~=2.2.0'
    ],
    author="Bartosz Bok",
    author_email="bok.bartosz@gmail.com",
    description="utils for `ai-trading` project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ai-traders-org/ai-trading-utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.10',
)
