import csv
import requests

user = 'python-demo'
password = 'claw30_bumps'

def import_csv_from_url(url):
    with requests.Session() as s:
        download = s.get(url, auth=(user, password))
        if (download.status_code == 401):
            return -1

        decoded = download.content.decode('utf-8')
        cr = csv.reader(decoded.splitlines(), delimiter=';')
        return list(cr)

def import_csv_from_file(path):
    data=[]
    try:
        with open(path, 'r') as csvfile:            
            file = csv.reader(csvfile, delimiter=';')
            for row in file:
                row_data = []
                for dat in row:
                    row_data.append(dat)
                data.append(row_data)

        return data
    except:
        return -1
