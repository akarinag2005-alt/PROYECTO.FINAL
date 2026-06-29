Algoritmo Ahorcado_juego
	
		
		Definir opcion, categoria, dificultad Como Cadena
		Definir palabra, letra Como Cadena
		Definir intentos, i Como Entero
		Definir ganar, salir, encontrada Como Logico
		Definir mostrada Como Cadena
		
		Dimension mostrada[20]
		
		salir <- Falso
		
		Mientras salir = Falso Hacer
			
			Limpiar Pantalla
			
			Escribir "1. Jugar"
			Escribir "2. Salir"
			Leer opcion
			
			Si opcion = "2" Entonces
				salir <- Verdadero
			SiNo
				
				Escribir "1. Programacion"
				Escribir "2. Animales"
				Leer categoria
				
				Escribir "1. Facil"
				Escribir "2. Dificil"
				Leer dificultad
				
				Si categoria = "1" Entonces
					Si dificultad = "1" Entonces
						palabra <- "JAVA"
					SiNo
						palabra <- "PYTHON"
					FinSi
				SiNo
					Si dificultad = "1" Entonces
						palabra <- "GATO"
					SiNo
						palabra <- "ELEFANTE"
					FinSi
				FinSi
				
				intentos <- 5
				
				Para i <- 1 Hasta Longitud(palabra) Hacer
					mostrada[i] <- "_"
				FinPara
				
				ganar <- Falso
				
				Mientras intentos > 0 Y ganar = Falso Hacer
					
					Escribir ""
					Para i <- 1 Hasta Longitud(palabra) Hacer
						Escribir Sin Saltar mostrada[i], " "
					FinPara
					
					Escribir ""
					Escribir "Intentos: ", intentos
					
					Escribir "1. Letra"
					Escribir "2. Pista"
					Escribir "3. Rendirse"
					Leer opcion
					
					Si opcion = "1" Entonces
						
						Escribir "Ingrese letra:"
						Leer letra
						
						encontrada <- Falso
						
						Para i <- 1 Hasta Longitud(palabra) Hacer
							
							Si Subcadena(palabra,i,i) = Mayusculas(letra) Entonces
								mostrada[i] <- Mayusculas(letra)
								encontrada <- Verdadero
							FinSi
							
						FinPara
						
						Si encontrada = Falso Entonces
							intentos <- intentos - 1
						FinSi
						
					FinSi
					
					Si opcion = "2" Entonces
						Escribir "PISTA:"
						Escribir "La primera letra es: ", Subcadena(palabra,1,1)
					FinSi
					
					Si opcion = "3" Entonces
						intentos <- 0
					FinSi
					
					ganar <- Verdadero
					
					Para i <- 1 Hasta Longitud(palabra) Hacer
						Si mostrada[i] = "_" Entonces
							ganar <- Falso
						FinSi
					FinPara
					
				FinMientras
				
				Si ganar Entonces
					Escribir "GANASTE"
					Escribir "La palabra era: ", palabra
				SiNo
					Escribir "PERDISTE"
					Escribir "La palabra era: ", palabra
				FinSi
				
				Escribir "Presione ENTER para volver al menu"
				Esperar Tecla
				
			FinSi
			
		FinMientras
		
FinAlgoritmo