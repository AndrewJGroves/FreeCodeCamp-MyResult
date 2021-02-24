def arithmetic_arranger(problems,doSum=False):

  if(len(problems) > 5):
    return 'Error: Too many problems.'

  topline=list()
  bottomline=list()
  operand=list()
  dashlist=list()
  sumlist=list()
  for i in problems:
    problem=i.split()
    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    if not problem[0].isnumeric() or not problem[2].isnumeric():
      return 'Error: Numbers must only contain digits.'
    if problem[1] != "+" and problem[1] != "-":
      return "Error: Operator must be '+' or '-'."
  
    sumnum=None
    if(problem[1] == '+'):  
      operand.append(problem[1])
      sumnum=str(int(problem[0])+int(problem[2]))
    elif(problem[1] == '-'):  
      operand.append(problem[1])
      sumnum=str(int(problem[0])-int(problem[2]))

    

    bottom=None
    if(len(problem[0]) >= len(problem[2])):
      if(len(problem[0])-len(problem[2]) == 0): space = ""
      if(len(problem[0])-len(problem[2]) == 1): space = " "
      if(len(problem[0])-len(problem[2]) == 2): space = "  "
      if(len(problem[0])-len(problem[2]) == 3): space = "   "
      if(len(problem[0])-len(problem[2]) == 4): space = "    "
      bottom=problem[1]+space+" "+problem[2]
    if(len(problem[0]) < len(problem[2])):
      bottom=problem[1]+" "+problem[2]
    bottomline.append(bottom)  

    dash=None
    if(len(bottom) == 7): 
      topline.append(problem[0].rjust(7))
      sumlist.append(sumnum.rjust(7))
      dash="-------"
    if(len(bottom) == 6): 
      topline.append(problem[0].rjust(6))
      sumlist.append(sumnum.rjust(6))
      dash="------"
    if(len(bottom) == 5): 
      topline.append(problem[0].rjust(5))
      sumlist.append(sumnum.rjust(5))
      dash="-----"
    if(len(bottom) == 4): 
      topline.append(problem[0].rjust(4))
      sumlist.append(sumnum.rjust(4))
      dash="----"
    if(len(bottom) == 3): 
      topline.append(problem[0].rjust(3))
      sumlist.append(sumnum.rjust(3))
      dash="---"
    dashlist.append(dash)


  space="    "
  output=topline[0]
  for i in range(1,len(topline)):
    output=output+space+topline[i]
  output=output+"\n"
  output=output+bottomline[0]
  for i in range(1,len(bottomline)):
    output=output+space+bottomline[i]
  output=output+"\n"
  output=output+dashlist[0]
  for i in range(1,len(dashlist)):
    output=output+space+dashlist[i]
  if(doSum):
    output=output+"\n"
    output=output+sumlist[0]
    for i in range(1,len(sumlist)):
      output=output+space+sumlist[i]
    return output
  else:
    return output