import itertools
import subprocess
from pathlib import Path
import os
import sys

if __name__ == "__main__":
    my_sha = "333cdb8c03fd2b2fa37d9333cc31dcd88b3a9b32"
    print(sys.argv)
    # x = subprocess.run(["git", "log", "--format=format:%H"], stdout=subprocess.PIPE)
    # res = len(list(itertools.takewhile(lambda sha: sha != my_sha, x.stdout.decode("utf-8").split("\n"))))
    # print(res)

    # repo_dir = Path.cwd()
    # repo_dir = repo_dir.parent.parent
    # print(repo_dir)
    # repo = git.Repo(repo_dir)
    # # commits = itertools.takewhile(lambda _: True, repo.iter_commits("main"))
    # print(os.environ["before"])
    # commits = list(repo.iter_commits("main"))
    # for c in commits:
    #     print(c.hexsha)

    # # print(os.environ["before"])
