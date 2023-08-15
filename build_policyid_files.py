'''
Extract data from change file and build new files for each policy id
format of file will be FTDname_CHGxxx.txt
'''

import tkinter.filedialog as fd

fs = fd.askopenfilename(title="Select a change order to load")

p = fs.split('/')
p = p[-1]
chg = p.rstrip('.txt')
print(chg)

with open(f'{fs}','r') as chgfile:
    saveto = fd.askdirectory(title='Save files to directory')
    print(f'Building rules for {chgfile}')
    for i in chgfile:
        if (i.startswith('FTD') or i.startswith('FTC')):
            fwfind = i.split(']')
            try:
                if 'access-list' in fwfind[1] and 'object' not in fwfind[1]:
                    fwname = fwfind[0]
                    fwrule = fwfind[1]
                    fwrule = fwrule.lstrip()
                    fwrule = fwrule.strip('\n')
                elif 'access-list' in fwfind[1] and 'object' in fwfind[1]:  #commenting out to ignore object rule creation
                    print(f"Rules containing objects must be loaded manually: {i}")
                
                #save to file
                with open(f'{saveto}\\{fwname}_{chg}.txt','a+') as ftd:
                    ftd.write(fwname + '] ' + fwrule + '\n')
            
            except NameError:
                pass
    
    #pause screen
    input("Complete. Press Enter to exit")

                #build log file
                #with open('ftdlogfile.txt','a+') as log:
                #    log.write(f'{chgfile} :: {fwname}] {fwrule}\n')

#input('Building rules for FWs complete, press ENTER to quit')
