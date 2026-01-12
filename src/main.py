import numpy as np

from signal_generator import (
    unit_step_ct, ramp_ct, sin_ct, exp_decay_ct, impulse_like_ct,
    unit_step_dt, ramp_dt, sin_dt, exp_decay_dt, impulse_dt
)

from plot_utils import set_plot_style

def main():
    set_plot_style()

    # RANDOMIZATION SETUP
    seed = None
    rng = np.random.default_rng(seed)

    # ============================================================
    # CONTINUOUS-TIME (CT) SETUP
    # ============================================================
    t = np.linspace(-1, 1, 2000)

    # RANDOM CT PARAMETERS
    A_ct = rng.uniform(0.5, 2.0)
    f_ct = rng.uniform(2.0, 10.0)
    phase_ct = rng.uniform(0.0, 2*np.pi)
    a_ct = rng.uniform(0.5, 5.0)
    width_imp_ct = rng.uniform(0.005, 0.05)
    noise_std_ct = rng.uniform(0.0, 0.05)

    print("\n================ RANDOM CT PARAMETERS ================")
    print(f"A_ct = {A_ct:.3f}")
    print(f"f_ct = {f_ct:.3f} Hz")
    print(f"phase_ct = {phase_ct:.3f} rad")
    print(f"a_ct = {a_ct:.3f}")
    print(f"impulse width = {width_imp_ct:.4f}")
    print(f"noise std = {noise_std_ct:.4f}")
    print("=======================================================")

    u_ct = unit_step_ct(t)
    r_ct = ramp_ct(t)

    # Randomized sine
    s_ct = sin_ct(t, f=f_ct, A=A_ct, phase=phase_ct)

    # Randomized exp decay
    e_ct = exp_decay_ct(t, a=a_ct)

    # Randomized impulse width
    imp_ct = impulse_like_ct(t, width=width_imp_ct)

    # Add random noise (same variable s_ct)
    noise_ct = noise_std_ct * rng.standard_normal(len(t))
    s_ct = s_ct + noise_ct

    # ============================================================
    # DISCRETE-TIME (DT) SETUP
    # ============================================================
    n = np.arange(-20, 21, 1)

    # RANDOM DT PARAMETERS
    A_dt = rng.uniform(0.5, 2.0)
    f_dt = rng.uniform(0.05, 0.45)   # cycles/sample
    phase_dt = rng.uniform(0.0, 2*np.pi)
    a_dt = rng.uniform(0.7, 0.99)

    print("\n================ RANDOM DT PARAMETERS =================")
    print(f"A_dt = {A_dt:.3f}")
    print(f"f_dt = {f_dt:.3f} cycles/sample")
    print(f"phase_dt = {phase_dt:.3f} rad")
    print(f"a_dt = {a_dt:.3f}")
    print("=======================================================")

    u_dt = unit_step_dt(n)
    r_dt = ramp_dt(n)

    # Randomized sine
    s_dt = sin_dt(n, f=f_dt, A=A_dt, phase=phase_dt)

    # Randomized exp decay
    e_dt = exp_decay_dt(n, a=a_dt)

    imp_dt = impulse_dt(n)
