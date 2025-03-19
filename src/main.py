#!/usr/bin/env python3
import numpy as np
from ez_diffusion_simulate_and_recover import EZ_diffusion_simulate_and_recover

def run_simulation_and_recover(n: int, iterations: int):
    """Runs the simulate-and-recover process for a given sameple size n and given number of iterations.
    This tests how good EZ diffusion is at recovering its own parameters"""
    biases, squared_errors = [], []

    for _ in range(iterations):
        simul = EZ_diffusion_simulate_and_recover(n)
        bias, squared_error = simul.simulate_and_recover()
        biases.append(bias)
        squared_errors.append(squared_error)

    avg_bias = np.nanmean(biases, axis=0)
    avg_squared_error = np.nanmean(squared_errors, axis=0)

    return avg_bias, avg_squared_error
    

def run_ez_diffusion_simulation_and_recover_exercises():
    """The main program to run all simulations and saved the results in a file"""
    N_value_list = [10, 40, 4000]
    iterations = 1000
    results = {}

    for n in N_value_list:
        print(f"Results for running simulation with sample size N={n}:")
        avg_bias, avg_squared_error = run_simulation_and_recover(n, iterations)
        results[n] = {'avg_bias': avg_bias, 'avg_squared_error': avg_squared_error}
        print(results[n])
        print(f"Results for N={n} saved.")

    with open("ez_diffusion_simulation_results.txt", "w") as f:
        for n, result in results.items():
            f.write(f"Sample Size N = {n}\n")
            f.write(f"Average Bias: {result['avg_bias']}\n")
            f.write(f"Average Squared Error: {result['avg_squared_error']}\n\n")

if __name__ == "__main__":
    run_ez_diffusion_simulation_and_recover_exercises()

