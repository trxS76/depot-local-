import matplotlib.pyplot as plt
def ue1():
    a=0
    notes=[]
    for i in range(14):
        notes.append(input("Saisir les notes ue1 ")),    
    
                 
    coef_ue1={
    'R101':10,
    'R102':10,
    'R103':7,
    'R104':7,
    'R106':5,
    'R108':6,
    'R110':5,
    'R111':4,
    'R112':2,
    'R113':5,
    'R114':5,
    'SAE11':20,
    'SAE12':20,
    'SAE16':7}

    for note,coef in zip(notes,coef_ue1.values()):
       a+=int(note)*coef/115
    
    b=0
    notes2=[]
    for i in range(12):
        notes2.append(input("Saisir la note ue2 ")),

    coef_ue2={
    'R101':4,
    'R103':2,
    'R104':8,
    'R105':6,
    'R110':5,
    'R111':5,
    'R112':2,
    'R113':9,
    'R114':9,
    'R115':3,
    'SAE13':29,
    'SAE16':7,}

    for note,coef in zip(notes2,coef_ue2.values()):
        b+=(int(note)*coef)/89
    c=0
    notes3=[]
    for i in range(13):
        notes3.append(input("Saisir les notes ue3 ")),

    coef_ue3={
    'R101':4,
    'R103':2,
    'R106':5,
    'R107':15,
    'R108':6,
    'R109':4,
    'R110':5,
    'R111':5,
    'R112':2,
    'R115':3,
    'SAE14':20,
    'SAE15':20,
    'SAE16':7,}

    for note,coef in zip(notes3,coef_ue2.values()):
        c+=int(note)*coef/98
    
    return a,b,c
    

def get_color(value):
    return 'green' if value >= 10 else 'red'

def tmps():
    a,b,c = ue1()
    colors=[get_color(val) for val in[a, b, c]]
    plt.bar(['A', 'B', 'C'], [a, b, c], color=colors)
tmps()