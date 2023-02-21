from github import Github
import os



token =  os.getenv("GITHUB_TOKEN")
g = Github(token)
user =  g.get_user()

def list_repos(user):
    for repo in user.get_repos():
        #list all repos with numbers
        print(repo.name)

def clone_repo(user):
    repo_name = input("Enter repo name: ")
    repo = user.get_repo(repo_name)
    clone_url = repo.clone_url
    os.system("git clone " + clone_url)

def create_repo(user):
    repo_name = input("Enter repo name: ")
    description = input("Enter description: ")
    repo = user.create_repo(repo_name, description=description)
    print("Repo created successfully")

def delete_repo(user):
    for repo in user.get_repos():
        print(repo.name)
    repo_name = input("Enter repo name: ")
    repo = user.get_repo(repo_name)
    if repo:
        repo.delete()
        print(f"{repo_name} Repository deleted successfully")
    else:
        print("Repo not found")

def delete_multiple_repos(user):
    for repo in user.get_repos():
        print(repo.name)
    repo_names = input("Enter repository names separated by space: ")
    repo_names = repo_names.split()
    for repo_name in repo_names:
        repo = user.get_repo(repo_name)
        repo.delete()
        print(f"{repo_name} Repository deleted successfully")


def main():
    while True:
        print("\n")
        print("1. List all repos")
        print("2. Clone a repo")
        print("3. Create a repo")
        print("4. Delete a repo")
        print("5. Delete multiple repos")
        print("6. Exit")
        print("\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            list_repos(user)
        elif choice == 2:
            clone_repo(user)
        elif choice == 3:
            create_repo(user)
        elif choice == 4:
            delete_repo(user)
        elif choice == 5:
            delete_multiple_repos(user)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

    







