import io
import re
from setuptools import setup

with io.open("state_machine/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)


setup(
    name="StateMachine",
    version=version,
    url="",
    author="Rafael S. Mueller",
    author_email="rafael.mueller1@gmail.com",
    description="",
    packages=["state_machine"],
    long_description=open("README.rst").read(), install_requires=['']
)
