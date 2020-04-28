from flask import Flask, render_template, jsonify
import plots

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resources_drifted')
def resources_drifted():
    plot = plots.plot_resources_drifted()
    return render_template('plot.html', plot=plot)


@app.route('/new_rule_violations')
def new_rule_violations():
    plot = plots.plot_new_rule_violations()
    return render_template('plot.html', plot=plot)


@app.route('/new_rule_violations_burn_down')
def new_rule_violations_burn_down():
    plot = plots.plot_new_rule_violations_burn_down()
    return render_template('plot.html', plot=plot)


if __name__ == '__main__':
    app.run(debug=True)
