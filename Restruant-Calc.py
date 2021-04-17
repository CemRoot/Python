Tables = dict()
for i in range(10):
    Tables[i] = 0 

def AddFee():
   TableNo = int(input("TableNo: "))
   ss = Tables[TableNo]
   add = float(input("Add to fee  "))
   Total = ss + add
   Tables[TableNo] = Total
   
def DelFee():
   TableNo = int(input("TableNo: "))
   ss = Tables[TableNo]
   add = float(input("Add to fee  "))
   Total = ss - add
   if Total < 0:
       print("Error syntax cannot be -")
   else:
       Tables[TableNo] = Total

   
    
def ControlAcc(File_Name):
    Data = list()
    try:
        File = open(File_Name)
        Data = File.read()
        Data = Data.split("\n")
        Data.pop()
        File.close()
        flag = True
        
    except FileNotFoundError:
        File = open(File_Name,"w")
        File.close()
        print("First time running! New File Added!")
        flag = False

    if flag:
        for i in enumerate(Data):
            Tables[i[0]] = float(i[1])
    else:
        pass

def UpdateCont():
        File = open("data.txt","w")
        for i in range(10):
            Fee = Tables[i]
            Fee = str(Fee)
            File.write(Fee + "\n")
        File.close()



def main():
    ControlAcc("data.txt")
    while True:
        print("""
            [1]Show Tables
            [2]Add  Fee
            [3]Del  Fee
            [Q]Quit

        """)

        choose = input("Your Choose: ")

        if choose == "1":
            for i in range(10):
                    print("The bill {} for this  the table {}".format(Tables[i],i))
            print("Process completed! Press Enter to return to the main menu!")
            input()

        elif choose == "2":
                AddFee()
                print("Process completed! Press Enter to return to the main menu!")
                input()


        elif choose == "3":
                 DelFee()
                 print("Process completed! Press Enter to return to the main menu!")
                 input()
        
        elif choose == "q" or choose == "Q":
            print("Exiting")
            quit()
        else:
            print("Syntax Error!")
            

main()