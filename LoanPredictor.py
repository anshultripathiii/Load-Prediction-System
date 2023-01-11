import tkinter as tk
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
class LoanPredictor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x550")
        self.title("Loan Predictor")
        self.config(bg = "sky blue")
        self.create_gui()


    def predictloan(self):
        #loading the dataset to pandas dataframe
        loan_dataset = pd.read_csv(r"C:\Users\PRANAV KANSAL\Desktop\AI\loan_predictor.csv")
        type(loan_dataset)

    #printing the first five rows
    loan_dataset.head()

    def create_gui(self):
        self.heading = tk.Label(self,text = "LOAN PREDICTOR",font=("new time romans", 13, "bold"), bg="sky blue", fg="purple")
        self.heading.config(width = 30,height =5)
        self.heading.grid(row =0,column =3,padx=5,pady=5)

        self.name = tk.Label(self, text="Name",bg = "sky blue",fg = "blue")
        self.name.grid(row =2,column =2,padx =5,pady =5)
        self.gender = tk.Label(self, text="Gender",bg ="sky blue",fg ="blue")
        self.gender.grid(row =3,column = 2,padx =5,pady =5)
        self.married = tk.Label(self,text = "Married",bg ="sky blue",fg = "blue")
        self.married.grid(row =4,column = 2,padx =5,pady =5)
        self.Dependants = tk.Label(self,text = "Dependants",bg ="sky blue",fg ="blue")
        self.Dependants.grid(row=5,column = 2,padx =5,pady =5)
        self.Education = tk.Label(self,text = "Education",bg ="sky blue",fg ="blue")
        self.Education.grid(row =6,column =2,padx =5,pady =5)
        self.Self_Employed = tk.Label(self,text = "Self Employed",bg ="sky blue",fg ="blue")
        self.Self_Employed.grid(row =7,column =2,padx =5,pady =5)
        self.Applicant_Income = tk.Label(self,text = "Applicant Income",bg ="sky blue",fg ="blue")
        self.Applicant_Income.grid(row =8,column =2,padx =5,pady =5)
        self.CoApplicant_Income = tk.Label(self,text = "Co-Applicant Income",bg ="sky blue",fg ="blue")
        self.CoApplicant_Income.grid(row =9,column =2,padx =5,pady =5)
        self.Loan_Amount = tk.Label(self,text = "Loan Amount",bg ="sky blue",fg ="blue")
        self.Loan_Amount.grid(row =10,column =2,padx =5,pady =5)
        self.Loan_Amount_Term = tk.Label(self,text = "Loan amount Term",bg ="sky blue",fg ="blue")
        self.Loan_Amount_Term.grid(row =11,column =2,padx =5,pady =5)

        namevalue = tk.StringVar()
        gendervalue = tk.StringVar()
        marriedvalue = tk.StringVar()
        dependantsvalue = tk.IntVar()
        educationvalue = tk.StringVar()
        selfemployedvalue = tk.StringVar()
        applicantincomevalue  = tk.IntVar()
        coapplicantincomevalue = tk.IntVar()
        loanamountvalue = tk.IntVar()
        loanamounttermvalue = tk.IntVar()


        nameentry = tk.Entry(self,textvariable = namevalue)
        nameentry.grid(row =2,column = 3)
        genderentry = tk.Entry(self,textvariable = gendervalue)
        genderentry.grid(row = 3,column =3)
        marriedentry = tk.Entry(self,textvariable =  marriedvalue)
        marriedentry.grid(row = 4,column = 3)
        dependantentry = tk.Entry(self, textvariable=dependantsvalue)
        dependantentry.grid(row=5, column=3)
        educationentry = tk.Entry(self, textvariable=educationvalue)
        educationentry.grid(row=6, column=3)
        selfemployedentry = tk.Entry(self, textvariable=selfemployedvalue)
        selfemployedentry.grid(row=7, column=3)
        applicantincomeentry = tk.Entry(self, textvariable=applicantincomevalue)
        applicantincomeentry.grid(row=8, column=3)
        coapplicantincomeentry = tk.Entry(self, textvariable=coapplicantincomevalue)
        coapplicantincomeentry.grid(row=9, column=3)
        loanamountentry = tk.Entry(self, textvariable=loanamountvalue)
        loanamountentry.grid(row=10, column=3)
        loanamounttermentry = tk.Entry(self, textvariable=loanamounttermvalue)
        loanamounttermentry.grid(row=11, column=3)


        self.submitbutton = tk.Button(self,text = "PREDICT" ,bg ="sky blue",fg ="purple",command = self.predictloan)
        self.submitbutton.grid(row = 13,column = 3,pady = 10)





if __name__ == '__main__':
    app = LoanPredictor()
    app.mainloop()