Experiment 4: GitHub Collaboration Using Pull Requests

Steps and Commands:

1. Clone repository
git clone <repository-url>
cd Git_PullRequests

2. Create file in main branch
touch file1.txt
echo "This file is created in main branch" > file1.txt
git status
git add file1.txt
git commit -m "Initial commit in main"

3. Push changes
git push origin main

4. Pull latest changes
git pull origin main

5. Create feature branch
git branch feature-1
git checkout feature-1

6. Modify files in feature branch
echo "This change is from feature-1 branch" >> file1.txt
touch feature.txt
echo "Feature branch file" > feature.txt
git status
git add .
git commit -m "Changes done in feature-1"

7. Push feature branch
git push origin feature-1

8. Create Pull Request using GitHub UI
Compare & Pull Request
Review
Merge

9. Update local main after merge
git checkout main
git pull origin main

10. Verify commit history
git log --oneline
