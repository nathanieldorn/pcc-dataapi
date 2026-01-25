import plotly.express as px
import requests


def call_api():
    """Creates the api call and checks the response"""
    url = "https://api.github.com/search/repositories"
    query = "?q=language:python+sort:stars+stars:>10001"
    api_query_url = "".join([url, query])

    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_query_url, headers=headers)

    # covnert the response into a dictionary
    response_dict = response.json()
    print(f"Status code: {response.status_code}")
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # check length of responses
    repo_dicts = response_dict["items"]
    print(f"Repositories returned: {len(repo_dicts)}")

    return repo_dicts


def plot_repos():
    """prints summary information about repos"""
    repo_dicts = call_api()

    # print("\nSelected information about first repository:\n")

    repo_names = [dict["name"] for dict in repo_dicts]
    repo_stars = [dict["stargazers_count"] for dict in repo_dicts]

    fig = px.bar(x=repo_names, y=repo_stars, color_discrete_sequence=["gold"])
    fig.update_layout(template="plotly_dark")
    fig.show()

    """
    # loop through the dictionary and print the summary info, limiting descrptions to 200 chars
    for repo in repo_dicts:
        print(f"\nName: {repo['name']}")
        print(f"Owner: {repo['owner']['login']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"Respository: {repo['html_url']}")
        print(f"Created: {repo['created_at']}")
        print(f"Updated: {repo['updated_at']}")
        print(f"Description: {repo['description']}"[:200])
    """
