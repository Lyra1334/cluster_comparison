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

#Filters output True if a line should remain on the csv, and False if they need to be removed.
#All filter functions need to have the same arguments
#To add another filter add it to the list on main.

def HierarchyFilter(list1, list2, distance):
    #Checks if two clusters belong to the same cluster.
    if len(list1) != len(list2):
        return True
    for i in range(len(list1)-1):
        if list1[i] != list2[i]:
            return True
    
    return False

def BlankFilter(list1, list2, distance):
    #Checks if a cluster has "blank" in it's adress
    for word in list1:
        if word.find("blank") != -1:
            return False
    for word in list2:
        if word.find("blank") != -1:
            return False
    return True

def DistanceFilter(list1, list2, distance):
    if distance < 0.5:
        return True
    else:
        return False

def TestFilters(filters, first_cluster, second_cluster, distance):
    #Tests all filters in a given line
    for filter in filters:
        if filter(first_cluster,second_cluster,distance) == False:
            return False
    
    return True


def main(args):
    input = open(args.csv_file,"r")
    output_list = []
    filters = [DistanceFilter, HierarchyFilter, BlankFilter]

    linha = input.readline().strip()
    while linha != "":
        itens = linha.split(",")
        primeiro, segundo = list(map(lambda a: a.strip(), itens[0].split("/"))), list(map(lambda a: a.strip(),itens[1].split("/")))
        if TestFilters(filters,primeiro,segundo, float(itens[2])):
            output_list.append((linha))
        linha = input.readline().strip()
    input.close()
    output = open(args.output_file,"w")
    for line in output_list:
        output.write(line+"\n")
    output.close()


             

if __name__ == "__main__":
    app.run(main,flags_parser=parse_args)