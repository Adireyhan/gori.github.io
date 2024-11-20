def buat_perjanjian(nama_audiens):
    perjanjian = f"""
    PERJANJIAN
    ===============================
    
    Kami yang membuat ini menyatakan:

    Nama Audiens: {nama_audiens}

    Dengan ini setuju untuk:
    1. memberikan waktu anda dalam kurun waktu seumur hidup, huhuhuhuhu.
    2. selalu lapang dada dan memaafkan atas pembullyan yang adi reyhan berikan.
    3. menyayangi dan mencintai adi reyhan dalam kurun waktu seumur hidup, yeyyy.
    4. selalu memaafkan atas ledekan ledekan yang adi reyhan al farizky lontarkan, maafin aku yakk.
    5. selalu jujur kepada adi reyhan. inget!!! tidak boleh boong, dosa.

    Demikian perjanjian yang adi reyha buat, dengan ini menyatakan bahwa kamu setuju dengan perjanjian yang adi reyhan buat terimakasih atas perhatian nya akhir kata penulis mengucapkan i love you sayangkuuuuuuuu
    .
    
    Tanggal: ______________________
    Tanda Tangan: ________________
    """
    return perjanjian

# Meminta input nama audiens
nama_audiens = input("Masukkan nama audiens: ")
perjanjian = buat_perjanjian(nama_audiens)

# Menampilkan perjanjian
print(perjanjian)