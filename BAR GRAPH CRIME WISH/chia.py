import pandas as pd
from scipy import stats
import array
data=pd.read_csv('project_file11.csv')  

rowhead=['rape','robbery','murder','total']
rowguj=[data["rape"][data["state_ut"] == "GUJARAT"].sum(),data["robbery"][data["state_ut"] == "GUJARAT"].sum(),data["murder"][data["state_ut"] == "GUJARAT"].sum()]
rowraj=[data["rape"][data["state_ut"] == "RAJASTHAN"].sum(),data["robbery"][data["state_ut"] == "RAJASTHAN"].sum(),data["murder"][data["state_ut"] == "RAJASTHAN"].sum()]
rowbihar=[data["rape"][data["state_ut"] == "BIHAR"].sum(),data["robbery"][data["state_ut"] == "BIHAR"].sum(),data["murder"][data["state_ut"] == "BIHAR"].sum()]
rowup=[data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum()]
rowt=data["rape"][data["state_ut"] == "GUJARAT"].sum()+data["rape"][data["state_ut"] == "RAJASTHAN"].sum()+data["rape"][data["state_ut"] == "BIHAR"].sum()+data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["robbery"][data["state_ut"] == "GUJARAT"].sum()+data["robbery"][data["state_ut"] == "RAJASTHAN"].sum()+data["robbery"][data["state_ut"] == "BIHAR"].sum()+data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum()+data["murder"][data["state_ut"] == "GUJARAT"].sum()+data["murder"][data["state_ut"] == "RAJASTHAN"].sum()+data["murder"][data["state_ut"] == "BIHAR"].sum()+data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum()
rowtot=["TOTAL",data["rape"][data["state_ut"] == "GUJARAT"].sum()+data["rape"][data["state_ut"] == "RAJASTHAN"].sum()+data["rape"][data["state_ut"] == "BIHAR"].sum()+data["rape"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["robbery"][data["state_ut"] == "GUJARAT"].sum()+data["robbery"][data["state_ut"] == "RAJASTHAN"].sum()+data["robbery"][data["state_ut"] == "BIHAR"].sum()+data["robbery"][data["state_ut"] == "UTTAR PRADESH"].sum(),data["murder"][data["state_ut"] == "GUJARAT"].sum()+data["murder"][data["state_ut"] == "RAJASTHAN"].sum()+data["murder"][data["state_ut"] == "BIHAR"].sum()+data["murder"][data["state_ut"] == "UTTAR PRADESH"].sum(),rowt]

table=[rowguj,rowraj,rowbihar,rowup]
print(table)
chi2_stat, p_val, dof, ex = stats.chi2_contingency(table)
print("===Chi2 Stat===")
print(chi2_stat)
print("\n")
print("===Degrees of Freedom===")
print(dof)
print("\n")
print("===P-Value===")
print(p_val)
print("\n")
print("===Contingency Table===")
print(ex)

