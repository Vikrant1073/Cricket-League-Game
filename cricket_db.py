import sqlite3


mycurs = sqlite3.connect('cricket_db.db')  
curs = mycurs.cursor()


curs.execute('''CREATE TABLE IF NOT EXISTS match (player TEXT NOT NULL,scored INTEGER,faced INTEGER,fours INTEGER,sixes INTEGER,bowled INTEGER,maiden INTEGER,given INTEGER,wkts INTEGER,catches INTEGER,stumping INTEGER,ro INTEGER);''')




curs.execute('''CREATE TABLE IF NOT EXISTS stats (player PRIMARY KEY,matches INTEGER,runs INTEGER,hundreds INTEGER,fifties INTEGER,value INTEGER,ctg TEXT NOT NULL);''')



curs.execute('''CREATE TABLE IF NOT EXISTS teams (name TEXT NOT NULL,players TEXT NOT NULL,value INTEGER);''')




sql="select * from match"
curs.execute(sql)


result=curs.fetchall()
if(result):
    for i in result:
        
    
        print(i)
    opt=input("\n add more players details ? (Y/N) : ")
else:
    print("No any players data found ")

    opt=input("\n add players data (Y/N) :")

while(opt=='y' or opt=='Y'):
    
    row=[input("Player name :")]
    row.append(int(input("Score:")))
    row.append(int(input("Faced: ")))
    row.append(int(input("Fours: ")))
    row.append(int(input("Sixes: ")))
    row.append(int(input("Bowled: ")))
    row.append(int(input("Maiden: ")))
    row.append(int(input("Given: ")))
    row.append(int(input("Wkts: ")))
    row.append(int(input("Catches: ")))
    row.append(int(input("Stumping: ")))
    row.append(int(input("RO: ")))
    
    
    try:
        curs.execute("INSERT INTO match (player,scored, faced, fours,sixes,bowled,maiden,given,wkts,catches,stumping,ro) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        mycurs.commit()

        print("records added successfully match table.")
    except:    # except block to handle exceptions
        print("Error in operation.")
        mycurs.rollback()
   

        
   #ADDING DATA TO STATS TABLE FROM USER 
    print("player information for State table ")
    row.append(int(input("Total matches: ")))
    row.append(int(input("Total runs: ")))
    row.append(int(input("100s: ")))
    row.append(int(input("50s: ")))
    row.append(int(input("Value: ")))
    row.append(input("Category as (BAT,BWL,AR,WK): "))
    
    try:
    
        curs.execute("INSERT INTO stats (player,matches,runs, hundreds, fifties,value,ctg) VALUES (?,?,?,?,?,?,?)", #adding data to database
                          (row[0],row[12], row[13], row[14],row[15],row[16],row[17]))
        mycurs.commit()

        print("records added successfully for stats table.")
    except: 
        print("Error in operation.")
        mycurs.rollback()
        
    opt=input("adding more player ? (Y/N) : ")

   

upd=input("Update Names? (Y/N)")

while(upd=="Y" or upd=="y"):

    #name = list(input("Player name"))
    
    sql="UPDATE match SET player=? WHERE scored=?"
    curs.execute(sql,("Ravindra Jadeja",18))
    mycurs.commit()

    print("records updated successfully for stats table.")
    upd=input("Update Names? (Y/N)")

#sql="DELETE FROM teams"
#curs.execute(sql)
#mycurs.commit()


   
curs.close() #close database

    
    
    
    
    
    

    
    

    
    
    
    
    
 
                          
        

        
     
        
        
    
    
    
        

    
    
    
    
    

    
    
         
    
    
                          
        

    
    
        
        
        
    
    
        

    

