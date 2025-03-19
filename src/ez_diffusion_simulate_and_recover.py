#!/usr/bin/env python3
import numpy as np

class EZ_diffusion_simulate_and_recover:
    def __init__(self, sample_size: int):
        self._n = sample_size   # sample size for the simulation
    
    def generate_true_parameters(self):
        """Randomly sample parameters within realistic cognitive model ranges."""
        v_true = np.random.uniform(0.5, 2)  # Drift rate
        a_true = np.random.uniform(0.5, 2)  # Boundary separation
        t_true = np.random.uniform(0.1, 0.5)  # Nondecision time
        return v_true, a_true, t_true

    def generate_predicted_summary_statistics(self, v_true, a_true, t_true):
        """use Forward EZ equations"""
        y = np.exp(-a_true * v_true)
        # Ensure v is not zero to prevent division by zero error
        if v_true == 0:
            m_pred = t_true  # Assign a reasonable default value when drift rate is 0
        else:
            m_pred = t_true + (a_true / (2 * v_true)) * ((1 - y) / (1 + y))

        r_pred = 1 / (y + 1)
        v_pred = (a_true / (2 * v_true**3)) * ((1 - 2 * a_true * v_true * y - y**2) / ((1 + y)**2))

        return r_pred, m_pred, v_pred

    def simulate_observed_summary_statistics(self, r_pred, m_pred, v_pred):
        """Simulate observed accuracy, mean RT, and variance using sampling distributions."""
        r_obs = np.random.binomial(self._n, r_pred) / self._n
        #m_obs = np.random.normal(m_pred, np.sqrt(v_pred / self._n))
        m_obs = np.random.normal(m_pred, (v_pred / self._n))
        v_obs = np.random.gamma((self._n - 1) / 2, (2 * v_pred) / (self._n - 1))
        return r_obs, m_obs, v_obs
    

    def compute_estimated_parameters_to_recover(self, r_obs, m_obs, v_obs):
        """Use Inverse EZ equations to estimate drift rate (v_est), boundary separation (a_est), and nondecision time (t_est)."""
        # Ensure R_obs is between 0 and 1 to avoid divide by 0 in L formula
        r_obs = max(min(r_obs, 0.9999), 0.0001)

        L = np.log(r_obs / (1 - r_obs))

        v_est = np.sign(r_obs - 0.5) * np.sqrt(np.sqrt((L * (r_obs**2 * L - r_obs * L + r_obs - 0.5)) / v_obs))
        if v_est == 0:
            a_est = 0
            t_est = 0
        else:
            a_est = L / v_est
            t_est = m_obs - (a_est / (2 * v_est)) * ((1 - np.exp(-v_est * a_est)) / (1 + np.exp(-v_est * a_est)))
    
        return v_est, a_est, t_est


    def compute_bias_and_squared_error(self, v_true, a_true, t_true, v_est, a_est, t_est):
        """Calculate bias and squared error."""
        bias = np.array([v_true - v_est, a_true - a_est, t_true - t_est])
        squared_error = bias ** 2
        return bias, squared_error

    def simulate_and_recover(self):
        # Step 1: Select some ‘true’ parameters (ν, α, τ) and a sample size N
        v_true, a_true, t_true = self.generate_true_parameters()
        # Step 2: Generate ‘predicted’ summary statistics
        r_pred, m_pred, v_pred = self.generate_predicted_summary_statistics(v_true, a_true, t_true)
        # Step 3: Simulate ‘observed’ summary statistics
        r_obs, m_obs, v_obs = self.simulate_observed_summary_statistics(r_pred, m_pred, v_pred)
        # Step 4: Compute ‘estimated’ parameters (ν_est, α_est, τ_est)
        v_est, a_est, t_est = self.compute_estimated_parameters_to_recover(r_obs, m_obs, v_obs)
        # Step 5: Compute the estimation bias b = (ν, α, τ ) − (νest, αest, τ est) and squared error b^2
        bias, squared_error = self.compute_bias_and_squared_error(v_true, a_true, t_true, v_est, a_est, t_est)
        return bias, squared_error
