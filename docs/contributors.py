import requests
import pandas as pd
import json
import textwrap
from datetime import date


url = "https://api.github.com/repos/modeci/modelspec/contributors"

response = requests.get(url=url, auth=("<github_username>", "<github_token>"))

json_data = response.json()

df = pd.DataFrame(json_data)

per_info = list(df["url"].unique())
len_per_info = len(per_info)

empty_list = []
for i in range(len_per_info):
    url = per_info[i]
    print(url)
    data = requests.get(url=url)
    requests_status = "unknown"
    while (requests_status == "unknown") or (requests_status == "unsuccessful"):
        if data.status_code == 200:
            requests_status = "successful"
            empty_list.append(data.json())
        else:
            # handle failure on requests to the url for mac os
            requests_status = "unsuccessful"
            print(f"Failed to get data from: {url}")
            # make request again to get data from the url
            data = requests.get(url=url)

df1 = pd.DataFrame(empty_list)
df1["name"] = df1["name"].fillna("")
name = df1["name"]
login = df1["login"]
url_html = df1["html_url"]
url_id = df1["id"]

login_html = list(zip(name, login, url_html))
zip_dict = dict(zip(url_id, login_html))

file = "sphinx/source/api/Contributors.md"
with open(file, "w") as f:
    print(
        textwrap.dedent(
            """\
        (Modelspec:contributors)=

        # Modelspec contributors

        This page list names and Github profiles of contributors to Modelspec, listed in no particular order.
        This page is generated periodically, most recently on {}.""".format(
                date.today()
            )
        ),
        file=f,
    )

    print("", file=f)

    for key, val in zip_dict.items():
        print("- {} ([@{}]({}))".format(val[0], val[1], val[2]), file=f)
