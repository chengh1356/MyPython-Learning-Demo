args=[3,6]
print list(range(*args))

def parrot(voltage,state="a stiff",action="voom"):
  print "-- This parrot wouldn't ",action,"\n",
  print "if you put",voltage,"volts through it.","\n",
  print "E's",state,"!"

if __name__ == "__main__":
    d = {"voltage":"four million","state":"bleedin demised","action":"VOOM"}
    parrot(**d)  
