import subprocess


path = "C:\\Users\\aruds\\source\\repos\\SATSolver\\SATSolver\\bin\\Release\\net7.0\\SATSolver.exe"
t=[]

for i in range(0,40):
    output=subprocess.getoutput(path)

    value = output.split(' ')[-1][2:]\

    t.append(float(value[0:2]+"."+value[6:9]))
