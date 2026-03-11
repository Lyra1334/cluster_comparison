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
        default="/home/mari/pibic/scripts/embeds"
    )
    parser.add_argument(
        "--output_file",
        type=str,
        help="File to write output.",
        default="/home/mari/pibic/scripts/embeds"
    )
    args = parser.parse_args(argv[1:])
    return args

def main(args):
    input = open(args.csv_file,"r")
    output = open(args.output_file,"w")

    linha = input.readline().strip()
    while linha != "":
        itens = linha.split(",")
        primeiro, segundo = itens[0].split("/"), itens[1].split("/")
        if primeiro[:-1] != segundo[:-1]:
            output.write(linha+"\n")
        linha = input.readline().strip()

             

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)