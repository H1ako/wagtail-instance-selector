from setuptools import setup

install_requires = ["django>=2.2.2", "wagtail>=2.15"]

__version__ = "3.0.5"

setup(
    name="wagtail-new-instance-selector",
    install_requires=install_requires,
    version=__version__,
    packages=["instance_selector"],
    include_package_data=True,
    description="A widget for Wagtail's admin that allows you to create and select related items",
    long_description="Documentation at https://github.com/H1ako/wagtail-instance-selector",
    author="The Interaction Consortium & Sobolev Nikita",
    author_email="nikita-sobolev-wd@yandex.ru",
    url="https://github.com/H1ako/wagtail-instance-selector",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Framework :: Wagtail :: 3",
        "Framework :: Wagtail :: 4",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
)
