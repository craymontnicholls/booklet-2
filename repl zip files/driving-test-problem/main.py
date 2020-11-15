def PassFail(MinorFaults):
  if MinorFaults < 16:
    return "pass"
  else:
    return "fail"

print(PassFail(14))