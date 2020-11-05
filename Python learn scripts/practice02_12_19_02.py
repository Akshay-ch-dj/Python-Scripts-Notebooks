class F1:
    def show(self):
        print(" messege from class F1")

class F2(F1):
    def disp(self):
        print("Messege from F2")

k = F1()
k.show()
p = F2()
p.show()
p.disp()
