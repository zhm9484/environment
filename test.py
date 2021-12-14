from neural_mmo.forge.trinity.env import Env
from projekt.config import SmallMultimodalSkills

env = Env(config)
env.reset()

for idx in range(128):
    env.step({})
