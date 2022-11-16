import requests
from plotly.graph_objs import Bar
from plotly import offline

site_url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}
response = requests.get(site_url, headers=headers)
response_json = response.json()

repo_names, repo_stars = [], []

for repo in response_json['items']:
    repo_names.append(repo['name'])
    repo_stars.append(repo['stargazers_count'])

data_plots = [{'type' : 'bar', 'x':repo_names , 'y': repo_stars}]
layout = {'title': 'GItHubs Most Popular Javascript Projects',
'xaxis': {'title': 'Repository'},
'yaxis': {'title': 'Stars'}}

fig = {'data': data_plots, 'layout': layout}
offline.plot(fig, filename='index.html')
