import requests


problems = {
    "algorithms": [
        {"name": "Warmup", "slug": "warmup"},
        {"name": "Implementation", "slug": "implementation"},
        {"name": "Strings", "slug": "strings"},
        {"name": "Sorting", "slug": "arrays-and-sorting"},
        {"name": "Search", "slug": "search"},
        {"name": "Graph Theory", "slug": "graph-theory"},
        {"name": "Greedy", "slug": "greedy"},
        {"name": "Dynamic Programming", "slug": "dynamic-programming"},
        {"name": "Constructive Algorithms", "slug": "constructive-algorithms"},
        {"name": "Bit Manipulation", "slug": "bit-manipulation"},
        {"name": "Recursion", "slug": "recursion"},
        {"name": "Game Theory", "slug": "game-theory"},
        {"name": "NP Complete", "slug": "np-complete-problems"},
        {"name": "Debugging", "slug": "algo-debugging"},
    ],
    "data-structures": [
        {"name": "Arrays", "slug": "arrays"},
        {"name": "Linked Lists", "slug": "linked-lists"},
        {"name": "Trees", "slug": "trees"},
        {"name": "Balanced Trees", "slug": "balanced-trees"},
        {"name": "Stacks", "slug": "stacks"},
        {"name": "Queues", "slug": "queues"},
        {"name": "Heap", "slug": "heap"},
        {"name": "Disjoint Set", "slug": "disjoint-set"},
        {"name": "Multiple Choice", "slug": "multiple-choice"},
        {"name": "Trie", "slug": "trie"},
        {"name": "Advanced", "slug": "data-structures"},
    ],
}

url_schema = (
    "https://www.hackerrank.com/rest/contests/master/tracks/{problem}/challenges"
)

params = {
    "offset": 0,
    "limit": 1000,
    "filters[subdomains][]": ...,
    "track_login": "true",
}

cookies = {
    "_hrank_session": ...,
}

session = requests.Session()

for problem, subdomains in problems.items():
    url = url_schema.format(problem=problem)
    print(f"### {problem}")
    for subdomain in subdomains:
        params["filters[subdomains][]"] = subdomain["slug"]

        result = session.get(
            url, params=params, headers={"User-Agent": "Hacker:)"}, cookies=cookies
        )

        if result.status_code == 200:
            print(f"#### {subdomain['name']}")
            for i, challenge in enumerate(result.json()["models"]):
                print(
                    "- [x]" if challenge.get("solved") else "- [ ]",
                    f"{i + 1}",
                    f"[{challenge['name']}](https://www.hackerrank.com/challenges/{challenge['slug']})",
                )
