# deploy app to Heroku
## polecenia wydajemy z terminala z wnętrza naszego venv

1. https://signup.heroku.com/ - zakładamy konto (Uwaga - wymagają karty kredytowej)
2. https://devcenter.heroku.com/articles/heroku-cli - instalujemy klienta do heroku
```shell
Konieczne pobranie 28,0 MB archiwów.
Po tej operacji zostanie dodatkowo użyte 0 B miejsca na dysku.
Pobieranie:1 https://cli-assets.heroku.com/apt ./ heroku 7.67.1-1 [28,0 MB]
Pobrano 28,0 MB w 3s (8 669 kB/s)    
Wybieranie wcześniej niewybranego pakietu heroku.
(Odczytywanie bazy danych ... 436476 plików i katalogów obecnie zainstalowanych.)
Przygotowywanie do rozpakowania pakietu .../heroku_7.67.1-1_amd64.deb ...
Rozpakowywanie pakietu heroku (7.67.1-1) ...
Konfigurowanie pakietu heroku (7.67.1-1) ...
heroku installed to /usr/bin/heroku
 ›   Warning: Our terms of service have changed: 
 ›   https://dashboard.heroku.com/terms-of-service
heroku/7.67.1 linux-x64 node-v14.19.0

```

3. Tworzymy nowy `venv` i tam wrzucamy aplikację i pliki
3. `heroku login` - z naszego venv w PyCharm
4. `heroku create <nasza_nazwa>` - nazwa opcjonalnie
5. `git init`
5. `git commit -a -m "Init files"` - dodajemy do naszego repo
5. `git push heroku master` - to wrzuca nam....
6. https://nasza_nazwa.herokuapp.com

## tutorial na podstawie: https://geekyhumans.com/how-to-deploy-flask-api-on-heroku/