import os
import warnings
warnings.filterwarnings('ignore')
from github import Github

def get_github_repo():
    access_token = os.getenv('GH_ACCESS_TOKEN')
    org_name = os.getenv('GH_ORG_NAME')
    repo_name = os.getenv('GH_REPO_NAME')
    # print(access_token, org_name, repo_name)
    g = Github(access_token)
    return g.get_organization(org_name).get_repo(repo_name)

def make_github_issue(title, body):
    return get_github_repo().create_issue(title=title, body=body)

if __name__ == "__main__":
    make_github_issue('Test', 'Test')