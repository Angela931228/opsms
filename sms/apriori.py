import subprocess
command = 'Rscript'
path2script = './sms/apriori.R'


def processApriori(args):
	cmd = [command, path2script] + args
	subprocess.check_output(cmd)
