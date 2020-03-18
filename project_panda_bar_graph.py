import pandas as pd
import pylab

data = pd.read_csv("F:\Project-MCA-SEM-4\project_file.csv")

lstyear = []
lstmurder = []
lstrape = []
lstrobbery = []
lsttheft = []
lstriots = []
lstcheating = []
lstdowry = []

lstyear = data["year"]
lstmurder = data["murder"]
lstrape = data["rape"]
lstrobbery = data["robbery"]
lsttheft = data["theft"]
lstriots = data["riots"]
lstcheating = data["cheating"]
lstdowry =data["dowry_deaths"]

pylab.figure("Number Of Dowry_Deaths")
pylab.bar(lstyear,lstdowry)
pylab.xlabel("years")
pylab.ylabel("Number of Dowry_Deaths Crimes")


pylab.figure("Number Of Cheating")
pylab.bar(lstyear,lstcheating)
pylab.xlabel("years")
pylab.ylabel("Number of Cheating Crimes")


pylab.figure("Number Of Riots")
pylab.bar(lstyear,lstriots)
pylab.xlabel("years")
pylab.ylabel("Number of Riots Crimes")


pylab.figure("Number Of Theft")
pylab.bar(lstyear,lsttheft)
pylab.xlabel("years")
pylab.ylabel("Number of Theft Crimes")


pylab.figure("Number Of Robberys")
pylab.bar(lstyear,lstrobbery)
pylab.xlabel("years")
pylab.ylabel("Number of Robberys Crimes")


pylab.figure("Number Of Murder")
pylab.bar(lstyear,lstmurder)
pylab.xlabel("years")
pylab.ylabel("Number of Murders Crimes")


pylab.figure("Number Of Rape")
pylab.bar(lstyear,lstrape)
pylab.xlabel("years")
pylab.ylabel("Number of Rape Crimes")


pylab.show()
