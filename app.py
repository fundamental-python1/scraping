import bs4
import requests
url = 'http://www.jadwalsholat.pkpu.or.id/?id=308'
konten = requests.get(url)


respon = bs4.BeautifulSoup(konten.text, "html.parser")
cari_elemen = respon.find_all('tr', 'table_highlight')
cari_elemen = cari_elemen[0]
print(cari_elemen)

for daftar_waktu in cari_elemen:
    print(daftar_waktu.get_text())

#sholat = {}
#a = 0
#for b in cari_elemen:
#    if a == 1:
#        sholat['subuh'] = b.get_text()
#    a += 1

#print(sholat)