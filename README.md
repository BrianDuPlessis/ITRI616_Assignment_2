<h1>Cliff Walker</h1>
<p>The Cliffwalker problem in the AI Gym environment presents a classic reinforcement learning challenge where an agent navigates a grid-world environment. 
The goal is to reach a target destination while avoiding falling off a cliff. This scenario often involves 
balancing the exploration of unknown territory with the risk of potential pitfalls, emphasizing the trade-off between maximizing rewards and minimizing risks.</p>
<br>
<p>This project solves the cliff walker problem by implementing Q-learning-based reinforcement learning, utilizing the SARSA algorithm.</p>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/9113b45e-1795-4cb8-9c6e-31b4d2c3233a">

<p>The solutions provided are both Q-learning solutions, however, one implements hyperparameter optimization with a simple grid search strategy</p>
<hr>
<h2>The execution of the code is straightforward, if training has yet to be done, the program can simply be executed. Information regarding the training process is displayed in the terminal as can be 
seen below: </h2>
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/2114c278-ed08-4896-bdb3-232f702238cb">
<hr>
The number of training episodes per iteration can be set by manipulating the global variable 'iterations' which is set to 500 iterations by default.
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/513c57b4-0652-4127-b6b6-c2d609808013">
<hr>
Q-table data is automatically saved in a file named 'cliff-walker', consequently, the user does not have to retrain the model every time the code is run. 
The user can toggle training on and off by simply commenting out the function call.
<img src="https://github.com/BrianDuPlessis/ITRI616_Assignment_2/assets/112475285/5781edbe-8e35-4e80-83c0-535b5242a93a">
