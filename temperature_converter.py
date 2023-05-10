#import tkinter as tk
import customtkinter as ctk


def frames():
    global celcius_page, kelvin_page, farenheit_page
    celcius_page=ctk.CTkFrame(window)
    celcius_page.grid(row=2, column=1, pady=(50, 10))

    kelvin_page=ctk.CTkFrame(window)
    kelvin_page.grid(row=2, column=1, pady=(50, 10))

    farenheit_page=ctk.CTkFrame(window)
    farenheit_page.grid(row=2, column=1, pady=(50, 10))
    
    
#function to display top buttons
def top_buttons():
    #button to dispay celcuius section
    celcius_button_display=ctk.CTkButton(window, text='Celcius', command=display_celcius)
    celcius_button_display.grid(row=1,column=0, pady=20, padx=20)

    #button to dispay kelvin section
    kelvin_button_display=ctk.CTkButton(window, text='Kelvin', command=display_kelvin)
    kelvin_button_display.grid(row=1,column=1, pady=20, padx=20)
    
    #button to dispay farenheit section
    farenheit_button_display=ctk.CTkButton(window, text='Farenheit', command=display_farenheit)
    farenheit_button_display.grid(row=1,column=2, pady=20)

#farenheit to celcius and kevin 
kelvin3=0
celcius3=0   
def farenheit_convertion():
    global kelvin3, celcius3
    fa_entry=farenheit_entry.get()
    farenheit_result1=(5/9) * (float(fa_entry) + 459.67)
    farenheit_result2= (float(fa_entry)- 32)  * (5/9)
    if kelvin3==0 and celcius3==0:
        kelvin = display_kelvin_resultlabel.configure(text=f'Kelvin: {round(farenheit_result1,2)}')
        celcius = display_celcius_resultlabel.configure(text=f'Celcius: {round(farenheit_result2,2)}')
        kelvin3=0
        celcius3=0

#display farenheit contents        
def fa_main_content():
    global farenheit_entry, display_kelvin_resultlabel, display_celcius_resultlabel
    instruction_label=ctk.CTkLabel(farenheit_page, text='Enter your temperature\nin FARENHEIT', font=font2)
    instruction_label.grid(row=0, column=0, padx=100, pady=20)
    
    farenheit_entry=ctk.CTkEntry(farenheit_page, placeholder_text='Temperature in FARENHEIT', font=font1, width=200)
    farenheit_entry.grid(row=1, column=0)
    
    farenheit_con_button=ctk.CTkButton(farenheit_page, text='Convert', font=font1, command=farenheit_convertion)
    farenheit_con_button.grid(row=2, column=0, pady=(20, 10))
    
    farenheit_result_display=ctk.CTkLabel(farenheit_page, text='Result:', font=font2, text_color='yellow')
    farenheit_result_display.grid(row=3, column=0)
    
    display_kelvin_resultlabel=ctk.CTkLabel(farenheit_page, text='Kelvin = 0', font=font1)
    display_kelvin_resultlabel.grid(row=4, column=0, pady=(5,0))
    
    display_celcius_resultlabel=ctk.CTkLabel(farenheit_page, text='Celcius = 0', font=font1)
    display_celcius_resultlabel.grid(row=5, column=0, pady=(5,40))
    
    
#section for kelvin  
#convert kelvin to other temperature
farenheit2=0
celcius2=0  
def kelvin_convertion():
    global farenheit2, celcius2
    ke_entry= kelvin_entry.get()
    kelvin_result1=((float(ke_entry)-273.15) * (9/5)) +32
    kelvin_result2= (float(ke_entry))  - 273
    if farenheit2==0 and celcius2==0:
        farenheit2 = display_kelvin_resultlabel2.configure(text=f'Farenheit: {round(kelvin_result1,2)}')
        celcius2 = display_celcius_resultlabel2.configure(text=f'Celcius: {round(kelvin_result2,2)}')
        farenheit2=0
        celcius2=0

        
def ke_main_content():
    global kelvin_entry, display_kelvin_resultlabel2, display_celcius_resultlabel2, instruction_label2
    instruction_label2=ctk.CTkLabel(kelvin_page, text='Enter your temperature\nin KELVIN', font=font2)
    instruction_label2.grid(row=0, column=0, padx=100, pady=20)
    
    kelvin_entry=ctk.CTkEntry(kelvin_page, placeholder_text='Temperature in KELVIN', font=font1, width=200)
    kelvin_entry.grid(row=1, column=0)
    
    kelvin_con_button=ctk.CTkButton(kelvin_page, text='Convert', font=font1, command=kelvin_convertion)
    kelvin_con_button.grid(row=2, column=0, pady=(20, 10))
    
    kelvin_result_display=ctk.CTkLabel(kelvin_page, text='Result:', font=font2, text_color='yellow')
    kelvin_result_display.grid(row=3, column=0)
    
    display_kelvin_resultlabel2=ctk.CTkLabel(kelvin_page, text='Farenheit = 0', font=font1)
    display_kelvin_resultlabel2.grid(row=4, column=0, pady=(5,0))
    
    display_celcius_resultlabel2=ctk.CTkLabel(kelvin_page, text='Celcius = 0', font=font1)
    display_celcius_resultlabel2.grid(row=5, column=0, pady=(5,40))
    
    
#section for celcius  
#convert celcius to other temperature
farenheit1=0
celcius1=0  
def celcius_convertion():
    global farenheit1, celcius1
    ce_entry= celcius_entry.get()
    celcius_result1=(((9/5)* float(ce_entry)) + 32) 
    celcius_result2= (float(ce_entry))  + 273
    if farenheit1==0 and celcius1==0:
        farenheit1 = display_celcius_resultlabel1.configure(text=f'Farenheit: {round(celcius_result1,2)}')
        celcius1 = display_celcius_resultlabel11.configure(text=f'Kelvin: {round(celcius_result2,2)}')
        farenheit1=0
        celcius1=0

        
def ce_main_content():
    global celcius_entry, display_celcius_resultlabel1, display_celcius_resultlabel11, instruction_label3
    instruction_label3=ctk.CTkLabel(celcius_page, text='Enter your temperature\nin CELCIUS', font=font2)
    instruction_label3.grid(row=0, column=0, padx=100, pady=20)
    
    celcius_entry=ctk.CTkEntry(celcius_page, placeholder_text='Temperature in CELCIUS', font=font1, width=200)
    celcius_entry.grid(row=1, column=0)
    
    celcius_con_button=ctk.CTkButton(celcius_page, text='Convert', font=font1, command=celcius_convertion)
    celcius_con_button.grid(row=2, column=0, pady=(20, 10))
    
    celcius_result_display=ctk.CTkLabel(celcius_page, text='Result:', font=font2, text_color='yellow')
    celcius_result_display.grid(row=3, column=0)
    
    display_celcius_resultlabel1=ctk.CTkLabel(celcius_page, text='Farenheit = 0', font=font1)
    display_celcius_resultlabel1.grid(row=4, column=0, pady=(5,0))
    
    display_celcius_resultlabel11=ctk.CTkLabel(celcius_page, text='Kelvin = 0', font=font1)
    display_celcius_resultlabel11.grid(row=5, column=0, pady=(5,40))
    


#functions to switch between pages
def display_celcius():
    farenheit_page.grid_forget()
    kelvin_page.grid_forget()
    celcius_page.grid(row=2, column=1, pady=(50, 10))
    
def display_kelvin():
    farenheit_page.grid_forget()
    kelvin_page.grid(row=2, column=1, pady=(50, 10))
    celcius_page.grid_forget()
    instruction_label2.grid(row=0, column=0, padx=100, pady=20)

    
def display_farenheit():
    farenheit_page.grid(row=2, column=1, pady=(50, 10))
    kelvin_page.grid_forget()
    celcius_page.grid_forget()


    
if __name__=='__main__':   
    #system settings   
    ctk.set_appearance_mode('Dark')
    ctk.set_default_color_theme('green')

    #Main app settings
    window=ctk.CTk()
    window.geometry('700x500')
    window.title('Temperature Converter by SAMSON')
    
    frames()
    font1=('montserat', 14,)
    font2=('montserat', 14, 'bold')

    top_buttons()
    ce_main_content()
    ke_main_content()
    fa_main_content()
    
    
    
    fa_entry=str()
    ke_entry=str()
    ce_entry=str()


    

    window.mainloop()