import os, paramiko, getpass


class TACBeast:
	
	def __init__(self):
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		paramiko.util.log_to_file("filename.log") # log to file removes error about transport.py
		self.user = raw_input("Your username: ")
		self.passw = getpass.getpass("Your password: ")
		self.commands = []

	def add_command(self, command="ls"):
		self.commands.append(command)

	def do_sth(self):
		try:
			self.ssh.connect('tex.cisco.com', username=self.user, password=self.passw)
			for cmd in self.commands:
				stdin, stdout, stderr = self.ssh.exec_command(cmd)
				print(stdout.read())
		except paramiko.ssh_exception.SSHException:
			print("SSH Server cannot start")
	
	def __del__(self):
		del self.ssh
	
obj = TACBeast()
obj.add_command()
obj.do_sth()