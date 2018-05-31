# https://plot.ly/python/bar-charts/
from flask import Flask, render_template, request

import json
import plotly

import pandas as pd
import numpy as np

from Helper.DataHelper import EdgeXInitHelper

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    videos = ['congo_2048', 'paris-by-diego']
    videos_types = ['mp4', 'mp4']
    videos_models = ['OVER_UNDER', 'EQUALRECT']

    EdgeXInitHelper.initEdgeXWithVideoInformations(videos=videos, videos_types=videos_types, videos_models=videos_models,
                                                   edgex_host='http://localhost:48081/api/v1/')

    return render_template('layouts/index.html',
                           videos=videos)


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    selected_video = request.form.get('selected_video')
    rng = pd.date_range('9/1/1995', periods=7500, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = [
        dict(
            data=[
                dict(
                    x=[1, 2, 3, 4],
                    y=[10, 20, 30, 40],
                    type='bar'
                ),
            ],
            layout=dict(
                title=str(selected_video)
            )
        ),

        dict(
            data=[
                dict(
                    x=['totoro', 'gaonasi', 'ponyo', 'yoobaba'],
                    y=[70, 10, 40, 0],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ],
            layout=dict(
                title='third graph'
            )
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('layouts/dashboard.html',
                           video_name=selected_video,
                           ids=ids,
                           graphJSON=graphJSON)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
