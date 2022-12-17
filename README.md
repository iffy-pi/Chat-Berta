# Chat-Berta
Chat-Berta Project File.

This also serves as the repository for ELEC498 Group 12 (JISH)

## Directory Information:
This entire repository is used to package the web application for Chat-Berta. This means most of the files here are all useful for the web server.

deploy-web-server.md contains information on how to deploy the web server (during its initial creation) and is archived as a good source of informaiton.

git-pr.bat is a simple batch script that streamlinees the opening of pull requests for the application.

server-void/ contains files and folders that are not relevant to the web server. That is the web server can be deployed without the files in this folder. **All files required by the server can NEVER be put in server-void/**

# Development Pipeline for Non Web App Changes
If you are making changes to files that are not used in the web application, e.g. prototype files or files in the server-void/ folder, then you can use the simple git change pipleine.

That is, git commit and git push.

# Development Pipeline for Web App Changes
This is intended to cover the general steps for making changes to the app or is its sub files.

First start up the virtual environment using:
```
venv\Scripts\activate.bat
```

## Simple Changes
This is for simple changes that we are **100% sure do not need extensive verification**. This would be something as simple as a character change. For more extensive changes, refer to the Big Changes section.

### Pull Latest Changes from mainline
Switch to mainline branch if you are not on there already:
```
git checkout main
```

Then pull:
```
git pull
```
### Change The Application Source Code
This can be any amount of changes we want, in this case we just do a simple change to the network message.

Note that whenever you install new packages, be sure to reupdate the requirements file with:
```
pip freeze > requirements.txt
```

### Test on the development server
Run the application with `python app.py` to test your changes on a developmental server.

### Commit Changes
Commit whatever changes you made to the branch you are working on.
```
git commit app.py -m "Simple test change!"
```
Make as many commits as you need.

### Push Commits To Main Branch
Push all your commits by using the command:
```
git push
```

### Deploy to Heroku (Can Only Be Done By Iffy)
Push to the Heroku remote.
```
git push heroku main
```
If you are not Iffy, contact iffy to push changes to the Heroku repository.



## Big Changes
### Pull Latest Changes from mainline
Switch to mainline branch if you are not on there already:
```
git checkout main
```

Then pull
```
git pull
```

### Create Developmental Branch
Create a new development branch of the current branch (main) with a descriptive name
```
git checkout -b iffy-sample-dev-branch
```

**Make sure to always include your name as the first part of the branch name**

Branches allow you to continue experimental work without interfering with the working code in mainline.

### Change The Application Source Code
This can be any amount of changes we want, in this case we just do a simple change to the network message.

Note that whenever you install new packages, be sure to reupdate the requirements file with:
```
pip freeze > requirements.txt
```

### Test on the development server
Run the application with `python app.py` to test your changes on a developmental server.

### Commit Changes
Commit whatever changes you made to the branch you are working on.
```
git commit app.py -m "Simple test change!"
```
Make as many commits as you need.

### Push Branch
Push all your commits by using the command:
```
git push
```
Note: You can make more commits and push as usual until you are ready to merge with the main branch.

### Merge With Main
Merge your branch with the mainline by initiating a pull request, this can be done using the added utility git-pr.bat:
```
git-pr.bat
```
Enter `Y` to open a pull request and make sure to select `main` as the branch to merge with.
Ideally, we should review merges to the mainline, but this may not be guaranteed.

### Deploy to Heroku (Can Only Be Done By Iffy)
Go back to the main branch and pull changes from the remote and then push to the Heroku remote.
```
git checkout main
git push heroku main
```
If you are not Iffy, contact iffy to push changes to the Heroku repository.