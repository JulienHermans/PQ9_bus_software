def function_clone():
  def clone(cmd):
	pipe = subprocess.Popen(cmd, shell=True)
	pipe.wait()

  for x in software:
    clone(x)
    

def function_RED():
  def subpRED(fRED):
	  f = pq9_path + fRED
	  cmd = "ln -s " + f + " " + folder
	  pipe = subprocess.Popen(cmd, shell=True)
	  pipe.wait()

  for x in software_RED:
	  subpRED(x)

  for x in software_PQ:
	  subpRED(x)

  for x in software_core:
	  subpRED(x)
    

def function_ADB():
  def subpADB(fADB):
	  f = pq9_path + fADB
	  cmd = "ln -s " + f + " " + folder
	  pipe = subprocess.Popen(cmd, shell=True)
	  pipe.wait()

  for x in software_ADB:
	  subpADB(x)

  for x in software_PQ:
	  subpADB(x)

  for x in software_core:
	  subpADB(x)
    

def function_EPS():
  def subpEPS(fEPS):
    f = pq9_path + fEPS
    cmd = "ln -s " + f + " " + folder
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()

  for x in software_EPS:
    subpEPS(x)

  for x in software_PQ:
    subpEPS(x)

  for x in software_core:
    subpEPS(x)
    
    
def function_OBC():
  def subpOBC(fOBC):
    f = pq9_path + fOBC
    cmd = "ln -s " + f + " " + folder
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()

  for x in software_OBC:
    subpOBC(x)

  for x in software_PQ:
    subpOBC(x)

  for x in software_core:
    subpOBC(x)
    
    
def function_ADCS():
  def subpADCS(fADCS):
    f = pq9_path + fADCS
    cmd = "ln -s " + f + " " + folder
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()

  for x in software_ADCS:
    subpADCS(x)

  for x in software_PQ:
    subpADCS(x)

  for x in software_core:
    subpADCS(x)
    
    
def function_COMMS():
  def subpCOMMS(fCOMMS):
    f = pq9_path + fCOMMS
    cmd = "ln -s " + f + " " + folder
    pipe = subprocess.Popen(cmd, shell=True)
    pipe.wait()

  for x in software_COMMS:
    subpCOMMS(x)

  for x in software_PQ:
    subpCOMMS(x)

  for x in software_core:
    subpCOMMS(x)


def function_pq9(fpath):
	f = pq9_path + fpath
	cmd = "ln -s " + f + " " + folder
	pipe = subprocess.Popen(cmd, shell=True)
	pipe.wait()


def function_path(fpath):
	f = path + fpath
	cmd = "ln -s " + f + " " + folder
	pipe = subprocess.Popen(cmd, shell=True)
	pipe.wait()
