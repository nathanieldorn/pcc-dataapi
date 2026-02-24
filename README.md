# A Data Visualization Project with Plotly
### Using Real Time API Data from GitHub and Hacker News
Add or remove comments from `main.py` to run functions for either Github, `plot_repos()`, or Hacker News, `get_story_info()`. Only one may be run at a time. 

## GitHub Most-Starred Python Repos
Display the top Python repositories queried from the GitHub API. Output is produced via Plotly to the browser. Tooltips display the repo name, total stars, and the description limited to 200 characters. Repo titles along the x-axis may be clicked to directly access the repo on GitHub.

![GitHub Most-Starred Pyton Repos](https://github.com/nathanieldorn/pcc-dataapi/blob/main/gh_most_starred_python.png)

## Hacker News Story Information
Provides an output of summary information about the stories on Hacker News with the most comments. The data is queried via an API. Output is print to the console and is limited to the top 10. This may be changed within the `get_story_info()` function by changing the for loop, `for id in submission_ids[:10]`. Change the `[:10]` to any integer X, greater than zero, to get the top X stories, `for id in submission_ids[:X]`. Status codes are returned to indicate a successful return of story data, 200 being successful.

```text
Status code: 200
id: 47129361    status: 200
id: 47127986    status: 200
id: 47122715    status: 200
id: 47088076    status: 200
id: 47130208    status: 200
id: 47120899    status: 200
id: 47123631    status: 200
id: 47128631    status: 200
id: 47128535    status: 200
id: 47119530    status: 200

Title: The Age Verification Trap: Verifying age undermines everyone's data protection
Discussion link: https://news.ycombinator.com/item?id=47122715
Comments: 939

Title: Ladybird adopts Rust
Discussion link: https://news.ycombinator.com/item?id=47120899
Comments: 575
...
```
