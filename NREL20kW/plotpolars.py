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
    p[1] = pd.read_csv(os.path.join('Airfoils','Plate.dat'),skiprows=55,nrows=52,delim_whitespace=True,header=None)
    p[2] = pd.read_csv(os.path.join('Airfoils','NACA4432-3D.dat'),skiprows=55,nrows=52,delim_whitespace=True,header=None)
    p[3] = pd.read_csv(os.path.join('Airfoils','NACA4430-2D.dat'),skiprows=55,nrows=52,delim_whitespace=True,header=None)
    p[4] = pd.read_csv(os.path.join('Airfoils','NACA4426-2D.dat'),skiprows=55,nrows=52,delim_whitespace=True,header=None)
    print(p[4].head())
    print(p[4].tail())
    return (p,)


@app.cell
def _(p, plt):
    f,ax = plt.subplots(2,1,figsize=(8,4))
    for i in range(4):
        ax[0].plot(p[i+1].iloc[:,0],p[i+1].iloc[:,1])
        ax[1].plot(p[i+1].iloc[:,0],p[i+1].iloc[:,2])
        ax[0].set_ylabel('Cl [-]')
        ax[1].set_ylabel('Cd [-]')
        ax[1].set_xlabel('AOA [deg]')
        ax[0].grid(True)
        ax[1].grid(True)
        ax[0].legend(['Plate','NACA4432-3D','NACA4430-2D','NACA4426-2D'])
    plt.tight_layout()
    plt.savefig('Polars.png')
    f
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
