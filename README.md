<h2><b>Acest proiect a fost realizat în cadrul cursului de <a href="https://cs.unibuc.ro/~crusu/asc/">Arhitectura Sistemelor de Calcul</a>, semestrul I, anul I.</b></h2>


<h2><b>Proiect realizat de:<b>
	<ul>
		<li><i>Dogărel Andrei – Grupa 132</i></li>
		<li><i>Dogaru Mihail-Dănuț – Grupa 132</i></li>
		<li><i>Simiraș Teofil – Grupa 132</i></li>
		<li><i>Cărăulașu Cătălin – Grupa 132</i></li>
	</ul>
</h2>

<h2><b>Scurtă descriere a proiectului:</b>
	<ul>
		<li><p align="justify">Proiectul are la bază cele două programe realizate în limbajul Python, comunicarea făcându-se prin intermediul IPC ce utilizează modulul socket. Programul <i>server_socket.py</i> reprezintă partea jocului Wordle care primește un cuvânt și colorează pozițiile literelor în funcție de apariția acestora în răspuns. Totodată aici este luat și răspunsul, și anume un cuvânt aleator din fișierul “cuvinte.txt”, ce urmează să fie ghicit de către client.
		Programul <i>client_socket.py</i> reprezintă partea ce joacă eficient jocul, algoritmul fiind următorul: parcurgem lista de cuvinte și îl trimitem la server pe cel mai bun conform entropiei lui Shanon, obținându-se astfel un pattern, conform căruia vom reduce lista de cuvinte posibile. Cât timp nu s-a găsit răspunsul, se vor parcurge acești pași. Entropia fiecărui cuvânt este calculată în felul următor: parcurgem toate cele 243 de pattern-uri posibile și calculăm probabilitatea, respectiv cantitatea de informație a fiecăruia, însumându-se la final.</p></li>
	</ul>
<h2>

<h2>Numărul mediu de încercări:	<i>5.05 încercări</i></h2>


<h2>Modul de rulare al programului:
	<ul>
		<li><p align="justify">Se vor deschide două terminale, urmând a fi rulate, în ordine, programele server_socket.py și client_socket.py cu ajutorul comenzii python3 (Linux) sau python (Windows).</p></li>
	</ul>
</h2>

<h2>Observații:
	<ul>
		<li>Programul necesită instalarea manuală a modului termcolor pentru a obține cuvintele colorate. Modulul se poate descărca utilizând comanda pip install termcolor.</li>
		<li>În cazul în care apare o problemă la rularea de mai multe ori a celor două programe, trebuie așteptat minim 30 de secunde între rulări. Este o eroare cauzată de comunicarea prin sockeți.</li>
	</ul>
</h2>

<h2>Referințe:
	<ul>
		<li>https://realpython.com/python-sockets/</li>
		<li>https://www.youtube.com/watch?v=v68zYyaEmEA&t=3s&ab_channel=3Blue1Brown</li>
	</ul>
</h2>
