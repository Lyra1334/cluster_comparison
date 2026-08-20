import os
import argparse

from absl import app
from absl.flags import argparse_flags

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--organized_files_csv",
        type=str,
        help="Folder where the csvs with organized documents are.",
        default="/home/mari/pibic/csvs"
    )
    parser.add_argument(
        "--data_folder",
        type=str,
        help="Folder to look for the original folders in.",
        default="/home/mari/pibic/dados/images"
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):
    organizados = set()
    pastas = {pasta: [x
                  for x in os.listdir(os.path.join(args.data_folder,pasta))
                  if os.path.isfile(os.path.join(args.data_folder,pasta,x))]
          for pasta in os.listdir(args.data_folder)
          if not os.path.isfile(os.path.join(args.data_folder,pasta))}
    for csv in os.listdir(args.organized_files_csv):
        path = os.path.join(args.organized_files_csv,csv)
        with open(path,"r") as documento:
            linha = documento.readline().strip()
            while linha != "":
                lista = linha.split(",")
                organizados.add(lista[1].strip())
                linha = documento.readline().strip()
    contagens = list()
    total_docs = 0
    total_organizado = 0
    for pasta in pastas.keys():
        cont = 0
        org = 0
        for doc in pastas[pasta]:
            cont +=1
            total_docs += 1
            if doc in organizados:
                org +=1
                total_organizado += 1
        contagens.append((pasta, (org/cont)*100))
    contagens.sort(key=lambda a : a[1], reverse=True)
    for i in contagens:
        print(f"{i[0]}: {i[1]}")
    print(f"total: {(total_organizado/total_docs)*100}")

    
if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)