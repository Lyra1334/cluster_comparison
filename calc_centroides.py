import os
from math import sqrt
import argparse

from absl import app
from absl.flags import argparse_flags

def centroideCsv(caminho : str):
    somatorio = [0 for _ in range(64)]
    cont_linhas = 0
    with open(caminho,"r") as arquivo:
        linha = arquivo.readline().strip()
        linha = arquivo.readline().strip()
        while linha != "":
            cont_linhas += 1
            linha = linha.split(",")[1:]
            linha[0] = linha[0][linha[0].find("[")+1:]
            linha[63] = linha[63][:linha[63].find("]")]
            linha = [float(num.strip()) for num in linha]
            somatorio = [somatorio[x]+linha[x] for x in range(64)]
            linha = arquivo.readline().strip()
    
    if cont_linhas > 0:
        return [(num/cont_linhas) for num in somatorio]
    else:
        print(f"Vazio em {caminho}")
        return False

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--embeds_folder",
        type=str,
        help="Folder to get the embedding csvs from.",
        default="/home/mari/pibic/scripts/embeds"
    )
    parser.add_argument(
        "--comparison_dest",
        type=str,
        help="Folder to output the cluster comparisons.",
        default="/home/mari/pibic/comp_centroides"
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):

    path_uso = args.embeds_folder
    path_output = args.comparison_dest
    docs = [cluster for cluster in os.listdir(path_uso) if cluster[-4:] == ".csv"]
    cont = 0
    centroides = list()
    comparacoes = list()


    for csv in docs:
        print(f"Processando csv {cont} de {len(docs)}")
        cont +=1

        caminho_csv = os.path.join(path_uso,csv)
        nome_csv = csv[:-4]
        centro = centroideCsv(caminho_csv)
        if centro != False:
            centroides.append((nome_csv,centro))

    for i in range(len(centroides)):
        print(f"Comparações {i} de {len(centroides)}")
        for j in range(len(centroides)):
            if i < j:

                dist = sqrt(sum([(centroides[i][1][x]-centroides[j][1][x])**2 for x in range(64)]))

                if len(comparacoes) > 0:
                    inseriu = False
                    pos = 0
                    while not inseriu and pos < len(comparacoes):
                        if dist < comparacoes[pos][2]:
                            comparacoes.insert(pos,[centroides[i][0],centroides[j][0],dist])
                            inseriu = True
                        else:
                            pos += 1

                    if not inseriu and pos == len(comparacoes):
                        comparacoes.append([centroides[i][0],centroides[j][0],dist])
                else:
                    comparacoes.append([centroides[i][0],centroides[j][0],dist])

    print(f"Escrevendo {len(comparacoes)} linhas")

    with open(os.path.join(path_output,"output.csv"),"w") as saida:
        for linha in comparacoes:
            saida.write(f"{linha[0]} e {linha[1]}, distância {linha[2]}\n")

    print("Acabou")

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)