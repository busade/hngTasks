from flask import Flask,request,jsonify
from datetime import datetime
import pytz
app = Flask(__name__)


@app.route('/path',methods=['GET'])
def info():
    #get queries
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')


    # return day
    day = datetime.now(pytz.UTC).strftime('%A')


    # time validation
    current_time = datetime.now(pytz.UTC)
    utc_diff = current_time.utcoffset().total_seconds() / 3600
    time_validation = "within +/-2 hours"
    if utc_diff < -2 or utc_diff > 2:
        time_validation = "outside +/-2 hours"



    # URLS
    git_file_url ="https://github.com/busade/hngTasks/blob/master/task_one.py"
    git_repo_url = "https://github.com/busade/hngTasks"


    # response
    response={
        "slack_name": slack_name,
        "Current_day": day,
        "Track": track,
        "utc_time": current_time.strftime('%Y-%m-%d %H:%M:%S UTC'),
        "github_file_url":git_file_url,
        "github_repo_file":git_repo_url,
        "status_code": 200

    }

    return jsonify(response)

    