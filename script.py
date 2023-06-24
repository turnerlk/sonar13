import subprocess
import requests
import os
from urllib.parse import urlparse, urlunparse, parse_qs
import signal
import sys
import urllib.parse
import base64
import colorama

colorama.init()
desenho = '''
         ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀..⠀⠀....
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀..
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣦⣀⠙⢿⣦⡀⠙⢿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣷⣄⠙⢿⣦⡀⠙⢿⣿⣿⡿⠋⠀⠀
⠀⠀⠀⠀⣠⣴⣿⣿⣿⠿⢻⣿⣿⣿⣿⣿⣿⣿⣧⡀⠙⠛⠂⠀⠙⠋⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⡿⠁⠀⣠⣿⣿⠋⠙⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣇⠘⣿⣿⣿⣿⣷⣾⣏⣉⣿⣀⣀⢸⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣧⡈⢻⣿⣿⡿⠋⠉⠛⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣷⣄⠙⢿⣿⣷⣦⣤⣽⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣷⣄⠙⠻⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⠿⣿⣿⣿⣿⣦⣄⡉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                   
  #####    #####   ##   ##    ##     ######              ##      ####          
 ##   ##  ##   ##  ###  ##   ####     ##  ##            ###     ##  ##      
 #        ##   ##  #### ##  ##  ##    ##  ##             ##         ##  
  #####   ##   ##  ## ####  ##  ##    #####              ##       ###    
      ##  ##   ##  ##  ###  ######    ## ##              ##         ##        
 ##   ##  ##   ##  ##   ##  ##  ##    ##  ##             ##     ##  ##      
  #####    #####   ##   ##  ##  ##   #### ##           ######    ####    
  ''' 
print(desenho)

def executar_nmap(alvo):
    current_directory = os.getcwd()
    nmap_binary = os.path.join(current_directory, "tools", "nmap")
    comando = f'{nmap_binary} {alvo}'

    try:
        resultado = subprocess.check_output(comando, shell=True)
        print(resultado.decode())
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao executar o Nmap.")
        print(e)


def execute_ffuf(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")
          



def execute_ffuf(command):
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

def testar_lfi(url, caminho_arquivo):
    url_alvo = f"{url}?arquivo={caminho_arquivo}"
    response = requests.get(url_alvo)

    if "Informações sensíveis" in response.text:
        print(f"Vulnerabilidade LFI detectada! Arquivo: {caminho_arquivo}")
    else:
        print(f"Não foi detectada vulnerabilidade LFI para o arquivo: {caminho_arquivo}")

def executar_testes_lfi(url):
    current_directory = os.getcwd()
    wordlist_file = os.path.join(current_directory, "tools", "lfi.txt")

    if not os.path.exists(wordlist_file):
        print("Arquivo de wordlist 'lfi.txt' não encontrado no diretório 'tools'.")
        return

    with open(wordlist_file, "r") as file:
        wordlist = file.read().splitlines()

    for arquivo in wordlist:
        testar_lfi(url, arquivo)



def gerar_payloads_reverse_shell():
    current_directory = os.getcwd()
    payloads_file = os.path.join(current_directory, "tools", "payloads.txt")

    if not os.path.exists(payloads_file):
        print("Arquivo 'payloads.txt' não encontrado no diretório 'tools'.")
        return

    with open(payloads_file, "r") as file:
        payloads = file.read()

    
    print(payloads)



def encode_payloads(payloads):
    encoded_payloads = urllib.parse.urlencode(payloads)
    return encoded_payloads



def encode_base64(texto):
    encoded_texto = base64.b64encode(texto.encode()).decode()
    return encoded_texto



def decode_base64(encoded_texto):
    decoded_texto = base64.b64decode(encoded_texto).decode()
    return decoded_texto




def execute_sqlmapapi():
    sqlmapapi_path = os.path.join(os.getcwd(), "tools", "sqlmap-dev", "sqlmap.py")
    command = f"python {sqlmapapi_path}"

    user_input = input("Digite os comandos para o sqlmap.py: ")
    command += f" {user_input}"

    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")

  

def signal_handler(sig, frame):
    print('Encerrando o programa...☢☢☢ \n Erre programa é radioativo demais, né? ☢☢☢')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)



while True:
    print("Bem-vindo ao Sonar 13, escolha as opções abaixo para executar a ferramenta!")

    print("1- Scan de portas......☢")
    print("2- Executar o FFUF.....☢")
    print("3- Testes de LFI....☢")
    print("4- Gerar payloads para reverse shell....☢")
    print("5- Encodar em URLEncod....☢")
    print("6- Encodar em base64....☢")
    print("7- Decodar base64....☢")
    print("8- Executar SQLMAP....☢")
    options = input("Digite as opções acima! ")

    if options == "1":
        
        print('Executando o Nmap....☢')

        alvo = input("Digite o alvo para a Varredura: ")
        executar_nmap(alvo)
    
    
    elif options == "2":
        print('Executando o FFUF....☢')
        print('Caso tiver duvida só digitar -h para ver o help da ferramenta. >:P' )
        alvo = input('Digite o alvo para a varredura: ')
        command = './tools/ffuf ' + alvo
        execute_ffuf(command)
             

      
    
    elif options == "3":

        print('Realizarndo testes de parâmetros....☢')
        url = input("Digite a URL alvo: ")
        executar_testes_lfi(url)

    elif options == "4":
        print('Gerando payloads para reverse shell....☢ \n \n \n')
        gerar_payloads_reverse_shell()
    
   
    elif options == "5":

        print('Encodar em URLEncod....☢ \n')
        texto = input("Digite o texto para realizar o encode: ")
        payloads = {'texto': texto}
        encoded_payloads = encode_payloads(payloads)
        print(f"Texto codificado: {encoded_payloads}")
    
    elif options == "6":
        print('Realizando codificação em Base64....☢')
        texto = input("Digite o texto para realizar a codificação: ")
        encoded_texto = encode_base64(texto)
        print(f"Texto codificado em Base64: {encoded_texto}")
    elif options == "7":
        print('Realizando decodificação em Base64....☢')
        encoded_texto = input("Digite o texto codificado em Base64: ")
        decoded_texto = decode_base64(encoded_texto)
        print(f"Texto decodificado: {decoded_texto}")
    
    elif options == "8":
        print('Executando o sqlmapapi....☢')
        execute_sqlmapapi()

        
        break




