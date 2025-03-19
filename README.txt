README: Simulate-and-Recover for the EZ Diffusion Model. 

This project involved implementing code for a simulate-and-recover procedure to evaluate the EZ Diffusion Model. The goal of this project is to determine if parameters estimated from our simulated data, such as bias, will align with the parameters to generate the data, such as sample size. This is important in psychological research because it can have many implications for data and results of experiments.

First, we randomly selected several model parameters: Boundary separation, drift rate, and nondecision time. For each set of parameters, I simulated data based on the EZ diffusion model. Then, I estimated parameters from the simulated data. I compared these to the original parameters to compute bias and squared error. Then, this is iterated.

These are the results I received:
Sample Size N = 10
Average Bias: [-0.18836319 -0.27696925  0.05462549]
Average Squared Error: [0.81058804 0.77264115 0.02852486]

Sample Size N = 40
Average Bias: [-0.05410313 -0.06544398  0.00856703]
Average Squared Error: [0.14829441 0.11818463 0.0041669 ]

Sample Size N = 4000
Average Bias: [-4.85691865e-04 -2.18256306e-04 -9.13811566e-05]
Average Squared Error: [1.10656922e-03 1.66779461e-04 2.00158054e-05]

The results aligned with my predictions. The output showed that as the sample size increases, the bias gets closer to 0. The squared error is also smaller, and decreases as you increase n. 
