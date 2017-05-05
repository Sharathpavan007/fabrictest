from fabric.api import local

def test1():
	local("cd /home/devops/fabric/fabrictest && touch file1 file2 file3")
	local("cd /home/devops/fabric/fabrictest && git add . && git commit -m test1")
	local("cd /home/devops/fabric/fabrictest && git push origin master")

