meme_dict = {
    "LOL" : "Tanggapan terhadap sesuatu yang lucu",
    "CRINGE" : "sesuatu yang aneh atau memalukan",
    "ROFL" : "Tanggapan terhadap lelucon",
    "SHEESH" : "sedikit ketidaksetujuan",
    "CREEPY" : "menakutkan, tidak menyenangkan",
    "AGGRO" : "untuk menjadi agresif/marah",
}

for i in range(len(meme_dict)):
    meme=(input("Masukkan key"))
    print(meme_dict[meme])
