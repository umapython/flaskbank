rm -rf .git

git init
git add .
git commit -m "first commit"
git remote add origin "remote url"
If the GitHub repo has seen new commits pushed to it, while you were working locally, I would advise using:
git pull --rebase origin main
git push origin main