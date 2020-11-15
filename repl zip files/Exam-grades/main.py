#function to input mark and recieve grade

def grade(mark):
  if mark >= 80:
    return "9"
  elif mark >= 67:
    
    print ("8")
    next_grade = 80 - mark
    print ("u needed", next_grade,"more marks for next grade")

  elif mark >= 54:
    
    print ("7")
    next_grade = 67 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 41:
    
    print ("6")
    next_grade = 54 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 31:
    
    print ("5")
    next_grade = 41 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 22:
    
    print ("4")
    next_grade = 31 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 13:
    
    print ("3")
    next_grade = 2 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 4:
    
    print ("2")
    next_grade = 13 - mark
    print ("u needed", next_grade,"more marks for next grade")
  elif mark >= 2:
    
    print ("1")
    next_grade = 4 - mark
    print ("u needed", next_grade,"more marks for next grade")
  else:
    return "U"
   
#change the value of mark to whatever the student got
mark = 4

print (grade(mark))