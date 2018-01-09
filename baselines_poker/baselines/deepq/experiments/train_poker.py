path = 'C:/Users/dsp21/NYDS/Project/Capstone Ideas/Poker bot/git_things/poker_history_gym/gym_poker_history/envs'
path2 = "C:/Users/dsp21/NYDS/Project/Capstone Ideas/Poker bot/git_things/baselines"
import sys
sys.path.insert(0, path)

import poker_hist_env
import gym


from baselines import deepq


def callback(lcl, glb):
    # stop training if reward exceeds 199
    is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199
    return is_solved


def main():
    print("starting main") #DP EDIT
    env = gym.make("CartPole-v0")

    print(env)
    model = deepq.models.mlp([64])
    act = deepq.pok_learn(
        env,
        q_func=model,
        lr=1e-3,
        max_timesteps=20000,
        buffer_size=50000,
        exploration_fraction=0.1,
        exploration_final_eps=0.02,
        print_freq=10,
        callback=callback
    )
    print("Saving model to cartpole_model.pkl")
    act.save("cartpole_model.pkl")


if __name__ == '__main__':
    main()
