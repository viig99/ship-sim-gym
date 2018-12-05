import time

import gym
import ship_gym
from ship_gym.ship_env import ShipEnv

from ship_gym.config import EnvConfig, GameConfig


gc = GameConfig
gc.FPS = 30
gc.SPEED = 10
gc.DEBUG = True

env = ShipEnv(game_config=gc, env_config=EnvConfig)

env.reset()

for _ in range(10000):

    total_reward = 0
    for _ in range(100):
        env.render()

        ret = env.step(env.action_space.sample()) # take a random action
        # ret = env.step(0) # take a random action
        total_reward += ret[1]

        if ret[2] == True:
            print(f"AGENT IS DONE. TOTAL REWARD = {total_reward}")
            env.reset()
            break

        # time.sleep(0.1)
        print(ret)

        # time.sleep(0.0)