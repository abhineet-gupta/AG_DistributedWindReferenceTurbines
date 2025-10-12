import marimo

__generated_with = "0.16.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import matplotlib.pyplot as plt
    import pandas as pd
    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv('spd_trq_gen.dat',header=None,delim_whitespace=True)
    return (df,)


@app.cell
def _(df, plt):
    plt.figure()
    plt.plot(df.iloc[:,0],df.iloc[:,1])
    plt.title('Variable Speed Torque Controller')
    plt.xlabel('Rotor Speed (RPM)')
    plt.ylabel('Generator Torque (Nm)')
    plt.grid(True)
    plt.savefig('TrqCtr.png')
    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
