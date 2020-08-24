# Git and GitHub

If you want to track the change history of your code or work as a team, you should use Git. Git is the most popular software version management tool. In Git terms, a software project is called a repository. Git is a distributed software version control system. It keeps your source code in local and remote repositories and keeps track of all the changes (snapshot) of your software assets include source code, configuration, documents, pictures and etc.

GitHub is a cloud service that hosts Git repositories. Saving your repositories in GitHub to have a reliable and central control of your source code.

## 1 Setup

First of all, please go to [https://github.com](https://github.com) to create an account if you don't have one. You can create GitHub repositories using your account.

Then go to [https://git-scm.com/downloads](https://git-scm.com/downloads) to download and install the latest version of Git. In you command line interface (CLI), run `git --version` to verify the installation. The CLI in Windows is `cmd` or `power shell`, the CLI in Mac is a terminal.

After downloading and installing git in your local computer, use `git config --global user.name "Your Name"` to set up a global username for all your repositories. Use `$ git config --global user.email "YourEmail@any.com"` to configure an email for your repositories.

### 2 Basic Git Concepts

Git keeps a history of your software changes by taking snapshots and store them in a `.git` directory of you project root folder. you can specify which files to be managed by a repository using `git add` command to **stage** file changes. The staging area is also called **cache** or **index**. You decide when to take a snapshot by issuing a `git commit` command. Git keeps all commit history and you can access any snapshot when you want.

![git add commit](images/git-add-commit.png)

The `git add` command and the `git commit` command work on a local repository. To save it in GitHub, you need to create a link between a local repository with a remote GitHub repository. There are two methods to create this link:

- Use `git clone github-repository-url` to clone a GitHub repository. The URL is displayed as a `Clone or download` green button in your GitHub repository page. This is recommended for a new project.
- Create a GitHub repository and use `git init` to create a local repository. Then use `git remote add` command to link the GitHub repository with the local repository. This is often used to save an existing project to GitHub.

Once you link a local repostiory with a remote repository, you can use `git push` to **push** changes to the remote repository or use `git pull` to **pull** changes made by others from the remote repository.

![Git local remote](./images/git-local-remote.png)

## 3 Ingored Files/Folders

Create a `.gitignore` file in your project root folder (the folder where `.git` folder sits) to add filenames or filename patterns for files that git should ignore. For node.js application, you don't want to check in installed NPM modules. Add the `node_modules/` to `.gitignore` will work.

## 4 Recommended Git Workflow with VS Code

You can perform basic git functions such as commit, push and pull within VS Code IDE -- this is much easy. The late part of [the VS Code video](https://youtu.be/fnPhJHN0jTE?t=1912) shows the Git operations built into the VS Code. The workflow now becomes the following:

### Step 1: Create a Github Repository

Create a new repository in Github. To add an appropriate `.gitignore` file, please select the "Node". Optionally, you can select a license to add a license copyright file and create a `README` file.

### Step 2: Clone the Repository

In your Github repoistory page, you can find the url. In your computer, open a terminal (`cmd` or `power shell` in Windows), use `git clone remote-repository-url` to clone the github repository to a folder in your local computer. The command will create a new folder named after the repository name.

### Step 3: Use VS Code to open the cloned folder

Use VS code IDE to open the cloned folder. Then work on this local repostiory. You can add new files, change existing files or delete unused files and the VS code shows the number of changed files.

### Step 4: Stage and Commit Changes

To stage and commit chagnes, click the VS code source control icon, the IDE is in source control mode. type in commit message and press enter to commit the changes. If it is the first, VS Code will ask you to confirm stage all changes, select `Always` stage changes and confirm the commit.

### Step 5: Push to Github Repository

When you click the source control icon, the IDE is in source control mode. Click the `...` icon on the top and it displays a list of source control commands, select `Push` to push the changes to GitHub repository. The first time you use the git operation, VS Code will prompt you for your GitHub account name and password.

## 5 Using Git Command Line

This is an exmaple using Git Command line. It explains what happen behind the VS Code GUI.

### Step 1: Create a Repository

If you create a new repository in Github, please select the right project type to add an appropriate `.gitignore` file. Optionally, you can select a license to add a license copyright file.

### Step 2: Clone the Github Repository

In your Github repoistory page, you can find the url. Use `git clone remote-repository-url` to clone it. The command will create a new folder named after the repository name.

### Step 3: Work on Local Repository

Then work on this local repostiory. Add new files, change existing files or delete unused files.

### Step 4: Stage Changes

when you are ready, run `git add .` to stage all changed files.

### Step 5: Commit Changes

Use `git commit -m "your change message"` to commit changes and create a new snapshot.

Often you want to commit all changes. It is common to combine the staging and committing in one step using command `git commit -a -m "your change message"`.

### Step 6: Push to Github Repository

Use `git push -u origin master` to push the changes to the remote repository. You may be asked for the username and passord of the remote repository.

Here the `origin` is the original Github respository. The `master` is the master branch of the local repository. As a solo developer, usually you only use one master branch. Optionally you can have mutiple branches for different feature development. But it is another topic.

### Other Common Tasks

Use `git status` to check current status frequently.

Use `git log` to check the history.

use `git pull` to pull changes from remote repository made by other developers.

## 6 Resources

- Document: [Working with GitHub in VS Code](https://code.visualstudio.com/docs/editor/github)
- vidoes: [How To Use GitHub with VS Code in 2020](https://www.youtube.com/watch?v=3Tn58KQvWtU&list=PLpPVLI0A0OkLBWbcctmGxxF6VHWSQw1hi&index=3)
