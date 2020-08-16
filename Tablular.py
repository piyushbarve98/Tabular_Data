from tabulate import tabulate

data= {'Name':['Piyush Barve','Prakhar Potdar','Ayush Tiwari','Praveen Dubey'],'Branch':['IT','CS','CS','CS'],'ID':['2341','1224','2342','4325']}
table= tabulate(data,headers='keys',tablefmt='pretty',showindex='always')
print(table)