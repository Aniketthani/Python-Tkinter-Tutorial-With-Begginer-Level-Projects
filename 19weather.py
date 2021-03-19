from tkinter import *
import requests
import json
root=Tk()
root.title("Weather App")
root.geometry("600x100")



def weathersearch():
    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+str(zip_box.get())+"&distance=5&API_KEY=Your Own Api Key")
        api=json.loads(api_request.content)
        city=api[0]["ReportingArea"]
        quality=api[0]["AQI"]
        category=api[0]["Category"]["Name"]

        if category=="Good":
            color="green"
        elif category=="Moderate":
            color="yellow"
        elif category=="Unhealthy for Sensitive Groups":
            color="#ff9900"
        elif category=="Unhealthy":
            color="#FF0000"
        elif category=="Very Unhealthy":
            color="#990066"
        elif category=="Hazardous":
            color="#660000"    
        root.configure(background=color)
        label=Label(root,text=city + " Air Quality " + str(quality) + " " + category,font=("Helvetica",21),background=color,pady=10)
        label.grid(row=2,column=0,columnspan=2)
    except :
        api="Error !!"
        print(api)


zip_label=Label(root,text="Zipcode :")
zip_label.grid(row=0,column=0)

zip_box=Entry(root,width=20)
zip_box.grid(row=0,column=1)

search=Button(root,text="Search",command=weathersearch)
search.grid(row=1,column=1,columnspan=2)



root.mainloop()
