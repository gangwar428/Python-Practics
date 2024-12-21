print("----Roadmap provider Project----")
level = input("Enter F for fresher E for experienced =")
if level == 'F':
    domains = input("Chose your intested domain Number:\nWeb Dev >1 \nApp Dev >2 \n DS/AI >3\n>")
    
    if domains == '1':
        print("Web Development Roadmap:  You need to learn these\n 1. HTML \n 2. CSS \n 3. JavaScript \n 4. Python Django")
    elif domains == '2':
        print("App Development Roadmap:  You need to learn these\n 1. Flutter \n 2. React Native \n 3. JAVA \n 4. DSA and Build Project")
    elif domains == '3':
        print("Data Science and AI Roadmap:  You need to learn these\n 1. Statistics \n 2. Mathematics \n 3. Python/R") 
    else:
        print("Invalid domain!")

elif level == 'E':
    domain = input("Enter your intrested doamin Name: \n 1. DA \n 2. CC \n 3. FE \n>")    
    
    if domain == 'DA':
        print("Data Analytics Roadmap: You need to learn these\n 1. Python \n 2. Excel \n 3. Power BI")
    elif domain == 'CC':
        print("Cloud Computing roadmap:  You need to learn these\n 1. Python for Automation \n 2. DevOps ")   
    elif domain == 'FE':
        print("Frontend Roadmap:  You need to learn these \n 1. learn python and Django for Backend")
else:
    print("Invalid level!")                         
    
    
