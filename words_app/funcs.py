from bs4 import BeautifulSoup
import re
def how_many_words(id_file):
    soup=BeautifulSoup(open("/home/estudiante/tarea1/Tarea1_BigData/words_app/"+id_file),'html.parser')
    ocurrences=soup.find_all('body')
    how_many=0
    for item in ocurrences:
        lines=item.get_text()
        how_many+=len(re.split('[\n ]+',lines))-2
    return how_many

#print(how_many_words('/home/estudiante/tarea1/Tarea1_BigData/words_app/reut2-008.sgm'))

