from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd

def convert_to_pdf(data, path, name):
    fig, ax = plt.subplots(figsize=(12, len(data.columns)))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=data.values, colLabels=data.columns, loc='center')
    pp = PdfPages(path + name)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()



"""from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import pandas as pd
def convert_to_pdf(data,path,name):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=data.values, colLabels=data.columns, loc='center')
    pp = PdfPages(path + name)
    pp.savefig(fig, bbox_inches='tight')
    pp.close()"""