from urllib import request
import json

def get_url(datum):
    result = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=" + datum
    return result

def get_content(datum):
    try:
        response = request.urlopen(get_url(datum))
        if response.status == 200:
            content = response.read()
    except Exception as inst:
        print(inst)
    return (content.decode("utf-8")).split("\n")

def get_record(line, datum):
    fields = line.split("|")
    try:
        record = {
                     "date": datum,
                     "currency": fields[3],
                     "ratio": fields[2],
                     "rate": fields[4].replace(",", ".")
                }
    except:
        record = {}
    return json.dumps(record)

def cnbrates(datum):
    lines = get_content(datum)

    count = 0.
    records = []
    for line in lines:
        if count > 1 and count < len(lines) - 1:
            records.append(get_record(line, datum))
        count += 1
    print(records)






