#!/bin/bash
# Script to push code to GitHub
# Usage: ./push_to_github.sh <your-github-repo-url>

if [ -z "$1" ]; then
    echo "Usage: ./push_to_github.sh <your-github-repo-url>"
    echo "Example: ./push_to_github.sh https://github.com/yourusername/mlops-project.git"
    exit 1
fi

REPO_URL="$1"

echo "=== Pushing to GitHub ==="
echo "Repository: $REPO_URL"
echo ""

# Check if remote already exists
if git remote get-url origin &>/dev/null; then
    echo "Remote 'origin' already exists. Updating..."
    git remote set-url origin "$REPO_URL"
else
    echo "Adding remote 'origin'..."
    git remote add origin "$REPO_URL"
fi

# Push to GitHub
echo ""
echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo "Repository URL: $REPO_URL"
else
    echo ""
    echo "❌ Push failed. Please check:"
    echo "  1. GitHub repository exists"
    echo "  2. You have push permissions"
    echo "  3. You're authenticated (git credential helper or SSH key)"
fi

