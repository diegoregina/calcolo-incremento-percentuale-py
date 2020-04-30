print("Calcolo sconto - incremento percentuale.\n")
print("Versione 0.1.1 (2015)\n")
print("sviluppato per la Tenda Sistem srl da Diego Regina\n\n\n")
risposta = "n"
while risposta != "s":
	PrezzoDiPartenza = float(input("\nPrezzo di partenza: "))
	PrezzoFinale = float(input ("Prezzo finale: "))
	Sconto = (-1*(100-(PrezzoFinale*100)/PrezzoDiPartenza))
	if Sconto < 0:
		print("+-----------------------------------------------+")
		print("Lo sconto e' del ", Sconto, "%")
		print("+-----------------------------------------------+")
	else:
		print("+-----------------------------------------------+")
		print("| L'incremento e' del ", Sconto, "%")
		print("+-----------------------------------------------+")
	risposta = str(input("\nvuoi uscire dal programma? si= s, no= invio "))
	

