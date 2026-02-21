    git status
    # git cofig --global user.email "mithilesh9shaw@gmail.com"
    # git --config --global user.name "mithilesh9shaw" or "mith_shaw" : existing one
    git init
39:00   .git is hidden folder we need to enable/disable it
        git status
42:15   git branch : Branch details
43:30   Initial commit is to register the master branch
        git add .
        git commit - m "initial commit"
        git branch : main
49:00   lets discuss every building blocks now
1:14:20 git commit : cand add message in actual file header or terminal header
1:21:10 New Branch will be created from head of the branch or latest commit
1:23:17 git log-
1:25:40 git log --oneline
1:35:20 .gitignore :- mention file name to avoid tracking some file under git initialised folder
1:35:50 git add .
        git status
1:38:40 Git dont track empty folder. It track folder with content only
        git status : run after creating empty folder and then after creating non empty folder
        bronze/ : adding in .gitignore to make untrack
1:42:00 .gitkeep : create .gitkeep file under silver folder to forcefully keeping track of non empty folder for future purpose
1:44:00 Brnaches details begins
        git branch
1:54:35 git switch main : always switch to main branch before creating any new branch 
        git checkout main : mainly used for multipurpose task like checking,switching branch etc. avoid using it for just switch

1:58:30 Working and Editing file on feature_mith_1 file begins from here
        git checkout -c feature_mith_1 or git switch -c feature_mith_1
		git branch
        git add .
        git commit -m "adding data on feature_mith_1"
        git log --online : 24095f1 (HEAD -> feature_mith_1) adding data on feature_mith_1
2:03:00 git switch main : head moves to main and the changes made in featue brnch disappers