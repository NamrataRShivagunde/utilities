import argparse
import pandas as pd
from matplotlib import pyplot as plt
from pandas.io import parsers
import numpy as np


#Get the filename and column names as argument
parser = argparse.ArgumentParser()
parser.add_argument("filename",help = "csv file name")
parser.add_argument("columnname", help = "column name of the given excel file name of which th epie chart has to be made")

#reads the argument and return the csv file
def parse_argument():
    args = parser.parse_args()
    filename = args.filename
    colname = args.columnname
    
    read_csv_file = pd.read_csv(filename)
    return read_csv_file , colname

#input is the csv file and output is the pie chart for the column sent as an argument
def create_piechart(dataframe, colname):
    item_count = dataframe[colname].value_counts()
    index = item_count.index.tolist()
    count = item_count.values.tolist()

    #without legend
    #plt.style.use('fivethirtyeight')
    fig1, ax1 = plt.subplots(figsize = (15,10))
    #explode =(0,0,0,0,0,0,0.5,0.5,0.5,0.5)
    #colors = ['#4c72b0', '#dd8452', '#55a868', '#c44e52', '#8172b3', '#937860', '#da8bc3', '#8c8c8c', '#ccb974', '#64b5cd']
    #muted
    colors = ['#4878d0', '#ee854a', '#6acc64', '#d65f5f', '#956cb4', '#8c613c', '#dc7ec0', '#797979', '#d5bb67', '#82c6e2']
    #wedges, text, _ = ax1.pie(count, explode = explode, autopct='%1.1f%%', pctdistance=0.5, labeldistance=0.6, textprops={'fontsize': 12},labels=index, startangle=360 , radius=1)
    wedges, text, _ = ax1.pie(count, autopct='%1.1f%%',colors=colors, pctdistance=0.9, labeldistance=0.6, textprops={'fontsize': 12} , radius=0.9, startangle=5)

    kw = dict(arrowprops=dict(arrowstyle="-" , color='grey' ), va="center")
    dely=0
    delx=0.2
    for p, label in zip(wedges, index):
        print(p)
        ang = np.deg2rad((p.theta1 + p.theta2)/2)
        print(p.theta2-p.theta1)
        if p.theta2-p.theta1 <5:
            y1 = np.sin(ang)
            x1 = np.cos(ang)
            y2 = np.sin(ang)+ dely
            x2 = np.cos(ang) + delx
            delx -= 0.2
            dely += 0.1    
        else:
            y1 = np.sin(ang)
            x1 = np.cos(ang)
            y2 = y1
            x2 = x1
        horizontalalignment = "center" if abs(x1) < abs(y1) else "right" if x1 < 0 else "left"
        ax1.annotate(label, xy=(0.9*x1,0.9*y1), xytext=(1.31*x2, 1.2*y2), fontsize = 23 ,horizontalalignment=horizontalalignment, **kw)

    #https://seaborn.pydata.org/tutorial/color_palettes.html
    import seaborn as sns
    pal = sns.color_palette('muted')
    print(pal.as_hex())

    #ax1.axis('equal')  
    #plt.tight_layout()
    plt.savefig('crossword_train_piechart')
    plt.savefig('crossword_train_piechart.pdf')
    plt.show()
    
    
    #with legend
    '''plt.style.use('fivethirtyeight')
    fig1, ax1 = plt.subplots(figsize = (7,5))
    ax1.pie(count, autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.2, startangle=360, radius=4, textprops={'fontsize': 8})
    ax1.axis('equal') 
    plt.tight_layout()
    plt.legend(index,bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.9)
    plt.show()'''
    
   

if __name__ == "__main__":
    csv_file , colname = parse_argument()
    create_piechart(csv_file, colname)