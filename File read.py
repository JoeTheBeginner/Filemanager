class randw :
 def __init__(self, read_from , write_to):   
   self.filename1 = read_from
   self.filename2 = write_to
 def reader(self):
   x = open(self.filename1, "r")
   global liste
   liste = [ line.strip() for line in x]
 def writer(self):
   y = open(self.filename2,'w')
  
   for n in liste :
       y.write( n + ' \n')
   y = open(self.filename2,'r')
   for line in y:
       print(line.strip())
