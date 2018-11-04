from ADTLib import ADT
import os

def write_vis(filename, upcode_str, dncode_str) :
    name = filename + ".ly"
    versionlp = '\\version "2.18.2"\n'
    upcode_st = "up=\\drummode {\n"
    upcode_ed = "}\n"
    dncode_st = "down=\\drummode {\n"
    dncode_ed = "}\n"
    basic_notation1 = "\\new DrumStaff<<\n"
    #basic_notation2 = "new DrumVoice {\\voiceOne \up}"
    basic_notation2 = " \\new DrumVoice {\\voiceTwo \\up}\n"
    basic_notation3 = " \\new DrumVoice {\\voiceTwo \\down}\n>>"
    basic_notation = basic_notation1+ basic_notation2 + basic_notation3
    vis = open(name,'w')
    vis.write(versionlp)
    vis.write(upcode_st)
    vis.write(upcode_ed)
    vis.write(dncode_st)
    vis.write(dncode_ed)
    vis.write(basic_notation)
    vis.close()

def read_vis(filename) :
    Onsets = ADT([filename], text="yes", tab="no")
    filename_txt = ''.join(filename.split('/')[-1].split('.')[:-1]) + '.txt'
    vis = open(filename_txt, 'r')

    return vis

def produce_pdf(filename) :
    os.system("lilypond result.ly")

write_vis("result1")
