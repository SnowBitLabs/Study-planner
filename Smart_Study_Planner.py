#Start of code
print("hello user!, please enter the required deatils to decide what and how to study")

# taking required details as inputs from user
name=input("Enter your name: ")
age= int(input("Enter your age: "))
hours=float(input("Enter available hours(decimal value): "))

fav_sub=input("Enter your favourite subject: ")
easy_topic=input("Enter your easy topics in favourite subject:")
weak_topic=input("Enter your weak topics in favourite subject:")

weak_sub=input("Enter your weak subject: ")
easy_topic1=input("Enter your easy topics in weak subject:")
weak_topic1=input("Enter your weak topics in weak subject:")

enrg_lvl=float(input("Enter your energy level on a scale of 1-10(in decimal value): "))

#deciding type of study approach and suggesting 

#  Emergency / override conditions (highest priority)
if enrg_lvl <= 2 or hours <= 1:
    print(" Critical Low State:")
    print("→ Take rest or do VERY light revision of", easy_topic)

#  Low energy handling (even if hours are high)
elif 2 < enrg_lvl <= 4:
    if hours >= 6:
        print(" Low Energy but High Time:")
        print("→ Start with", easy_topic, "then slowly move to", weak_topic)
    elif 3 <= hours < 6:
        print(" Controlled Session:")
        print("→ Revision + short practice of", easy_topic)
    else:
        print(" Light Mode:")
        print("→ Only revision or concept videos of", easy_topic)

#  Medium energy (most flexible zone)
elif 4 < enrg_lvl <= 7:
    if hours >= 6:
        print(" Productive Mode:")
        print("→ Mix of", weak_topic, "and", easy_topic)
        print("→ Include 1-2 breaks")
    elif 3 <= hours < 6:
        print(" Balanced Session:")
        print("→ Focus on", weak_topic, "with some revision")
    else:
        print(" Short Session:")
        print("→ Quick revision of", easy_topic," or" ,easy_topic1 ," or practice questions")

#  High energy zone
elif 7 < enrg_lvl <= 9:
    if hours >= 6:
        print(" Deep Work Mode:")
        print("→ Focus on", weak_topic1, "in", weak_sub)
        print("→ Add problem solving + active recall")
    elif 3 <= hours < 6:
        print(" Focused Mode:")
        print("→ Do hard topics from", fav_sub)
    else:
        print(" Quick Attack Mode:")
        print("→ Solve challenging questions quickly")

#  Peak state (max performance)
elif enrg_lvl > 9:
    if hours >= 6:
        print(" BEAST MODE:")
        print("→ Attack hardest topics from", weak_sub)
        print("→ No distractions, deep focus")
    else:
        print(" High Energy Burst:")
        print("→ Finish toughest pending work quickly")

#  Fallback (rare cases)
else:
    print(" Default Mode:")
    print("→ Mix of revision + practice based on comfort")
    
# taking feedback from user
feedback= input("Please enter your feedback for our service(excellent/good/average/poor/disappointing): ")

# deciding reponse based on user's feedback
feedback = feedback.lower()
if feedback =="excellent" :
    print("thankyou for your feedback!,\n This means a lot for us\nWe are glad to know that our service pleased you!")
elif feedback =="good" :
    print("Thankyou for your feedback!,\n This means a lot for us\nWe are glad to know that our service was of some use for you, \nWe are trying to improve")
elif feedback =="average":
    print("Thankyou for your feedback!,\n This means a lot for us\n We are trying to improve our service, \nWe hope that next time our service pleases you")
elif feedback =="poor":
    print("We are really sorry if our service felt poor to you, \n your feedback means a lot for us,\n we are trying to improve our service and hope our service pleases you next time")
elif feedback =="disappointing":
    print(" We are greatly sorry for our disappointing service,\n we are countinuously trying to improve our service and hope that our service pleases you next time")
else:
    print("Error!, invalid input for feedback")
# exiting program
ext= input("Type exit to exit the program: ")
ext = ext.lower()
if ext =="exit":
    print("Exiting program")
else:
    print("Error!, unable to exit program,\n invlaid input for exiting program")




