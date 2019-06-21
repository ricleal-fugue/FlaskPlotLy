from flask import Flask, render_template, jsonify
import plots

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot1d')
def plot1d():
    plot = plots.plot1d()
    return render_template('plot.html', plot=plot)


@app.route('/plot2d')
def plot2d():
    plot = plots.plot2d()
    return render_template('plot.html', plot=plot)


@app.route('/plot3d')
def plot3d():
    plot = plots.plot3d()
    return render_template('plot.html', plot=plot)


@app.route('/plot1d_multiple/<int:n>')
def plot1d_multiple(n):
    plot = plots.plot1d_multiple(n)
    return render_template('plot_multiple.html', plot=plot)


@app.route('/plot1d_multiple_ajax/<int:n>')
def plot1d_multiple_ajax(n):
    plot = plots.plot1d_multiple(n)
    return plot


@app.route('/plotIq')
def plotIq():
    plot = plots.plotIq()
    return render_template('plot_fit.html', plot=plot)


@app.route('/plot_live')
def plot_live():
    plot = plots.plotLive()
    return render_template('plot_live.html', plot=plot)


@app.route('/plot_live_update')
def plot_live_update():
    plot = plots.live_plot_get_data_serialized()
    return jsonify([plot])


@app.route('/plot3d_scatter')
def plot3d_scatter():
    plot = plots.plot3D_scatter()
    return render_template('plot.html', plot=plot)


if __name__ == '__main__':
    app.run(debug=True)
