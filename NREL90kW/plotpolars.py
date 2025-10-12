import marimo

__generated_with = "0.16.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    return os, pd, plt


@app.cell
def _(os, pd):
    p = {}
    p[1] = pd.read_csv(os.path.join('AeroData','Polars','Polar_001.dat'),skiprows=54,nrows=362,delim_whitespace=True,header=None)
    p[2] = pd.read_csv(os.path.join('AeroData','Polars','Polar_006.dat'),skiprows=54,nrows=362,delim_whitespace=True,header=None)
    p[3] = pd.read_csv(os.path.join('AeroData','Polars','Polar_011.dat'),skiprows=54,nrows=362,delim_whitespace=True,header=None)
    p[4] = pd.read_csv(os.path.join('AeroData','Polars','Polar_016.dat'),skiprows=54,nrows=362,delim_whitespace=True,header=None)
    print(p[2].head())
    print(p[2].tail())
    return (p,)


@app.cell
def _(p, plt):
    f,ax = plt.subplots(3,1,figsize=(8,6))
    for i in range(4):
        ax[0].plot(p[i+1].iloc[:,0],p[i+1].iloc[:,1])
        ax[1].plot(p[i+1].iloc[:,0],p[i+1].iloc[:,2])
        ax[2].plot(p[i+1].iloc[:,0],p[i+1].iloc[:,3])
        ax[0].set_ylabel('Cl [-]')
        ax[1].set_ylabel('Cd [-]')
        ax[2].set_ylabel('Cm [-]')
        ax[2].set_xlabel('AOA [deg]')
        ax[0].grid(True)
        ax[1].grid(True)
        ax[2].grid(True)
        ax[0].legend(['Airfoil-001','Airfoil-006','Airfoil-011','Airfoil-016'])
    plt.tight_layout()
    plt.savefig('Polars.png')
    f
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
