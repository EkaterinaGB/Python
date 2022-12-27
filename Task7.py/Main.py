from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv
from File_writing import writing_txt
import logger as lg


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()

lg.logging.info('Start')
