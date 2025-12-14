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

## 🛠 Step 1: Initialize Git & DVC

```bash
git init
python -m dvc init
