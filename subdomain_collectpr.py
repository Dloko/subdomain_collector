import subprocess
import multiprocessing.dummy as mp

print("(sem www, gov e etc)")
domain = input('@ ')

apagar = subprocess.run("rm subdomain", shell=True)

def func1(*args):
    enumerar1 = subprocess.run("subfinder -d " + domain + " >> subdomain", shell=True)

p = mp.Pool(8)
p.map(func1, range(0, 1))
p.close()


def func2(*args):
    enumerar2 = subprocess.run("amass enum -d " + domain +  " >> subdomain", shell=True)

p2 = mp.Pool(8)
p2.map(func2, range(0, 1))
p2.close()

enumerar3 = subprocess.run('curl https://crt.sh/?q=' + domain + ' | grep "." | grep "stone" | cut -d ">" -f2 | cut -d "<" -f1 | cut -d "*" -f1 | cut -d ":" -f1 | sort -u  >> subdomain', shell=True)

d = subprocess.run('cat subdomain |grep "' + domain + '" |cut -d "|" -f2 | cut -d "|" -f1 >> subdomain2', shell=True)


