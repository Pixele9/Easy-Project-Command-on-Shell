import sys, os
from github import Github

token = "here goes your github token"
username = "your github username"


try:
	if str(sys.argv[1]) == "-h":
		# instructions
		print("")
		print(" To create project with github repo")
		print("\t Use the '-r' flag")
		print("\t 'create -r [Folder] [Project Name]'\n")

		print(" To create a basic project without repo")
		print("\t 'create [Folder] [Project Name]\n")

		print(" Available Folders")
		print("\tPython")
		print("\tWeb_Development")
		print("\tJavaScript")
		print("\tGolang")
		print("\tC#")
		print("\tReactNative")

	# create proj with github repo
	elif str(sys.argv[1]) == "-r":
		g = Github(token)
		user = g.get_user()

		# The folder name has to be on your specified directory
		folder = str(sys.argv[2]) # for instance, Python, JS, Web
		proj_name = str(sys.argv[3])
		# Specify your directory where your projects live
		os.chdir("path to your projects")
		os.chdir(folder)
		os.system(f"mkdir {proj_name}")
		os.chdir(proj_name)
		os.system("touch README.md")
		os.system("git init")

		# create new repo with given project name
		repo = user.create_repo(proj_name)
		print(f"this is the name of the new repo {repo}")

		os.system(f"git remote add origin https://github.com/{username}/{proj_name}.git")
		os.system("git add .")
		os.system("git commit -m 'initial commit'")
		os.system("git push -u origin master")
		os.system("code .") # open project on VS Code
		print("Project named {} SUCCESSFULLY CREATED".format(proj_name))
	else:
		# Basic project wihtout repo
		folder = str(sys.argv[1])
		proj_name = str(sys.argv[2])

		os.chdir("path to your projects")
		os.chdir(folder)
		os.system(f"mkdir {proj_name}")
		os.chdir(proj_name)
		os.system("touch app.py")
		os.system("code .")
		os.system("open -a iTerm .")

		print("Project named {} SUCCESSFULLY CREATED".format(proj_name))

except Exception as e:
	print(f"Error: Enter a valid argument -> Exception: {e}")