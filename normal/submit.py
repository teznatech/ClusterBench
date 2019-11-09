import os, time, sys, datetime

if len(sys.argv) <= 1:
    print("Usage: $ python3 submit.py <int:count>")
    print("count is total number of jobs to run")
    exit(0)



start_time = time.time()
basedir = os.path.abspath(os.path.dirname(__file__))

os.system("mkdir "+ str(basedir) + "/plots")
for i in range(int(sys.argv[1])):
    os.system("R --vanilla -f "+ str(basedir) + "/generate.R --args "+ str(time.time()) + "plot" + str(i))



end_time = time.time()

print("Done: " + str(end_time-start_time) + " seconds")

