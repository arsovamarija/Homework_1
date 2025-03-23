import unittest
from power_flow import dec_compare, power_flow, S_max  # Import the new power_losses function

class TestPowerFlow(unittest.TestCase):

    def test_dec_compare(self):
        """Test decimal comparison function."""
        self.assertTrue(dec_compare(1.2341, 1.23449))  # Should be equal
        self.assertFalse(dec_compare(1.234, 1.235))  # Should not be equal

    def test_power_flow(self):
        """Test power flow calculation with known values."""
        U1, Un, R, X, B, P2, Q2, l = 112, 110, 0.07, 0.2, 1.4, 30, 15, 100
        U2, dP, dQ, S1_real, S1_imag = power_flow(U1, Un, R, X, B, P2, Q2, l)

        # Expected values will vary, use approximate checking
        self.assertTrue(0.90 * Un <= U2 <= 1.1 * Un)
        self.assertTrue(0 <= dP <= P2 * 0.05)  # Range of P losses in 5%
        self.assertTrue(-Q2 * 0.2 <= dQ <= Q2 * 0.2)  # Range of Q losses in 20%

    @unittest.expectedFailure
    def test_power_flow_fail(self):
        """This test is expected to fail, checking incorrect results."""
        U1, Un, R, X, B, P2, Q2, l = 112, 110, 0.07, 0.2, 1.4, 30, 15, 100
        U2, dP, dQ, S1_real, S1_imag = power_flow(U1, Un, R, X, B, P2, Q2, l)
        self.assertAlmostEqual(U2, 100, places=2)  # Wrong expected value, should fail

    def test_Smax(self):
        U1, Un, R, X, B, P2, cosfi, l = 112, 110, 0.07, 0.2, 1.4, 30, 0.8, 100
        Pmax, Qmax = S_max(P2, 0.8, U1, Un, R*l, X*l, B*l) # Call the S_max function to calculate the maximum apparent power (Pmax, Qmax)
        U2, dP, dQ, S1_real, S1_imag = power_flow(U1, Un, R, X, B, Pmax, Qmax, l)   # Implement power_flow function with calculated Pmax and Qmax
        self.assertAlmostEqual(U2, 0.9*Un, places=1) # Check if the resulting voltage U2 is within 90% of the nominal voltage (Un)

if __name__ == "__main__":
    unittest.main()