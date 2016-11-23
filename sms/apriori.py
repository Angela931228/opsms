import subprocess
command = 'Rscript'
path2script = './sms/apriori.R'


def processApriori(args):

	#args = ['1','0.001', '0.8','9835','whole milk', 'whole milk']

	cmd = [command, path2script] + args

	subprocess.check_output(cmd)


#processApriori(['1','0.001', '0.8','9835','whole milk', 'whole milk'])
