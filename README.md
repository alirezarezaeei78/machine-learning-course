# Machine Learning Course Projects

Four notebook-based mini-projects covering classical machine learning, neural networks, imbalanced classification, and reinforcement learning.

Developed in the context of the Machine Learning course at **K. N. Toosi University of Technology**, taught by **Dr. Mahdi Aliyari Shoorehdeli**. This repository presents Alireza Rezaei's project material and experiments.

## Project guide

| Project | Topics and examples |
| --- | --- |
| [Mini-project 1](Mini_project_1/) | Synthetic classification; linear, logistic, and ridge regression; bearing-signal features; weather data analysis |
| [Mini-project 2](Mini_project_2/) | Perceptrons and activation functions; multilayer neural networks; decision trees and ensembles; Coimbra breast-cancer classification |
| [Mini-project 3](Mini_project_3/) | SVMs, dimensionality reduction, kernel methods, and imbalanced credit-card classification with SMOTE and autoencoders |
| [Mini-project 4](Mini_project_4/) | DQN and Double DQN for LunarLander, including replay buffers and training comparisons |

The folders contain notebooks and project-specific dependency files. Some include separate instructions and project reports.

## Running the notebooks

```sh
git clone https://github.com/alirezarezaeei78/machine-learning-course.git
cd machine-learning-course
python -m venv .venv
```

Activate the environment, then install Jupyter and the requirements for the selected project. For example:

```sh
python -m pip install notebook
python -m pip install -r Mini_project_1/requirements.txt
python -m notebook
```

Use a separate environment for each mini-project when dependencies differ. Requirements capture the original experiments; some packages are pinned to older versions.

Before running a notebook:

1. Read its imports and data-loading cells.
2. Provide the referenced datasets and adjust paths. Several notebooks retain Google Colab `/content/drive/...` paths and Drive mounting cells.
3. Check the Python and library versions expected by that project. Reinforcement-learning notebooks use the original Gym API and may need adaptation for newer environments.
4. Run cells in order and reproduce the experiment before interpreting saved results.

Referenced datasets include CWRU bearing data, weather-history data, Coimbra breast-cancer data, Iris, and credit-card transaction data. Dataset availability and usage terms are separate from this repository.

## Scope

These are educational experiments. Scores depend on data splits, preprocessing, environment, and training configuration; they should not be treated as production guarantees.

## Author and course credit

**Project material:** [Alireza Rezaei](https://www.linkedin.com/in/alireza-rezaei-24963a210/)

**Course instructor:** Dr. Mahdi Aliyari Shoorehdeli, K. N. Toosi University of Technology.
