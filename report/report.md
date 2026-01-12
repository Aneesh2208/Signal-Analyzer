# Signal Analyzer (ECE) — Project Report

## 1. Title
**Signal Analyzer (ECE): Generation, Visualization, Operations, and Convolution of CT & DT Signals using Python**

---

## 2. Objective
The objective of this project is to build a Python-based mini toolkit that can:

1. Generate standard **Continuous-Time (CT)** and **Discrete-Time (DT)** signals.
2. Visualize them using proper plots.
3. Perform basic **signal operations** such as:
   - amplitude scaling
   - shifting
   - time reversal
   - addition and multiplication
4. Implement **Discrete-Time convolution** manually and verify it using NumPy.
5. Implement **Continuous-Time convolution** using numerical approximation and validate the impulse property.

This project builds foundational understanding of signals and systems concepts used in Electronics and Communication Engineering.

---

## 3. Tools / Technologies Used
- **Python 3**
- **NumPy** (numerical computation, arrays, convolution)
- **Matplotlib** (plotting and saving graphs)
- VS Code (development environment)

---

## 4. System Overview (Modules)

### 4.1 `signal_generator.py`
This module generates standard CT and DT signals.

#### Continuous-Time Signals
- Unit step: $u(t)$
- Ramp: $r(t)$
- Sine: $x(t) = \sin(2\pi f t)$
- Exponential decay: $x(t) = e^{-at}\,u(t)$
- Impulse-like approximation (finite narrow pulse)

#### Discrete-Time Signals
- Unit step: $u[n]$
- Ramp: $r[n]$
- Sine: $x[n] = \sin(2\pi f n)$
- Exponential decay: $x[n] = a^n u[n]$
- Unit impulse: $\delta[n]$

---

### 4.2 `plot_utils.py`
This module handles clean plotting and saving results.
Main utilities:
- consistent theme/style
- CT plotting
- DT stem plots
- CT vs DT comparison plots

All plots are saved automatically inside the `plots/` folder.

---

### 4.3 `signal_operations.py`
This module implements operations on signals.

#### CT Operations
- Amplitude scaling: $y(t) = A\,x(t)$
- Time shifting: $y(t) = x(t - t_0)$
- Time reversal: $y(t) = x(-t)$

#### DT Operations
- Amplitude scaling: $y[n] = A\,x[n]$
- Index shifting: $y[n] = x[n - k]$
- Time reversal: $y[n] = x[-n]$

#### Combining Signals
- Addition: $y = x_1 + x_2$
- Multiplication: $y = x_1 \cdot x_2$

---

### 4.4 `convolution.py`
This module implements convolution.

#### Discrete-Time Convolution
Manual convolution uses the summation:

$$
y[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]
$$

NumPy validation uses:
```python
np.convolve(x, h)
