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

    # create tootips
    hover_texts = []
    for repo in repo_dicts:
        owner = repo["owner"]["login"]
        description = repo["description"]
        hover_text = f"{owner} <br />{description}"
        hover_texts.append(hover_text)

    # plot repos as bar chart
    title = "GitHub's Most-Starred Python Projects"
    labels = {"x": "Repository", "y": "Stars"}
    fig = px.bar(
        x=repo_names,
        y=repo_stars,
        title=title,
        labels=labels,
        color_discrete_sequence=["gold"],
        hover_name=hover_texts,
    )
    fig.update_layout(
        title_font_size=24,
        xaxis_title_font_size=18,
        yaxis_title_font_size=18,
        template="plotly_dark",
        hoverlabel=dict(
            bgcolor="white",
            font_size=16,
        ),
    )
    fig.show()
