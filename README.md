# 📦 DVC + Git Practice Project (Data & Model Versioning)

This repository is a **learning project** to understand how **Git** and **DVC (Data Version Control)** work together to version:

- Code  
- Datasets  
- Machine Learning models  

### 🎯 Goals
- Track multiple versions of data and models  
- Switch between versions safely  
- Store large files outside Git  
- Reproduce exact versions using Git + DVC  

---

## 🧠 Core Concept

- **Git** → tracks code and metadata  
- **DVC** → tracks actual data and models  
- **Branches / commits** → represent different ML versions (`v1`, `v2`, etc.)

---

## 📁 Files & Folders Explained

| File / Folder | Created by | What it is | Why it exists / What it teaches |
|--------------|-----------|------------|----------------------------------|
| `.git/` | Git | Git internal directory | Stores commits, branches, HEAD, and history |
| `.dvc/` | DVC | DVC configuration directory | Enables DVC inside the Git repository |
| `.dvc/config` | DVC | DVC config file | Stores DVC remote (where data/models are stored) |
| `.dvc/.gitignore` | DVC | Ignore rules | Prevents DVC cache files from being tracked by Git |
| `.dvcignore` | DVC | DVC ignore file | Tells DVC which files not to track |
| `.gitignore` | Git + DVC | Git ignore file | Prevents large data/model files from being committed |
| `Linear_Regression_Data.csv` | You | Dataset | Real data used for training |
| `Linear_Regression_Data.csv.dvc` | DVC | Data pointer file | Links a Git commit to an exact dataset version |
| `model.pkl` | You | Trained ML model | Output of model training |
| `model.pkl.dvc` | DVC | Model pointer file | Enables model versioning |
| `training.py` | You | Training script | Code that generates the model |
| `alter_data.py` | You | Data modification script | Used to create new dataset versions |
| `commands_to_fetch_any_version` | You | Notes / helper file | Reference for Git + DVC commands |
| `dvc_storage/` | DVC | DVC remote storage | Stores actual data and model files |
| `master` branch | Git | Main branch | Represents latest version (v2) |
| `v1` branch | Git | Version branch | Represents stable version 1 |
| Git commit | Git | Snapshot | Points to exact code + `.dvc` files |
| DVC cache | DVC | Local cache | Speeds up restore and version switching |

---

## Step 1: Initialize Git & DVC

```bash
git init
python -m dvc init
```
- Creates a Git repository
- Enables DVC tracking
- Adds the .dvc/ configuration folder

## Step 2: Track Dataset (Version 1)

```bash
python -m dvc add Linear_Regression_Data.csv
git add Linear_Regression_Data.csv.dvc .gitignore
git commit -m "this is the v1 of data"
```
- Dataset is stored in the DVC cache
- .dvc file stores a hash (pointer) to the data
- Git tracks only the .dvc file, not the actual dataset


## Step 3: Track Model (Version 1)

```bash
python -m dvc add model.pkl
git add model.pkl.dvc
git add training.py alter_data.py commands_to_fetch_any_version
git commit -m "this is v1"
```
- Model is versioned with DVC
- Code is versioned with Git


## Step 4: Create Version 2 (Data + Model Change)

```bash
python -m dvc add Linear_Regression_Data.csv
python -m dvc add model.pkl
git add .
git commit -m "this is the v2"
```
- v1 → old data + old model
- v2 → updated data + updated model


## Step 5: View Commit History

```bash
git log --oneline
```


## Step 6: Go Back to Version 1 (Detached HEAD)

```bash
git checkout ca6512c
dvc pull
```
- Switches Git metadata to v1
- Restores v1 dataset and model using DVC


## Step 7: Create a Branch for v1

```bash
git checkout master
git checkout -b v1 ca6512c
```
- master → v2
- v1 → stable version 1


## Step 8: Add DVC Remote Storage

```bash
dvc remote add -d storage ./dvc_storage
git add .dvc/config
git commit -m "added storage"
```
- This configures where DVC stores real data and models.


## Step 9: Push Data & Models to DVC Remote

```bash
dvc push
```
- Uploads Dataset and Model into dvc_storage/

⚠️Important:
In real projects, dvc_storage/ should NOT be committed to Git.
(It was committed here only for learning purposes.)


## Step 10: Switch Branches and Restore Correct Data

```bash
git checkout master
dvc pull
```
```bash
git checkout v1
dvc pull
```
Each branch restores:
- Its correct dataset
- Its correct model


## Step 8: Add DVC Remote Storage

```bash
dvc remote add -d storage ./dvc_storage
git add .dvc/config
git commit -m "added storage"
```
- This configures where DVC stores real data and models.


## Step 8: Add DVC Remote Storage

```bash
dvc remote add -d storage ./dvc_storage
git add .dvc/config
git commit -m "added storage"
```
- This configures where DVC stores real data and models.
