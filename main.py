import db
import webAutomation

print("Início do Código")
webAuto = webAutomation.webAutomation()
data = db.database()


def loop():
    while True:
        print("loop")

        command = input("O que você quer fazer?")

        if command == "create":
            product_name = input("Nome do Produto:")
            product_code = input("Código do Produto:")
            data.create(product_name, product_code)

        elif command == "seeAll":
            data.findAll()

        elif command == "search":
            product_name = input("Nome do Produto:")
            product_code = data.find_one_by_name(product_name)
            webAuto.search(product_code)

        elif command == "delete":
            product_name = input("Nome do Produto:")
            data.destroy(product_name)
            

        response = input("Quer finalizar? [s/n]")

        if response == "s":
            break

if __name__ == "__main__":
    loop()
