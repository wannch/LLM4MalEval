from setuptools import setup
from setuptools.command.install import install  # Import the correct install class
import subprocess
import os

PACKAGE_NAME = 'formatter-test-package'  # Replace with your actual package name

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # Call the parent install function
        install.run(self)
        
        # Post-install actions
        os.environ['PACKAGE_NAME'] = PACKAGE_NAME
        subprocess.call(["python", "-m", f"{PACKAGE_NAME}.utils.analyze"])

setup(
    name=PACKAGE_NAME,
    version='0.0.1',
    packages=[PACKAGE_NAME, f"{PACKAGE_NAME}.utils"],
    install_requires=[
        'requests>=2.20.0',   # Ensures that 'requests' is installed
        'psutil>=5.8.0',      # Ensures that 'psutil' is installed
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
)