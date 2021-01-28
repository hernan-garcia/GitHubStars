import requests

url = "https://api.github.com/graphql"

payload="{\"query\":\"\\r\\n{\\r\\n  user(login:\\\"hagarciag\\\") {\\r\\n    starredRepositories {\\r\\n      totalCount\\r\\n    }\\r\\n    repositories(first: 10) {\\r\\n      edges {\\r\\n        node {\\r\\n          name\\r\\n          description\\r\\n          primaryLanguage {\\r\\n            name\\r\\n          }        \\r\\n          languages(first: 5) {\\r\\n            nodes {\\r\\n              name\\r\\n            }\\r\\n          }\\r\\n          stargazers {\\r\\n            totalCount\\r\\n          }\\r\\n          forks {\\r\\n            totalCount\\r\\n          }\\r\\n          watchers {\\r\\n            totalCount\\r\\n          }\\r\\n          issues(states:[OPEN]) {\\r\\n            totalCount\\r\\n          }\\r\\n          createdAt\\r\\n        }\\r\\n      }\\r\\n    }\\r\\n  }\\r\\n}\",\"variables\":{}}"
headers = {
  'Authorization': 'Bearer 257b8da2c40f980b2d7dcc68ec6ade4853eaba4a',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
