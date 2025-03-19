README: Simulate-and-Recover for the EZ Diffusion Model. 

This project involved implementing code for a simulate-and-recover procedure to evaluate the EZ Diffusion Model. The goal of this project is to determine if parameters estimated from our simulated data, such as bias, will align with the parameters to generate the data, such as sample size. This is important in psychological research because it can have many implications for data and results of experiments.

First, we randomly selected several model parameters: Boundary separation, drift rate, and nondecision time. For each set of parameters, I simulated data based on the EZ diffusion model. Then, I estimated parameters from the simulated data. I compared these to the original parameters to compute bias and squared error. Then, this is iterated.

The results found that as the sample size increases, the bias gets closer to 0. The squared error is also smaller, and decreases as you increase n. 