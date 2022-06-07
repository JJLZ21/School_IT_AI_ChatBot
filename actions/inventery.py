import gspread
path = "./.env/sheet_credentials.json"
service = gspread.service_account(filename=path)

sheet = service.open("dummy_inventery")

inventery = sheet.worksheet("db")

inventery_list = {
    'headphone': "A2",
    'ipad': 'B2',
    'macbook': 'C2',
    'headphones': "A2",
    'ipads': 'B2',
    'macbooks': 'C2',
}


def get_count(item):
    item = item.lower()
    if item in inventery_list:
        return int(inventery.acell(inventery_list.get(item)).value)


def update_count(item, count):
    item = item.lower()
    if item in inventery_list:
        item_count = int(inventery.acell(inventery_list.get(item)).value)
        if item_count - count < 0:
            return f"No enough item, current we have {inventery.acell(inventery_list.get(item)).value} left"
        else:
            inventery.update(inventery_list.get(item), str(item_count-count))
            return "success"
    else:
        return f"We only have headphone: {inventery.acell('A2').value}, iPad: {inventery.acell('B2').value}, Macbook: {inventery.acell('C2').value}"


update_count("ipads", 1)
