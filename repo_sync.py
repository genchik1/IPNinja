"""
repo_sync

Основной модуль для работы с репозиторием https://github.com/firehol/blocklist-ipsets

Created at 12.10.2020 by genchik1.
Project IPNinja

Примеры использования:

TODO

"""

__author__ = 'genchik1'
__maintainer__ = 'genchik1'
__status__ = "Development"
__copyright__ = "MIT"

__version__ = "20201012"


import os
import settings as s
from subprocess import run

import git
from unidiff import PatchSet


class RepoSync:
    def __init__(self):
        self.git_blocklist = 'https://github.com/firehol/blocklist-ipsets'
        self.repo_path = s.REPO_PATH

    def clone_repo(self):
        try:
            git.Repo.clone_from(self.git_blocklist,
                                self.repo_path, branch='master')
        except:
            print('Error cloned')

    def diff(self):

        repo = git.cmd.Git(self.repo_path)
        repo.checkout("master")
        repo.fetch("origin")
        diff_stdout = repo.execute(
            ["git", "diff", "master", "origin/master"], True).split("\n")

        udiff = PatchSet(diff_stdout)
        repo.execute(["git", "reset", "--hard", "origin/master"])
        repo.merge()

        return udiff
