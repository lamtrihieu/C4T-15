

salary1 = {
    "name": "Huy",
    "position": "Waiter",
    "time": 12,
    "salary": 0.8,
}
salary2 = {
    "name": "Tung",
    "position": "Chef",
    "time": 24,
    "salary": 1.5,
}
salary3 = {
    "name": "Duc",
    "position": "Manager",
    "time": 20,
    "salary": 2,
}
salary = [salary1, salary2, salary3]

# print(salary)


# salary1["name"] = "Huyen"
# salary1["position"] = "Waitress"
# salary1["time"] = 14
# salary1["salary"] = 1


# print(salary1)


# salary.pop(len(salary)-1)


# print(salary)


# print(*salary,sep="\n")

listSalary = []
for i in range(len(salary)):
    month_salary = 30 * salary[i]["time"] * salary[i]["salary"]
    listSalary.append(month_salary)
print(sum(listSalary))
