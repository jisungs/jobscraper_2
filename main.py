from flask import Flask, render_template, request
from requests import get
from bs4 import BeautifulSoup
from extractor.wwr import extract_wwr_jobs
from extractor.remoteok import remoteok_jobs


app = Flask(__name__)

# jobs = extract_wwr_jobs("python")
# for job in jobs:
#     print(job)
#     print("------------------")
db = {}

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        jobs= extract_wwr_jobs(keyword)
        rk_jobs = remoteok_jobs(keyword)
        return render_template("index.html", keyword = keyword, jobs=jobs, rk_jobs=rk_jobs)
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)