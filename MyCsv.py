'''
Created on 2013/05/07

@author: dmn1003
'''
import csv
def readMyCsv():
    print "Please input file name"
    filename=raw_input()
    csvfile = open(filename)
    data=[]
    for row in csv.reader(csvfile):
        #print row # 
        tmpData=[]
        for elem in row:
            
            tmpData.append(elem)
            data.append(tmpData)
    csvfile.close()
    return data

def writeMyCsv(outData):
    print "Please input output file name"
    filename=raw_input()
    writer = csv.writer(file(filename, 'w'))
    writer.writerows(outData)
