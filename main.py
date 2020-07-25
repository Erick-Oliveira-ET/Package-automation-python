import db
import webAutomation

print("Qualquer problemas ou sujestões, entre em contato pelo github: ")
print("https://github.com/Erick-Oliveira-ET/Package-automation-python")
print("\nInicializando processos...")
webAuto = webAutomation.webAutomation()
data = db.database()

def loop():
    while True:

        command = input("O que você quer fazer? (digite 'help' para ver comandos disponíveis) ")

        if "help" in command:
            print("'create': cria um novo produto na lista de encomendas")
            print("'seeAll': mostra toda a lista de encomendas")
            print("'search': procura o pacote pelo nome salvo na lista de encomendas")
            print("'delete': deleta um pacote da lista de encomendas")


        elif "create" in command.lower():
            product_name = input("Nome do Produto: ")
            product_code = input("Código do Produto: ")
            data.create(product_name, product_code)

        elif "seeall" in command.lower():
            data.findAll()

        elif "search" in command.lower():
            product_name = input("Nome do Produto: ")
            product_code = data.find_one_by_name(product_name)
            webAuto.search(product_code)

        elif "delete" in command.lower():
            product_name = input("Nome do Produto: ")
            data.destroy(product_name)
            

        response = input("Quer finalizar? [s/n] ")

        if response.lower() in ["s", "sim", "ss"]:
            break

if __name__ == "__main__":
    loop()
