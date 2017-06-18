from flask import Flask, render_template
from DbClass import DbClass
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def index():
    total_time = datetime.now() - datetime.now()
    teller = 0
    time = 0
    total_distance = 0
    max_speed = 0
    average_speed = 0


    db = DbClass()
    sessies = db.getSessies()
    for sessie in sessies:
        teller += 1
        time = sessie[2]-sessie[1]
        total_time = total_time + time
        total_distance += sessie[3]
        average_speed += sessie[5]
        if sessie[4] > max_speed:
            max_speed = sessie[4]

    total_distance = total_distance / 1000
    average_speed = average_speed / teller


    return render_template('index.html', total_time = total_time, total_distance = round(total_distance,2), max_speed = round(max_speed,1), average_speed = round(average_speed,1))

@app.route('/sessions')
def sessions():
    db = DbClass()
    sessions = db.getSessies()
    return render_template('sessions.html',sessions= sessions)

@app.route('/add_session')
def add_session():
    teller = 0
    max_speed = 0
    distance = 0
    time = "00:00:00"
    avg = 0

    db = DbClass()
    laatsteRegel = db.getLaatsteRegelSessies()

    if laatsteRegel[0][7]  == 0:
        db = DbClass()
        db.setSessie(str(datetime.now()),"0000-00-00 00:00:00",0,0,0,1,1) #laatst één wil zeggen; sessie gestart, in de code van de hall sensor kunnen er nu deelsessies gemaakt worden

        return render_template('add_session.html')
    else:
        db = DbClass()
        laatsteRegel = db.getLaatsteRegelSessies()
        db = DbClass()
        deelsessies = db.getBepaaldeDeelsessies(laatsteRegel[0][0])
        for deelsessie in deelsessies:
            teller += 1
            distance += deelsessie[2]
            # time += deelsessie[1]
            if deelsessie[3] > max_speed:
                max_speed = deelsessie[3]

        avg = distance * 3.6 / teller
        distance = distance / 1000

        time = str(datetime.now() - laatsteRegel[0][1])
        time = time[0:7]





        db = DbClass()
        sessions = db.getLaatste5RegelsDeelsessies(laatsteRegel[0][0])
        return render_template('add_session.html', sessions = sessions, max_speed = round(max_speed,1), distance = round(distance,2), avg = round(avg,1), time = time)


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
    average_speed = (totalDistance * 3.6) / teller
    print(totalDistance)
    print(max_speed)
    print(average_speed)

    db.UpdateSession(laatstRegel[0][0],datetime.now(),totalDistance,max_speed,average_speed,1,0) #laatst één wil zeggen; sessie gestart, in de code van de hall sensor kunnen er nu deelsessies gemaakt worden

    sessie_is_bezig = 0

    return render_template('gestopte_sessie_pagina.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    host = "169.254.10.1"
    app.run(host=host, port=port, debug=True)
