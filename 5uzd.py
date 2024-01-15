def ievadit_varu():
    vara_n = input("Lūdzu, ievadiet savu vārdu: ")
    return vara_n

def izveidot_failu(faila_nosaukums, vara_n):
    try:
        with open(faila_nosaukums, 'a') as f:
            f.write(vara_n + '\n')
        return True
    except IOError:
        return False

def paziņot(rezultats):
    if rezultats:
        print("Vārds veiksmīgi ierakstīts failā!")
    else:
        print("Neizdevās ierakstīt vārdu failā! Lūdzu, mēģiniet vēlreiz.")

if __name__ == "__main__":
    vara_n = ievadit_varu()
    rezultats = izveidot_failu("lietotajs.txt", vara_n)
    paziņot(rezultats)