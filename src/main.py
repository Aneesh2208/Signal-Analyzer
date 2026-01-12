import numpy as np

# Import convolution functions
from convolution import (
    conv_dt_manual, conv_dt_numpy,
    conv_output_index_dt,
    conv_ct_manual
)

# to be done after code in signal_operations is ready:
from signal_operations import (
    amplitude_scale,
    time_shift_ct, time_reverse_ct,
    shift_dt, reverse_dt,
    add_signals, multiply_signals
)

from signal_generator import (
    unit_step_ct, ramp_ct, sin_ct, exp_decay_ct, impulse_like_ct,
    unit_step_dt, ramp_dt, sin_dt, exp_decay_dt, impulse_dt
)

from plot_utils import (
    set_plot_style, plot_ct_signal, plot_dt_signal, plot_ct_dt_comparison
)


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
    # PLOT AND SAVE CT SIGNALS
    # ============================================================
    plot_ct_signal(t, u_ct, "CT Unit Step u(t)", "ct_unit_step.png")
    plot_ct_signal(t, r_ct, "CT Ramp r(t)", "ct_ramp.png")
    plot_ct_signal(t, s_ct, "CT Sine Wave x(t) = sin(2πft) (RANDOM)", "ct_sine.png")
    plot_ct_signal(t, e_ct, "CT Exponential Decay x(t) = e^(-at)u(t) (RANDOM)", "ct_exp_decay.png")
    plot_ct_signal(t, imp_ct, "CT Impulse-like Approximation (RANDOM)", "ct_impulse_like.png")

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

    # ============================================================
    # PLOT AND SAVE DT SIGNALS
    # ============================================================
    plot_dt_signal(n, u_dt, "DT Unit Step u[n]", "dt_unit_step.png")
    plot_dt_signal(n, r_dt, "DT Ramp r[n]", "dt_ramp.png")
    plot_dt_signal(n, s_dt, "DT Sine Sequence x[n] = sin(2πfn) (RANDOM)", "dt_sine.png")
    plot_dt_signal(n, e_dt, "DT Exponential Decay x[n] = a^n u[n] (RANDOM)", "dt_exp_decay.png")
    plot_dt_signal(n, imp_dt, "DT Impulse δ[n]", "dt_impulse.png")

    # ============================================================
    # CT vs DT COMPARISON PLOTS
    # ============================================================
    plot_ct_dt_comparison(
        t, u_ct,
        n, u_dt,
        "Unit Step: Continuous vs Discrete",
        "compare_step.png"
    )

    plot_ct_dt_comparison(
        t, r_ct,
        n, r_dt,
        "Ramp: Continuous vs Discrete",
        "compare_ramp.png"
    )

    # ============================================================
    # SIGNAL OPERATIONS (CT + DT)
    # ============================================================

    # CT sine operations
    s_ct_scaled = amplitude_scale(s_ct, scale=2)
    t_s_ct_signal, s_ct_shifted = time_shift_ct(t, s_ct, shift=0.2)
    t_s_ct_reversed, s_ct_reversed = time_reverse_ct(t, s_ct)

    plot_ct_signal(t, s_ct, "CT Sine (random original)", "ct_sine_original.png", folder="plots/operations/ct")
    plot_ct_signal(t, s_ct_scaled, "CT Sine (random scaled)", "ct_sine_scaled.png", folder="plots/operations/ct")
    plot_ct_signal(t_s_ct_signal, s_ct_shifted, "CT Sine (random shifted)", "ct_sine_shifted.png", folder="plots/operations/ct")
    plot_ct_signal(t_s_ct_reversed, s_ct_reversed, "CT Sine (random reversed)", "ct_sine_reversed.png", folder="plots/operations/ct")

    # DT sine operations
    s_dt_scaled = amplitude_scale(s_dt, scale=2)
    n_s_dt_signal, s_dt_shifted = shift_dt(n, s_dt, shift=3)
    n_s_dt_reversed, s_dt_reversed = reverse_dt(n, s_dt)

    plot_dt_signal(n, s_dt, "DT Sine (random original)", "dt_sine_original.png", folder="plots/operations/dt")
    plot_dt_signal(n, s_dt_scaled, "DT Sine (random scaled)", "dt_sine_scaled.png", folder="plots/operations/dt")
    plot_dt_signal(n_s_dt_signal, s_dt_shifted, "DT Sine (random shifted)", "dt_sine_shifted.png", folder="plots/operations/dt")
    plot_dt_signal(n_s_dt_reversed, s_dt_reversed, "DT Sine (random reversed)", "dt_sine_reversed.png", folder="plots/operations/dt")

    # ADD/MULTIPLY operations
    s_plus_u_ct = add_signals(s_ct, u_ct)
    s_mult_u_ct = multiply_signals(s_ct, u_ct)

    plot_ct_signal(t, s_plus_u_ct, "CT Sine + Unit Step (random)", "ct_sine_plus_step.png", folder="plots/operations/ct")
    plot_ct_signal(t, s_mult_u_ct, "CT Sine * Unit Step (random)", "ct_sine_mult_step.png", folder="plots/operations/ct")

    s_plus_u_dt = add_signals(s_dt, u_dt)
    s_mult_u_dt = multiply_signals(s_dt, u_dt)

    plot_dt_signal(n, s_plus_u_dt, "DT Sine + Unit Step (random)", "dt_sine_plus_step.png", folder="plots/operations/dt")
    plot_dt_signal(n, s_mult_u_dt, "DT Sine * Unit Step (random)", "dt_sine_mult_step.png", folder="plots/operations/dt")

    # ============================================================
    # CONVOLUTION (DT)
    # ============================================================

    x_dt = s_dt
    h_dt = imp_dt

    n_y = conv_output_index_dt(n, n)
    y_dt_manual = conv_dt_manual(x_dt, h_dt)
    y_dt_np = conv_dt_numpy(x_dt, h_dt)

    dt_error = y_dt_manual - y_dt_np
    dt_max_error = np.max(np.abs(dt_error))
    dt_rmse = np.sqrt(np.mean(dt_error**2))

    print("\n============== DT Convolution Validation ==============")
    print("Property tested: Manual convolution ≈ NumPy convolution")
    print(f"Max absolute error: {dt_max_error:.12f}")
    print(f"RMSE: {dt_rmse:.12f}")
    print("=======================================================\n")

    plot_dt_signal(n, x_dt, "DT Input x[n] (random sine)", "conv_dt_x.png", folder="plots/convolution")
    plot_dt_signal(n, h_dt, "DT System h[n] (impulse)", "conv_dt_h.png", folder="plots/convolution")
    plot_dt_signal(n_y, y_dt_manual, "DT Output y[n] (Manual Convolution)", "conv_dt_y_manual.png", folder="plots/convolution")
    plot_dt_signal(n_y, y_dt_np, "DT Output y[n] (NumPy Convolution)", "conv_dt_y_numpy.png", folder="plots/convolution")

    # ============================================================
    # DT IMPULSE PROPERTY VALIDATION
    # x[n] * δ[n] = x[n]
    # ============================================================

    mask_dt = (n_y >= n[0]) & (n_y <= n[-1])
    n_y_crop = n_y[mask_dt]
    y_crop = y_dt_manual[mask_dt]

    if len(y_crop) == len(x_dt):
        err_imp = x_dt - y_crop
        max_err_imp = np.max(np.abs(err_imp))
        rmse_imp = np.sqrt(np.mean(err_imp**2))

        print("\n============ DT Impulse Property Validation ===========")
        print("Property tested: x[n] * δ[n] = x[n]")
        print(f"Max absolute error: {max_err_imp:.12f}")
        print(f"RMSE: {rmse_imp:.12f}")
        print("=======================================================\n")
    else:
        print("\nDT impulse validation skipped: length mismatch.")
        print(f"len(y_crop)={len(y_crop)}, len(x_dt)={len(x_dt)}\n")

    import matplotlib.pyplot as plt
    import os

    os.makedirs("plots/convolution", exist_ok=True)

    plt.figure(figsize=(10, 5))
    plt.stem(n, x_dt, label="x[n] input")
    plt.stem(n_y_crop, y_crop, label="y[n] = x*δ (manual)")
    plt.title("DT Impulse Property Validation: x[n] vs y[n]")
    plt.xlabel("n")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/convolution/dt_impulse_property_overlay.png", dpi=300)
    plt.close()



    # ============================================================
    # CONVOLUTION (CT)
    # ============================================================

    x_ct = s_ct
    h_ct = imp_ct

    t_y_ct, y_ct = conv_ct_manual(t, x_ct, h_ct)

    plot_ct_signal(t, x_ct, "CT Input x(t) (random sine)", "conv_ct_x.png", folder="plots/convolution")
    plot_ct_signal(t, h_ct, "CT System h(t) (impulse-like random)", "conv_ct_h.png", folder="plots/convolution")
    plot_ct_signal(t_y_ct, y_ct, "CT Output y(t) = x(t) * h(t)", "conv_ct_y.png", folder="plots/convolution")

    t_y_ct, y_ct = conv_ct_manual(t, x_ct, h_ct)

    mask_ct = (t_y_ct >= t[0]) & (t_y_ct <= t[-1])
    t_y_crop_ct = t_y_ct[mask_ct]
    y_crop_ct = y_ct[mask_ct]

    y_interp_ct = np.interp(t, t_y_crop_ct, y_crop_ct)

    ct_error = x_ct - y_interp_ct
    ct_max_error = np.max(np.abs(ct_error))
    ct_rmse = np.sqrt(np.mean(ct_error**2))

    print("\n============== CT Convolution Validation ==============")
    print("Property tested: x(t) * δ(t) ≈ x(t)")
    print(f"Max absolute error: {ct_max_error:.6f}")
    print(f"RMSE: {ct_rmse:.6f}")
    print("=======================================================\n")

    # Save input + aligned output plots
    plot_ct_signal(t, x_ct, "CT Validation Input x(t)", "ct_validation_input.png", folder="plots/convolution")
    plot_ct_signal(t, y_interp_ct, "CT Validation Output y(t) aligned", "ct_validation_output_aligned.png", folder="plots/convolution")

    # Save overlay plot
    import matplotlib.pyplot as plt
    import os

    os.makedirs("plots/convolution", exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(t, x_ct, label="x(t) input")
    plt.plot(t, y_interp_ct, "--", label="y(t) = x*h (aligned)")
    plt.title("CT Validation: x(t) vs y(t) (Impulse-like Convolution)")
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/convolution/ct_validation_overlay.png", dpi=300)
    plt.close()


    # ============================================================
    # CT IMPULSE PROPERTY VALIDATION
    # x(t) * δ(t) ≈ x(t)
    # ============================================================

    mask_ct = (t_y_ct >= t[0]) & (t_y_ct <= t[-1])
    t_y_crop_ct = t_y_ct[mask_ct]
    y_crop_ct = y_ct[mask_ct]

    y_interp_ct = np.interp(t, t_y_crop_ct, y_crop_ct)

    ct_error = x_ct - y_interp_ct
    ct_max_error = np.max(np.abs(ct_error))
    ct_rmse = np.sqrt(np.mean(ct_error**2))

    print("\n============== CT Convolution Validation ==============")
    print("Property tested: x(t) * δ(t) ≈ x(t)")
    print(f"Max absolute error: {ct_max_error:.6f}")
    print(f"RMSE: {ct_rmse:.6f}")
    print("=======================================================\n")

# ============================================================
# CT IMPULSE WIDTH VALIDATION (ONLY 1 RANDOM WIDTH)
# ============================================================

    print("\n============== CT IMPULSE WIDTH VALIDATION ============")

    width = rng.uniform(0.005, 0.05)   

    h_ct_test = impulse_like_ct(t, width=width)
    t_y_ct_test, y_ct_test = conv_ct_manual(t, x_ct, h_ct_test)

    mask_test = (t_y_ct_test >= t[0]) & (t_y_ct_test <= t[-1])
    t_y_crop_test = t_y_ct_test[mask_test]
    y_crop_test = y_ct_test[mask_test]
    y_interp_test = np.interp(t, t_y_crop_test, y_crop_test)

    error_test = x_ct - y_interp_test
    max_error_test = np.max(np.abs(error_test))
    rmse_test = np.sqrt(np.mean(error_test**2))

    print(f"Impulse width used: {width:.4f}")
    print("Property tested: x(t) * h_width(t) ≈ x(t)")
    print(f"Max absolute error: {max_error_test:.6f}")
    print(f"RMSE: {rmse_test:.6f}")
    print("=======================================================\n")

    os.makedirs("plots/convolution", exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(t, x_ct, label="x(t) input")
    plt.plot(t, y_interp_test, "--", label=f"y(t) width={width:.4f}")
    plt.title("CT Random Width Validation: x(t) vs y(t)")
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/convolution/ct_width_random_overlay.png", dpi=300)
    plt.close()



if __name__ == "__main__":
    main()
