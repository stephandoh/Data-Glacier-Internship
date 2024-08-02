import pickle

class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO: {}, ENAME: {}, ESAL: {}, EADDR: {}'.format(self.eno, self.ename, self.esal, self.eaddr))

# Create an Employee object
emp = Employee(101, 'John', 4500, 'NYC')

# Serialize the Employee object
with open('emp.pkl', 'wb') as f:
    pickle.dump(emp, f)
    print("Pickling completed")

# Deserialize the Employee object
with open('emp.pkl', 'rb') as f:
    loaded_emp = pickle.load(f)
    print("Unpickling completed")
    loaded_emp.display()
