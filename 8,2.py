# Masukan nama file
nama_file = input("nama file1 : ")

# Mengecek apakah nama file benar
try :
    # Membuka file
    with open(nama_file, "r", encoding="utf8") as file:
        # Pertanyaan dan jawaban sebagai list kosong
        pertanyaan = []
        jawaban = []
        
        # Loop dalam file
        for line in file:
            # Dibagi menjadi list yang ada 2 isi yaitu pertanyaan dan jawaban
            tanya_jawab = line.strip().split("||")
            
            # Masing-masing dimasukan ke dalam list tersendiri
            pertanyaan.append(tanya_jawab[0])
            jawaban.append(tanya_jawab[1])
        
        # Mencari jumlah baris tertinggi
        max_len = max(len(pertanyaan), len(jawaban))
        
        # Loop dalam jangkauan max_len
        for i in range(max_len):
            # Print pertanyaan
            print(pertanyaan[i])
            
            # Meminta jawaban
            user_input = input()
            
            # mengecek apakah jawaban benar dan sesuai dengan pertanyaan
            if user_input.strip().lower() == jawaban[i].strip().lower():
                print("Jawaban benar!")
            else:
                print("Jawaban salah!")
except:
    print("masukan file yang benar")
