#!/home/steve/anaconda3/bin/python3.7

# functions to read a file from srt into just the text that is said
import os
import numpy as np

def clean_duplicates(speech):
    clean_speech = [speech[0]]
    for i in speech:
        try: 
            if i not in clean_speech[-3:]:
                clean_speech.append(i)
        except:
            if i not in clean_speech:
                clean_speech.append(i)

    clean_speech = [i for i in clean_speech if i!=' \n']

    return clean_speech
            

def to_txt(fname='out.srt'):
    with open(fname,'r') as f:
        lines = f.readlines()

    actual_speech = []
    for l in lines:
        if l=='\n': continue
        try:
            if l[2]==':': 
                continue
        except: pass
        try:
            int(l[0])
            continue
        except: pass
        actual_speech.append(l)
    
    actual_speech = clean_duplicates(actual_speech)

    # write the file
    with open(fname[:-4]+'.txt','w') as f:
        for l in actual_speech:
            f.write(l)

    return actual_speech

def fix_vtt_syntax(fnames):
    for name in fnames:
        os.system('mv *'+name[1:-1]+'* '+name)

def make_srt(fnames):
    for name in fnames:
        name = name
        srt_name = name[:-4]+".srt"
        print("name : ",name,'\nsrt_name : ',srt_name,'\n\n')
        # execute bash command
        os.system("ffmpeg -i '"+name+"' '"+srt_name+"'")

if __name__ == '__main__':
    # first convert .vtt to .srt
    #fnames = [i for i in os.listdir() if '.vtt' in i]
    #fix_vtt_syntax(fnames)

    fnames = [i for i in os.listdir() if '.vtt' in i]
    make_srt(fnames)

    fnames =[i for i in os.listdir() if '.srt' in i]
    for fname in fnames:
        speech = to_txt(fname=fname)
    print(speech)
