def state(a):
  if a >= 100:
    return "gaseous"
  elif 1 <= a <= 99:
    return "liquid"
  elif a < 1:
    return "solid"


print(state(float(45.2)))

