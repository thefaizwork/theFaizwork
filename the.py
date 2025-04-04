import os
import subprocess
import random
from datetime import datetime, timedelta

# Set your GitHub repository URL
GITHUB_REPO = "https://github.com/your-username/github-green-hack.git"

# Set up Git user (optional but recommended)
os.system('git config --global user.name "your-username"')
os.system('git config --global user.email "your-email@example.com"')

# Generate 1000 random past commit dates
for i in range(1000):  # 1000 commits to fully greenify the GitHub graph
    random_days_ago = random.randint(1, 365)  # Pick a random day in the past year
    commit_date = (datetime.now() - timedelta(days=random_days_ago)).strftime("%Y-%m-%d %H:%M:%S")
    
    with open("commit.txt", "a") as f:
        f.write(f"Commit {i + 1} on {commit_date}\n")

    os.system("git add commit.txt")
    os.environ["GIT_COMMITTER_DATE"] = commit_date
    subprocess.run(["git", "commit", "--date", commit_date, "-m", f"Commit {i + 1} on {commit_date}"])

# Push commits to GitHub
os.system("git branch -M main")
os.system("git remote add origin " + GITHUB_REPO)
os.system("git push -u origin main --force")

print("✅ Done! Check your GitHub profile now!")
