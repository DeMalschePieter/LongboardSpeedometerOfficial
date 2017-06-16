from flask import Flask, render_template
from DbClass import DbClass
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sessions')
def sessions():
    db = DbClass()
    deelsessies = db.getDeelSessies()
    db.getDataFromDatabaseMetVoorwaarde()
    return render_template('sessions.html',deelsessies= deelsessies)

@app.route('/add_session')
def add_session():
    db = DbClass()
    db.setSessie(str(datetime.now()),"0000-00-00 00:00:00",0,0,0,1,1) #laatst één wil zeggen; sessie gestart, in de code van de hall sensor kunnen er nu deelsessies gemaakt worden
    return render_template('add_session.html')

@app.route('/stop_session')
def stop_session():
    totalDistance = 0
    max_speed = 0
    average_speed = 0
    teller = 0

    db = DbClass()
    laatstRegel = db.getLaatsteRegelSessies()
    db2 = DbClass()
    deelsessies = db2.getBepaaldeDeelsessies(laatstRegel[0][0])
    for deelsessie in deelsessies:
        totalDistance += float(deelsessie[2])
        teller += 1
        if float(deelsessie[3]) > max_speed:
            max_speed = float(deelsessie[3])
    average_speed = totalDistance/teller
    print(totalDistance)
    print(max_speed)
    print(average_speed)





    db.UpdateSession(laatstRegel[0][0],datetime.now(),totalDistance,max_speed,average_speed,1,0) #laatst één wil zeggen; sessie gestart, in de code van de hall sensor kunnen er nu deelsessies gemaakt worden
    return render_template('gestopte_sessie_pagina.html')




if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    host = "169.254.10.1"
    app.run(host=host, port=port, debug=True)
