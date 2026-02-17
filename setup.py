from setuptools import setup, find_packages

setup(
    name="server-creator",
    version="0.1.0",
    author="ERREKID-Things",
    description="A tool to quickly create a local server",
    # Esto busca automáticamente la carpeta 'server'
    packages=find_packages(), 
    # Aquí puedes añadir versiones de Python compatibles
    python_requires=">=3.6",
    install_requires=[
        # Como usas 'http.server' y 'socket', no necesitas librerías externas.
        # Si luego usas Flask, lo pondrías aquí abajo:
        # "flask",
    ],
)
