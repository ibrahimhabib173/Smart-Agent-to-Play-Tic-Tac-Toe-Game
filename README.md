# Tic Tac Toe Smart Agent
Is a RL Project using Python language
## About the project (game) 
Our project focuses on applying Reinforcement Learning (RL) techniques to train an agent to play the game of Tic Tac Toe. Tic Tac Toe is a popular two-player game played on a 3x3 grid. The objective is to be the first to place three of your marks (either X or O) in a row, column, or diagonal. By utilizing RL algorithms, we aimed to develop an AI agent that can learn optimal strategies for playing Tic Tac Toe.
## Technologies and Tools 
•	Programming language (Python) We integrate the code with UI using : 
1.	Tkinter 
2.	 pygame libiraries 
## Methodology 
To accomplish our project goals, we employed the following tools and techniques:
1. Reinforcement Learning : We utilized RL, a branch of machine learning, where an agent learns to make decisions through interacting with an environment. The agent receives feedback in the form of rewards or penalties, which helps it learn optimal strategies over time. 
2. Q-Learning : We employed Q-Learning, a widely used RL algorithm, to train our Tic Tac Toe agent. Q-Learning is a model free algorithm that learns an action-value function (Q-function) to estimate the expected future rewards for each state-action pair. By iteratively updating Q-values based on the agent's experiences, it gradually learns the optimal strategy. 
(𝒔𝒕𝒂𝒕𝒆,𝒂𝒄𝒕𝒊𝒐𝒏) += 𝒂𝒍𝒑𝒉𝒂∗(𝒓𝒆𝒘𝒂𝒓𝒅+𝒈𝒂𝒎𝒎𝒂∗𝐦𝐚𝐱 (𝑸(𝒏𝒆𝒙𝒕𝒔𝒕𝒂𝒕𝒆)−𝑸(𝒔𝒕𝒂𝒕𝒆,𝒂𝒄𝒕𝒊𝒐𝒏)) 
3. Game Environment : We developed a Tic Tac Toe environment that simulates the game board, tracks the game state, and provides a set of actions available to the agent. The environment also includes the rules of the game, ensuring that the agent's actions are valid. 
4. Exploration-Exploitation Tradeoff : To balance exploration and exploitation during training, we used an epsilon-greedy policy. This policy selects a random action with a certain probability (epsilon) to explore different strategies, and otherwise, selects the action with the highest Q-value to exploit the learned knowledge.
## Some additional information :
1.	The game has 2 mode [Easy , Hard] 
2.	You can choose the mark [X , O] that you want to play with 
3.	Player X always play first whether it's you or AI 4. Can you press 𝑐𝑡𝑟𝑙 + 𝑅 to play again


