
# Mini Project 4: Deep Reinforcement Learning for Lunar Lander

## Overview

This project aims to apply deep reinforcement learning techniques, specifically DQN and DDQN, to solve the Lunar Lander environment from OpenAI Gym. The project explores the effects of different batch sizes on agent performance and compares the efficiency of DQN and DDQN algorithms.

## Table of Contents
1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Environment Details](#environment-details)
4. [Methodology](#methodology)
    - [Deep Q-Learning (DQN)](#deep-q-learning-dqn)
    - [Double Deep Q-Learning (DDQN)](#double-deep-q-learning-ddqn)
5. [Results](#results)
    - [Batch Size Comparison](#batch-size-comparison)
    - [DQN vs DDQN](#dqn-vs-ddqn)
6. [Conclusion](#conclusion)
7. [References](#references)

## Introduction

The Lunar Lander environment involves controlling a spacecraft to land safely on a designated landing pad. The agent must learn to navigate the lander using thrusters to control its horizontal and vertical velocities while considering the spacecraft's angle and leg contact with the ground.

## Project Structure

- **Code**: Implementation of the DQN and DDQN agents.
- **Reports**: Detailed analysis and results of the experiments.
- **Notebooks**: Jupyter notebooks containing code and explanations.
- **Videos**: Recordings of the agent's performance during training.

## Environment Details

- **State Space**: 8-dimensional continuous space representing the lander's position, velocity, angle, and leg contact.
- **Action Space**: 4 discrete actions:
  - Do nothing
  - Fire main engine
  - Fire left engine
  - Fire right engine
- **Reward System**:
  - +100 to +140 points for landing
  - -100 points for crashing
  - +10 points for each leg contact
  - -0.03 points for firing the main engine
  - -0.1 points for each frame without termination

## Methodology

### Deep Q-Learning (DQN)

DQN uses a neural network to approximate the Q-value function, which represents the expected future rewards for each action given a state. The agent interacts with the environment and stores experiences in a replay buffer. The neural network is trained using mini-batches sampled from the replay buffer to break the correlation between consecutive experiences.

### Double Deep Q-Learning (DDQN)

DDQN addresses the overestimation bias in Q-learning by using two networks: a value network and a target network. The value network is used to select actions, while the target network is used to evaluate them. This decoupling helps in providing more accurate value estimates.

## Results

### Batch Size Comparison

We experimented with three batch sizes: 32, 64, and 128. The results are as follows:

- **Batch Size 32**: Shows significant initial volatility but stabilizes over time.
- **Batch Size 64**: Provides a good balance between stability and learning speed.
- **Batch Size 128**: Exhibits the highest stability and fastest convergence but may be slower in individual updates.

### DQN vs DDQN

- **DQN**: Prone to overestimation bias, which can lead to suboptimal policies.
- **DDQN**: More stable and provides better performance by mitigating the overestimation bias.

## Conclusion

Through this project, we demonstrated the application of DQN and DDQN algorithms in the Lunar Lander environment. DDQN outperforms DQN by providing more accurate value estimates, leading to better policy learning. The batch size significantly impacts the training stability and convergence speed, with larger batch sizes generally performing better.

## References

- [OpenAI Gym](https://gym.openai.com/)
- [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3)
- [Deep Q-Learning Paper](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
- [Double Q-Learning Paper](https://arxiv.org/abs/1509.06461)

For detailed code implementation and analysis, please refer to the Jupyter notebooks and reports provided in this repository. The video recordings of the agent's performance are also available for a visual understanding of the training process.
