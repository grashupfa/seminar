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

for i in range (0, 250):
    
    print("round...%d",i);

    p = subprocess.Popen("prism.bat IEEE_802.15.4_protocol_channel_modified.prism -simpath 500,vars=(c1,c2,z),sep=comma stdout", stdout=subprocess.PIPE);
    stdout, stderr = p.communicate();
    
    string = stdout.decode("utf-8");
    split_str = string.split(",");
    
    list_begin = False;
    final_string = "";
    
    for i in range(0, len(split_str)):
        if (list_begin):
            if (RepresentsInt(split_str[i])):
                final_string += split_str[i] + "_";
            
            if ('\r' in split_str[i]): #last entry, for z
                str_r = split_str[i].replace('\r\n', '?');
                value = str_r.split("?")[0];
                if ("z" != value):
                    final_string+=value + ",";
                
        if ("step" in split_str[i]):
            list_begin = True;          
            
    final_string_list.append(final_string);
        
print("finished reading, start writing csv!");

f = open('data.csv', 'w');
w = csv.writer(f, delimiter = ',');


for i in range(0, len(final_string_list)):
    new_split_string = "";
    split_string = final_string_list[i].split(",");
    
    for i in range(0, len(split_string)):
        
        split_string_sub = split_string[i];
        states = split_string_sub.split("_");
        
        if (len(states)>2):
            new_split_string += states[1]+states[2]+",";
        
        
    w.writerow(new_split_string.split(','));

f.close();