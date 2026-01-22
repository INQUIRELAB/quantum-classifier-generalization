Raw Data and Plotting Scripts for

“Development of Hybrid Quantum Classifiers for Realistic Classification Tasks”

Overview

This repository contains the raw numerical data and Python scripts used to generate the figures in the manuscript:

Development of Hybrid Quantum Classifiers for Realistic Classification Tasks
Authors: Sara Aminpour, Sarah Sharif and Mike Banad
School of Electrical and Computer Engineering, University of Oklahoma, Norman, OK 73019, USA
Center for Quantum and Technology, University of Oklahoma, Norman, OK 73019 USA

The released materials enable full reproducibility of the plotted results, including training accuracy, test accuracy, and training sample size sweeps across multiple classification patterns and minimization strategies.

Each figure in the manuscript is accompanied by a self-contained Python script that stores the underlying raw data explicitly and regenerates the corresponding plot.

Repository Structure

Fig_*.py
Python scripts containing the raw data arrays and plotting routines.

Fig_*.png
The figure image generated directly from the corresponding script.

Each script can be executed independently and does not require access to external datasets.

Example: Figure 2

Figure 2 presents the relationship between training accuracy and test accuracy for a single-qubit hybrid quantum classifier trained using the COBYLA minimizer, across nine classification patterns.

The script Fig_2.py contains:

Explicit numerical arrays for:

Training accuracy, Test accuracy, Number of training samples, One subplot per classification pattern,

Color-coded markers indicating training sample size, A star marker denoting the highest test accuracy for each pattern

Classification Patterns (Subplots a–i)
Subplot	Pattern Name
(a)	Circle
(b)	Crown
(c)	Tricrown
(d)	Line
(e)	2 Lines
(f)	Squares
(g)	Wavy Lines
(h)	3 Circles
(i)	6 Rectangles
Raw Data Description

Within each Fig_*.py file, the raw data are stored as Python dictionaries with the following structure:

train_acc_data[pattern]
List of training accuracies (%) obtained for increasing numbers of training samples.

test_acc_data[pattern]
Corresponding list of test accuracies (%) evaluated on a fixed test set.

num_samples_data[pattern]
Number of training samples used for each experiment (typically ranging from 1 to 200).

All accuracy values are reported as percentages.

How to Reproduce the Figures

Requirements

Python ≥ 3.8
NumPy
Matplotlib
Execution

For example, to regenerate Figure 2: 
python Fig_2.py


This will:

Load the raw accuracy data stored in the script

Generate the multi-panel scatter plot

Save the output as Fig_2.png

Notes on Reproducibility

No randomness is introduced at plotting time.

All numerical values correspond exactly to those used in the manuscript.

Training and test sets were generated and evaluated as described in the Methods section of the paper.

Each figure script is self-contained and does not rely on hidden preprocessing steps.

Intended Use

These raw data files are released to support:

Reproducibility and transparency
Independent verification of reported trends
Meta-analysis of training-size effects in hybrid quantum machine learning
Educational use and benchmarking for future HQML studies

Citation

If you use this data or code, please cite the associated manuscript:

Sara Aminpour, Sarah Sharif, and Mike Banad,
Development of Hybrid Quantum Classifiers for Realistic Classification Tasks,
IOP Publishing.

