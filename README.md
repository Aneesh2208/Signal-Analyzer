# Signal Analyzer Toolkit (CT & DT) with Convolution Validation

A Python-based toolkit for generating and analyzing continuous-time (CT) and discrete-time (DT) signals, performing fundamental signal operations, and validating LTI system convolution (DT + CT) using both theoretical properties and numerical simulations.

---

## 🚀 Project Highlights
- Generated standard **CT and DT signals** (step, ramp, sine, exponential decay, impulse/impulse-like).
- Implemented core **signal operations**:
  - amplitude scaling
  - time shifting
  - time reversal
  - signal addition and multiplication
- Implemented **Discrete-Time Convolution**:
  - manual convolution (nested-loop implementation)
  - NumPy convolution (validation baseline)
- Implemented **Continuous-Time Convolution (numerical)**:
  - approximated CT convolution using discrete samples and scaling by `dt`
  - impulse-like convolution validation with time-axis alignment
- Added **validation metrics**:
  - Max absolute error
  - RMSE
- Added **randomization** of key parameters (frequency/amplitude/phase/noise/impulse width) to ensure the toolkit works for general signals.

---

## 📁 Folder Structure

```bash
Signal-Analyzer-ECE/
├── src/
│   ├── main.py
│   ├── signal_generator.py
│   ├── signal_operations.py
│   ├── convolution.py
│   └── plot_utils.py
├── plots/
│   ├── signals/
│   ├── operations/
│   │   ├── ct/
│   │   └── dt/
│   └── convolution/
├── report/
│   └── project_report.md
├── README.md
├── requirements.txt
└── .gitignore
```
---

## 🧠 Concepts Covered
This project strengthens fundamentals in:
- Signals and Systems (CT & DT)
- LTI System properties
- Convolution (DT exact + CT numerical approximation)
- Impulse response & impulse property
- Time-index alignment for convolution outputs
- Validation of simulations using numerical error metrics

---

## ✅ Outputs (Plots & Validation)
### Signal Generation
- CT: unit step, ramp, sine, exponential decay, impulse-like approximation
- DT: unit step, ramp, sine, exponential decay, impulse
- CT vs DT comparisons

### Operations
- scaling, shifting, reversal
- add and multiply with unit step (CT and DT)

### Convolution
- DT: manual vs NumPy convolution match validation
- DT impulse property: `x[n] * δ[n] = x[n]`
- CT: impulse-like convolution validation (`x(t) * δ(t) ≈ x(t)`)
- CT alignment + overlay comparison plots

---
