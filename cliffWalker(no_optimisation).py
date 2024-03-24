import numpy as np
import gym
import pickle

class WalkerAgent:
    def __init__(self, env, alpha=0.2, gamma=0.9, epsilon=0.9):
        self.env = env
        self.alpha = alpha            # Learning rate
        self.gamma = gamma            # Discount factor
        self.epsilon = epsilon        # exploration rate
        self.epsilonDecay = 0.00009    # epsilon decay rate. 0.9/0.00009 = 10,000
        self.q_table = np.zeros((env.observation_space.n, env.action_space.n))
        self.rng = np.random.default_rng()

    def choose_action(self, state):
        if self.rng.random() < self.epsilon:
            return self.env.action_space.sample()  # Choose a random action
        else:
            return np.argmax(self.q_table[state, :])  # Choose the action with the highest Q-value


    def update_q_table(self, state, action, reward, next_state, next_action):
        predict = self.q_table[state, action]
        target = reward + self.gamma * self.q_table[next_state, next_action]
        self.q_table[state, action] += self.alpha * (target - predict)


def training(episodes):
    env = gym.make("CliffWalking-v0")
    agent = WalkerAgent(env)

    for episode in range(episodes):
        state = env.reset()
        action = agent.choose_action(state)

        total_reward = 0
        done = False
        while not done:
            next_state, reward, done, _ = env.step(action)
            next_action = agent.choose_action(next_state)
            agent.update_q_table(state, action, reward, next_state, next_action)

            state = next_state
            action = next_action
            total_reward += reward

        agent.epsilon = max(agent.epsilon - agent.epsilonDecay, 0)

        if(agent.epsilon==0):
            agent.alpha = 0.0001    


        print("Episode:", episode+1, "Total Reward:", total_reward)

    env.close()
    f = open("cliff_walker","wb")
    pickle.dump(agent.q_table, f)
    f.close()

def run():
    #load training data into current Q-table
    f = open('cliff_walker', 'rb')
    q_table = pickle.load(f)
    f.close()

    env = gym.make("CliffWalking-v0")
    agent = WalkerAgent(env)
    agent.q_table = q_table
    state = env.reset()
    done = False
    while not done:
        action = np.argmax(agent.q_table[state, :])
        next_state, reward, done, _ = env.step(action)
        env.render()
        state = next_state
    env.close()



training(10000)
run()
    

    

