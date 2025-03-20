README: Simulate-and-Recover for the EZ Diffusion Model. 

This project involved implementing code for a simulate-and-recover procedure to evaluate the EZ Diffusion Model. 

The EZ Diffusion Model is a simplified version of the Drift Diffusion Model, also known as the DDM, which estimates parameters quickly. The DDM is often used psychological experiments such as evaluating cognitive processes for decision-making. These can require really complex methods for estimating parameters, which can be slow. The EZ Diffusion Model simplifies this by using summary stats (accuracy rate, mean response time, response time variance) to compute key parameters, such as drift rate: the speed that evidences goes towards a decision, boundary separation: cautiousness in decision making, and nondecision time: time taken by other processes that don't contribute to decision-making. The EZ Diffusion Model is much more efficient and simple compared to the DDM.

To test the EZ Diffusion Model, it's important to use a "simulate and recover" method. This generates data, computes summary statistics, and uses the EZ Diffusion to estimate parameters based on these. Then, the estimated parameters are compared to the original values, and bias and accuracy can be assessed.

The goal of this project is to determine if parameters estimated from our simulated data, such as bias, will align with the parameters to generate the data, such as sample size. This is important in psychological research because it can have many implications for data and results of experiments.

First, we randomly selected several model parameters: Boundary separation, drift rate, and nondecision time. For each set of parameters, I simulated data based on the EZ diffusion model. Then, I estimated parameters from the simulated data. I compared these to the original parameters to compute bias and squared error. Then, this is iterated.

I took several different approaches to this. Initially, I tried to separate my simulate and my recover code into two distinct files. Eventually, I realized that it would be most efficient and easy for me to combine everything into one EZ

These are the results I received:
Sample Size N = 10
Average Bias: [-0.18836319 -0.27696925  0.05462549]
Average Squared Error: [0.81058804 0.77264115 0.02852486]

The bias for sample size 10 is relatively large, especially for the first two parameters. This might mean poorer recovery at a smaller sample size.

Sample Size N = 40
Average Bias: [-0.05410313 -0.06544398  0.00856703]
Average Squared Error: [0.14829441 0.11818463 0.0041669 ]

When the sample size is 40, the bias is reduced significantly compared to a sample size of 10, which might indicate improvement in estimation. 

Sample Size N = 4000
Average Bias: [-4.85691865e-04 -2.18256306e-04 -9.13811566e-05]
Average Squared Error: [1.10656922e-03 1.66779461e-04 2.00158054e-05]

At a sample size of N = 4000, which is significantly larger than previous sizes, the bias is almost at 0 across all parameters, suggesting excellent recovery. This confirms that as sample size increases, EZ diffusion estimates become more accurate.


The results aligned with my predictions. The output showed that as the sample size increases, the bias gets closer to 0. The squared error is also smaller, and decreases as you increase n. 

This indicates that the EZ Diffusion model I created recovers its own parameters well across different sample sizes. 
