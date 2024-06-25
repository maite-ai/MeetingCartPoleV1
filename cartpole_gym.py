import gymnasium as gym
import imageio

# proper render_mode to save all my frames
env = gym.make("CartPole-v1", render_mode="rgb_array")
# to save all frames
frames = []  

episodes = 10000
score = 0
observation, info = env.reset()
#max_reward = 500

for _ in range(episodes):
    # generates a random action
    random_action = env.action_space.sample()
    # passes our random action through the step method
    observation, reward, terminated, truncated, info = env.step(random_action)
    # accumulates the reward and save it as the score
    score += reward
    
    # renders the environment/view the graphical representation of that environment
    # --This function won't work this way on Collab--
    frame = env.render()
    frames.append(frame)

    # Whether it's terminated (exceeded values) or truncated (reached its goal)
    if terminated or truncated:
        break
# always close the environment
env.close()

# save the video with imageio.mimsave() method and the "frames" list
imageio.mimsave('mi_carrito.mp4', frames, fps=30)