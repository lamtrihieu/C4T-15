district_names =["ST","BD","BTL","CG","DD","HBT"]
district_population =[150300,247100,333300,266800,420900,31800]
district_area=[117.43,9.224,4335,12.04,9.96,10.09]
district_density=[]
for i,n in enumerate(district_population):
    a = district_population[i]/district_area[i]
    print(a)
    district_density.append(a)
print(district_density)

sum_district_population = sum (district_population)
average_density = sum_district_population/(len(district_names)+1)
print (average_density)

