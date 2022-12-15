# deploy app to Heroku
## polecenia wydajemy z terminala z wnętrza naszego venv

1. https://signup.heroku.com/ - zakładamy konto
2. https://devcenter.heroku.com/articles/heroku-cli - instalujemy klienta do heroku
3. Tworzymy nowy `venv` i tam wrzucamy aplikację i pliki
3. `heroku login`
4. `heroku create <nasza_nazwa>` - nazwa opcjonalnie
5. `git push heroku master` - to wrzuca nam....
6. https://nasza_nazwa.herokuapp.com

## tutorial na podstawie: https://geekyhumans.com/how-to-deploy-flask-api-on-heroku/