import pdfkit as pdf
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [ 'https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive' ]

credentials = ServiceAccountCredentials.from_json_keyfile_name('Projekat-73ef94dc4536.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Hospital").sheet1

df = pd.DataFrame(wks.get_all_records())

html = df.to_html()

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ]

}

pdf = pdf.from_string(html, "Hospital.pdf", options=options)
print(pdf)
