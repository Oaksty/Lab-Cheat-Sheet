Directory Navigation

cd                # Show current directory

cd <folder>       # Enter a folder

cd ..             # Go up one folder

mkdir <folder>    # Create a new folder



⚙️ Git Configuration \& Repository Setup

git config --list            # View Git configuration

git init                     # Initialize a new Git repository

git remote add origin <url>  # Link local repo to GitHub

git remote set-url origin {URL} #change to new repo

git remote -v                # View remote repository URLs



🔍 Checking Repository Status \& Differences

git status   # Track changed and untracked files

git diff     # Show detailed unstaged changes



✏️ Adding \& Committing Files

git add <file>               # Stage a file to commit

git commit                   # Commit staged files (opens editor)

git commit -m "message"      # Commit with a custom message



🌿 Branching \& Merging

git branch                   # List all branches

git branch <name>            # Create a new branch

git checkout <name>          # Switch to a branch

git merge <branch>           # Merge branch into current one



🚀 Pushing to GitHub

git push                                # Push commits to GitHub

git push --set-upstream origin master   # First push to remote

git push -u origin                      # Set tracking to origin

git push origin <tag>                   # Push a specific tag



🏷 Tagging Releases

git tag -a v1.0 -m "Initial release"    # Create annotated tag

git push origin v1.0                    # Upload tag to GitHub



📦 Git Submodules

git submodule add <repo-url>        # Add an external repo as a submodule

git clone <repo-url>                #clone the files into your local device

