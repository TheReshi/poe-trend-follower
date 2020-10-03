import resources as res
from datetime import datetime
import time

urls = res.read_file('categories')

while True:
    if int(datetime.now().strftime('%M')) % 10 == 0:
        file = open('data/' + datetime.now().strftime('%Y-%m-%d_%H-%M'), 'w+')
        for url in urls:
            data = res.get_data(url)
            headers = res.get_headers(data)
            row_data = res.get_rows(data, len(headers))

            for row in row_data:
                new_item = ""
                for item in row:
                    new_item += item + ';'
                file.write(new_item[:-1] + '\n')

        file.close()
        print("Writing done: " + datetime.now().strftime('%Y-%m-%d_%H-%M'))
    time.sleep(61)

res.close_browser()