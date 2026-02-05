import os
import argparse

from absl import app
from absl.flags import argparse_flags

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--root_folder",
        type=str,
        help="Folder to start looking for clusters in.",
        default="/home/mari/arrumado/specification"
    )
    parser.add_argument(
        "--csv_dest",
        type=str,
        help="Folder to output the cluster embeddings.",
        default="/home/mari/pibic/scripts/embeds"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        help="Pretrained model (Resnet).",
        default="/home/mari/pibic/programa/doc-zsl/dataset_creation/resnet_cluster_best.pt"
    )
    parser.add_argument(
        "--calculate_distances_path",
        type=str,
        help="Path to the calculate_distances script.",
        default="/home/mari/pibic/programa/doc-zsl/src/calculate_distances.py"
    )
    args = parser.parse_args(argv[1:])
    return args

def is_cluster(path):
    #Checa se uma pasta é um cluster final ou não
    if os.path.isfile(path):
        return False
    itens = os.listdir(path)
    if itens == [item for item in itens if os.path.isfile(os.path.join(path,item))]:
        return True
    else:
        return False

def recursive_generate(root : str, path : str, executavel : str, modelo : str, destino : str):
    #Recursivamente procura os clusters finais/"de ponta"
    directories = [item for item in os.listdir(path) if not os.path.isfile(os.path.join(path,item))]
    for item in directories:
        if is_cluster(os.path.join(path,item)):
            nome_doc_embed = path.replace(root+"/", "").replace("/","_-") + "_-" + item + ".csv"
            os.system(f'python3 "{executavel}" --model_path "{modelo}" --device "cuda" --dataset_path "{os.path.join(path,item)}" --output_file "{os.path.join(destino,nome_doc_embed)}"')
        elif os.path.isdir(os.path.join(path,item)):
            recursive_generate(root, os.path.join(path,item),executavel,modelo,destino)

def main(args):
    recursive_generate(args.root_folder,
                       args.root_folder,
                       args.calculate_distances_path,
                       args.model_path,
                       args.csv_dest)

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)

