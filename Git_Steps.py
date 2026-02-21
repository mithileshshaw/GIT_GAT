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
       

2:05:30	Inviting another developer for contribution
		git switch main : first switch to main
2:07:10	git checkout -b feature_shaw_1 : feature_shaw_1 comes to same level of main
        git add .
        git commit -m "Added details 2:05:30 to 2:07:10"