import openpyxl as xl

def create_list(sheet):
    all_data = tuple(sheet.columns)

    eng1 = list()
    pbi1 = list()
    pbi2 = list()
    pbi3 = list()
    all_pbi = (eng1, pbi1, pbi2, pbi3)

    count = 0
    for a in all_pbi:
        for i in all_data[count]:
            a.append(str(i.value).replace(' ', ''))
        count += 1
    return all_pbi


def search_word(my_list, word):
    word = word.replace(' ', '')

    try:
        index = (my_list[1].index(word))
    except ValueError:
        try:
            index = (my_list[2].index(word))
        except ValueError:
            try:
                index = (my_list[3].index(word))
            except ValueError:
                print('Not found')
    return my_list[0][index]


xl_sheet = xl.load_workbook('Test1.xlsx')
sheet = xl_sheet['Sheet1']

my_list = create_list(sheet)
print(search_word(my_list, '    ਮੈਖਾਨਾ   '))