from truthtable_js import function_translation_key
#compilation
def main(source):
    global data_sect
    data_sect={
        "ind":[],
        "dat":[]
    }
    trimmed_lines=deadspace_out(source.readlines())
    
    to_data_sect(trimmed_lines)
    
    print(data_sect)
    print(trimmed_lines)



def deadspace_out(lines:list):
    constructor=[]
    #removes comments, newlines, and spaces
    for line in filter(lambda a : not a.startswith("//"), lines):

        if len(line.replace("\n","").replace(" ","")) == 0:
            continue

        constructor.append(line.replace("\n","").replace(" ",""))
    return(constructor)

def to_data_sect(lines:list):
    for l in filter(lambda a: "=" in a,lines):
        l=l.split("=")
        if l[0] in data_sect["ind"]:
            data_sect["dat"][data_sect["ind"].index(l[0])]=l[1]
            continue
        data_sect["ind"].append(l[0])
        data_sect["dat"].append(l[1])

with open("testing.nnc","r") as file:
    main(file)