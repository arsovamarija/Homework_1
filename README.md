# Homework_1

This repository contains a set of functions that model the behavior of electrical transmission lines. Specifically, the functions calculate how power flows through the lines and how voltage drops across the line due to resistance and reactance. These calculations are essential for understanding the efficiency of power transmission, how much energy is lost as it travels along the line, and ensuring that the system operates within safe voltage limits. Additionally, the functions help determine the maximum amount of power that can be transmitted through the line while maintaining stable voltage at the end of the line, which is crucial for safe and efficient energy distribution.

## Functions:

- **`dec_compare(x, y)`**  
This function compares two decimal numbers (x and y) up to three decimal places. It is useful for checking whether two values are close enough to each other, which is important when iterating to find a solution. For example, in the power flow calculations, we want to see if the voltage at the end of the line has stabilized, and this function helps to confirm that.

- **`power_flow(U1, Un, R, X, B, P2, Q2, l)`**
  This function calculates the power flow through a transmission line and the voltage drop across the line. It considers several key factors:

  *Starting Voltage (U1): The voltage at the beginning of the line.*

  *Nominal Voltage (Un): The target voltage that should be maintained at the end of the line.*

  *Resistance (R) and Reactance (X): These values describe how the line resists and reacts to the flow of electrical current.*

  *Susceptance (B): A value related to how the line stores and releases electrical energy.*

  *Power at the end of the line (P2): The amount of active (real) power being delivered at the end of the line.*

  *Reactive Power (Q2): The portion of power that oscillates between the source and load, which doesn’t do useful work but is necessary for maintaining voltage levels.*

  *Line Length (l): The length of the transmission line, which affects the resistance and reactance.*

  The function adjusts for the line length by scaling the resistance, reactance, and susceptance accordingly. It also calculates how much power is lost due to these factors, and returns the final voltage at the end of the line along with the power losses. This helps ensure that the line can deliver power efficiently while minimizing losses.

- **`S_max(P, cosfi, U1, Un, R, X, B)`**  
This function calculates the maximum amount of power that can be sent through the line while ensuring that the voltage at the end of the line stays above 90% of the nominal voltage (Un). This is important because if the voltage drops too low, it can cause electrical equipment to malfunction or even damage sensitive components in the grid.

  *Apparent Power (S): This is the total power being transmitted, including both active power (P) and reactive power (Q).*

  *Power Factor (cosfi): This indicates how efficiently electrical power is being used. A power factor of 1 means all the power is being used effectively.*

  The function iterates by increasing the apparent power until the voltage at the end of the line drops to 90% of the nominal voltage. It then returns the maximum active and reactive power that can be delivered through the line without violating the voltage limit. The maximum active and reactive power are crucial because they determine the system's capacity to deliver power safely. Knowing these values helps engineers design transmission systems that operate efficiently and avoid overloading.

## Note:
I intentionally allowed `ruff` to handle the formatting. This results in the code exceeding the 40-line limit. While it could be manually compacted (as it was in the beginning), I decided to keep both the `format` and `check` functions in the project. This choice was made to fully demonstrate the implementation and functionality of `ruff`'s formatting feature, rather than just using the `check` function.

## License

Copyright 2025 Marija Arsova

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
