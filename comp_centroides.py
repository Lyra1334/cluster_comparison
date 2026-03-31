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
        "--centroid_csv",
        type=str,
        help="File to read cluster centroids from.",
        default="/home/mari/pibic/comp_centroides"
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):
    centroides = list()
    comparacoes = list()

    with open(args.centroid_csv, "r") as input:
        texto = input.readline().strip()
        while texto != "": 
            linha = texto.split(",")
            centroides.append((linha[0],list(map(int,linha[1:]))))
            texto = input.readline().strip()
    
    for i in range(len(centroides)):
        print(f"Comparações {i} de {len(centroides)}")
        for j in range(len(centroides)):
            if i < j:

                dist = sqrt(sum([(centroides[i][1][x]-centroides[j][1][x])**2 for x in range(64)]))
                comparacoes.append([centroides[i][0],centroides[j][0],dist])
    
    print("Organizando")

    comparacoes.sort(key= lambda a : a[2])

    with open(args.output_file, "w") as output:
        for linha in comparacoes:
            output.write(f"{linha[0],linha[1],linha[2]}")

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)