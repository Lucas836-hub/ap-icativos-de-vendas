import os
from PIL import Image


def eh_imagem(nome_arquivo):
    if nome_arquivo.endswith('png') or nome_arquivo.endswith('jpg') or nome_arquivo.endswith('jpeg'):
        return True
    return False

def reduzir_tamanho_imagens(input_dir, output_dir,id,ext='.jpeg'):
    #print("foncao recortar iniciada")
    #print("Diretorio : ",os.listdir(input_dir))
    #print(lista_de_arquivos)
    
    imagem = Image.open(os.path.join(input_dir)).convert('RGB')
    #redimensionada = imagem.resize((tam[0],tam[1]))
    #print("imagem redimensionada")
   # nome_sem_ext = os.path.splitext(nome)[0]
    imagem.save(os.path.join(output_dir, id + ext))

#if __name__ == "__main__":
#    diretorio = '/storage/emulated/0/pydroid/app vendas/imagens/fundo.jpeg'
#    
#    tam=[300,299]

#    reduzir_tamanho_imagens(diretorio, '/storage/emulated/0/pydroid/app vendas/imagens/recortadas/','$3 foi',tam)