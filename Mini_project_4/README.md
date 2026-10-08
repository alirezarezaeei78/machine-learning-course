# Mini-project 4: Deep Reinforcement Learning

DQN for LunarLander-v3 with experience replay, a target network, soft parameter updates, and training plots. The current notebook implements standard DQN; the assignment may discuss additional variants.

## Notebooks

- [Mini_project_4.ipynb](Mini_project_4.ipynb)

## Setup

Create an isolated Python environment and install Jupyter plus this folder's `requirements.txt`. Dependencies reflect the original experiments and may require compatible older library versions.

From the repository root:

```sh
python -m pip install notebook
python -m pip install -r Mini_project_4/requirements.txt
python -m notebook
```

Inspect the notebook's imports and data-loading cells before execution. Provide the required datasets and adjust Colab or local paths. Run cells in order and record the environment, data split, preprocessing, and random seed when comparing results.

See the [course project guide](../README.md) for context and course credit. These notebooks are educational experiments; saved outputs should be reproduced before interpreting their scores.

Use Gymnasium dependencies from `requirements.txt`. If Box2D needs a source build, install SWIG first with `python -m pip install swig`. Episode truncation ends the interaction loop while preserving bootstrap targets. Changed training outputs were cleared and require a fresh run.
