# Tag 14 – Higher Lower Spiel 📊

Ein terminalbasiertes Spiel, bei dem der Benutzer zwei Persönlichkeiten vergleicht und rät, wer mehr Instagram-Follower hat.

## Funktionen

- Zufällige Auswahl von Persönlichkeiten mit Name, Beruf und Land
- Der Spieler rät, wer mehr Follower hat: A oder B
- Punktestand erhöht sich bei korrekter Antwort
- B wird zur neuen A in der nächsten Runde
- Spiel läuft weiter bis zu einem Fehler
- Anzeige des Endpunktestands
- Klar strukturierte Ausgabe mit ASCII-Art

## Spielablauf

- Zwei zufällige Einträge aus den Daten werden ausgewählt.
- Der Spieler sieht die Namen, Beschreibungen und Herkunftsländer.
- Der Spieler entscheidet, wer mehr Follower hat.
- Bei richtiger Wahl gibt es einen Punkt und das Spiel geht weiter.
- Bei falscher Wahl endet das Spiel mit Endpunktestand.

## Beispielausgabe
```
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Compare A: Beyoncé a Musician, from United States

 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Compare B: David Beckham a Footballer, from United Kingdom
Who has more followers? Type 'A' or 'B':
```


## Gelernt

- Arbeiten mit Dictionaries und verschachtelten Datensätzen
- Zufallsauswahl und Validierung
- Modulare Funktionen mit Übergabeparametern
- Spielsteuerung mit Schleifen und Status-Tracking
- Verwaltung von Punktestand und Spiellogik
- Benutzereingabe und strukturierte Konsolenausgabe
