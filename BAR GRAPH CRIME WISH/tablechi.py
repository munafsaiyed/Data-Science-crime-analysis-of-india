import pandas as pd
from scipy.stats import chisquare
import csv
data=pd.read_csv('project_file11.csv')  
with open('writeData.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    writer.writerow(['state','rape','robbery','murder','total'])
    writer.writerow(["GUJARAT",data["rape"][data["state_ut"] == "GUJARAT"].sum(),data["robbery"][data["state_ut"] == "GUJARAT"].sum(),data["murder"][data["state_ut"] == "GUJARAT"].sum(),data["rape"][data["state_ut"] == "GUJARAT"].sum()+data["robbery"][data["state_ut"] == "GUJARAT"].sum()+data["murder"][data["state_ut"] == "GUJARAT"].sum()])
    writer.writerow(["RAJASTHAN",data["rape"][data["state_ut"] == "RAJASTHAN"].sum(),data["robbery"][data["state_ut"] == "RAJASTHAN"].sum(),data["murder"][data["state_ut"] == "RAJASTHAN"].sum(),data["rape"][data["state_ut"] == "RAJASTHAN"].sum()+data["robbery"][data["state_ut"] == "RAJASTHAN"].sum()+data["murder"][data["state_ut"] == "RAJASTHAN"].sum()])
    writer.writerow(["BIHAR",data["rape"][data["state_ut"] == "BIHAR"].sum(),data["robbery"][data["state_ut"] == "BIHAR"].sum(),data["murder"][data["state_ut"] == "BIHAR"].sum(),data["rape"][data["state_ut"] == "BIHAR"].sum()+data["robbery"][data["state_ut"] == "BIHAR"].sum()+data["murder"][data["state_ut"] == "BIHAR"].sum()])
    writer.writerow(["UTTAR PRADESH",data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum()])
    rowt=data["rape"][data["state_ut"] == "GUJARAT"].sum()+data["rape"][data["state_ut"] == "RAJASTHAN"].sum()+data["rape"][data["state_ut"] == "BIHAR"].sum()+data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["robbery"][data["state_ut"] == "GUJARAT"].sum()+data["robbery"][data["state_ut"] == "RAJASTHAN"].sum()+data["robbery"][data["state_ut"] == "BIHAR"].sum()+data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["murder"][data["state_ut"] == "GUJARAT"].sum()+data["murder"][data["state_ut"] == "RAJASTHAN"].sum()+data["murder"][data["state_ut"] == "BIHAR"].sum()+data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum()
    writer.writerow(["TOTAL",data["rape"][data["state_ut"] == "GUJARAT"].sum()+data["rape"][data["state_ut"] == "RAJASTHAN"].sum()+data["rape"][data["state_ut"] == "BIHAR"].sum()+data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["robbery"][data["state_ut"] == "GUJARAT"].sum()+data["robbery"][data["state_ut"] == "RAJASTHAN"].sum()+data["robbery"][data["state_ut"] == "BIHAR"].sum()+data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["murder"][data["state_ut"] == "GUJARAT"].sum()+data["murder"][data["state_ut"] == "RAJASTHAN"].sum()+data["murder"][data["state_ut"] == "BIHAR"].sum()+data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum(),rowt])





