import hangman.game, mysql.connector,webbrowser
word_save=[]
status_list=[]
#asking the name form the user
name=str(input("Enter your name : "))

#Menu of the game
print("""------------------HANGMAN'S GAME-------------------------
START---->P
END------>X """)
print()


#Start the game or exit the game
opt=input("Enter option : ")

#looping the opition to enter the game
#Adding the package module an function to run the game
while opt=="P" or opt=="p":
    word_save, status_list =hangman.game.Mygame(word_save,status_list)
    print()
    opt=input("Press P to enter the next level or Press X to exit the game : ")
print()

print("Thank you for playing HANGMAN'S GAME")    

# Initializing the database
data_base={'host':'localhost',
           'database':'hangman',
           'user':'root',
           'password':''}

db=mysql.connector.connect(**data_base)
cursor=db.cursor()
sql=f"INSERT INTO game VALUES(%s,%s,%s,%s)"


for i in range(len(word_save)):
    values=(name,word_save[i],(len(word_save[i])),status_list[i])
    cursor.execute(sql,values)
    db.commit()

cursor.execute(f"SELECT * FROM game WHERE Players_Name = {'name'}")
data=cursor.fetchall()
print(data)
   

html_c= f"<html> <head> </head>  <h1>""</h1> <body> </body> </html>"

with open("index.html", "w")as html_file:
    html_file.write(str(html_c))
    print("Html file created sucessfully !!")

