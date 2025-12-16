# Setup Guide - Lab 15 Tasks

## ✅ Task 1.1 - Project Setup (COMPLETED)

### What's Been Done:
- ✅ Git repository initialized
- ✅ `.gitignore` file created
- ✅ Project structure created:
  - `data/` - for datasets
  - `src/` - for source code
  - `models/` - for trained models
- ✅ `requirements.txt` created with dependencies
- ✅ Sample dataset created at `data/dataset.csv`
- ✅ Training script created at `src/train.py`

### Screenshots Needed:
1. **Folder Structure**: Run `tree -L 2` or `find . -maxdepth 2` to show structure
2. **Git Init Output**: Already initialized (see git status)

### Next Steps:
```bash
# Install Python dependencies (if not already installed)
pip install -r requirements.txt

# Stage initial files
git add .gitignore requirements.txt src/ README.md
git commit -m "Initial project setup"
```

---

## 📋 Task 1.2 - Initialize DVC (TO RUN)

### Commands to Execute:

```bash
# 1. Install DVC (if not installed)
pip install dvc

# 2. Initialize DVC
dvc init

# 3. Add remote storage
dvc remote add -d myremote ./dvcstore

# 4. Track dataset with DVC
dvc add data/dataset.csv

# 5. Stage DVC files
git add data/.gitignore data/dataset.csv.dvc .dvc .dvcignore

# 6. Commit
git commit -m "Add dataset with DVC"
```

### Screenshots Needed:
1. **DVC commands output** - Screenshot of `dvc init` and `dvc add` commands
2. **`.dvc` file** - Screenshot of `data/dataset.csv.dvc` file
3. **DVC status** - Run `dvc status` and screenshot the output

### Alternative: Use the setup script
```bash
chmod +x setup_dvc.sh
./setup_dvc.sh
```

---

## 📋 Task 1.3 - Create Training Pipeline (TO RUN)

### Commands to Execute:

```bash
# Create DVC pipeline
dvc run -n train_model \
  -d src/train.py \
  -d data/dataset.csv \
  -o models/model.pkl \
  python src/train.py

# Stage pipeline files
git add dvc.yaml dvc.lock

# Commit pipeline
git commit -m "Add training pipeline"
```

### Screenshots Needed:
1. **Successful DVC pipeline run** - Screenshot of `dvc run` command output
2. **dvc.yaml file** - Screenshot of the generated `dvc.yaml` file

### Verify Pipeline:
```bash
# Check pipeline status
dvc status

# Reproduce pipeline
dvc repro train_model

# View pipeline graph
dvc dag
```

---

## Quick Reference

### Project Structure:
```
Mlops-Project/
├── .git/              # Git repository
├── .gitignore         # Git ignore rules
├── data/
│   ├── .gitkeep
│   └── dataset.csv    # Dataset (will be tracked by DVC)
├── src/
│   └── train.py       # Training script
├── models/
│   ├── .gitkeep
│   └── model.pkl      # Trained model (output of pipeline)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── setup_dvc.sh       # DVC setup script
```

### Useful Commands:
- `git status` - Check git status
- `dvc status` - Check DVC status
- `dvc repro` - Reproduce pipeline
- `dvc dag` - Show pipeline dependency graph
- `python src/train.py` - Run training script directly

