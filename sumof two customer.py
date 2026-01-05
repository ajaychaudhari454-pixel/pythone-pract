customer=[
    {"name":"ajay","sale":25000,"city":"jalgaon"},
    {"name":"sanaji","sale":24000,"city":"bhogaon"},
    {"name":"vishal","sale":27000,"city":"chinawal"},
    {"name":"sanket","sale":285000,"city":"yawal"},
    {"name":"rahul","sale":35000,"city":"butti bori"},
    {"name":"vijay","sale":26000,"city":"bhusawal"}
]

for c in customer:
    print(c)
    
    total =0 
    
    for c in customer:
        if c["name"]=="ajay" or c["name"]=="vishal":
            total +=c["sale"]
            print(total)