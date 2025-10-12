import marimo

__generated_with = "0.16.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np):
    x = np.arange(0,1.05,0.05)
    return (x,)


@app.cell
def _():
    coeff= [
     0.5709,
     0.6277,
    -1.0914,
     1.6765,
    -0.7837,
    ]
    coeff2 = [
    -13.9109,
     18.8824,
    -48.1009,
     76.3808,
    -32.2513,
    ]
    return coeff, coeff2


@app.cell
def _(coeff, coeff2, np, x):
    y1 = np.zeros(len(x))
    y2 = np.zeros(len(x))
    for i,c in enumerate(coeff):
        c2 = coeff2[i]
        y1 += c*x**(i+2)
        y2 += c2*x**(i+2)
    return y1, y2


@app.cell
def _(plt, x, y1, y2):
    f,ax = plt.subplots(2,1,figsize=(8,6))
    ax[0].plot(x,y1*0,'k--')
    ax[0].plot(x,y1)
    ax[0].grid()
    ax[0].set_xlabel('Tower height fraction')
    ax[0].set_ylabel('Modal deflection')
    ax[0].set_title('First tower mode')
    ax[1].plot(x,y2*0,'k--')
    ax[1].plot(x,y2)
    ax[1].grid()
    ax[1].set_xlabel('Tower height fraction')
    ax[1].set_ylabel('Modal deflection')
    ax[1].set_title('Second tower mode')
    f.tight_layout()
    f.savefig('TowerModeShapes.png')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
