testing from testingbranch

taken from https://gist.github.com/oshingc/9411880
//Get the project
git clone git@github.com:username/repositoryname.git

//Make changes to the project
//Problem! You made changes to the project beeing on master branch, how do you save those changes to a new branch?

//Save a stack
git stash

//Check actual file mode
git config core.fileMode

//Set file Mode to false
git config core.fileMode false

//fetch develop branch, make the branch appears
//set up to track remote branch develop from origin
git branch --track develop origin/develop

develop
*master

//change to the branch develop
git checkout develop

*develop 
master

//change to a new branch 'cambio'
git checkout -b cambio

*cambio
develop
master

//recover the changes we save on the stack to the branch cambio
git stash pop

//Prepare to commit
git add -A

git commit -m "we add constants"

//Check the state of fileMode, should be false
git config core.fileMode

false


//Push our branch cambio
git push origin cambio

//The next step is go to github.com and Create Pull Request
//Edit and select develop>cambio
//Send Pull Request
//Merge Pull Request
//END

//To delete a branch
git branch -D branch_to_delete

//Rename a branch
git branch -m oldname newname
//Rename current branch
git branch -m newname

//Merge conflicts
git mergetool

//Create or push a repository from command lines
1. Create local project (maven, spring)
2. git init
3. touch README.md
4. git add -A
5. git commit -m "first commit"
6. git remote add origin git@github.com:oshingc/AgendaInTheCloud.git (si no existe el repositorio en la nube, se creará)
7. git push -u origin master

//Recover an item from the queue git stash
git stash apply stash      # apply top of stash stack
git stash apply stash@{1}  # and mix in next stash stack entry too

Install p4merge tool

git config --global mergetool.p4merge.cmd "p4merge.exe \"$BASE\" \"$LOCAL\" \"$REMOTE\" \"$MERGED\""


How to update a fork


git remote add upstream https://github.com/whoever/whatever.git

# Fetch all the branches of that remote into remote-tracking branches,
# such as upstream/master:

git fetch upstream

# Make sure that you're on your master branch:

git checkout master

# Rewrite your master branch so that any commits of yours that
# aren't already in upstream/master are replayed on top of that
# other branch:

git rebase upstream/master

#see history
git log
gitk

#see dependency between branches
git lga
