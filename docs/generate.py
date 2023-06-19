import shutil
import os

shutil.copy("../README.md", "sphinx/source/api/Introduction.md")

for file_ in os.listdir("../examples"):
    if ("document" in file_) or ("README" in file_):
        shutil.copy(
            "../examples/%s" % file_, os.path.join("sphinx/source/api/examples", file_)
        )
