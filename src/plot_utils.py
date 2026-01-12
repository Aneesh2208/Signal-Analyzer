##PLOT UTILITIES MODULE
#HAS PLOT CODES THAT ARE REUSEABLE, for both CT and DT signals.
#this keeps the plots consistent and avoids repetition of code.

import os
import numpy as np
import matplotlib.pyplot as plt


def ensure_folder(folder_path):
    """
    ENSURE THAT A FOLDER EXISTS. IF NOT, CREATE IT.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


##PLOTTING CONTINUOUS-TIME SIGNALS
def plot_ct_signal(t, x, title, filename, folder="plots/signals"):
    """
    Plot a continuous-time (CT) signal.

    Inputs:
    - t: time array
    - x: signal array x(t)
    - title: plot title (string)
    - filename: name of the png file to save
    - folder: folder path where plot is saved
    """

    ensure_folder(folder)
    plt.figure()
    plt.plot(t, x)
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    save_path = os.path.join(folder, filename)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()



##PLOTTING DISCRETE-TIME SIGNALS
def plot_dt_signal(n, x, title, filename, folder="plots/signals"):
    """
    Plot a discrete-time (DT) signal.

    Inputs:
    - n: index array
    - x: signal array x[n]
    - title: plot title (string)
    - filename: name of the png file to save
    - folder: folder path where plot is saved
    """

    ensure_folder(folder)
    plt.figure()
    markerline, stemlines, baseline = plt.stem(n, x)
    plt.xlabel("Index (n)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    save_path = os.path.join(folder, filename)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


##plotting comparision of two signals
def plot_ct_dt_comparison(t, x_ct, n, x_dt, title, filename, folder="plots/signals"):
    """
    Plot CT and DT versions of a signal in one figure (side-by-side).

    Inputs:
    - t, x_ct: continuous-time signal
    - n, x_dt: discrete-time signal
    - title: overall title
    - filename: save filename
    - folder: folder path
    """

    ensure_folder(folder)
    plt.figure(figsize=(10, 4))

    # ---- CT subplot ----
    plt.subplot(1, 2, 1)
    plt.plot(t, x_ct)
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude")
    plt.title("Continuous-Time")
    plt.grid(True)

    # ---- DT subplot ----
    plt.subplot(1, 2, 2)
    plt.stem(n, x_dt)
    plt.xlabel("Index (n)")
    plt.ylabel("Amplitude")
    plt.title("Discrete-Time")
    plt.grid(True)

    plt.suptitle(title)
    save_path = os.path.join(folder, filename)
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.close()


##SET FORMATTING PARAMETERS FOR ALL PLOTS
def set_plot_style():

    plt.rcParams["font.size"] = 11
    plt.rcParams["axes.titlesize"] = 12
    plt.rcParams["axes.labelsize"] = 11
    plt.rcParams["legend.fontsize"] = 10
    plt.rcParams["figure.titlesize"] = 13
