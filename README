<b>Acest proiect a fost realizat în cadrul cursului de <a href="https://cs.unibuc.ro/~crusu/asc/">Arhitectura Sistemelor de Calcul</a>, semestrul I, anul I.</b>


Proiect realizat de:
•	Dogărel Andrei – Grupa 132
•	Dogaru Mihail-Dănuț – Grupa 132
•	Simiraș Teofil – Grupa 132
•	Cărăulașu Cătalin – Grupa 132


Scurtă descriere a proiectului:
	Proiectul are la bază cele două programe realizate în limbajul Python, comunicarea făcându-se prin intermediul IPC ce utilizează modulul socket. Programul server_socket.py reprezintă partea jocului Wordle care primește un cuvânt și colorează pozițiile literelor în funcție de apariția acestora în răspuns. Totodată aici este luat și răspunsul, și anume un cuvânt aleator din fișierul “cuvinte.txt”, ce urmează să fie ghicit de către client.
	Programul client_socket.py reprezintă partea ce joacă eficient jocul, algoritmul fiind următorul: parcurgem lista de cuvinte și îl trimitem la server pe cel mai bun conform entropiei lui Shanon, obținându-se astfel un pattern, conform căruia vom reduce lista de cuvinte posibile. Cât timp nu s-a găsit răspunsul, se vor parcurge acești pași. Entropia fiecărui cuvânt este calculată în felul următor: parcurgem toate cele 243 de pattern-uri posibile și calculăm probabilitatea, respectiv cantitatea de informație a fiecăruia, însumându-se la final.


Numărul mediu de încercări:	5.05 încercări


Modul de rulare al programului:
	Se vor deschide două terminale, urmând a fi rulate, în ordine, programele server_socket.py și client_socket.py cu ajutorul comenzii python3 (Linux) sau python (Windows).


Observații:
•	Programul necesită instalarea manuală a modului termcolor pentru a obține cuvintele colorate. Modulul se poate descărca utilizând comanda pip install termcolor.
•	În cazul în care apare o problemă la rularea de mai multe ori a celor două programe, trebuie așteptat minim 30 de secunde între rulări. Este o eroare cauzată de comunicarea prin sockeți.


Referințe:
•	https://realpython.com/python-sockets/
•	https://www.youtube.com/watch?v=v68zYyaEmEA&t=3s&ab_channel=3Blue1Brown
