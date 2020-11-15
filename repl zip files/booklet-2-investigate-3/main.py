def YearGroup(Year):
  if Year >= 1 and Year <= 2:
    print("Key Stage 1")
  elif Year >= 3 and Year <= 6:
    print("Key Stage 2")
  elif Year >= 12 and Year <= 14:
    print("Sixth Form")
  else:
    print("invalid")
YearGroup(11)