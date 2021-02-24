def add_time(start, duration,day=None):
  days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  counter=-1
  if(day != None):
    for i in days:  
      counter+=1
      if(i.lower() == day.lower()):
        break
  clock, period = start.split()
  hours, minutes = clock.split(":")
  duration=duration.split(":")
  add_hours=duration[0]
  add_minutes=duration[1]
  tadd_minutes=int(add_hours)*60+int(add_minutes)
  if(tadd_minutes == 0):
    minFinal=minutes
    minFinal=minFinal.zfill(2)
    return hours+":"+minFinal+" "+period
  tminutes=int(hours)*60+int(minutes)
  totalMin=tminutes+tadd_minutes
  sindayChange=False
  MuldayChange=False
  dayChange=False

  numDay=0
  newPeriod=None
  if(24*60 < totalMin):
    newHour=totalMin/60
    numDay=int(int(newHour)/24)
    newHour=newHour-numDay*24

    minFrac=newHour-int(newHour)
    newMin=minFrac*60
    if(int(newHour) >= 12):  
      newHour=int(newHour)-12
      if(newHour == 0): newHour=12  
      if(period == "AM"):
        newPeriod="PM"
      if(period == "PM"):
        numDay=numDay+1
        newPeriod="AM"
    else:
      newPeriod=period
  else:
    newHour=totalMin/60
    minFrac=newHour-int(newHour)
    newMin=minFrac*60
    if(int(newHour) >= 12):  
      newHour=int(newHour)-12
      if(newHour == 0): newHour=12  
      if(period == "AM"):
        newPeriod="PM"
      if(period == "PM"):
        sindayChange=True
        newPeriod="AM"
    else:
      newPeriod=period

  if(numDay == 1):
    if(day != None): finDay=days[counter+1]
    sindayChange=True
  if(numDay > 1):
    if(day != None):
      test=7*(numDay/7-int(numDay/7))
      finDay=days[int((counter+test)-7)]
    MuldayChange=True
    dayNum=" ("+str(numDay)+" days later)"


  minFinal=str(int(newMin))
  minFinal=minFinal.zfill(2)
  final=None

  if(MuldayChange and day != None):
    final=str(int(newHour))+":"+minFinal+" "+newPeriod+", "+finDay+dayNum
  elif(sindayChange and day != None):
    final=str(int(newHour))+":"+minFinal+" "+newPeriod+", "+finDay+" (next day)"
  elif(day != None):
    final=str(int(newHour))+":"+minFinal+" "+newPeriod+", "+days[counter]
  elif(MuldayChange):
    final=str(int(newHour))+":"+minFinal+" "+newPeriod+dayNum
  elif(sindayChange):
    final=str(int(newHour))+":"+minFinal+" "+newPeriod+" (next day)"
  else:
    final=str(int(newHour))+":"+minFinal+" "+newPeriod

  return final

