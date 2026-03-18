import argparse

from absl import app
from absl.flags import argparse_flags

def parse_args(argv):
    parser = argparse_flags.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--csv_file",
        type=str,
        help="Input file to be edited.",
        default="/home/mari/pibic/comp_centroides/output.csv"
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="File to write output.",
        default="/home/mari/pibic/comp_centroides/filtrado.csv"
    )
    args = parser.parse_args(argv[1:])
    return args

def AreListsEqual(list1, list2):
    #Outputs True if lists are equal, False otherwise.
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

def main(args):
    input = open(args.csv_file,"r")
    output = open(args.output_file,"w")

    linha = input.readline().strip()
    while linha != "":
        itens = linha.split(",")
        primeiro, segundo = list(map(lambda a: a.strip(), itens[0].split("/"))), list(map(lambda a: a.strip(),itens[1].split("/")))
        if not AreListsEqual(primeiro[:-1],segundo[:-1]):
            output.write(linha+"\n")
        linha = input.readline().strip()

             

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)