# quantum-classifier-generalization
It enables full reproducibility of reported results by exposing training accuracy, test accuracy, and training sample size sweeps across multiple classification patterns and minimization strategies in hybrid quantum machine learning.
# 📊 Raw Data for Hybrid Quantum Classifier Generalization

## 👩‍🔬👨‍🔬 Authors

Sara Aminpour  
Sarah Sharif  
Mike Banad  

School of Electrical and Computer Engineering, University of Oklahoma, Norman, OK 73019, USA  
Center for Quantum Research and Technology, University of Oklahoma, Norman, OK 73019, USA  

---

## 🧠 Abstract

This repository contains the raw numerical data and Python plotting scripts associated with the manuscript  
**“Development of Hybrid Quantum Classifiers for Realistic Classification Tasks.”**  
The released materials enable full reproducibility of the reported results by providing explicit training accuracy, test accuracy, and training sample size sweeps across multiple classification patterns and classical minimization strategies. Each figure in the manuscript is accompanied by a self-contained Python script that stores the underlying raw data and regenerates the corresponding plot without reliance on external datasets.

---

## 🗂️ Repository Structure

Each script can be executed independently.

## 📈 Data Description

Within each `Fig_*.py` file, raw data are stored explicitly as Python dictionaries:

- `train_acc_data[pattern]`  
  Training accuracy (%) for increasing numbers of training samples.

- `test_acc_data[pattern]`  
  Test accuracy (%) evaluated on a fixed test set.

- `num_samples_data[pattern]`  
  Number of training samples (typically ranging from 1 to 200).

All accuracy values are reported as percentages.

---

## 🔁 Reproducibility

- No randomness is introduced at plotting time.
- All numerical values correspond exactly to those used in the manuscript.
- Training and test sets were generated and evaluated as described in the Methods section.
- Each figure script is fully self-contained and does not rely on hidden preprocessing steps.

---

## 🎯 Intended Use

The data and scripts in this repository are released to support:

- Reproducibility and transparency in hybrid quantum machine learning research  
- Independent verification of reported trends  
- Meta-analysis of training-size effects and generalization behavior  
- Educational use and benchmarking for future HQML studies  

---

## 📖 Citation

If you use this data or code, please cite:

Sara Aminpour, Sarah Sharif, and Mike Banad,  
*Development of Hybrid Quantum Classifiers for Realistic Classification Tasks*,  
IOP Publishing.

---

## ⚖️ License

This project is released under the **MIT License**.


