import subprocess

subprocess.check_output(["mpc", "idle"])
print(subprocess.check_output(["mpc", "status"]))
