import random

def guessDegreeInThree():
    response = input("Is Your Degree related to health or education? (yes/no) : ")
    if response.lower() == "yes":
        #AB
        response = input("Is your degree focused on education? (yes/no) : ")
        if response.lower() == "yes":
            #Phys ed, education,child studies
            response = input("Does your degree focus on children?? (yes/no) : ")
            if response.lower() == "yes":
                print("Your degree is child studies")
                return
            if response.lower() == "no":
                degree = random.choice(["Your degree is Education","Your degree is Physical Education"])
                print(degree)
                return
        if response.lower() == "no":
            response = input("Does your degree focus on mental health? (yes/no) : ")
            if response.lower() == "yes":
                print("Your degree is Social Work")
                return
            if response.lower() == "no":
                degree = random.choice(["Your degree is Nursing","Your degree is MidWifery"])
                print(degree)
                return
    if response.lower() == "no":
        response = input("Does your degree favour creativity over hard logic? (yes/no) : ")
        if response.lower() == "yes":
            response = input("Does your degree favour people skills over creativity? (yes/no) : ")
            if response.lower() == "yes":
                print("Your degree is business")
                return
            if response.lower() == "no":
                degree = random.choice(["Your degree is Bacholor of Arts","Your degree is Interior Design"])
                print(degree)
                return
        if response.lower() == "no":
            
            response = input("Does your degree involve computer programming(yes/no) : ")
            if response.lower() == "yes":
                degree = random.choice(["our degree is bacholor of computer information systems","our degree is bacholor of Science"])
                print(degree)
                return
            if response.lower() == "no":
                print("Your degree is Communication")
                return
        

guessDegreeInThree()