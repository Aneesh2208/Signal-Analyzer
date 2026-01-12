# Signal Analyzer Project Report

## Abstract
This project presents the design and implementation of a Python-based Signal Analyzer to generate and visualize standard continuous-time and discrete-time signals commonly used in Electronics and Communication Engineering (ECE). The system supports key signals including unit step, ramp, sinusoidal waveforms, exponential decay, and impulse (discrete) / impulse-like approximation (continuous). A consistent plotting pipeline is developed to automatically generate and save labeled signal plots. The results demonstrate clear differences between continuous-time and discrete-time representations, providing a strong foundation for future extensions such as signal operations, LTI system analysis, and convolution-based validation.


## Introduction
Signals form the mathematical foundation of ECE, representing physical quantities such as voltage, current, electromagnetic waves, and information-bearing waveforms. Understanding how signals behave in time and how they differ in continuous-time and discrete-time domains is essential before progressing to advanced topics such as digital signal processing, communication systems, and semiconductor timing analysis.

This project focuses on building a reusable Signal Analyzer that can generate standard test signals and visualize them clearly. The system is implemented in Python using NumPy for signal generation and Matplotlib for plotting. The generated plots are saved in a structured format to support documentation, reporting, and future experimentation.


## Methodology
The project is implemented using a modular Python structure. Signal generation and plotting are separated into dedicated source files to maintain readability and reusability.

### Signal Generation
A set of standard signals is generated for both time domains:

**Continuous-time (CT) signals** are generated over a dense time grid:
- Time axis: \( t \in [-1, 1] \)
- Generated signals:
  - Unit step \( u(t) \)
  - Ramp \( r(t) = t\,u(t) \)
  - Sine wave \( x(t) = A\sin(2\pi ft + \phi) \)
  - Exponential decay \( x(t) = e^{-at}u(t) \)
  - Impulse-like approximation (finite-width pulse with unit area)

**Discrete-time (DT) signals** are generated over integer sample indices:
- Index axis: \( n \in [-20, 20] \)
- Generated signals:
  - Unit step \( u[n] \)
  - Ramp \( r[n] = n\,u[n] \)
  - Sine sequence \( x[n] = A\sin(2\pi fn + \phi) \)
  - Exponential decay \( x[n] = a^n u[n] \)
  - Unit impulse \( \delta[n] \)

### Plotting and Output Storage
To ensure consistent visuals across the project, all plotting logic is implemented in a reusable plotting utility module. Both CT (line plots) and DT (stem plots) signals are visualized with proper titles, axis labels, and grid formatting.

All generated plots are saved automatically into a structured directory:
- `plots/signals/` for signal visualization
- additional folders reserved for future project stages such as operations and convolution

### Execution Pipeline
A single runner script (`main.py`) is used to execute the complete pipeline:
1. Generate CT and DT signal sets
2. Plot each signal
3. Save all results as `.png` files
4. Generate comparison plots (CT vs DT)


## Results
(To be updated)

## Theory and Validation
(To be updated)

## Conclusion
(To be updated)
