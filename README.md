# MLOps Project - Lab 15

This project demonstrates MLOps practices using Git and DVC (Data Version Control).

## Project Structure

```
Mlops-Project/
├── data/              # Dataset files (tracked by DVC)
├── src/               # Source code
│   └── train.py      # Training script
├── models/            # Trained models
├── .gitignore        # Git ignore rules
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Initialize DVC

```bash
# Initialize DVC
dvc init

# Add remote storage
dvc remote add -d myremote ./dvcstore
```

### 3. Track Dataset with DVC

```bash
# Add dataset to DVC
dvc add data/dataset.csv

# Stage DVC files
git add data/.gitignore data/dataset.csv.dvc
git commit -m "Add dataset with DVC"
```

### 4. Create Training Pipeline

```bash
# Create DVC pipeline
dvc run -n train_model \
  -d src/train.py \
  -d data/dataset.csv \
  -o models/model.pkl \
  python src/train.py

# Stage pipeline files
git add dvc.yaml dvc.lock
git commit -m "Add training pipeline"
```

## Running the Training Script

You can run the training script directly:

```bash
python src/train.py
```

Or use DVC to run the pipeline:

```bash
dvc repro train_model
```

## DVC Commands Reference

- `dvc status` - Check status of data files
- `dvc push` - Push data to remote storage
- `dvc pull` - Pull data from remote storage
- `dvc repro` - Reproduce pipeline
- `dvc dag` - Show pipeline dependency graph

