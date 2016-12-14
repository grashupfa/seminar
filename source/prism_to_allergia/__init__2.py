import subprocess
import csv
from findall import findall


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    

filename = "IEEE_802.15.4_protocol_fix.prism";
final_string_list = [];

for i in range (0, 300):
    
    print("round...%d",i);

    p = subprocess.Popen("prism.bat IEEE_802.15.4_protocol_be_max6.prism -simpath 500,vars=(s,s2,c1,c2,t),sep=comma stdout", stdout=subprocess.PIPE);
    stdout, stderr = p.communicate();
    
    string = stdout.decode("utf-8");
    split_str = string.split(",");
    
    list_begin = 0;
    final_string = "0_0_0_0_0_0,";
    
    for i in range(0, len(split_str)):
        if (list_begin > 0):
            if (RepresentsInt(split_str[i])):
                final_string += split_str[i] + "_";
            
            if ('\r' in split_str[i]): #last entry, for z
                str_r = split_str[i].replace('\r\n', '?');
                value = str_r.split("?")[0];
                if ("t" != value):
                    final_string+=value + ",";
                    
            list_begin = list_begin -1;
                
        if ("time" in split_str[i]):
            list_begin = 6;          
            
    final_string_list.append(final_string);
        
print("finished reading, start writing csv!");

f = open('data.csv', 'w',newline='');
w = csv.writer(f, delimiter = ',');


for i in range(0, len(final_string_list)):
    new_split_string = "";
    split_string = final_string_list[i].split(",");
    
    for j in range(0, len(split_string)):
        
        split_string_sub = split_string[j];
        states = split_string_sub.split("_");
        
        if (len(states)>2):
            new_split_string += states[1]+states[2]+states[3]+states[4]+",";
        
        
    w.writerow(new_split_string.split(','));

f.close();

target = open("alphabet", 'w')

written_strings = [];

for i in range(0, len(final_string_list)):
    new_split_string = "";
    split_string = final_string_list[i].split(",");
    
    for j in range(0, len(split_string)):
        split_string_sub = split_string[j];
        states = split_string_sub.split("_");
        
        if (len(states)>2):
            string_concat = states[1]+states[2]+states[3]+states[4];
            
            if (string_concat not in written_strings):
                target.write(string_concat);
                target.write("\n");
                written_strings.append(string_concat);    
target.close();

