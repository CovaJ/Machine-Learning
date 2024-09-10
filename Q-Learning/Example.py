import gym

env = gym.make('FrozenLake-v0')  #FrozenLake enviornment

print(env.observation_space.n)   # get number of states
print(env.action_space.n)   # get number of actions

env.reset()  # reset enviornment to default state

action = env.action_space.sample()  # get a random action 

new_state, reward, done, info = env.step(action)  # take action, notice it returns information about the action

env.render()   # render the GUI for the enviornment 