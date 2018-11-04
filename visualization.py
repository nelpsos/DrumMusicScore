from ADTLib import ADT
import os
import numpy as np
import sys

def write_vis(filename, tar_name) :
    name = filename + ".ly"
    upcode_ac = []
    dncode_ac = []
    f = open(tar_name,'r')

    while True:

        line = f.readline()
        if not line: break
        tmp = line.split(" ")
        #print(tmp)
        if tmp[0] == "hh":
            upcode_ac.append('hh ')
        else:
            upcode_ac  .append('r ')
        # print(tmp)
        if tmp[1] == 'sn':
            dncode_ac.append('sn ')
        if tmp[2] == 'bd\n':
            dncode_ac.append('bd ')
        else:
            dncode_ac  .append('r ')
    #print(len(dncode_ac))
    #print(len(upcode_ac))
    versionlp = '\\version "2.18.2"\n'
    upcode_st = "up=\\drummode {\n"
    upcode_ed = "}\n"
    dncode_st = "down=\\drummode {\n"
    dncode_ed = "}\n"
    basic_notation1 = "\\new DrumStaff<<\n"
    basic_notation2 = " \\new DrumVoice {\\voiceTwo \\up}\n"
    basic_notation3 = " \\new DrumVoice {\\voiceTwo \\down}\n>>"
    basic_notation = basic_notation1+ basic_notation2 + basic_notation3
    vis = open(name,'w')
    vis.write(versionlp)
    vis.write(upcode_st)
    for i in range(0,len(upcode_ac),1):
        #print("ppppp")
        vis.write(upcode_ac[i])
    vis.write(upcode_ed)
    vis.write(dncode_st)
    for i in range(0,len(dncode_ac),1):
            #print("ppppp")
        vis.write(dncode_ac[i])
    vis.write(dncode_ed)
    vis.write(basic_notation)
    vis.close()

def read_vis(filename) :
    Onsets = ADT([filename], text="yes", tab="no")
    filename_ = ''.join(filename.split('/')[-1].split('.')[:-1])
    filename_txt = filename_ + ".ADT.txt"

    snare = []
    times = []
    kick = []
    hihat = []

    ti = int(0)

    vis = open(filename_txt, 'r')

    while True:

        line = vis.readline()

        if not line: break

        tmp = line.split()

        if ti == 0:
            times.append(tmp[0])
            before = tmp[0]
            ti += 1
            #print("case1")
        else:
            if tmp[0] == before:
                ti += 1

            else:
                before = tmp[0]
                times.append(tmp[0])
                ti += 1
        #print(tmp)
        if tmp[1] == "SD":
            snare.append(tmp[0])
            #print("SD in")
        elif tmp[1] == "HH":
            hihat.append(tmp[0])
            #print("HH in")
        elif tmp[1] == "KD":
            kick.append(tmp[0])
            #print("KD in")

    vis.close()


    snare = list(np.float_(snare))
    hihat = list(np.float_(hihat))
    kick = list(np.float_(kick))
    times = list(np.float_(times))

    #print(hihat)

    #print(times)
    #print("\n")
    #print(hihat)
    #print("\n")
    #print(kick)
    sn = int(0)
    hh = int(0)
    kk = int(0)
    n = int(0)

    f = open("dataset_"+filename_txt,'w')
    print("len(times) is: ", len(times))
    for i in range(0,len(times)-1,1):
        print(i)
        if snare[sn] == times[i] and kick[kk] == times[i] and hihat[hh] == times[i]:
            f.write("hh sn bd\n") #hh sn bd
            sn = sn + 1 if sn < len(snare) - 1 else sn
            kk = kk + 1 if kk < len(kick ) - 1 else kk
            hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done1")
        elif snare[sn] != times[i] and kick[kk] == times[i] and hihat[hh] == times[i]:
            f.write("hh r bd\n")
            # sn = sn + 1 if sn < len(snare) - 1 else sn
            kk = kk + 1 if kk < len(kick ) - 1 else kk
            hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done2")
        elif snare[sn] == times[i] and kick[kk] != times[i] and hihat[hh] == times[i]:
            f.write("hh sn r\n")
            sn = sn + 1 if sn < len(snare) - 1 else sn
            # kk = kk + 1 if kk < len(kick ) - 1 else kk
            hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done3")
        elif snare[sn] == times[i] and kick[kk] == times[i] and hihat[hh] != times[i]:
            f.write("r sn bd\n")
            sn = sn + 1 if sn < len(snare) - 1 else sn
            kk = kk + 1 if kk < len(kick ) - 1 else kk
            # hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done4")
        elif snare[sn] != times[i] and kick[kk] != times[i] and hihat[hh] == times[i]:
            f.write("hh r r\n")
            # sn = sn + 1 if sn < len(snare) - 1 else sn
            # kk = kk + 1 if kk < len(kick ) - 1 else kk
            hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done5")
        elif snare[sn] != times[i] and kick[kk] == times[i] and hihat[hh] != times[i]:
            f.write("r r bd\n")
            # sn = sn + 1 if sn < len(snare) - 1 else sn
            kk = kk + 1 if kk < len(kick ) - 1 else kk
            # hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done6")
        elif snare[sn] == times[i] and kick[kk] != times[i] and hihat[hh] != times[i]:
            f.write("sn r r\n")
            sn = sn + 1 if sn < len(snare) - 1 else sn
            # kk = kk + 1 if kk < len(kick ) - 1 else kk
            # hh = hh + 1 if hh < len(hihat) - 1 else hh
            print("done7")

    f.close()
    return filename_

def produce_pdf(filename) :
    os.system("lilypond" + filename ".ly")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python visualization.py [<path> [<path> ...]]")
        print("   <path>:\tPath of input audio files to extract drum music score")
    else:
        file_paths = sys.argv[1:]
        for file_path in file_paths:
            # try:
            filename_ = read_vis(file_path)
            write_vis(filename_, "dataset_"+filename_+".ADT.txt")
            produce_pdf(filename_)
            # except Exception as e:
            #     print(e)
