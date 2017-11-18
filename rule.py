def rule(value, list_n):
  sum = 0
  for i in range(0,len(list_n),1):
    sum = sum + list_n[i]
  if value == 1:
    if sum == 2 or sum == 3:
      return 1
    else:
      return 0
  else:
    if sum == 3:
      return 1
    else:
      return 0
