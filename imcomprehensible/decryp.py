def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')  # Convertir la lettre chiffrée en nombre (0-25)
        k = ord(key[i % key_length]) - ord('A')  # Convertir la lettre de la clé en nombre
        p = (c - k) % 26  # Déchiffrement
        plaintext += chr(p + ord('A'))  # Reconversion en lettre
    return plaintext

ciphertext = "LLRXLRVOEHBNAEROQFNEEWZRVICOMANUWFMACDVXFRCMZOTRWELIKRWTMLVTCSZACANSVUQRMEKRQYNSUHVBVMVHAYNSEBUCQERVZRYRVVMACAEWTRBNVQCSQAIVLRBOEMIEMIEDOVEEIQGPNSFHCIAEJPITRSKUIYNSJRVGDNYBUANACDVNCUIHIYJLLPQRAEVWIHGRVITRCSJXZYNALOMHACFPXBBIKLWABAEVTVPNVGPBAIQRVCUOEJMYNSGHKGJTVXZQJNJXVRJTDRACQEIHNYXTKDVGNEKPMQRTRWQINRVYMYJNKXVRXBJHZIJTZRVZNTZFCYNUJHMGBEEVQOUEUXUBWDVYMTNTRO"
key = "JARDIN" # car Claude Monet est célèbre pour son jardin à Giverny.
                # L’ancien directeur et le conservateur avaient probablement choisi une clé symbolique et culturelle.
                # "JARDIN" est un mot de 6 lettres, en lien direct avec l’œuvre décrite.
plaintext = vigenere_decrypt(ciphertext, key)
print(plaintext)