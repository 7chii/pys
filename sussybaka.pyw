from tkinter import *
from tkinter import ttk
import random as rd


#lista
capitals_countries = ["Kabul","Afghanistan" , 
             "Tirana" , "Albania",
             "Algiers", "Algeria",
             "Andorra la Vella", "Andorra",
             "Luanda", "Angola",   
             "Saint John's","Antigua and Barbuda",
             "Buenos Aires",	"Argentina",
             "Yerevan",	"Armenia",
             "Canberra",	"Australia",
             "Vienna",	"Austria",
             "Baku"	,"Azerbaijan",
             "Nassau",	"Bahamas",
             "Manama",	"Bahrain",
             "Dhaka",	"Bangladesh",
             "Bridgetown",	"Barbados",
             "Minsk",	"Belarus",
             "Brussels"	,"Belgium",
             "Belmopan",	"Belize",
             "Porto Novo",	"Benin",
             "Thimphu"	,"Bhutan",
             "La Paz administrative, Sucre" 	,"Bolivia",
             "Sarajevo"	,"Bosnia e Herzegovina",
             "Gaborone"	,"Botswana",
             "Brasilia"	,"Brazil",
             "Bandar Seri Begawan",	"Brunei",
             "Sofia"	,"Bulgaria",
             "Ouagadougou"	,"Burkina Faso",
             "Gitega"	,"Burundi",
             "Phnom Penh"	,"Cambodia",
             "Yaounde"	,"Cameroon",
             "Ottawa",	"Canada",
             "Praia"	,"Cape Verde",
             "Bangui"	,"Central African Republic",
             "N'Djamena",	"Chad",
             "Santiago",	"Chile",
             "Beijing",	"China",
             "Bogota"	,"Colombia",
             "Moroni"	,"Comoros",
             "Kinshasa",	"Congo",
             "San Jose",	"Costa Rica",
             "Yamoussoukro"	,"Côte d'Ivoire (Ivory Coast)",
             "Zagreb",	"Croatia",
             "Havana",	"Cuba",
             "Nicosia"	,"Cyprus",
             "Prague"	,"Czech Republic Czechia",
             "Copenhagen"	,"Denmark",
             "Djibouti",	"Djibouti",
             "Roseau"	,"Dominica",
             "Santo Domingo"	,"Dominican Republic",
             "Dili",	"East Timor",
             "Quito",	"Ecuador",
             "Cairo",	"Egypt",
             "San Salvador",	"El Salvador",
             "London",	"England",
             "Malabo"	,"Equatorial Guinea",
             "Asmara",	"Eritrea",
             "Tallinn",	"Estonia",
             "Mbabana",	"Eswatini Swaziland",
             "Addis Ababa",	"Ethiopia",
             "Palikir",	"Federated States of Micronesia",
             "Suva",	"Fiji",
             "Helsinki",	"Finland",
             "Paris"	,"France",
             "Libreville",	"Gabon",
             "Banjul",	"Gambia",
             "Tbilisi",	"Georgia",
             "Berlin",	"Germany",
             "Accra"	,"Ghana",
             "Athens",	"Greece",
             "Saint George's"	,"Grenada",
             "Guatemala City"	,"Guatemala",
             "Conakry",	"Guinea",
             "Bissau"	,"Guinea-Bissau",
             "Georgetown",	"Guyana",
             "Port au Prince",	"Haiti",
             "Tegucigalpa",	"Honduras",
             "Budapest",	"Hungary",
             "Reykjavik",	"Iceland",
             "New Delhi",	"India",
             "Jakarta",	"Indonesia",
             "Tehran",	"Iran",
             "Baghdad",	"Iraq",
             "Dublin"	,"Ireland",
             "Rome",	"Italy",
             "Kingston",	"Jamaica",
             "Tokyo",	"Japan",
             "Amman",	"Jordan",
             "Nur-Sultan",	"Kazakhstan",
             "Nairobi"	,"Kenya",
             "Tarawa Atoll",	"Kiribati",
             "Pristina",	"Kosovo",
             "Kuwait City",	"Kuwait",
             "Bishkek",	"Kyrgyzstan",
             "Vientiane",	"Laos",
             "Riga",	"Latvia",
             "Beirut",	"Lebanon",
             "Maseru",	"Lesotho",
             "Monrovia",	"Liberia",
             "Tripoli",	"Libya",
             "Vaduz",	"Liechtenstein",
             "Vilnius",	"Lithuania",
             "Luxembourg",	"Luxembourg",
             "Antananarivo",	"Madagascar",
             "Lilongwe",	"Malawi",
             "Kuala Lumpur",	"Malaysia",
             "Male",	"Maldives",
             "Bamako",	"Mali",
             "Valletta",	"Malta",
             "Majuro",	"Marshall Islands",
             "Nouakchott", "Mauritania", 
             "Port Louis"	,"Mauritius",
             "Mexico City",	"Mexico",
             "Chisinau"	,"Moldova",
             "Monaco"	,"Monaco",
             "Ulaanbaatar",	"Mongolia",
             "Podgorica",	"Montenegro",
             "Rabat",	"Morocco",
             "Maputo"	,"Mozambique",
             "Nay Pyi Taw",	"Myanmar",
             "Windhoek",	"Namibia",
             "No official capital",	"Nauru",
             "Kathmandu",	"Nepal",
             "Amsterdam",	"Netherlands",
             "Wellington",	"New Zealand",
             "Managua",	"Nicaragua",
             "Niamey",	"Niger",
             "Abuja",	"Nigeria",
             "Pyongyang",	"North Korea",
             "Skopje",	"North Macedonian Macedonia",
             "Belfast",	"Northern Ireland",
             "Oslo",	"Norway",
             "Muscat",	"Oman",
             "Islamabad",	"Pakistan",
             "Melekeok",	"Palau",
             "Panama City",	"Panama",
             "Port Moresby",	"Papua New Guinea",
             "Asuncion",	"Paraguay",
             "Lima",	"Peru",
             "Manila",	"Philippines",
             "Warsaw",	"Poland",
             "Lisbon",	"Portugal",
             "Doha",	"Qatar",
             "Bucharest",	"Romania",
             "Moscow",	"Russia",
             "Kigali",	"Rwanda",
             "Basseterre",	"Saint Kitts e Nevis",
             "Castries",	"Saint Lucia",
             "Kingstown",	"Saint Vincent e the Grenadines",
             "Apia",	"Samoa",
             "San Marino",	"San Marino",
             "Sao Tome",	"Sao Tome e Principe",
             "Riyadh"	,"Saudi Arabia",
             "Edinburgh",	"Scotland",
             "Dakar",	"Senegal",
             "Belgrade",	"Serbia",
             "Victoria",	"Seychelles",
             "Freetown",	"Sierra Leone",
             "Singapore",	"Singapore",
             "Bratislava"	,"Slovakia",
             "Ljubljana",	"Slovenia",
             "Honiara",	"Solomon Islands",
             "Mogadishu",	"Somalia",
             "Pretoria, Bloemfontein, Cape Town", "South Africa",
             "Seoul",	"South Korea",
             "Juba",	"South Sudan",
             "Madrid",	"Spain",
             "Sri Jayawardenapura Kotte",	"Sri Lanka",
             "Khartoum",	"Sudan",
             "Paramaribo",	"Suriname",
             "Stockholm",	"Sweden",
             "Bern",	"Switzerland",
             "Damascus",	"Syria",
             "Taipei",	"Taiwan",
             "Dushanbe",	"Tajikistan",
             "Dodoma",	"Tanzania",
             "Bangkok"	,"Thailand",
             "Lome"	,"Togo",
             "Nuku'alofa"	,"Tonga",
             "Port of Spain",	"Trinidad e Tobago",
             "Tunis",	"Tunisia",
             "Ankara",	"Turkey",
             "Ashgabat",	"Turkmenistan",
             "Funafuti"	,"Tuvalu",
             "Kampala",	"Uganda",
             "Kyiv ou Kiev",	"Ukraine",
             "Abu Dhabi"	,"United Arab Emirates",
             "London"	,"United Kingdom",
             "Washington D.C."	,"United States",
             "Montevideo",	"Uruguay",
             "Tashkent"	,"Uzbekistan",
             "Port Vila"	,"Vanuatu",
             "Vatican City"	,"Vatican City",
             "Caracas"	,"Venezuela",
             "Hanoi"	,"Vietnam",
             "Cardiff"	,"Wales",
             "Sana'a"	,"Yemen",
             "Lusaka"	,"Zambia",
             "Harare"	,"Zimbabwe" ]

capitais = capitals_countries[0::2]
paises = capitals_countries[1::2]

#func randchoice
def rand_reset():
   global x
   global y
   global z
   
   x = rd.choice(capitais)
   y = capitals_countries.index(x) + 1
   z = capitals_countries[y]
   
   string3 = z
   label.configure(text=string3)


#init tkinter
win= Tk()

#geo and name
win.title("A MAIOR COMPETICAO DE TODOS OS TEMPOS!!!")
win.geometry("750x350")


#def display_text():
   #global entry
   #string= entry.get()
   #label.configure(text=string)

#Initialize a Label to display the User Input
label=Label(win, text=" ", font=("Courier 22 bold"))
label.pack()

#label=Label(win, text=z , font=("Courier 22 bold"))
#label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

#textos
#label1 = Label(win, text=" ",font=("Courier 22 bold"))#.grid(column=5, row=10)
#label1.pack()
#comando resporta botao
def resp_bot():
   global entry
   string1 = entry.get()
   if entry.get() == x:
       label1.configure(text=string1) # = Label(win, text=string1).grid(column=5, row=10)
       label2.configure(text="YAAAY")#.grid(column=5, row=15)
   else: 
      label2.configure(text="errou :(")#.grid(column=5, row=15)

#clear
def clear_bot():
   global entry
   label1.configure(text=" ")
   label2.configure(text=" ")


      
label1 = Label(win, text=" ", font=("Courier 22 bold"))#.grid(column=5, row=10)
label1.pack()

label2= Label(win, text=" ", font=("Courier 22 bold"))
label2.pack()


#Create a Button to validate Entry Widget
ttk.Button(win, text= "Answer",width= 20, command= resp_bot).pack(pady=20)

ttk.Button(win, text="Clear",width= 20, command=clear_bot).pack(pady=5)

ttk.Button(win, text="Init/Reset",width= 20, command=rand_reset).pack(pady=5)

win.mainloop()



