print("----Checking Certificate Eligibility----")
# Get user's input
attende = input("Enter your Answer:\n 1. All Days \n 2. Day Gap \n >")
# Check user's input

if attende == '1':
    assignment = input("Have you completed the assignment? (True/False): \n").capitalize()
    live_class = input("Have you attend to live classes? (True/False): \n").capitalize()
    camra_on = input("Was your camra on during the Classes? (True/False): \n").capitalize()
    if assignment == "True" and camra_on == "True" and live_class == "True":
        print("Wow! You are Eligible for Certificate")
    else:
        print("You are not Eligible for Certificate due to some other reason")    
elif attende == '2':
    print("Not eligible for Certificate")
else:
    print("Invalid input!")