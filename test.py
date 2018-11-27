import subprocess

subprocess.check_output(["echo", "Hello World!"])
print(subprocess.check_output("mpc idle"))
subprocess.check_output(["echo", "Hello World!"])
