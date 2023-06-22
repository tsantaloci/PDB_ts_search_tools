import csv

class Data( object ):
    def __init__( self ):
        with open('payload.csv', newline='') as csvfile:
            readcsv = csv.reader(csvfile, delimiter = ',', quotechar='|')

            self.rows = [row for row in readcsv]

        self.DATA = []

    def makeDict( self ):
        columns, datacols = self.rows[0], self.rows[1:len(self.rows)]
        columns.append('null')
        columns = [i for i in columns if i]

        for datacol in datacols:
            dataDict = {}

            for col, d in zip(columns, datacol):
                dataDict[col] = d

            self.DATA.append(dataDict)

    def __call__( self ):
        self.makeDict()

        return self.DATA

class Decider:
    def __init__( self, DATA ):
        self.DATA = DATA

    def Charged( self ):
        chargedList = [i for i in self.DATA if i['residue_type'] == 'positive' or i['residue_type'] == 'negative']
        noChargedList = [i for i in self.DATA if i not in chargedList]

        YES_CHARGE = [i for i in chargedList if float(i['ABS_Total']) > 5]
        NO_CHARGE = [i for i in chargedList if i not in YES_CHARGE]

        YES_NOCHARGE = [i for i in noChargedList if float(i['ABS_Total']) > 5]
        NO_NOCHARGE = [i for i in noChargedList if i not in YES_NOCHARGE]

        return len(YES_CHARGE), len(NO_CHARGE), len(YES_NOCHARGE), len(NO_NOCHARGE)

    def Polarity( self ):
        polarList = [i for i in self.DATA if i['residue_type'] == 'polar']
        nonpolarList = [i for i in self.DATA if i['residue_type'] == 'hydrophobic']

        YES_POLAR = [i for i in polarList if float(i['ABS_Total']) > 5]
        NO_POLAR = [i for i in polarList if i not in YES_POLAR]

        YES_NONPOLAR = [i for i in nonpolarList if float(i['ABS_Total']) > 5]
        NO_NONPOLAR = [i for i in nonpolarList if i not in YES_NONPOLAR]

        return len(YES_POLAR), len(NO_POLAR), len(YES_NONPOLAR), len(NO_NONPOLAR)

    def ChainType( self ):
        MC = [i for i in self.DATA if i['typeofchain'] == 'MC' or i['typeofchain'] == 'WAT']
        SC = [i for i in self.DATA if i['typeofchain'] == 'SC']

        YES_MC = [i for i in MC if float(i['ABS_Total']) > 5]
        NO_MC = [i for i in MC if i not in YES_MC]

        YES_SC = [i for i in SC if float(i['ABS_Total']) > 5]
        NO_SC = [i for i in SC if i not in YES_SC]

        return len(YES_MC), len(NO_MC), len(YES_SC), len(NO_SC)

    def Distance( self ):
        THRESH = 7

        moreThanThresh = [i for i in self.DATA if float(i['distance']) > THRESH]
        lessThanTresh = [i for i in self.DATA if i not in moreThanThresh]

        YES_MORE = [i for i in moreThanThresh if float(i['ABS_Total']) > 5]
        NO_MORE = [i for i in moreThanThresh if i not in YES_MORE]

        YES_LESS = [i for i in lessThanTresh if float(i['ABS_Total']) <= 5]
        NO_LESS = [i for i in lessThanTresh if i not in YES_LESS]

        return len(YES_MORE), len(NO_MORE), len(YES_LESS), len(NO_LESS)

def GINI( Yes, No ):
    net = Yes + No

    return (1-(Yes/net))**2 - (1-(No/net))**2

def total_impurity(**kwargs):
    leftLeafs = kwargs['LeftLeafs']
    rightLeafs = kwargs['RightLeafs']

    avgLeft = sum(leftLeafs)/len(leftLeafs)
    avgRight = sum(rightLeafs)/len(rightLeafs)

def main():
    data = Data()()
    decider = Decider(data)
    YES_CHARGE_COUNT, NO_CHARGE_COUNT, YES_NOCHARGE_COUNT, NO_NOCHARGE_COUNT = decider.Charged()
    YES_MC_COUNT, NO_MC_COUNT, YES_SC_COUNT, NO_SC_COUNT = decider.ChainType()
    YES_MORE_COUNT, NO_MORE_COUNT, YES_LESS_COUNT, NO_LESS_COUNT = decider.Distance()
    YES_POLAR_COUNT, NO_POLAR_COUNT, YES_NONPOLAR_COUNT, NO_NONPOLAR_COUNT = decider.Polarity()

    POLAR_GINI = GINI(YES_POLAR_COUNT, NO_POLAR_COUNT)
    NONPOLAR_GINI = GINI(YES_NONPOLAR_COUNT, NO_NONPOLAR_COUNT)

    print(POLAR_GINI, NONPOLAR_GINI)

    CHARGE_GINI = GINI(YES_CHARGE_COUNT, NO_CHARGE_COUNT)
    NOCHARGE_GINI = GINI(YES_NOCHARGE_COUNT, NO_NOCHARGE_COUNT)

    MC_GINI = GINI(YES_MC_COUNT, NO_MC_COUNT)
    SC_GINI = GINI(YES_SC_COUNT, NO_SC_COUNT)

    MORE_GINI = GINI(YES_MORE_COUNT, NO_MORE_COUNT)
    LESS_GINI = GINI(YES_LESS_COUNT, NO_LESS_COUNT)

if __name__ == '__main__':
    main()