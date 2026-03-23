## Q1: Role of Query Parameters
Query parameters in an API request allow us to customize and filter the data we want from the server.  
In this case:
- `q=python` → searches repositories related to Python.
- `sort=stars` → sorts repositories by the number of stars.
- `order=desc` → ensures results are shown in descending order.
- `per_page=5` → limits the results to 5 repositories.

They act like filters or instructions that tell the API exactly what data we want.

---

## Q2: Why use `response.json()` instead of `response.text`?
- `response.text` returns the raw response as a string.
- `response.json()` parses the response into a Python dictionary, making it easier to access specific fields (like `items`, `name`, `stargazers_count`).
- Since the GitHub API returns data in JSON format, using `response.json()` is the most efficient way to work with the structured data.
