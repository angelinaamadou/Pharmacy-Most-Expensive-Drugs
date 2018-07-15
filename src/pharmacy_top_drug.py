import sys

f = open(sys.argv[1],"r")
drug_dict = dict()

## Skip line with quotes
def reduce_line(list_line):
    for i in range(len(list_line)):
        if '"' in list_line[i]:
            list_line[i] += ","+list_line[i+1]
            list_line.remove(list_line[i+1])
            if len(list_line)==5:
                break
    return list_line
    


for line in f: 
   
   ## Split line  with commas and check to see if there are 5 attributes
    new_line = line.split(",")
    ## check for empty line
    if len(new_line) < 5:
        continue
    if len(new_line) >= 5:
        new_line = reduce_line(new_line)
        #print(new_line)
     
    drug_id,lname,fname,drug_name,drug_cost = new_line
    try:
        drug_cost = float(drug_cost)
    except ValueError:
            # drug_cost is not a number, ignore this line
        continue
        
    if not drug_name in drug_dict:
        drug_dict[drug_name] = [drug_cost]

    else:
        drug_dict[drug_name].append(drug_cost)
        
 
  
## Process drug by getting the  number of prescription and the total prescription 
drug_list =  [[k,len(v),sum(v)] for k,v in drug_dict.items()]
drug_list = sorted(drug_list, key=lambda x: x[2], reverse=True)



headers =["drug_name,","num_prescriber,","total_cost"]

## Provide filename for output
if len(sys.argv) >2:
    filename = sys.argv[2]
else:
    filename = 'top_cost_drug.txt'

with open(filename, 'w') as f:
    f.writelines(headers)
    f.writelines("\n")
    f.writelines("%s,%s,%s\n" % (drug[0],drug[1],drug[2]) for drug in drug_list)

