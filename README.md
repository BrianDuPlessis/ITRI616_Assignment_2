<h1>Cliff Walker</h1>
<p>The Cliffwalker problem in the AI Gym environment presents a classic reinforcement learning challenge where an agent navigates a grid-world environment. 
The goal is to reach a target destination while avoiding falling off a cliff. This scenario often involves 
balancing the exploration of unknown territory with the risk of potential pitfalls, emphasizing the trade-off between maximizing rewards and minimizing risks.</p>
<br>
<p>This project solves the cliff walker problem by implementing Q-learning-based reinforcement learning, utilizing the SARSA algorithm.</p>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/9113b45e-1795-4cb8-9c6e-31b4d2c3233a">
<br>
<p>The project offers two solutions based on Q-learning. However, one of these solutions incorporates hyperparameter optimization using a straightforward grid search strategy.</p>
<br>
<p>The code execution process is uncomplicated. If training hasn't been completed yet, simply running the program suffices. Details about the training progress are printed in the terminal, as demonstrated below: </p>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/2114c278-ed08-4896-bdb3-232f702238cb">
<br>
The number of training episodes per iteration can be set by manipulating the global variable 'iterations' which is set to 500 iterations by default.
<br>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/513c57b4-0652-4127-b6b6-c2d609808013">
<br>
The Q-table data is automatically saved in a file named 'cliff-walker'. Consequently, users need not retrain the model each time the code is executed. Enabling or disabling training can be easily achieved by commenting out the function call.
<br>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/5781edbe-8e35-4e80-83c0-535b5242a93a">
