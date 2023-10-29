import base64
import os
from collections import Counter
import socket
import pickle


CHARSET = base64._b85alphabet.decode()
N = len(CHARSET)


# Fonction pour calculer la fréquence des caractères en base 85 dans un texte
def calculate_base85_frequency(text):
    # Définition de l'alphabet Base85
    base85_alphabet = base64._b85alphabet.decode()
    
    # Utilisation de Counter pour calculer la fréquence des caractères
    frequency = Counter(char for char in text if char in base85_alphabet)
    
    return frequency


def get_key(plaintext, known_text):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += CHARSET[(CHARSET.find(known_text[i]) - CHARSET.find(plaintext[i])) % N]
    return ciphertext

known_text = "LQOUR3"
texts = []
host="instances.challenge-ecw.fr" 
port=40750


"""
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((host, port))
	response = sock.recv(4096)
	print(response)

	for i in range(20000):
		if i% 100 == 0:
			print(i)
		sock.send("1\n".encode())
		response = sock.recv(4096)
		response = response.decode().split("\n")
		texts.append(response[0])

		
	sock.close()


with open('res2.pkl', 'wb') as f:
	pickle.dump(texts, f)
"""

"""
with open('res.pkl', 'rb') as f:
	texts = pickle.load(f)

with open('res2.pkl', 'rb') as f:
	texts += pickle.load(f)



text_length = len(texts[0])
print(text_length)

res = ""

# Parcourir chaque index
for index in range(text_length):
    # Liste pour stocker les caractères à l'index donné
    characters = [text[index] for text in texts]

    # Compter la fréquence de chaque caractère à l'index donné
    character_count = Counter(characters)

    # Trouver le caractère le plus fréquent
    most_common_character = character_count.most_common(1)[0]
    #print(most_common_character[0])
    res += most_common_character[0]
    # Afficher le résultat pour chaque index


print(res)

"""
#print(calculate_base85_frequency(text))

a =  "LQUQV00000004>r004Xd003(M000F5000317ytkO002}5000vU000vU000000000000000{{R600093000000002TqQgZ+R00000000000000000000000000000000000000000000000000000000006200000000000000000000000000000000960|NsC000000000000RR90|NsC0|Nj600RR9000030|NsC0|NsC0|Ns90000000RR9000000000000RR90|NsC0|Nj6000000|NsC0|Nj600000000030|NsC0{{R3000000000000RR9000030|NsC0{{R30|NsC0|Nj600RR90|Ns90000000RR90|NsC0|Nj600000000030|NsC0{{R300000000960{{R30|NsC0|Nj6000000|NsC0|Nj60000000000000960{{R300000000960|NsC000030|NsC0{{R300000000960{{R300000000960|NsC0000000000000000|NsC0|Nj600RR9000030|Nj6000000|Ns90000000RR90|NsC0|NsC0{{R30|NsC0|NsC0|NsC0|Ns9000960{{R30|Ns9000960|NsC0|Ns9000960|NsC000030|NsC0{{R30|Ns9000960|NsC000030|NsC0|NsC0|Ns9000960|NsC0|NsC0|NsC0|NsC000030|NsC0{{R30|NsC0|Nj600RR9000030|NsC0{{R30|Ns9000960|NsC000030|Nj600RR90|Ns9000960{{R30|Ns9000960|NsC000030|NsC0|NsC0|NsC0|NsC0{{R30|NsC0|Nj600RR9000030|Nj600RR90|Ns9000960|NsC0|Ns90000000RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0{{R30|Ns90000000000000030|NsC0{{R30|NsC0|NsC0|NsC000030|NsC0{{R30|NsC0|Nj600RR900000000960|NsC000030|NsC0{{R30|NsC0|Nj6000000|NsC0|Nj600000000030|NsC0|NsC0|NsC0|NsC0|NsC000030|NsC0{{R30|NsC0|Nj600RR9000030|NsC0{{R30|Ns9000960|NsC000030|Nj600RR90|Ns9000960{{R30|Ns9000960|NsC000030|NsC0|NsC0|NsC0|NsC0{{R30|NsC0|Nj600RR9000030|Nj600RR90|Ns9000960{{R3000030|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nj600RR9000030|NsC0{{R3000000000000RR90|NsC0|NsC0{{R30|NsC0|NsC0|NsC000030|NsC0|NsC0|NsC0|Nj600RR90|Ns9000960|NsC000000000000RR90|Ns9000960|NsC000030|Nj600RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC000000000000RR900000000960|NsC0|Ns90000000RR90|NsC0|Nj600000000030|Nj600RR90|Ns9000960{{R30|NsC0|Nj6000000|NsC0|NsC0|NsC0|NsC0|NsC0{{R300000000960|NsC0|NsC0|NsC0{{R300000000960|NsC000000000000RR90|NsC0|NsC0|NsC0|NsC0|Nj600RR9000030|NsC0{{R30|Ns9000000000000000000960|NsC000000000000RR9000030|NsC0|NsC0|NsC0|Nj600RR90|Ns90000000RR9000030|NsC0|NsC0|NsC0|Nj6000000|NsC0|Nj60000000000000960|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC000030|NsC0|NsC0|NsC0|NsC0{{R30|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0{{R30|NsC0|NsC0|NsC000030|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nj600RR9000030|Nj6000000|Ns90000"

b = base64.b85decode(a)

with open("flag.bmp","bw") as f:
	f.write(b)