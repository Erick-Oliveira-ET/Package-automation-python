import csv


class database:
    def __init__(self):
        self.db = "db.csv"
    
    def findAll(self):
        try:
        with open(self.db, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Nome do Produto       |        Código do produto")
            for row in reader:
                print(row['product_name'], "                  ", row['product_code'])
            
        except FileNotFoundError as error:
           print("Arquivo não encontrado. Reporte esse erro pro desenvolvedor.")
           print(error)
        

    def find_one_by_name(self, name):
        try:
        with open(self.db, 'r', newline='') as csvfile :
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product_name'].lower() in name.lower():
                    return row['product_code']
        except FileNotFoundError as error:
           print("Arquivo não encontrado. Reporte esse erro pro desenvolvedor.")
           print(error)
        
    def create(self, name, code):
        try:
        with open(self.db, 'a', newline='') as csvfile:
            fieldnames = ['product_name', 'product_code']
        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'product_name': name, 'product_code': code})
        
        except FileNotFoundError as error:
           print("Arquivo não encontrado. Reporte esse erro pro desenvolvedor.")
           print(error)
        
    def destroy(self, name):
        temp = []
        try:
        with open(self.db, 'r', newline='') as csvfile:
            fieldnames = ['product_name', 'product_code']

            with open(self.db, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row['product_name'] is not name:
                        temp.append([row['product_name'], row['product_code']])
                        

        with open(self.db, 'w', newline='') as csvfile:
            fieldnames = ['product_name', 'product_code']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in temp:
                writer.writerow({'product_name': row[0], 'product_code': row[1]})
        except FileNotFoundError as error:
           print("Arquivo não encontrado. Reporte esse erro pro desenvolvedor.")
           print(error)
                

            

    pass
