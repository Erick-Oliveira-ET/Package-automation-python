import csv
import glob

class database:
    def __init__(self):
        self.db = "db.csv"
    
    def dbCreate(self):
        fileExist = glob.glob("db.csv", recursive = True) #search if the file exist and return a list
        if not fileExist:
            with open(self.db, 'w', newline='') as csvfile:
                fieldnames = ['product_name', 'product_code']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()


    def findAll(self):
        try:
            with open(self.db, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                print("Nome do Produto       |        Código do produto")
                for row in reader:
                    print(row['product_name'], "                  ", row['product_code'])
            
        except FileNotFoundError as error:
           print("Banco de Dados não encontrado. Um novo será criado.")
           print(error)
           self.dbCreate()
        

    def find_one_by_name(self, name):
        try:
            with open(self.db, 'r', newline='') as csvfile :
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['product_name'].lower() in name.lower():
                        return row['product_code']
        
        except FileNotFoundError as error:
           print("Banco de Dados não encontrado. Um novo será criado.")
           print(error)
           self.dbCreate()
        
    def create(self, name, code):
        try:
            #a is to append the new line on the file
            with open(self.db, 'a', newline='') as csvfile:
                fieldnames = ['product_name', 'product_code']
            
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({'product_name': name, 'product_code': code})
        
        except FileNotFoundError as error:
           print("Banco de Dados não encontrado. Um novo será criado.")
           print(error)
           self.dbCreate()
        
    def destroy(self, name):
        #As there's no way to delete a line using open,
        #the easiest way was to pass everydata on the file to a list 
        #except the line that will be "deleted" and then passing
        #the data to the file again
        temp = []
        try:
            with open(self.db, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not (row['product_name'] in name):
                        temp.append([row['product_name'], row['product_code']])
                        
            with open(self.db, 'w', newline='') as csvfile:
                fieldnames = ['product_name', 'product_code']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for row in temp:
                    writer.writerow({'product_name': row[0], 'product_code': row[1]})
        
        except FileNotFoundError as error:
           print("Banco de Dados não encontrado. Um novo será criado.")
           print(error)
           self.dbCreate()
                