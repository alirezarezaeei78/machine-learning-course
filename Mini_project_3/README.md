
# Mini Project 3: Machine Learning Course

## Overview

Welcome to the repository for Mini Project 3 of the Machine Learning Course. This project focuses on advanced implementations and evaluations of Support Vector Machines (SVM) and Autoencoder Neural Networks for data classification. This README provides detailed instructions on setting up, using, and understanding the project's structure and results.

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

Mini Project 3 is a comprehensive part of the Machine Learning Course, designed to deepen your understanding of the following:

1. **Support Vector Machines (SVM):**
   - Implementing and analyzing SVM with different kernel functions (linear, polynomial, RBF).
   - Evaluating SVM performance on the Iris dataset.
   - Visualizing decision boundaries and confusion matrices for various kernel functions and degrees.

2. **Autoencoder Neural Networks:**
   - Implementing an autoencoder for credit card fraud detection.
   - Addressing the challenges of imbalanced data using techniques such as oversampling.
   - Evaluating model performance using metrics such as accuracy, precision, recall, and F1-score.

---

## Setup Instructions

### Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/alirezarezaeei78/miniproject3.git
cd miniproject3
```

### Install Required Packages

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

Start Jupyter Notebook to access the project's notebooks:

```bash
jupyter notebook Soal1.ipynb
```

## Datasets

### Iris Dataset

The Iris dataset is a well-known dataset in the field of machine learning. It contains 150 samples of iris flowers, with each sample having four features: sepal length, sepal width, petal length, and petal width. The samples are classified into three species: Iris-setosa, Iris-versicolor, and Iris-virginica. This dataset is used to evaluate the performance of SVM models.

### Credit Card Fraud Detection Dataset

This dataset contains transactions made by credit cards in September 2013 by European cardholders. It presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. The dataset is highly imbalanced, with the positive class (frauds) accounting for 0.172% of all transactions. This dataset is used to evaluate the performance of autoencoder neural networks.

## Code Structure

The project is organized into several parts, each focusing on different aspects of machine learning tasks:

- `MLproject_partOne.ipynb`: Notebook covering the implementation and evaluation of SVM on the Iris dataset.
- `MLproject_partTwo.ipynb`: Notebook focusing on the implementation of autoencoder neural networks for credit card fraud detection.
- `requirements.txt`: File listing all necessary Python packages and dependencies for the project.

## Experiments and Results

### Support Vector Machines (SVM)

- **Model Implementation:** Implemented SVM using different kernel functions (linear, polynomial, RBF) to understand their impact on learning and performance.
- **Training and Evaluation:** Trained SVM models on the Iris dataset and evaluated their performance using accuracy, precision, recall, F1-score, and confusion matrices.
- **Visualization:** Visualized decision boundaries for various kernel functions and degrees to understand the model's classification capabilities.

### Autoencoder Neural Networks

- **Model Implementation:** Implemented an autoencoder neural network for credit card fraud detection.
- **Handling Imbalanced Data:** Addressed the challenges of imbalanced data using oversampling techniques to improve model performance.
- **Evaluation Metrics:** Evaluated model performance using metrics such as accuracy, precision, recall, F1-score, and confusion matrices. Also analyzed the model's performance across different thresholds.

### Advanced Techniques

- **Hyperparameter Tuning:** Fine-tuned model hyperparameters to achieve optimal performance using techniques such as grid search.
- **Cross-Validation:** Applied K-Fold and Stratified K-Fold Cross-Validation to assess model robustness and generalization capabilities.
- **Visualization Tools:** Used tools like t-SNE and PCA for data visualization and understanding feature importance.

## Usage

To execute the experiments and review the results:

1. Ensure all required packages are installed.
2. Open the respective Jupyter Notebooks (`MLproject_partTwo.ipynb`, `MLproject_partTwo.ipynb`) in Jupyter Notebook.
3. Execute the cells sequentially as per the instructions provided in each notebook.
4. Analyze the outputs and visualizations generated to understand the results of the experiments.

## Contributing

We welcome contributions to enhance this project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request for review.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact Information

For questions, feedback, or additional information, please open an issue on GitHub or contact the course instructors directly.

This documentation aims to facilitate your understanding and execution of Mini Project 3, ensuring a comprehensive grasp of advanced machine learning concepts and their practical applications.
