import random
import time
from tkinter import *

upper={1:"push ups",2:"shoulder lift arc (poids)",3:"wrist curls (poids)",4:"dips",5:"clap arms (poids)",6:"down to high (poids)",7:"biceps curls (poids)",8:"punches",9:"triceps extension (poids)",10:"side papillon (poids)",11:"body dips",12:"elbow taps (poids)",13:"bent over rows (poids)"}
core={1:"low plank",2:"plank touch shoulder",3:"bicycle kicks",4:"crunches",5:"full bod crunches",6:"plank up down",7:"bicycle crunches",8:"twist plank",9:"russian twist",10:"side to side crunch"}
legs={1:"squats",2:"lunges",3:"leg raise",4:"swipe calf raise",5:"calf raise (on the toe)",6:"wall sit",7:"flutter kicks",8:"bridge"}

flexi=[
    "standing touching floor",
    "foot over leg, arm on knee",
    "hand on back, other hand on elbow",
    "butterfly legs",
    "sphinx",
    "head on groud arm extended",
    "knees to chest",
    "dead body",
    "lunging hip",
    "split"
    ]

def generate_workout():
    upper1=random.randint(1,13)
    upper2=random.randint(1,13)
    while upper1==upper2:
        upper2=random.randint(1,13)
    core1=random.randint(1,10)
    core2=random.randint(1,10)
    while core1==core2:
        core2=random.randint(1,10)
    leg=random.randint(1,8)
    workout=[]
    workout.append(upper[upper1])
    workout.append(upper[upper2])
    workout.append(core[core1])
    workout.append(core[core2])
    workout.append(legs[leg])
    return workout


def timer(temps):
    t=temps
    print("GO")
    while t >0:
        if t>5:
            print(t," sec")
        else:
            print("! ",t," sec !")
        t-=1
        time.sleep(1)
    print("FIN")


def action(temps,t,etape,i,w,tour):
    temps.configure(text=str(t)+' sec')
    etape.configure(text=str(w[i] + " - "+str(tour)))
    if t > 0:
        temps.after(1000,action,temps,t-1,etape,i,w,tour)
    else:
        if i == int(len(w)-1):
            if tour == 3:
                etape.configure(text='FIN')
            else:
                etape.configure(text='Pause')
                i=0
                t=45
                tour+=1
                etape.after(15000,action,temps,t,etape,i,w,tour)
        else:
            i+=1
            etape.configure(text="Rest")
            t=45
            temps.after(15000,action,temps,t,etape,i,w,tour)

def main():
    w=generate_workout()
    print(w)
    tk=Tk()
    i=0
    t=46
    tour=1
    tk.title("Workout Generator")
    tk.geometry('600x600')
    etape=Label(text=str(w[i] + " - "+str(tour)),font=('Courier',20))
    temps=Label(text=str(t)+' sec',font=('Courier',30),fg="red")
    workoutArm=Label(text=str(w[0])+' & '+str(w[1]),font=('Courier',10))
    workoutCore=Label(text=str(w[2])+' & '+str(w[3]),font=('Courier',10))
    workoutLeg=Label(text=str(w[4]),font=('Courier',10))
    workoutArm.pack()
    workoutCore.pack()
    workoutLeg.pack()
    etape.pack()
    temps.pack()
    etape.place(x=300,y=100,anchor='center')
    temps.place(x=300,y=300,anchor='center')
    workoutArm.place(x=300,y=500,anchor="center")
    workoutCore.place(x=300,y=525,anchor="center")
    workoutLeg.place(x=300,y=550,anchor="center")
    tk.resizable(False,False)
    temps.after(3000,action(temps,t,etape,i,w,tour))
    tk.mainloop()
    print()
    print('30 sec each stretch')
    for f in flexi:
        print('* ',f)


main()

