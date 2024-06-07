#!/usr/bin/env python3
import requests
import sys

def download_file(url, output_name):
    try:
        response = requests.get(url, allow_redirects=True)
        response.raise_for_status()  # Verifica se ocorreu alguma exceção
        with open(output_name, 'wb') as file:
            file.write(response.content)
        print(f"Download do arquivo {output_name} concluído com sucesso!")
    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        _, url, output_name = sys.argv
        download_file(url, output_name)
    else:
        print("Uso: ./download_file.py <URL> <Nome do Arquivo de Saída>")
