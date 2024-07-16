
# Mini Project 2: Machine Learning Course

## Overview

Welcome to the repository for Mini Project 2 of the Machine Learning Course. This project delves into advanced machine learning concepts and techniques, emphasizing neural networks, feature extraction, and rigorous model evaluation. This README file provides comprehensive instructions on setup, usage, and the project's structure.

---

## Table of Contents

1. [Project Description](#project-description)
2. [Setup Instructions](#setup-instructions)
3. [Datasets](#datasets)
4. [Code Structure](#code-structure)
5. [Experiments and Results](#experiments-and-results)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact Information](#contact-information)

---

## Project Description

Mini Project 2 is an advanced segment of the Machine Learning Course, designed to enhance your understanding of:

1. **Neural Networks:**
   - Implementing and analyzing neural networks using various activation functions such as ReLU and Sigmoid.
   - Designing and training both simple and multi-layer perceptron models.
   - Evaluating neural network performance in classification tasks, focusing on accuracy, precision, recall, and F1-score.

2. **Feature Engineering:**
   - Extracting and selecting relevant features from complex datasets to improve model performance.
   - Implementing data preprocessing techniques including normalization and shuffling to enhance training efficiency and model accuracy.

3. **Model Evaluation and Comparison:**
   - Comparing performance metrics of different machine learning algorithms such as Artificial Neural Networks (ANN) and Naive Bayes.
   - Utilizing techniques such as K-Fold and Stratified K-Fold Cross-Validation to assess model robustness and generalization capabilities.
   - Analyzing confusion matrices and detailed classification reports to understand model strengths and weaknesses.

---

## Setup Instructions

To get started with this project, follow these steps:

### Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/alirezarezaeei78/Mini_project_2.git
cd Mini_project_2
```

### Install Required Packages

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

Start Jupyter Notebook to access the project's notebooks:

```bash
jupyter notebook MLproject_partOne.ipynb
```

---

## Datasets

### Breast Cancer Coimbra Dataset

This dataset, retrieved from the UCI Machine Learning Repository, includes various anthropometric and blood analysis parameters. It is used to predict the presence of breast cancer based on features such as Age, BMI, Glucose, Insulin, HOMA, Leptin, Adiponectin, Resistin, and MCP-1. The dataset contains both healthy controls and patients diagnosed with breast cancer.

### CWRU Bearing Dataset

The CWRU Bearing Dataset is sourced from the Case Western Reserve University Bearing Data Center. It includes data from bearings in normal and faulty conditions. This dataset is essential for fault detection tasks and includes various conditions such as drive-end faults, fan-end faults, and normal operational states.

---

## Code Structure

The project is organized into several parts, each focusing on different aspects of machine learning tasks:

- `MLproject_partOne.ipynb`: Covers initial data exploration, preprocessing, and visualization.
- `MLproject_partTwo.ipynb`: Focuses on feature extraction, selection, and initial model training.
- `MLproject_partThree.ipynb`: Delves into advanced model training, including neural networks and hyperparameter tuning.
- `MLproject_partFour.ipynb`: Compares various models, evaluates their performance, and includes advanced analysis techniques.
- `requirements.txt`: File listing all necessary Python packages and dependencies for the project.

---

## Experiments and Results

### Neural Networks Implementation

- **Model Design**: Implemented neural networks using different activation functions (ReLU and Sigmoid) to understand their impact on learning and performance.
- **Training**: Trained both simple and multi-layer perceptron models on the datasets.
- **Evaluation**: Assessed model performance using accuracy, precision, recall, F1-score, and visualized decision boundaries.

### Feature Engineering

- **Extraction and Selection**: Applied feature extraction techniques to identify the most relevant features from the datasets, improving model predictions.
- **Preprocessing**: Used normalization and data shuffling to ensure consistent and efficient training processes.

### Model Evaluation

- **Comparison of Algorithms**: Compared the performance of ANN and Naive Bayes classifiers in predicting breast cancer, highlighting their strengths and weaknesses.
- **Cross-Validation**: Used K-Fold and Stratified K-Fold Cross-Validation to evaluate model robustness and generalization capabilities.
- **Performance Analysis**: Generated detailed confusion matrices and classification reports to analyze model performance comprehensively.

### Advanced Techniques

- **Loss Functions and Optimizers**: Explored the impact of different loss functions and optimizers on model training and performance.
- **Model Tuning**: Fine-tuned model hyperparameters to achieve optimal performance, using techniques such as grid search.

---

## Usage

To execute the experiments and review the results:

1. Ensure all required packages are installed.
2. Open the respective Jupyter Notebooks (`MLproject_partOne.ipynb`, `MLproject_partTwo.ipynb`, `MLproject_partThree.ipynb`, `MLproject_partFour.ipynb`) in Jupyter Notebook.
3. Execute the cells sequentially as per the instructions provided in each notebook.
4. Analyze the outputs and visualizations generated to understand the results of the experiments.

---

## Contributing

We welcome contributions to enhance this project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request for review.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact Information

For questions, feedback, or additional information, please open an issue on GitHub or contact the course instructors directly.

---

This documentation aims to facilitate your understanding and execution of Mini Project 2, ensuring a comprehensive grasp of advanced machine learning concepts and their practical applications.
