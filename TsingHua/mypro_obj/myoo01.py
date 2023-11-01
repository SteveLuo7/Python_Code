
class SalaryAccount:

    def __call__(self, salary):
        yearSalary = salary * 12
        daySalary = salary // 27.5
        hourSalary = daySalary // 8
        print("计算工资")

        return dict(yearSalary=yearSalary, daySalary=daySalary, hourSalary=hourSalary)

s = SalaryAccount()
print(s(40000))
