Mit TestBuilder lassen sich beliebig viele verschiedene Arbeitsblätter, Test, Klausuren usw. für fast alle Standardaufgaben der Oberstufe und zum Teil der Mittelstufe (in Arbeit) sowie deren Lösung (Erwartungshorizont) im Fach Mathematik erzeugen. Langfristig soll sie für alle Klassenstufen und Fächer weiterentwickelt werden.
So soll die Transformation der Schule weg von der Klassen- hin zur Lernstruktur ermöglicht werden, wie es bereits einige ausgezeichnete Schulen, zum Beispiel die Alemannenschule Wutöschingen  (https://asw-wutoeschingen.de), gemacht haben. 

Um TestBuilder zu nutzen, benötigen Sie:
1. [Python](https://www.python.org/downloads/)
2. [MiKTeX](https://miktex.org/download)
3. [Perl](https://strawberryperl.com/)
4. [PyCharm Community Edition](https://www.jetbrains.com/de-de/pycharm/download) (ist weiter unten auf der Webseite)

**Installieren Sie die Software in der gegebenen Reihenfolge. Dann müssen Sie, wenn Sie PyCharm gestartet haben:**
1. Oben rechts auf "Get from VCS" gehen
2. Dort dann diesen Link `https://github.com/HerrjeAlf/TestBuilder.git` bei URL eingeben
3. Wenn sich das Projekt geöffnet hat, müssen Sie nur noch die benötigten Python Packages installieren. 
Dazu im Terminal von PyCharm (Alt+F12) `pip install -r requirements.txt` eingeben.

*Jetzt sollte alles funktionieren.*

***Hinweise:***

Im Projektordner "pdf" finden Sie eine Datei "Übersicht der Aufgaben", in der alle Aufgaben gelistet sind und wie diese 
aufgerufen werden. Außerdem sind alle Parameter und Teilaufgaben erläutert. Wenn Sie etwas erzeugen (Arbeitsblatt, Test usw.) 
finden Sie die zugehörige pdf-Datei auch im Ordner "pdf". 
Die Übersicht wird regelmäßig mit den neu fertig gestellten Aufgaben ergänzt. 

Wenn Sie das erste Mal z.B. einen Test erzeugen, werden Sie aufgefordert für MiKTeX einige Pakete zu installieren.
Sie können die voreingestellte Quelle "Beliebiges Repository im Internet" verwenden.

Die Kopfzeile bei den Vorlagen der Klausur, dem Vorabi und der mündl. Prüfung können Sie ändern, indem Sie im Ordner "img" die Datei kopfzeile.png mit einer Bilddatei der Kopfzeile ihrer Schule ersetzen.

Sollten Sie Bugs oder fehlerhafte Rechnungen bzw. Ergebnisse finden, würden wir uns über eine Rückmeldung freuen.
