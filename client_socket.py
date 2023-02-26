import socket
import math
import string


LENGTH = 5  # definim lungimea cuvantului nostru

def ternary(n):     # aceasta functie transforma un numar din baza 10 in baza 3 sub forma unui string (o vom folosi la pattern-uri)
    if n == 0:
        return '00000'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    nums = ''.join(reversed(nums))
    if len(nums) < 5:
        nums = "0" * (5-len(nums)) + nums
    return nums


def match(cand, word, pattern):     # aceasta functie verifica daca doua cuvinte fac un match pe baza pattern-ului
    count = 0
    for i in range(5):
        if pattern[i] == '0' and cand[i] not in word:
            count += 1
        elif pattern[i] == '1' and cand[i] in word and cand[i] != word[i]:
            count += 1
        elif pattern[i] == '2' and cand[i] == word[i]:
            count += 1

    if count == 5:
        return 1
    else:
        return 0


def matchy(word, list_of_sets):    # aceasta functie returneaza true daca parametrul word poate fi o solutie
    if len(word) != len(list_of_sets):
        return False
    for i in range(len(word)):
        if word[i] not in list_of_sets[i]:
            return False
    return True


def entropie(word, words):      # aceasta functie calculeaza entropia parametrului word
    res = 0.0
    for i in range(0, 243):
        pattern = ternary(i)
        cazuri_fav = 0
        for pair in words:
            if match(pair, word, pattern):
                cazuri_fav += 1
        if cazuri_fav != 0:
            res += (cazuri_fav / len(words)) * math.log2(len(words) / cazuri_fav)
    return res


def client_program():       # acesta este programul principal ce face comunicarea cu server-ul
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))     # facem conexiunea catre server

    with open("cuvinte.txt", "r") as file:  
        text = file.read()
        words = list(map(str, text.split()))

    word_list_of_sets = [set(string.ascii_uppercase) for _ in range(LENGTH)]       # cream o lista de 5 multimi ce contine toate caracterele uppercase de la A la Z
    guess = "TAREI"
    while True:
        print(f"Cuvantul ales: {guess}", round(entropie(guess, words), 2))
        client_socket.send(guess.encode())      # trimitem guess-ul la server
        pattern = client_socket.recv(1024).decode()     # primim feedback-ul de la server sub forma unui pattern
        if str(pattern) == "GGGGG":     # daca pattern-ul este verde in intregime, am ghicit cuvantul
            print("Correct! You solved the WORDLE!")
            break
        
        for index in range(len(pattern)):       # parcurgem pattern-ul si eliminam litere din multimile cu index-ul unde caracterul este Y sau _
            if pattern[index] == "G":
                word_list_of_sets[index] = {guess[index]}       # daca litera se afla pe o pozitie verde, multimea cu index-ul index va contine numai acea litera
            elif pattern[index] == "Y":         # daca litera se afla pe o pozitie galbena, o eliminam din multimea cu index-ul index, intrucat nu apare pe acea pozitie in raspuns
                try:
                    word_list_of_sets[index].remove(guess[index])
                except KeyError:
                    pass
            else:       # daca litera este pe o pozitie gri, o eliminam din toate cele 5 multimi
                for nr_multime in range(len(word_list_of_sets)):
                    try:
                        word_list_of_sets[nr_multime].remove(guess[index])
                    except KeyError:
                        pass
        
        words = [word for word in words if matchy(word, word_list_of_sets)]     # filtram doar cuvintele ce respecta lista de multimi
        max_entropy = 0
        for word in words:      # calculam cuvantul cu entropia mexima
            curr_entropy = entropie(word, words)
            if curr_entropy > max_entropy:
                guess = word
                max_entropy = curr_entropy
        if len(words) == 1:
            guess = words[0]

    client_socket.close()  # inchidem conexiunea

if __name__ == '__main__':
    client_program()