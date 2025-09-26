import os

def salvar_em_arquivo(caminho, conteudo):
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'a', encoding='utf-8') as f:
        f.write(conteudo + "\n")