"""
Load the current version into the project
"""

import re
import subprocess

import toml


def run_command(command):
    """
    run a command on the system
    """
    return subprocess.run(command, stdout=subprocess.PIPE, text=True).stdout


# Load the pyproject.toml file
pyproject = toml.load("pyproject.toml")

# Get the version on git
version = run_command(["git", "tag", "-l", "--points-at", "HEAD"])
if version.startswith("v"):
    version = version[1:]

# find version from pdm if not found on git
if version == "":
    version = pyproject["project"]["version"]


# replace in file
with open("src/tcgdexsdk/__init__.py", "r+") as file:
    content = file.read()
    file.seek(0)

    # Use a regex to replace the existing __version__ variable
    new_content = re.sub(
        r'__version__ = ".*?"', f'__version__ = "{version.strip()}"', content
    )

    file.write(new_content)
    file.truncate()
