import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _(FO):
    df = FO('NREL15kW.outb').toDataFrame()
    df1 = FO('NREL15kW_rosco.outb').toDataFrame()
    df2 = FO('NREL15kW_rosco2.outb').toDataFrame()
    df3 = FO('NREL15kW_rosco3.outb').toDataFrame()
    dff = FO('NREL15kW_FBP.outb').toDataFrame()
    df.columns
    return (df,)


@app.cell
def _(df, plt):
    xvar = 'Wind1VelX_[m/s]'
    vars  = ['Wind1VelX_[m/s]','RotSpeed_[rpm]','RotTorq_[kN-m]','GenPwr_[kW]']
    nvars = len(vars)
    f,ax = plt.subplots(nvars,1,figsize=(10,6))
    if nvars ==1:
        ax = [ax]
    for _i, _var in enumerate(vars):
        ax[_i].plot(df[xvar],df[_var])
        ax[_i].set_ylabel(_var)
        ax[_i].grid(True)
        # ax[_i].plot(df1[xvar],df1[_var])
        # ax[_i].plot(df2[xvar],df2[_var])
        # ax[_i].plot(df3[xvar],df3[_var])
        # ax[_i].plot(dff[xvar],dff[_var])
    ax[_i].set_xlabel('Wind Speed [m/s]')
    f.savefig('NREL15KW.png')
    return nvars, vars, xvar


@app.cell
def _(df, go, make_subplots, nvars, vars, xvar):
    fig = make_subplots(rows=nvars, cols=1, shared_xaxes=True)

    for _i, _var in enumerate(vars):
        fig.add_trace(go.Scatter(x=df[xvar],  y=df[_var],  mode='lines', name=f"{_var} (df)"),  row=_i+1, col=1)
        # fig.add_trace(go.Scatter(x=df1[xvar], y=df1[_var], mode='lines', name=f"{_var} (df1)"), row=_i+1, col=1)
        # fig.add_trace(go.Scatter(x=df2[xvar], y=df2[_var], mode='lines', name=f"{_var} (df2)"), row=_i+1, col=1)
        fig.update_yaxes(title_text=_var, row=_i+1, col=1)

    fig.update_layout(height=300*nvars, showlegend=True)
    fig.show()
    return


@app.cell
def _():
    from openfast_io.FAST_output_reader import FASTOutputFile as FO
    import matplotlib.pyplot as plt
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    return FO, go, make_subplots, plt


if __name__ == "__main__":
    app.run()
