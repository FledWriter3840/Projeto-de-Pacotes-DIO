from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Projeto de Pacotes DIO",
    version="0.0.1",
    author="Matheus de Souza Soares",
    author_email="desouzasoaresmatheus@gmail.com",
    description="Gera senhas seguras e avalia sua força",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FledWriter3840/Projeto-de-Pacotes-DIO"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)