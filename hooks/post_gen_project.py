from pathlib import Path
from subprocess import run, CalledProcessError
import shlex

import virtualenv
import os


pkg_name = '{{ cookiecutter.package_name }}'
repo = '{{ cookiecutter.url }}'


def clean_up_docopt():
    """If click is selected, remove docopt-specific files."""
    cli_tool = '{{ cookiecutter.cli_tool}}'
    if cli_tool != "docopt":
        to_remove = Path.cwd() / pkg_name / 'from_docopt.py'
        to_remove.unlink()


def set_markup_style():
    """Use either markdown or org-mode as the default markup language."""
    markup_language = '{{ cookiecutter.markup_language }}'
    if markup_language == "org":
        to_remove = Path.cwd() / 'README.md'
        to_remove.unlink()
    elif markup_language == "markdown":
        to_remove = Path.cwd() / 'README.org'
        to_remove.unlink()


#def install_deps():
#    """Install dependencies """
#    venv_dir = "venv"
#    virtualenv.create_environment(venv_dir)
#
#    #pip_dev = run('pip install -r requirements.txt'.split(), check=True)
#    #print('Installed dependencies and virtual environment.')
#    pass


def init_repo():
    """Initialize a git repository for this project."""
    print(f"Initializing development environment for {pkg_name}")
    try:
        git_init = run('git init .'.split(), check=True)
        print('Initialized git repository')
        if repo:
            git_add_remote = run(f'git remote add origin {repo}'.split(), check=True)
            print(f'Found url, set origin: {repo}')
        git_add = run('git add -A'.split(), check=True)
        git_commit = run(shlex.split(f'git commit -m "first commit of {pkg_name} "'), check=True)
        git_tag = run(shlex.split('git tag -a -m "first tag" 0.0.1'), check=True)
        print('Installed package in development mode.')
        git_add_after = run('git add -A'.split(), check=True)
        git_commit_after = run(shlex.split('git commit -m "added versioneer support."'), check=True)
        print('second commit.')
        print('All set!')
    except CalledProcessError as e:
        print(e)


def main():
    clean_up_docopt()
    set_markup_style()

#    install_deps()
    init_repo()


if __name__ == "__main__":
    main()
