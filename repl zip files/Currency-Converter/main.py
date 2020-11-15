def converter(pounds,new_currency):
  if new_currency == "US dollars":
    return pounds * 1.31
  elif new_currency == "Euro":
    return pounds * 1.115 
  elif new_currency == "Yen":
    return pounds * 136.25
  elif new_currency == "Yuan":
    return pounds * 8.65

print(converter(16,"Yen"))
