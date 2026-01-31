from operator import itemgetter

import requests


def get_submission_ids(url="https://hacker-news.firebaseio.com/v0/topstories.json"):
    """Call the api and record the response"""
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    submission_ids = response.json()
    return submission_ids


def get_story_info():
    submission_dicts = []
    submission_ids = get_submission_ids()
    for id in submission_ids[:10]:
        # call api for each submission
        url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
        r = requests.get(url)
        print(f"id: {id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # build a dictionary for each article
        submission_dict = {
            "title": response_dict["title"],
            "hn_link": f"https://news.ycombinator.com/item?id={id}",
            "comments": response_dict["descendants"],
        }
        submission_dicts.append(submission_dict)

    submission_dicts = sorted(
        submission_dicts, key=itemgetter("comments"), reverse=True
    )

    for submission in submission_dicts:
        print(f"\nTitle: {submission['title']}")
        print(f"Discussion link: {submission['hn_link']}")
        print(f"Comments: {submission['comments']}")
