import bs4
import requests
url = 'http://www.jadwalsholat.pkpu.or.id/?id=308'
konten = requests.get(url)


respon = bs4.BeautifulSoup(konten.text, "html.parser")
cari_elemen = respon.find_all('tr', 'table_highlight')
cari_elemen = cari_elemen[0]
# print(cari_elemen)

# for i in cari_elemen:
#     a = i.get_text()
#     print(a)

sholat = {}
i = 0
for waktu in cari_elemen:
    # cari_elemen = cari_elemen.get_text()
    if i == 0:
        sholat ['Nomor'] = waktu.get_text()
    elif i == 1:
        sholat['Shubuh'] = waktu.get_text()
    elif i == 2:
        sholat['dhuhur'] = waktu.get_text()
    elif i == 3:
        sholat['ashar'] = waktu.get_text()
    elif i == 4:
        sholat['maghrib'] = waktu.get_text()
    elif i == 5:
        sholat['isya'] = waktu.get_text()
    i += 1
print(sholat)
print(sholat['ashar'])



#a = {}
#kolom = 0
# for daftar_waktu, val in enumerate(cari_elemen):
#     # a = daftar_waktu.get_text()
#     print(daftar_waktu, val)

# zz = ['s','d','f','g','h']
# if i, g in enumerate(zz):
#     print(i,g)


