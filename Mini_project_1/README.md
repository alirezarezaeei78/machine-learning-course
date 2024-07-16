
# Mini Project 1: Machine Learning Course

## Overview

Welcome to the repository for Mini Project 1 of the Machine Learning Course. This project is designed to provide hands-on experience with machine learning models and techniques, encompassing model training, evaluation, feature engineering, and advanced techniques. This README will guide you through the setup, usage, and structure of the project.

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

Mini Project 1 is an integral part of the Machine Learning Course, offering practical exposure to the following:

1. **Model Evaluation and Training:**
   - Developing and assessing linear classifiers.
   - Transitioning from binary to multi-class classification.
   - Visualizing decision boundaries and evaluating model performance using various metrics.

2. **Feature Engineering:**
   - Creating and visualizing synthetic datasets.
   - Extracting and selecting relevant features.
   - Analyzing the impact of feature selection on model performance.

3. **Advanced Techniques:**
   - Implementing data shuffling and normalization.
   - Exploring and applying various machine learning algorithms.
   - Comparing performance metrics across different models and hyperparameters.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alirezarezaeei78/miniproject1.git
   cd miniproject1
   ```

2. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook:**
   ```bash
   jupyter notebook Miniproject_1.ipynb
   ```

---

## Datasets

- **Synthetic Dataset:**
  - Generated using `sklearn.datasets.make_classification`.
  - Contains 1000 samples with 3 features and 4 classes.

- **CWRU Bearing Dataset:**
  - Retrieved from the Case Western Reserve University Bearing Data Center.
  - Includes data for normal and faulty bearings, useful for fault detection tasks.

---

## Code Structure

- `Miniproject_1.ipynb`: Main Jupyter Notebook containing project tasks, code, and explanations.
- `requirements.txt`: List of required Python packages.

---

## Experiments and Results

1. **Model Training and Evaluation:**
   - Implemented logistic regression and SGD classifier.
   - Evaluated models using accuracy, precision, recall, and confusion matrix.

2. **Feature Engineering:**
   - Generated synthetic datasets.
   - Applied feature selection and extraction techniques.
   - Visualized the impact of feature engineering on model performance.

3. **Advanced Techniques:**
   - Applied data shuffling and normalization.
   - Implemented custom loss functions for evaluation.
   - Compared different machine learning algorithms and hyperparameters.

---

## Usage

To execute the experiments and review results, follow these steps:

1. Ensure all required packages are installed.
2. Open `Miniproject_1.ipynb` in Jupyter Notebook.
3. Execute the cells sequentially as per the instructions.
4. Analyze the outputs and visualizations generated in the notebook.

---

## Contributing

We welcome contributions to enhance this project. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact Information

For questions, feedback, or additional information, please open an issue on GitHub or contact the course instructors directly.

---

This documentation aims to facilitate your understanding and execution of Mini Project 1, ensuring a comprehensive grasp of machine learning concepts and their practical applications.
