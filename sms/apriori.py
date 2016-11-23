import subprocess
command = 'Rscript'
path2script = 'apriori.R'

args = ['1','0.001', '0.8','9835','whole milk', 'whole milk']

cmd = [command, path2script] + args

x = subprocess.check_output(cmd, universal_newlines=True)



