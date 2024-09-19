from requests import get
from json import loads
from terminaltables import AsciiTable
CITIES = input('Podaj miasto : ')
def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru','Temperatura', 'Ciśnienie','Predkosc wiatru m/s','Suma opadu mm']
    ]
    for row in loads(response.text):
        if row['stacja'] in CITIES:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie'],
                row['predkosc_wiatru'],
                row['suma_opadu']

            ])
    table = AsciiTable(rows)
    print(table.table)

if __name__ =='__main__':
    main()