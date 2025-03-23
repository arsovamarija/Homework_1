import math 

def dec_compare(x, y):
    """Compare values up to 3 decimal places."""
    return round(x, 3) == round(y, 3)

def power_flow(U1, Un, R, X, B, P2, Q2, l):
    """Compute the power flow and voltage drops."""
    # Scale resistance, reactance, and susceptance by line length
    R, X, B = R * l, X * l, B * l
    U2 = Un  # Initialize voltage U2

    for _ in range(20):  # Maximum 20 iterations
        Qc2 = (B / 2) * U2**2 / 1e6  # Calculate reactive power compensation
        Q2 -= Qc2  # Adjust Q2 value

        # Compute voltage drops in real and reactive components
        dUd, dUq = (P2 * R + Q2 * X) / U2, (P2 * X - Q2 * R) / U2
        U2_new = math.sqrt(U1**2 - dUq**2) - dUd  # Compute new voltage

        if dec_compare(U2, U2_new):  # Check for convergence
            break
        U2, Q2 = U2_new, Q2 + Qc2  # Update U2 and reset Q2

    # Compute power losses
    dP, dQ = ((P2**2 + Q2**2) / U2**2) * R, ((P2**2 + Q2**2) / U2**2) * X
    Qc1 = (B / 2) * U1**2 / 1e6  # Compute reactive compensation at start
    return U2, dP, dQ, P2 + dP, Q2 + dQ - Qc1  # Return computed values

def S_max(P, cosfi, U1, Un, R, X, B):
    """Calculate the apparent power S (and corresponding P, Q) that result in U2 = 90% of nominal voltage."""
    U2_target, Qc2, S = 0.9 * Un, (B / 2) * (0.9 * Un) ** 2 / 1e6, P  # Set target voltage, reactive compensation, and initial S
    
    for _ in range(1000):  # Loop up to 1000 iterations
        P2, Q2 = S * cosfi, S * math.sqrt(1 - cosfi ** 2) - Qc2  # Calculate active and reactive power
        dUd, dUq = (P2 * R + Q2 * X) / U2_target, (P2 * X - Q2 * R) / U2_target  # Calculate voltage drops
        U2_new = math.sqrt(U1 ** 2 - dUq ** 2) - dUd  # New voltage at the end of the line
        if  U2_new <= U2_target: break  # Check if voltage is below target
        S += 0.1  #  # If not, increment the apparent power S to bring U2 closer to the target
    P_max, Q_max = S * cosfi, S * math.sqrt(1 - cosfi ** 2)  #Return the active power (P) and reactive power (Q) corresponding to the final apparent power (S)

    return P_max, Q_max  # Return maximum active power (P) and maximum reactive power (Q)
