#fahrenheit=float(input('Entre com a temperatura em fahrenheit:\n'))
#fahrenheit=input('Entre com a temperatura em fahrenheit:\n')
#Celsius=(fahrenheit-32)*5/9
#print(fahrenheit,"fahrenheit é igual a {:.2f}". format(Celsius), "celsius")

segundos=int(input("Entre com a quantidade total de segundos:\n"))
dias=segundos//(3600*24)
horas=segundos%(3600*24)
minutos=horas%3600
horas=horas//3600
segundos=minutos%60
minutos=minutos//60
print(dias,"dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")