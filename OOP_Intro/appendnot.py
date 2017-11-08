def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str

def missing_char(str, n):
  front = str[:n]
  print front
  back = str[n+1:]
  print back
  return front + back

def stargs(str,n):
  

print missing_char("disable", 4)

print not_string("not a super long string except it really is")
print not_string("strut")
print not_string(" strut")
print not_string("")
