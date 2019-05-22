district_names =["ST","BD","BTL","CG","DD","HBT"]
district_population =[150300,247100,333300,266800,420900,31800]
print (min(district_population))
for i,n in enumerate(district_population):
    if n == min(district_population):
        print ("The district with the least people is:",district_names[i])

print (max(district_population))
for m,l in enumerate(district_population):
    if l == max(district_population):
        print ("The district with the least people is:",district_names[m])