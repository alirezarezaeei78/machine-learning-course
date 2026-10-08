"""Exercise short notebook code paths without datasets or model training."""
from collections import deque
import json
from pathlib import Path
import types
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def cell_source(relative_path, index):
    nb = json.loads((ROOT / relative_path).read_text(encoding='utf-8'))
    return ''.join(nb['cells'][index]['source'])


class NotebookRegressions(unittest.TestCase):
    def test_deque_replay_sampling_works(self):
        namespace = {}
        exec(cell_source('Mini_project_4/Mini_project_4.ipynb', 9), namespace)
        replay = namespace['ExperienceReplay'](4)
        replay.store_transition([0], 0, [1], 1, False)
        self.assertEqual(len(replay.sample(1)), 1)

    def test_truncation_ends_episode_but_remains_bootstrappable(self):
        transitions = []
        closed = []

        class Environment:
            def reset(self):
                return np.zeros(8), {}

            def step(self, action):
                if transitions:
                    raise AssertionError('Episode continued after truncation')
                return np.ones(8), 1.0, False, True, {}

            def close(self):
                closed.append(True)

        class Agent:
            def __init__(self, *args, **kwargs):
                self.experience_replay = types.SimpleNamespace(store_transition=lambda *args: transitions.append(args))

            def take_action(self, state, eps):
                return 0

            def update_params(self):
                pass

        namespace = dict(DQNAgent=Agent, state_size=8, action_size=4, BATCH_SIZE=1,
                         np=np, deque=deque, n_episodes=1, eps=1.0,
                         eps_decay_rate=0.97, eps_end=0.01,
                         gym=types.SimpleNamespace(make=lambda *args, **kwargs: Environment()))
        exec(cell_source('Mini_project_4/Mini_project_4.ipynb', 16), namespace)
        self.assertEqual(len(transitions), 1)
        self.assertFalse(transitions[0][-1])
        self.assertEqual(closed, [True])


if __name__ == '__main__':
    unittest.main()
