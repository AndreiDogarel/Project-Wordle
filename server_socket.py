import socket
import random
from termcolor import colored       # necesita o descarcare pentru a putea fi folosita (comanda pentru terminal: pip install termcolor)

def guessVerdict(answer, guess):        # aceasta functie returneaza un tuplu format din cuvantul feedback colorat in functie de pattern si pattern-ul
    verdict = ""
    pattern = ""
    elements = list(answer)
    green = []
    yellow = []
    position = 0
    for i in guess:
        if i == answer[position]:
            green.append(position)
            elements[position] = False
        position += 1
    position = 0
    for i in guess:
        if i != answer[position] and i in elements:
            yellow.append(position)
            try:
                elements.remove(i)
            except ValueError:
                pass
        position += 1
    for i in range(len(guess)):
        if i in green:
            verdict += colored(guess[i], 'green', attrs = ['reverse'])
            pattern += "G"
        elif i in yellow:
            verdict += colored(guess[i], 'yellow', attrs = ['reverse'])
            pattern += "Y"
        else:
            verdict += colored(guess[i], 'grey', attrs = ['reverse'])
            pattern += "_"
    return verdict, pattern

def color_green(word):      # functia returneaza parametrul word colorat complet cu verde, este folosita cand client-ul a ghicit cuvantul
    res = ""
    for letter in word:
        res += colored(letter, 'green', attrs = ['reverse'])
    return res

def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))

    with open("cuvinte.txt", "r") as file:      # obtinem lista de cuvinte
        text = file.read()
        words = list(map(str, text.split()))
    answer = random.choice(words)       # alegem un cuvant random din lista noastra de cuvinte
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:        # daca nu primim date, dam break
            break
        candidate = str(data)
        if answer == candidate:         # daca am ghicit cuvantul
            pattern = "GGGGG"
            print(color_green(candidate))
            conn.send(pattern.encode())     # trimitem pattern-ul catre client
            break
        verdict, pattern = guessVerdict(answer, candidate)      # in caz contrar, pastram un cuvant colorat in functie de pattern (verdict) si pattern-ul ce va fi trimis la client
        print(verdict)
        print("\n")
        conn.send(pattern.encode())     # trimitem pattern-ul clientului

    conn.close()        # inchidem conexiunea


if __name__ == '__main__':
    server_program()