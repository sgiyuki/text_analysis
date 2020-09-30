#!/usr/bin/python3

import sys
import csv
########################################################################
def PrintInputError1():
    print("!!! TEXT ANALYSIS INPUT ERROR(INPUT FILE) !!!")
    print("Error: ./text_analysis.py [input1.csv] [input2.txt]... !!!")
    sys.exit()

def PrintInputError2():
    print("!!! TEXT ANALYSIS INPUT ERROR(INPUT CSV or TXT FILE) !!!")
    print("Error: ./text_analysis.py [input1.csv] [input2.txt]... !!!")
    sys.exit()

def csv2list(csv_reader):
    lis = []
    tmp = []
    for row in csv_reader:
        for i in range(len(row)):
            tmp.append(row[i])
        #
        lis.append(tmp)
        tmp = []
    return lis

##############################################
# sample1.csv
# src_lis = [['aaa', 'bbb'], ['ccc', 'ddd']]
# dst_lis = [['AAA', 'BBB'], ['CCC', 'DDD']]
##############################################
def Analysis(src_lis):
    dst_lis = src_lis # initialize with src_lis size
    for i in range(len(src_lis)):
        for j in range(len(src_lis[i])):    
            dst_lis[i][j] = src_lis[i][j].upper()
    return dst_lis

def pre_csv_analysis(path):
    index = path.rfind(".")
    dst_path = path[:index] + "_dst." + "csv"

    with open(path) as f:
        reader = csv.reader(f)
        src_lis = csv2list(reader)
    ### close

    print(path)
    print(src_lis)

    dst_lis = Analysis(src_lis)

    print(dst_path)
    print(dst_lis, "\n")

    with open(dst_path, "w") as f:
        writer = csv.writer(f)
        for i in range(len(dst_lis)):
            writer.writerow(dst_lis[i])
    ### close

def pre_txt_analysis(path):
    index = path.rfind(".")
    dst_path = path[:index] + "_dst." + "txt"

    with open(path) as f:
        src_lis = f.readlines()
        src_lis = [src_lis]
    ### close
    
    print(path)
    print(src_lis)
    
    dst_lis = Analysis(src_lis)

    print(dst_path)
    print(dst_lis, "\n")

    with open(dst_path, "w") as f:
        f.writelines(dst_lis[0])
    ### close
        
            
########################################################################
if __name__ == '__main__':

    argv = sys.argv

    if (len(argv) == 1):
        PrintInputError1()
    ### else

    for i in range(1, len(argv)):
        input_file = argv[i]
        extension = input_file.split(".")[-1]
        if (extension == "csv"):
            pre_csv_analysis(input_file)
        elif (extension == "txt"):
            pre_txt_analysis(input_file)
        else: ### (extension != "csv" and extension != "txt")
            PrintInputError2()

    print("!!! Finish text_analysis !!!")
