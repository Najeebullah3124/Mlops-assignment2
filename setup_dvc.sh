#!/bin/bash
# DVC Setup Script
# Run this script after installing DVC: pip install dvc

echo "Initializing DVC..."
dvc init

echo "Adding DVC remote..."
dvc remote add -d myremote ./dvcstore

echo "Adding dataset to DVC..."
dvc add data/dataset.csv

echo "Staging DVC files..."
git add data/.gitignore data/dataset.csv.dvc .dvc .dvcignore

echo "Creating DVC pipeline..."
dvc run -n train_model \
  -d src/train.py \
  -d data/dataset.csv \
  -o models/model.pkl \
  python src/train.py

echo "Staging pipeline files..."
git add dvc.yaml dvc.lock

echo "Setup complete!"
echo "Next steps:"
echo "1. Review the changes: git status"
echo "2. Commit: git commit -m 'Add dataset with DVC and training pipeline'"

