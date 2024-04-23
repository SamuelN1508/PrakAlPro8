# Membuka file pertama
with open("8,11.txt", "r", encoding="utf8") as filex:
    # membaca seluruh baris
    lines1 = filex.readlines()

# Membuka file kedua
with open("8,12.txt", "r", encoding="utf8") as filey:
    lines2 = filey.readlines()
    
def compare(lines1, lines2):
    # Mencari jumlah baris terbanyak
    max_len = max(len(lines1), len(lines2))
    
    # Loop dalam range baris terbanyak
    for i in range(max_len):
        # Jika jumlah baris lines1 lebih sedikit, maka baris yang kosong akan diisi dengan None
        if i < len(lines1):
            baris1 = lines1[i].strip()
        else:
            baris1 = None
            
        # Jika jumlah baris lines2 lebih sedikit, maka baris yang kosong akan diisi dengan None           
        if i < len(lines2):
            baris2 = lines2[i].strip()
        else:
            baris2 = None
        
        # Mengecek perbaris apakah ada yang berbeda
        if baris1 != baris2:
            print(f'Perbedaan pada baris {i+1}:')
            print(f'File 1: {baris1}')
            print(f'File 2: {baris2}')
        
compare(lines1, lines2)