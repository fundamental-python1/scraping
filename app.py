import bs4
import requests
url = 'http://www.jadwalsholat.pkpu.or.id/?id=308'
konten = requests.get(url)


respon = bs4.BeautifulSoup(konten.text, "html.parser")
cari_elemen = respon.find_all('tr', 'table_highlight')
cari_elemen = cari_elemen[0]
# print(cari_elemen)

i = {}
# barisss = 0
for i in cari_elemen:
    # if baris == 0:
    # print(i.get_text())
    i['kata'] = i.get_text()
    print (i)


#a = {}
#kolom = 0
# for daftar_waktu, val in enumerate(cari_elemen):
#     # a = daftar_waktu.get_text()
#     print(daftar_waktu, val)

# zz = ['s','d','f','g','h']
# if i, g in enumerate(zz):
#     print(i,g)





    # if kolom == 1:
    #     a['subuh'] = daftar_waktu.get_text()
    # elif kolom == 2:
    #     a['dhuhur'] = daftar_waktu.get_text()
    # elif kolom == 3:
    #     a['ashar'] = daftar_waktu.get_text()
    # elif kolom == 4:
    #     a['maghrib'] = daftar_waktu.get_text()
    # elif kolom == 1:
    #     a['isya'] = daftar_waktu.get_text()
    # kolom += 1
   # print(a)


#sholat = {}
#a = 0
#for b in cari_elemen:
#    if a == 1:
#        sholat['subuh'] = b.get_text()
#    a += 1

#print(sholat)