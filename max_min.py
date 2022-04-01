import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name,'-- cpu_usage : ', cpu_usage)
        app_name_dict.update({name:cpu_usage})

keymax = max(app_name_dict, key = app_name_dict.get )
print(keymax)
keymin = min(app_name_dict, key = app_name_dict.get)
print(keymin)
name_list = [keymax, keymin]
print(name_list)

app = app_name_dict.values()
final_max = max(app)
print("Maximum", final_max)
final_min = min(app)
print("Minimum", final_min)
final_min_max_list = [final_max, final_min]

plt.figure(figsize=(15,8))
plt.xlabel("Min-Max CPU Consumption")
plt.ylabel("Usage")
plt.bar(name_list,final_min_max_list,width=0.6,color=("blue","red") )
plt.show()