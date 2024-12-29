import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ft_package",
    version="0.0.1",
    author="eagle",
    author_email="eagle@42.fr",
    description="A sample test package",
    url="https://github.com/eagle/ft_package",
    download_url="https://github.com/eagle/\
ft_package/archive/refs/tags/v0.0.1.tar.gz",
    maintainer="eagle",
    maintainer_email="eagle@42.fr",
    license="MIT",
    keywords=["sample", "package"],
    platforms=["unix", "linux", "windows"],
    packages=setuptools.find_packages(),
    include_package_data=True
)
