def quote(job):
  if job == "Engineer":
    return "The engineer has been, and is, a maker of history"
  elif job == "Developer":
    return "Logical thinking, passsion and perseverance is the paint on your palette"
  elif job == "Analyst":
    return "Seeing what other people can't see gives you great vision"
  else:
    return "I'm sorry. We could not find a quote for your job"



print(quote("analyst"))
