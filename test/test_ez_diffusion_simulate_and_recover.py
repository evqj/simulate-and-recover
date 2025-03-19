import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
import numpy as np
from ez_diffusion_simulate_and_recover import EZ_diffusion_simulate_and_recover

class Test_EZ_diffusion_simulate_and_recover(unittest.TestCase):

    def test_generate_true_parameters(self):
        """Test generate_true_parameters creates values in the expected range"""
        simul = EZ_diffusion_simulate_and_recover(100)
        v_true, a_true, t_true = simul.generate_true_parameters()

        self.assertTrue(0.5 <= v_true <= 2)
        self.assertTrue(0.5 <= a_true <= 2)
        self.assertTrue(0.1 <= t_true <= 0.5)

    def test_compute_predicted_statistics(self):
        """Test generate_predicted_summary_statistics returns values in the expected range"""
        simul = EZ_diffusion_simulate_and_recover(100)
        r_pred, m_pred, v_pred = simul.generate_predicted_summary_statistics(1.0, 1.0, 0.3)
        self.assertGreater(r_pred, 0)
        self.assertGreater(m_pred, 0)
        self.assertGreater(v_pred, 0)
    
    def test_simulate_observed_summary_statistics(self):
        simul = EZ_diffusion_simulate_and_recover(100)
        r_obs, m_obs, v_obs = simul.simulate_observed_summary_statistics(1.0, 1.0, 0.3)
        self.assertGreater(r_obs, 0)
        self.assertGreater(m_obs, 0)
        self.assertGreater(v_obs, 0)
    
    def test_compute_estimated_parameters_to_recover(self):
        simul = EZ_diffusion_simulate_and_recover(100)
        v_est, a_est, t_est = simul.compute_estimated_parameters_to_recover(1.0, 1.0, 0.3)
        self.assertTrue(v_est != 0)
        self.assertTrue(a_est != 0)
        self.assertTrue(t_est != 0)
    
    def test_compute_bias_and_squared_error(self):
        simul = EZ_diffusion_simulate_and_recover(10)
        bias, squared_error = simul.compute_bias_and_squared_error(1.0, 1.0, 0.3, 1.0, 1.0, 0.3)
        for b in bias:
            self.assertEqual(b, 0)
        for s in squared_error:
            self.assertEqual(s, 0)
    
    def test_simulate_and_recover(self):
        """Test squared error should decrease if sample size N is increased"""
        squared_errors1 = []
        squared_errors2 = []

        for _ in range(3000):
            simul1 = EZ_diffusion_simulate_and_recover(10)
            bias1, squared_error1 = simul1.simulate_and_recover()
            squared_errors1.append(squared_error1)
            simul2 = EZ_diffusion_simulate_and_recover(10000)
            bias2, squared_error2 = simul2.simulate_and_recover()
            squared_errors2.append(squared_error2)

        avg_squared_error1 = np.nanmean(squared_errors1, axis=0)
        avg_squared_error2 = np.nanmean(squared_errors2, axis=0)

        for se1, se2 in zip(avg_squared_error1, avg_squared_error2):
            self.assertTrue(se1 > se2)


if __name__ == "__main__":
    unittest.main()