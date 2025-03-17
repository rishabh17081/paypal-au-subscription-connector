from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="paypal-au-subscription-connector",
    version="0.1.0",
    author="Rishabh Sharma",
    author_email="rishabhsharma1708@gmail.com",
    description="PayPal Account Updater Subscription Connector for MCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rishabh17081/paypal-au-subscription-connector",
    packages=find_packages(),
    py_modules=["paypal_au_subscription_mcp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
