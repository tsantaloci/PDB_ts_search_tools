import numpy as np
import pandas as pd
import os
from pdb_file_checker import atom
from pdb_file_checker import atom_creator


    
def answer_1(atm_list):
    result = []
    for i in atm_list:
        for x in atm_list:
            if i.atom_serial_number == 'O':
                if bond_length(i,x) > 1.1:
                    #print(bond_length(i, x))
                    result.append('N')
    if result == []:
        return 'Y'
    else:
        return 'N'

def bond_length(atm1,atm2):
    r = (atm1.xcoord-atm2.xcoord)**2+(atm1.ycoord-atm2.ycoord)**2+ (atm1.zcoord-atm2.zcoord)**2
    return r ** 0.5
def atm_dict_creator(atm_list):
    atm_dict = {}
    for i in atm_list:
        atm_dict[i.atom_serial_number,i.residue,i.residue_number,i.chain_id]=i
    return atm_dict 



def answer_2(atm_dict):
    a = bond_length(atm_dict['OE1','GLU','143','A'],atm_dict['H1','WT1','212','A'])
    b = bond_length(atm_dict['OE1','GLU','143','A'],atm_dict['H2','WT1','212','A'])
    c = bond_length(atm_dict['OE2','GLU','143','A'],atm_dict['H2','WT1','212','A'])
    d = bond_length(atm_dict['OE2','GLU','143','A'],atm_dict['H1','WT1','212','A'])
    '''
    print(a)
    print(b)
    print(c)
    print(d)
    '''
    if a < 1.2 or b < 1.2 or c < 1.2 or d < 1.2:
        return 'Y'
    else:
        return 'N'

def answer_3(atm_dict):
    print(atm_dict.keys())
    a = bond_length(atm_dict['N','LEU','207','A'],atm_dict['H1','WT1','212','A'])
    b = bond_length(atm_dict['N','LEU','207','A'],atm_dict['H2','WT1','212','A'])
    #print(a)
    #print(b)
    if a < 1.2 or b < 1.2:
        return 'Y'
    else:
        return 'N'

def answer_4(atm_dict):
    #print(atm_dict.keys())
    a = bond_length(atm_dict['N','LEU','207','A'],atm_dict['C','CS1','206','A'])
    #print(a)
    if a < 1.69:
        return 'Y'
    else:
        return 'N'





def main():
    file_1 = '../files/ts-02-irc1-out.pdb'
    file_2 = '../files/ts-02-irc2-out.pdb'
    file_3 = '../files/ts-10-irc1-out.pdb'
    file_4 = '../files/ts-10-irc2-out.pdb'
    file_5 = '../files/ts-09-irc2-out.pdb'
    file_6 = '../files/ts-11-irc1-out.pdb'
    file_7 = '../files/ts-11-irc2-out.pdb'
    file_8 = '../files/ts-12-irc1-out.pdb'
    file_9 = '../files/ts-12-irc2-out.pdb'
    q1 = 'If WT1 212 has two hydrogens?'
    q2 = 'Does GLU 143 have a hydrogen from WT1212?'
    q3 = 'Does LEU 207 N have a hydrogen from WT1212?'
    q4 = 'Is LEU 207 N bonded too CS1 206 C?'


    df = {
        'path':[],
        q1:[],
        q2:[],
        q3:[],
        q4:[],
        'step':[]
    }
    file = [file_1,file_2,file_3,file_4,file_5,file_6,file_7,file_8,file_9]
    for pdb in file:



    #question_1 = "Does WT1:A:212 atom_name: H2 have a hydrogen that is greater than 1.2 angstroms?"
   # atom_name_1 = 
   
        wt1_A_212 = []
        glu_A_143 = []
        casn_A_206 = []
        leu_A_207 = []
        atoms = atom_creator(pdb)
        for atm in atoms:
            if atm.chain_id +':'+atm.residue_number == 'A:212': 
                wt1_A_212.append(atm)
            elif atm.chain_id +':'+atm.residue_number == 'A:143': 
                glu_A_143.append(atm)
            elif atm.chain_id +':'+atm.residue_number == 'A:206': 
                casn_A_206.append(atm)
            elif atm.chain_id +':'+atm.residue_number == 'A:207': 
                leu_A_207.append(atm)



        q_1 = answer_1(wt1_A_212)
        #glu_A_143.append(wt1_A_212)
        tot = glu_A_143 + wt1_A_212
        atm_dict = atm_dict_creator(tot)
        q_2 = answer_2(atm_dict)
        #print(q_2)

        '''
        tot_wt1_casn = casn_A_206+wt1_A_212
        atm_dict = atm_dict_creator(tot_wt1_casn)
        q_3 = answer_3(atm_dict)
        print(q_3)
        '''

        tot_wt1_leu = leu_A_207+wt1_A_212 
        atm_dict = atm_dict_creator(tot_wt1_leu)
        q_3 = answer_3(atm_dict)

        tot_cs1_leu = leu_A_207+casn_A_206
        atm_dict = atm_dict_creator(tot_cs1_leu)
        q_4 = answer_4(atm_dict)
        df['path'].append(pdb)
        df[q1].append(q_1)
        df[q2].append(q_2)
        df[q3].append(q_3)
        df[q4].append(q_4)
        print(q1,q2,q3,q4)
        if q_1 == 'Y' and q_2 == 'N' and q_3 == 'N' and q_4 == 'Y':
            df['step'].append('I')
        elif ('N','Y','N','Y')==(q_1,q_2,q_3,q_4):
            df['step'].append('II')
        elif ('N','N','Y','Y')==(q_1,q_2,q_3,q_4):
            df['step'].append('III')
        elif ('N','Y','Y','N')==(q_1,q_2,q_3,q_4):
            df['step'].append('IV')
        else:
            df['step'].append('Check it out')


        df['step']
        #print(q_4)
        print(q_1,q_2,q_3,q_4)
    df = pd.DataFrame(df)
    df = df.sort_values(by='step')
    print(df)
    




    


    return
main()