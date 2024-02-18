from tkinter import *

window = Tk()
window.title("CV Generator")
 
label_name = Label(window, text="Name: ")
label_name.pack_configure()
entry_name= Entry(window)
entry_name.pack_configure()

label_email = Label(window, text="Email: ")
label_email.pack_configure()
entry_email= Entry(window)
entry_email.pack_configure()

label_address = Label(window, text="Address: ")
label_address.pack_configure()
entry_address= Entry(window)
entry_address.pack_configure()

label_website = Label(window, text="Website: ")
label_website.pack_configure()
entry_website= Entry(window)
entry_website.pack_configure()

label_skills = Label(window, text="Skills(Enter one skill per line)")
label_skills.pack_configure()
entry_skills = Text(window,height=5)
entry_skills.pack_configure()

label_education = Label(window, text="Education(One per line in format 'Degree':'University')")
label_education.pack_configure()
entry_education = Text(window,height=5)
entry_education.pack_configure()

label_experience = Label(window, text="Experience(Enter one per line in format 'Job Title':'Description')")
label_experience.pack_configure()
entry_experience = Text(window,height=5)
entry_experience.pack_configure()

label_about_me = Label(window, text="About Me")
label_about_me.pack_configure()
entry_about_me = Text(window,height=5)
entry_about_me.pack_configure()


button_generate = Button(window, text="Generate CV")

window.mainloop()