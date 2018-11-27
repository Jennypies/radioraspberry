import subprocess

subprocess.check_output(["mpc", "idle"])
print(repr(subprocess.check_output(["mpc", "status"])))
