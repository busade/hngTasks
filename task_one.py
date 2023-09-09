from flask import Flask,request,Response

from datetime import datetime, timedelta
import pytz, json
app = Flask(__name__)


@app.route('/api',methods=['GET'])
def info():
    #get queries
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')


    # return day
    day = datetime.now(pytz.UTC).strftime('%A')


    # time validation
    current_time = datetime.now(pytz.UTC)
    current = current_time + timedelta(hours=1)
    iso_datetime = current.strftime('%Y-%m-%dT%H:%M:%SZ')

    utc_diff = current_time.utcoffset().total_seconds() / 3600
    time_validation = "within +/-2 mins"
    if utc_diff < -2 or utc_diff > 2:
        time_validation = "outside +/-2 mins"



    # URLS
    git_file_url ="https://github.com/busade/hngTasks/blob/master/task_one.py"
    git_repo_url = "https://github.com/busade/hngTasks"


    # response
    response={
        "slack_name": slack_name,
        "current_day": day,
        "utc_time": iso_datetime,
        "track":track,
        "github_file_url":git_file_url,
        "github_repo_url":git_repo_url,
        "status_code": 200

    }
    response_json = json.dumps(response, sort_keys=False)
    return Response(response_json, content_type= "application/json")


