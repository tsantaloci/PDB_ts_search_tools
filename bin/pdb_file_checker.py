import numpy as np
import pandas as pd
import os
import itertools

class atom(object):
    def __init__(self,index,atom_serial_number,residue,residue_number,chain_id,xcoord,ycoord,zcoord):
        self.index = index
        self.atom_serial_number = atom_serial_number
        self.residue = residue
        self.residue_number = residue_number
        self.chain_id = chain_id
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.zcoord = zcoord
def atom_creator(file_1):
    """
    makes atoms objects for a pdb files
    """
    value_1 = []
    with open(file_1,'r') as fp:
        data = fp.readlines()
        for line in data:
            index_number = line[5:11].strip()
            atom_serial_number = line[12:17].strip()
            residue = line[17:21].strip()
            residue_number = line[22:27].strip()
            chain_id = line[21]
            xcoord = line[30:39].strip()
            ycoord = line[38:47].strip()
            zcoord = line[46:55].strip()
            value_1.append(atom(index_number,atom_serial_number,residue,residue_number,chain_id,xcoord,ycoord,zcoord))
    return value_1
def difference_finder(list1,list2):
    '''
    finds the percent change for x,y,z coords of two pdb files
    '''
    differ_x = []
    differ_y = []
    differ_z = []
    if len(list1) == len(list2):
        for num,atm_1 in enumerate(list1):
            if atm_1.residue_number == list2[num].residue_number and atm_1.atom_serial_number == list2[num].atom_serial_number:
                differ = float(atm_1.xcoord) - float(list2[num].xcoord)
                percent_differ = (differ/float(atm_1.xcoord))*100
                differ_x.append(percent_differ) 

                differ_2 = float(atm_1.ycoord) - float(list2[num].ycoord)
                percent_differ_2 = (differ_2/float(atm_1.ycoord))*100
                differ_y.append(percent_differ_2)


                differ_3 = float(atm_1.zcoord) - float(list2[num].zcoord)
                percent_differ_3 = (differ_3/float(atm_1.ycoord))*100
                differ_z.append(percent_differ_3)
    else:
        print('The pdb files are different lengths please check to see if they are the same protein')
    return differ_x,differ_y,differ_z


def average_finder(list1):
    '''
    calculates the average of a list
    '''
    return sum(list1)/len(list1)


def main():
    file_1 = '../files/ts-10-irc2-out.pdb'
   # file_2 = '../files/ts-12-irc2-out.pdb'
   # file_2 = '../files/ts-11-irc2-out.pdb'
    file_2 = '../files/ts-02-irc2-out.pdb'
   # file_1 = 'ts-12-irc2-out.pdb'
    repeats = []
    value_1 = atom_creator(file_1)
    value_2 = atom_creator(file_2)
    xchg,ychg,zchg = difference_finder(value_1,value_2)
    xavgchg = average_finder(xchg)
    yavgchg = average_finder(ychg)
    zavgchg = average_finder(zchg)
    
    
    print('average percent change for the x coordinate: '+ str(xavgchg))
    print('average percent change for the y coordinate: '+ str(yavgchg))
    print('average percent change for the z coordinate: '+ str(zavgchg))
    tot =  abs(xavgchg)+abs(yavgchg)+abs(zavgchg)
    print(tot)

    if abs(xavgchg)+abs(yavgchg)+abs(zavgchg)>=.01:
        print(file_1 +' ' + file_2 + ' are not the same')
    else:
        print(file_1 +' ' + file_2 + ' Same')
        repeats.append(file_2)
    '''
    Uncomment to compare a list of files to one file
    file_list = []
    os.chdir('../files')
    file_1 = []
    for i in os.listdir():
        file_list.append(i)
    for file_2 in file_list:
        if file_1 == file_2:
            pass
        else:

            value_1 = atom_creator(file_1)
            value_2 = atom_creator(file_2)
            xchg,ychg,zchg = difference_finder(value_1,value_2)
            xavgchg = average_finder(xchg)
            yavgchg = average_finder(ychg)
            zavgchg = average_finder(zchg)
    
    
            print('average percent change for the x coordinate: '+ str(xavgchg))
            print('average percent change for the y coordinate: '+ str(yavgchg))
            print('average percent change for the z coordinate: '+ str(zavgchg))
            tot =  abs(xavgchg)+abs(yavgchg)+abs(zavgchg)
            print(tot)

            if abs(xavgchg)+abs(yavgchg)+abs(zavgchg)>=.01:
                print(file_1 +' ' + file_2 + ' are not the same')
            else:
                print(file_1 +' ' + file_2 + ' Same')
                repeats.append(file_2)
    print('These files are repeats of '+ str(file_1)+': ')
    print(repeats)
    '''

    
     
    return
main()