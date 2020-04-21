import requests
import black
from datetime import date

pull_requests = requests.get("https://api.github.com/repos/Umuzi-org/tech-department/pulls")

print(pull_requests.json)

def pull_requests(owner, repo_name, start_date, end_date):
    pull_requests = requests.get(f"https://api.github.com/repos/{owner}/{repo_name}/pulls?id=37012297")
    return pull_requests

repos = {
    "id": 37012297,
    "created_at": "2020-04-20T11:23:53Z",
    "updated_at": "2020-04-20T11:23:53Z",
}

for key, value in repos.items():
    if "2020-04-16T04:27:19Z" > pulls < "2020-04-20T11:23:53Z":
        print(pulls)