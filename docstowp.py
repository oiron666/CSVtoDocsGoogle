import gspread
import csv
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

creds = ServiceAccountCredentials.from_json_keyfile_name('googlecreds.json', scope)
client = gspread.authorize(creds)
sheet = client.open('apka1').sheet1
output = sheet.get_all_records()
gspread #googleapi stuff
i = 0

while True: #searching for empty cell
    i +=1
    cellcontent = sheet.cell(i, 1).value
    if cellcontent == '':
         break

with open('csvfile.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)

    for line in reader:
        title = line[0]
        url = line[1]
        author = line[2]
        ups = line[3]
        downs = line[4]
        comments = line[5]
        over18 = line[6]
        sheet.update_cell(i, 1, title)
        sheet.update_cell(i, 2, url)
        sheet.update_cell(i, 3, author)
        sheet.update_cell(i, 4, ups)
        sheet.update_cell(i, 5, downs)
        sheet.update_cell(i, 6, comments)
        sheet.update_cell(i, 7, over18)
        i +=1
