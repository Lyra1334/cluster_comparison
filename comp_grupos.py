import os
from math import sqrt
import argparse

from absl import app
from absl.flags import argparse_flags

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="File to write comparisons in.",
        default="/home/mari/pibic/scripts/embeds"
    )
    parser.add_argument(
        "--centroid1_csv",
        type=str,
        help="File to read group 1 cluster centroids from.",
        default="/home/mari/pibic/comp_centroides"
    )
    parser.add_argument(
        "--centroid2_csv",
        type=str,
        help="File to read group 2 cluster centroids from.",
        default="/home/mari/pibic/comp_centroides"
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):
    centroides1 = list()
    centroides2 = list()
    comparacoes = list()

    with open(args.centroid1_csv, "r") as input:
        texto = input.readline().strip()
        while texto != "": 
            linha = texto.split(",")
            centroides1.append((linha[0],list(map(int,linha[1:]))))
            texto = input.readline().strip()
    
    with open(args.centroid2_csv, "r") as input:
        texto = input.readline().strip()
        while texto != "": 
            linha = texto.split(",")
            centroides2.append((linha[0],list(map(int,linha[1:]))))
            texto = input.readline().strip()
    
    for i in range(len(centroides1)):
        print(f"Comparações {i} de {len(centroides1)}")
        for j in range(len(centroides2)):
            if i < j:

                dist = sqrt(sum([(centroides1[i][1][x]-centroides2[j][1][x])**2 for x in range(64)]))
                comparacoes.append([centroides1[i][0],centroides2[j][0],dist])
    
    print("Organizando")

    comparacoes.sort(key= lambda a : a[2])

    with open(args.output_file, "w") as output:
        for linha in comparacoes:
            output.write(f"{linha[0],linha[1],linha[2]}")

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)