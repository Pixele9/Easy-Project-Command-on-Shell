# Easy project creation on shell

Create command to start new projects with repo or without repo

### Prerequisites

Install PyGithub

```bash
pip install PyGithub
```

Get your GitHub account token by going to

1. Settings
2. Developer Settings
3. Personal access tokens
4. Generate new token

Copy that token and paste it into create.py variable named "token"

## Set it up

Move .create_command.sh to your home directory

Change directory to home

```bash
cd ~
```

Now lets make the command available from anywhre on the terminal
If you use ZSH open ~/.zshrc if not ~/.bashrc

- Open ~/.bashrc or ~/.zshrc using any text editor you have
- Add the following command after the last line or anywhere you want

```bash
source ~/.my_custom_commands.sh
```

- Save file after adding the new line and exit the terminal

## Usage

#### Basic syntax

- To create project with **GitHub** repo
  Use the '-r' flag
  'create -r [Folder] [Project Name]'

- To create a basic project without repo
  'create [Folder] [Project Name]
