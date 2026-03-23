import requests

def search_github_repos():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "python",
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        for repo in data["items"]:
            print(f"Repository: {repo['name']} | Stars: {repo['stargazers_count']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    search_github_repos()
