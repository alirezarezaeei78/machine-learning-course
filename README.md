# Machine Learning Course Projects

Four notebook-based mini-projects covering classical machine learning, neural networks, imbalanced classification, and reinforcement learning.

Developed in the context of the Machine Learning course at **K. N. Toosi University of Technology**, taught by **Dr. Mahdi Aliyari Shoorehdeli**. This repository presents Alireza Rezaei's project material and experiments.

## Project guide

| Project | Topics and examples |
| --- | --- |
| [Mini-project 1](Mini_project_1/) | Synthetic classification; linear, logistic, and ridge regression; bearing-signal features; weather data analysis |
| [Mini-project 2](Mini_project_2/) | Perceptrons and activation functions; multilayer neural networks; decision trees and ensembles; Coimbra breast-cancer classification |
| [Mini-project 3](Mini_project_3/) | SVMs, dimensionality reduction, kernel methods, and imbalanced credit-card classification with SMOTE and autoencoders |
| [Mini-project 4](Mini_project_4/) | DQN for LunarLander, with replay buffers, target networks, and training plots |

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

Use a separate environment for each mini-project when dependencies differ. Requirements provide starting version ranges; they are not a fully locked reproduction environment.

Before running a notebook:

1. Read its imports and data-loading cells.
2. Provide the referenced datasets and adjust paths. Several notebooks retain Google Colab `/content/drive/...` paths and Drive mounting cells.
3. Check the Python and library versions expected by that project. The reinforcement-learning notebook uses Gymnasium and LunarLander-v3. Install SWIG before the Box2D dependencies if your platform builds Box2D from source.
4. Run cells in order and reproduce the experiment before interpreting saved results.

Referenced datasets include CWRU bearing data, weather-history data, Coimbra breast-cancer data, Iris, and credit-card transaction data. Dataset availability and usage terms are separate from this repository.

## Scope

These are educational experiments. Scores depend on data splits, preprocessing, environment, and training configuration; they should not be treated as production guarantees.

## Author and course credit

**Project material:** [Alireza Rezaei](https://www.linkedin.com/in/alireza-rezaei-24963a210/)

**Course instructor:** Dr. Mahdi Aliyari Shoorehdeli, K. N. Toosi University of Technology.

## Maintenance and validation

Preprocessing fixes keep test data out of scaler fitting and preserve training-set category encodings. The Lunar Lander notebook now uses Gymnasium v3, handles episode truncation, samples deque replay buffers on Python 3.11+, and closes each environment. Repeated operating-system package installation cells have been consolidated. Requirements list starting version ranges rather than a fully locked environment.

Historical outputs in changed notebooks were cleared. Re-run with the original datasets to produce new metrics; a full training run is not part of the maintenance checks. Run `python -m unittest discover -s tests -v` for the short replay-buffer and truncation regressions.

The [Gymnasium Lunar Lander documentation](https://gymnasium.farama.org/environments/box2d/lunar_lander/) describes the v3 environment and rendering interface.
