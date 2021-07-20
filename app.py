import bs4
import requests
url = 'http://www.jadwalsholat.pkpu.or.id/?id=308'
konten = requests.get(url)


respon = bs4.BeautifulSoup(konten.text, "html.parser")
cari_elemen = respon.find_all('tr', 'table_highlight')
print(cari_elemen)

sholatt = {cari_elemen'td'}
print(sholatt)