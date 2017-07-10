import argparse
import pypyodbc as odbc
import os

parser = argparse.ArgumentParser()
#parser.add_argument('-i',help='The Way you choose. You can Pick an interactive or a Param way.',action='store_true')
#parser.add_argument('-page',type=str,default='ERROR404',help='Its the name of the page you want to see')
#parser.add_argument('-l',help='Shows you everry Entry in the Database',action='store_true')
#parser.add_argument('-c',type=str,help='Create a spezified Entry.')
#parser.add_argument('-d',type=str,help='Delete a spezified Entry.')
parser.add_argument('-uid',type=str,default='',help='Enter your Username.')
parser.add_argument('-pwd',type=str,default='',help='Enter your Password.')
args=parser.parse_args()
Pfad="C:\\Users\\Ericn\\Desktop\\Stundenplan"
HTML=""
database = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\Ericn\Desktop\Stundenplan\plan.mdb;'
    r'UID='+args.uid+';'
    r'PWD='+args.pwd+''
    )

def printHTML(Text):
    global HTML
    HTML = HTML + Text

def createHTML(studgang, gruppe):
    global Pfad
    global HTML
    conn = odbc.connect(database)
    cur = conn.cursor()
    #Generating the Head
    printHTML('<html lang="en"><head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"><meta charset="utf-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1"><title>'+studgang+' '+gruppe+'</title><!-- Bootstrap Core CSS --><link href="css/bootstrap.min.css" rel="stylesheet"><!-- Stundenplan CSS --><link href="css/plan.css" rel="stylesheet"></head>')
    #Generating the Body until the first <tbody>(Tag not included)
    printHTML('<body><br><div class = "text-center"><strong ><font size="3" face="Arial">'+studgang+' '+gruppe+'</font></strong></div><br><!-- Stundenplan, welcher nur auf normalen Desktops (md) und großen Desktops (lg) angezeigt wird --><div class="table-responsive, hidden-xs hidden-sm"><table class="table table-bordered table-condensed table-large"><thead>')
    printHTML('<tr><th><font size="2" face="Arial">Zeit</font></th><th width="150" align="center"><font size="2" face="Arial">Montag</font></th><th width="150" align="center"><font size="2" face="Arial">Dienstag</font></th><th width="150" align="center"><font size="2" face="Arial">Mittwoch</font></th><th width="150" align="center"><font size="2" face="Arial">Donnerstag</font></th><th width="150" align="center"><font size="2" face="Arial">Freitag</font></th><th width="150" align="center"><font size="2" face="Arial">Samstag</font></th></tr></thead><tbody>')

    list = []
    for uhrzeit in range(8, 23):
        printHTML('<tr><td><font size="2" face="Arial">{0}:00</font></td>'.format(uhrzeit))

        for wochentag in range (1,7):
            sql = "select v.Bezeichnung ,HOUR(b.Beginn) , HOUR(b.Ende),d.Titel, d.Name, v.Bemerkung, r.Bezeichnung from RaumZuBuchung rzb, Raum r, DozentZuBuchung dzb, Dozent d, VeranstaltungZuBuchung vzb, Veranstaltung v,Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'{0}' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'{1}' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID AND vzb.BuchungID = b.ID AND vzb.VeranstaltungID =v.ID AND HOUR(b.Beginn) LIKE'{2}' AND weekday(b.Beginn,2) LIKE'{3}' AND b.ID = dzb.BuchungID AND dzb.DozentID = d.ID AND b.ID = rzb.BuchungID AND rzb.RaumID = r.ID;".format(studgang, gruppe, uhrzeit,wochentag)
            cur.execute(sql)
            result = cur.fetchone()
            if result == None:
                status = False
                for listenelemet in list:
                    start,laenge,tag = listenelemet
                    if tag == wochentag:
                        for j in range(laenge):
                            h = j + start
                            if h == uhrzeit:
                                status = True
                if not status:
                    printHTML('<td>&nbsp;</td>')
            else:
                Beschreibung, BeginnStunde, EndeStunde, Titel, Profname, Bemerkung, Raumnummer = result
                if Bemerkung == None:
                    Bemerkung  = ""
                printHTML('<td rowspan="{0}" width="150" bgcolor="#f0f0f0" align="left"><font size="1" face="Arial">'.format(str(EndeStunde-BeginnStunde)))
                printHTML('{0}\n{1} {2} {3}\n{4}'.format(Beschreibung,Titel,Profname,Raumnummer,Bemerkung))
                printHTML('</font></td>')
                list.append((BeginnStunde,(EndeStunde-BeginnStunde),wochentag))
        printHTML('</tr>')
    printHTML('</tbody></table></div>')
    list.clear()
    printHTML('<!-- Stundenplan, welcher nur auf Smartphones (xs) und Tablets (sm) angezeigt wird --><div class="table-responsive, hidden-lg hidden-md">')
    StrTag = ""
    for wochentag in range(1,7):
        if (wochentag == 1):
             StrTag = "Montag"
        if (wochentag == 2):
            StrTag = "Dienstag"
        if (wochentag == 3):
            StrTag = "Mittwoch"
        if (wochentag == 4):
           StrTag = "Donnerstag"
        if (wochentag == 5):
           StrTag = "Freitag"
        if (wochentag == 6):
           StrTag = "Samstag"
        if (wochentag == 7):
          StrTag = "Sonntag"
        printHTML('<button class="accordion">{0}</button><div class="panel"><table class="table table-bordered table-condensed"><thead><tr><th><font size="2" face="Arial">Zeit</font></th><th width="150" align="center"><font size="2" face="Arial">Veranstaltungen</font></th></tr></thead><tbody>'.format(
                  StrTag))
        i = 7
        while i<22:
            i= i+1
            printHTML('<tr><td><font size="2" face="Arial">{0}:00</font></td>'.format(i))
            sql = "select v.Bezeichnung ,HOUR(b.Beginn) , HOUR(b.Ende),d.Titel, d.Name, v.Bemerkung, r.Bezeichnung from RaumZuBuchung rzb, Raum r, DozentZuBuchung dzb, Dozent d, VeranstaltungZuBuchung vzb, Veranstaltung v,Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'{0}' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'{1}' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID AND vzb.BuchungID = b.ID AND vzb.VeranstaltungID =v.ID AND HOUR(b.Beginn) LIKE'{2}' AND weekday(b.Beginn,2) LIKE'{3}' AND b.ID = dzb.BuchungID AND dzb.DozentID = d.ID AND b.ID = rzb.BuchungID AND rzb.RaumID = r.ID ORDER BY HOUR(b.Beginn);".format(
            studgang, gruppe, i, wochentag)
            cur.execute(sql)
            result = cur.fetchone()
            if result == None:
                printHTML('<td>&nbsp;</td>')
            else:
                Beschreibung, BeginnStunde, EndeStunde, Titel, Profname, Bemerkung, Raumnummer = result
                if Bemerkung == None:
                    Bemerkung=""
                printHTML('<td rowspan="{0}" width="150" bgcolor="#f0f0f0" align="left"><font size="1" face="Arial">{1}\n{2} {3} {4}\n{5}</font></td>'.format(str(EndeStunde-BeginnStunde),Beschreibung,Titel,Profname,Raumnummer,Bemerkung))

                for dummy in range(i+1,i+(EndeStunde-BeginnStunde)):
                    printHTML('<tr><td><font size="2" face="Arial">{0}:00</font></td></tr>'.format(dummy))
                i = i + (EndeStunde - BeginnStunde)-1
            printHTML('</tr>')
        printHTML('</tbody></table></div>')


    printHTML('</tbody></table></div></div><br>')

    printHTML('<!-- Responsive Stundenplan JavaScript --><script src="js/plan.js"></script><!-- jQuery Version 1.11.1 --><script src="js/jquery.js"></script><!-- Bootstrap Core JavaScript --><script src="js/bootstrap.min.js"></script></body></html>')
    cur.close()
    conn.close()
    plan = open(Pfad+'\\htm\\{0}\\{1}.htm'.format(studgang,gruppe),'w')
    plan.write(HTML)
    plan.close()
    HTML = ""

def list():
    conn = odbc.connect(database)
    cur = conn.cursor()
    datum="Date(2016, 9, 26, 0, 0)"
    studgang="WIB"
    gruppe="1.Sem_1.Gr"

    print('\n\nAnfragen für Inf.B. 4. Semester Gruppe1:\n')
    print('Studiengang:')
    sql = "select s.Kurzzeichen from Studiengang s WHERE s.Kurzzeichen LIKE'"+studgang+"';"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)
    print('\nGruppe:')
    sql = "select g.Bezeichnung from Studiengang s,gruppe g WHERE s.Kurzzeichen LIKE'"+studgang+"' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'"+gruppe+"';"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)
    print('\nBuchungsID:\n')
    sql = "select gzb.BuchungID from Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'"+studgang+"' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'"+gruppe+"' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID;"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)

    print('Buchungen:')
    sql ="select b.dauer, b.ID from Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'"+studgang+"' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'"+gruppe+"' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID;"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)

    print('Veranstaltungen:')
    sql = "select v.Bezeichnung from Veranstaltung v, VeranstaltungZuBuchung vzb, Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'{0}' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'{1}' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID AND vzb.BuchungID = b.ID AND vzb.VeranstaltungID =v.ID;".format(
        studgang, gruppe)
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        print(item)
    print("\n\n")
    print('Veranstaltungen für '+studgang+" "+gruppe+':')
    sql = "select v.Bezeichnung ,weekday(b.Beginn,2),HOUR(b.Beginn) , HOUR(b.Ende) from VeranstaltungZuBuchung vzb, Veranstaltung v,Buchung b, GruppeZuBuchung gzb,Studiengang s,Gruppe g WHERE s.Kurzzeichen LIKE'{0}' AND g.Studiengang =s.ID AND g.Bezeichnung LIKE'{1}' AND gzb.GruppeID = g.ID AND gzb.BuchungID = b.ID AND vzb.BuchungID = b.ID AND vzb.VeranstaltungID =v.ID;".format(
        studgang, gruppe)
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        Beschreibung,BeginnTag,BeginnStunde,EndeStunde = item
        StrTag = str(BeginnTag)
        if(BeginnTag==1):
            StrTag = "Montag"
        if (BeginnTag == 2):
            StrTag = "Diensntag"
        if (BeginnTag == 3):
            StrTag = "Mittwoch"
        if (BeginnTag == 4):
            StrTag = "Donnerstag"
        if (BeginnTag == 5):
            StrTag = "Freitag"
        if (BeginnTag == 6):
            StrTag = "Samstag"
        if (BeginnTag == 7):
            StrTag = "Sonntag"

        STRBeginn = str(BeginnStunde)
        STREnde = str(EndeStunde)
        print("Beschreibung: "+Beschreibung)
        print("Wochentag: "+StrTag)
        print("Länge: "+str(EndeStunde-BeginnStunde)+":00 Stunden")
        print("Beginn: "+STRBeginn+":00 Uhr")
        print("Ende: "+STREnde+":00 Uhr")
    cur.close()
    conn.close()

def wayChooser(args):
    conn = odbc.connect(database)
    cur = conn.cursor()
    sql="select sg.Kurzzeichen,g.Bezeichnung from Studiengang sg, gruppe g WHERE g.Studiengang = sg.ID"
    cur.execute(sql)
    result = cur.fetchall()
    for item in result:
        studgang,gruppe = item
        try:
            os.makedirs(Pfad+"\\htm\\{0}".format(studgang))
        except:
            pass
        createHTML(studgang,gruppe)

wayChooser(args)
exit()