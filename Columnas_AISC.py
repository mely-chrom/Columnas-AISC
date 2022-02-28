
#Código para determinar columnas AISC
from math import pi, sqrt
def esfuerzo_critico(klr, fy, e):
	if klr==0:
		fcr = fy
	else:
		fe = (pi**2*e)/klr**2
		limite = 4.71*sqrt(e/fy)
		if klr<=limite:
			fcr = (0.658**(fy/fe))*fy
		else:
			fcr = 0.877*fe
	return fcr

if __name__ == '__main__':
	u = -1
	while u!=1 and u!=2:
		print("¿Desea usar unidades del SI (1) o del Sistema inglés (2)?")
		u = float(input())
	if u==1:
		e = 200000
		un = "MPa"
	else:
		e = 29000
		un = "ksi"
	fy = -1
	while fy<=0:
		print("Ingrese el esfuerzo de fluencia del material Fy en ",un," (Fy > 0)")
		fy = float(input())
	klr = -1
	while klr<0 or klr>200 or klr!=int(klr):
		print("Ingrese el valor de la relación de esbeltez KL/r")
		klr = float(input())
	fcr = esfuerzo_critico(klr,fy,e)
	print("")
	print("Para una columna de acero con módulo de elasticidad ",e," ",un)
	print("Con la relación de esbeltez ",klr," el esfuerzo crítico de pandeo es ",fcr," ",un)
	klrv = [float() for ind0 in range(201)]
	fcrv = [str() for ind0 in range(201)]
	for i in range(1,202):
		klrv[i-1] = i-1
		fcrv[i-1] = esfuerzo_critico(klrv[i-1],fy,e)
	print("")
	print(" Esfuerzo crítico de pandeo E=",e," ",un," Fy=",fy," ",un)
	print(" KL/r    Fcr [",un,"]")
	print("------  -----------")
	for i in range(1,202):
		print(" ",klrv[i-1],"       ",fcrv[i-1])

