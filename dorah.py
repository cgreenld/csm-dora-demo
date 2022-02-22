from flask import render_template, Flask, flash, redirect
from datetime import datetime 
from flask_bootstrap import Bootstrap
from forms import LoginForm
from flask_wtf import FlaskForm
from config import Config
from wtforms import SubmitField, SelectField, StringField, BooleanField, IntegerField, DecimalField
from wtforms.validators import InputRequired
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
STEP 1: The following two lines are imports within python. They manage the Python SDK referenced in the README and allow this app to connect to LD
UNCOMMENT lines 17 and 18 before proceeding.  You may need to look at the Pythond SDK Page in order find the correct import command
"""
# import ldclient
# from ldclient.config import Config
import config
import os


#mttr_data = pd.read_csv('/data/mttr.csv')
count = 0
#datasets
tips = sns.load_dataset('tips')
#mttr = sns.load_dataset('mttr')

# Set sdk_key to your LaunchDarkly SDK key before running
"""
STEP 2: This is the key that will authenticate with your Launch Darkly Environment, lets the LaunchDarkly know where to look when the application reaches out to us.
An SDK key is environment specific. In this case I am looking at the `cgreen` environment in support service
UNCOMMENT line 35 before proceeding
"""
#sdk_key = "sdk-7084b95b-76c3-4353-95ed-fd75ba818bbc"


#form for entry page
class entry_form(FlaskForm):
    #select field is options
    metric = SelectField('Metric Name', choices = [(i,i) for i in  ['MTTR (in minutes)', 'Releases per Month','Chance of Rollback','Uptime Percentage']])
    #string field
    value = StringField('Enter your Metric:', validators=[InputRequired ()])
    # Submit Field
    submit = SubmitField('Submit Metric')

#form for calculator page
class calc_form(FlaskForm):
    #lost revenue
    revhour = IntegerField('Revenue per hour', validators = [InputRequired ()])
    downtime = IntegerField('Downtime (in hours)', validators=[InputRequired ()])
    uptimep = DecimalField('Uptime Percentage', places=2, rounding=None, validators=[InputRequired ()])
    #lost productivity
    salaryhour = IntegerField('Employee Salary per hour', validators = [InputRequired ()])
    utilization = DecimalField('Utilization Percentage', places=2, rounding=None, validators=[InputRequired ()])
    numemployees = IntegerField('Number of Employees', validators=[InputRequired ()])
    #recovery cost
    recoverycost = IntegerField('Recovery Cost', validators = [InputRequired ()])
    #intangible cost
    intangiblecost = IntegerField('Intangible Cost', validators = [InputRequired ()])
    #submit field
    calcsubmit = SubmitField('Calculate Downtime Cost')

class visualize_form(FlaskForm):
    #select field is options
    viz_metric = SelectField('Vizualize Metric', choices = [(i,i) for i in  ['MTTR (in minutes)', 'Releases per Month','Chance of Rollback','Uptime Percentage']], validators = [InputRequired ()])
    #string field
    viz_Industry = SelectField('Choose Industry (opt)', choices = [(i,i) for i in  ['Finance', 'Retail','Technology',
                                                                                    'Healthcare','Government','Media','Insurance','Education','Industrial & Manufacturing',
                                                                                    'Telecommunications','Energy']])
    # Submit Field
    Viz_submit = SubmitField('Show Visualization')

#dynamic variable
todays_date = datetime.now()
date_as_string = todays_date.strftime('%m/%d/%Y %H:%M:%S')


app = Flask(__name__)

app.config.from_object(Config)
bootstrap = Bootstrap(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/')
def index():
    user = {'username': 'Greg'}
    return render_template('index.html', date = date_as_string, user = user)



@app.route('/entry', methods = ['GET', 'POST'])
def entry():
    user = {'username': 'Greg'}
    form = entry_form()

    if form.validate_on_submit():
        metric = form.metric.data
        value = form.value.data


        return render_template('entry_results.html', 
                           date = date_as_string, user = user,form = form, metric = metric, value = value)

    else: 

        return render_template('data_entry.html', date = date_as_string, user = user, form = form)


@app.route('/visualize', methods = ['GET', 'POST'])
def visualize():
    user = {'username': 'Greg'}
    form = visualize_form()

    if form.validate_on_submit():
        global count
        viz_metric = form.viz_metric.data

        metric_data = pd.read_csv('data/mttr.csv')

        

        import matplotlib.pyplot as plt
        import base64
        from io import BytesIO

        fig = plt.figure()
        #plot sth
        plt.hist(metric_data.mttr_m)
        #plt.savefig('static/hist_html.png')

        tmpfile = BytesIO()
        fig.savefig(tmpfile, format='png')
        encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

        html = '<img src=\'data:image/png;base64,{}\'>'.format(encoded)

        
        count += 1
        plt.close()

        return render_template('data_vis_results.html', 
                           date = date_as_string, user = user, form = form, viz_metric = viz_metric,
                           count = str(count-1), html = html)
    else:
        return render_template('data_vis.html', date = date_as_string, user = user, form = form)

@app.route('/calculator', methods = ['GET', 'POST'])
def calculator():
    user = {'username': 'Greg'}
    form = calc_form()

    if form.validate_on_submit():
        revhour = form.revhour.data
        downtime = form.downtime.data
        uptimep = form.uptimep.data

        salaryhour = form.salaryhour.data
        utilization = form.utilization.data
        numemployees = form.numemployees.data

        recoverycost = form.recoverycost.data

        intangiblecost = form.intangiblecost.data
#Cost of Downtime (per hour) = Lost Revenue + Lost Productivity + Recovery Costs + Intangible Costs
        lost_revenue = (revhour * downtime * uptimep)
        lost_productivity = (salaryhour * utilization * numemployees)

        downtime_cost = (lost_revenue + lost_productivity + recoverycost + intangiblecost)


        return render_template('calc_results.html', 
                           date = date_as_string, user = user,form = form, revhour = revhour, downtime = downtime,
                           uptimep = uptimep, salaryhour = salaryhour, utilization = utilization, numemployees = numemployees,
                           recoverycost = recoverycost, intangiblecost = intangiblecost, lost_revenue = lost_revenue, 
                           lost_productivity = lost_productivity, downtime_cost = downtime_cost)

    else: 

        return render_template('data_calc_grid.html', date = date_as_string, user = user,form = form)

if __name__ == '__main__':

    """
    STEP 3: We are going to use the code from the import in step 1, in order to configure LaunchDarkly.
    UNCOMMENT lines 197-203 to see the configuration for our environemnt passed.  We then check if our SDK was successfully initalized
    """
    # ldclient.set_config(Config(sdk_key))
    # # The SDK starts up the first time ldclient.get() is called
    # if ldclient.get().is_initialized():
    #     print("SDK successfully initialized!")
    # else:
    #     print("SDK failed to initialize")
    #client = ldclient.get()

    """
    STEP 4: Let's evaluate a flag, first we need an example
    UNCOMMENT line 209 to reference a flag in this test environment
    """
    #feature_flag_key = "csm-dora-demo-test"

    """
    STEP 5: We need to pass a user for sever side variatons, in this case we will just pass a key, the only required field.  Other information can be added to this object: https://docs.launchdarkly.com/home/users/attributes
    UNCOMMENT line 215 to create a user object
    """
    #user = {"key": "user@test.com"}

    """
    STEP 6: Let's evaluate a flag!! We are going to do two things:
        - First pass the user, flag key, and our default evaluation (just in case something goes wrong) to the client we created
        - Then we are going to use an if statement to tell us if the flag matches what is currently in support service
        UNCOMMENT lines 224-228
    """
    
    # show_feature = client.variation(feature_flag_key, user, False)
    # if show_feature:
    #     print("The Flag is on")
    # else:
    #     print("The Flag is off")

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    app.run(debug=True)