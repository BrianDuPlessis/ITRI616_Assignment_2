import numpy as np
import gym
import pickle
iterations = 500

class WalkerAgent:
    def __init__(self, env, alpha=0.2, gamma=0.9, epsilon=0.9, epsilon_decay = 0.00000009):
        self.env = env
        self.alpha = alpha                   # Learning rate
        self.gamma = gamma                   # Discount factor
        self.epsilon = epsilon               # exploration rate
        self.epsilonDecay = epsilon_decay    # epsilon decay rate.
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


def train_q_table(episodes, alpha, gamma, epsilon,decay):
    env = gym.make("CliffWalking-v0")
    agent = WalkerAgent(env, alpha, gamma, epsilon, decay)

    for episode in range(episodes):
        state = env.reset()
        action = agent.choose_action(state)

        total_reward = 0
        done = False
        while not done:
            # truncated is total steps
            next_state, reward, done, _ = env.step(action)
            next_action = agent.choose_action(next_state)
            agent.update_q_table(state, action, reward, next_state, next_action)

            state = next_state
            action = next_action
            total_reward += reward

        agent.epsilon = max(agent.epsilon - agent.epsilonDecay, 0)

        if(agent.epsilon==0):
            agent.alpha = 0.0001    

    env.close()
    return agent.q_table, total_reward
    

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


def training(episodes):
    #hyperparameters to be tested
    alpha_values = [0.1, 0.2, 0.3]
    gamma_values = [0.95, 0.9, 0.99]
    epsilon_values = [0.1, 0.9, 0.3]
    decay_values = [0.000000000000009, 0.0000009]

    best_q_table = None
    best_reward = float("-inf")

    sum = 0

    #perform grid search
    for alpha in alpha_values:
        for gamma in gamma_values:
            for epsilon in epsilon_values:
                for decay in decay_values:
                    q_table, total_reward = train_q_table(episodes, alpha, gamma, epsilon, decay)
                    sum += 1
                    result = "{:.2f}".format((sum/(len(alpha_values)*len(gamma_values)*len(epsilon_values)*len(decay_values)))*100)
                    print(str(sum)+".)  Alpha: "+ str(alpha) + "     Gamma: "+ str(gamma) + "      Epsilon: " + str(epsilon) + "      Decay: "+ str(decay) +"      Reward: "+ str(total_reward) +  "\t\t" + str(result)+ " percent finished")
                    if(total_reward > best_reward):
                        best_reward = total_reward
                        best_q_table = q_table

    print("\n Done.......")
    f = open("cliff_walker","wb")
    pickle.dump(best_q_table, f)
    f.close()

#training(iterations)
run()

    

    

