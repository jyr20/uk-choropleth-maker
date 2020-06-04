def make_map(filename,xname,yname,colorscale):
    import json
    import plotly.express as px
    import pandas as pd
    import numpy as np
    with open('lad.json') as json_file:
        countiesUK = json.load(json_file)

    df = pd.read_csv(filename,header=0)
    N=len(countiesUK["features"])
    df2 = pd.DataFrame()
    names = []
    for i in range(N):
        name = countiesUK["features"][i]['properties']['LAD13NM']
        if name not in df[xname].values: names.append(name)
    df2[xname] = names
    cases = np.zeros(len(names))
    df2[yname] = cases
    df = df.append(df2)
    fig = px.choropleth(df, geojson=countiesUK, color=yname,
                        locations=xname, featureidkey="properties.LAD13NM",
                        projection="mercator", 
                        color_continuous_scale=colorscale
                       )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig