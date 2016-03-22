#! python3
import openpyxl, bs4, requests, sys

wb = openpyxl.load_workbook('PlayerID.xlsx')
sheet = wb.get_sheet_by_name('PLAYERIDMAP')

def fangraphs(name):
    stats ={}
    stats2 = []
    for r in range(2, sheet.max_row+1):
        if name == sheet['B' + str(r)].value:
            ID = sheet['I' + str(r)].value
            res = requests.get('http://www.fangraphs.com/statss.aspx?playerid='
                               + str(ID))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            page = soup.select('div th')
            if page == []:
                print('Nothing here.')
            else:
                for h in range(len(page)):
                    stats.setdefault(page[h].getText(), [])
                    stats2.append(page[h].getText())
            page2 = soup.find_all('td', {'class':['grid_line_regular','grid_line_break']})
            c = 0
            for d in range(len(page2)):
                #print(page2[d].getText())
                if page2[d].getText() == '\xa0':
                    stats[stats2[c]].append(' ')
                else:
                    stats[stats2[c]].append(page2[d].getText())
                c += 1
                if c == 21:
                    c = 0
            #print(stats[stats2[0]])
            #print(stats2[0])
fangraphs('Mike Trout')          

                   
# print stats to see if dictionary is properly being made

# find out why post season is being printed, how to stop it
