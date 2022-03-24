import git
import os
import sys
import ctypes
from git import Repo
import tkinter as tk
from tkinter import simpledialog

cwd = os.getcwd()
local_repo = Repo(path=cwd)
local_branch = local_repo.active_branch.name
g = git.cmd.Git(cwd)

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
commit_message = simpledialog.askstring(title="Git",
                                        prompt="Commit message:")


g.execute("git add -A")
try:
    g.execute("git commit -m \"" + commit_message + "\"")
except:
    ctypes.windll.user32.MessageBoxW(
        0, u"Nothing to commit, working tree clean.", u"Info", 0)
    sys.exit()

command = "git push origin " + local_branch
g.execute(command)

ctypes.windll.user32.MessageBoxW(
    0, u"Active branch "+local_branch+" is pushed to origin/"+local_branch, u"Info", 0)
