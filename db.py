import csv


class database:
    def __init__(self):
        self.db = "db.csv"
    
    def findAll(self):
        with open(self.db, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row['product_name'], row['product_code'])

    def find_one_by_name(self, name):
        with open(self.db, 'r', newline='') as csvfile :
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['product_name'] == name:
                    return row['product_code']
        
    def create(self, name, code):
        with open(self.db, 'a', newline='') as csvfile:
            fieldnames = ['product_name', 'product_code']
        
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'product_name': name, 'product_code': code})

    def destroy(self, name):
        temp = []
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
                

            

    pass
