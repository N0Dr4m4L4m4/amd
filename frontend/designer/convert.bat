echo off
pyuic5 manager.ui > ../app/userinterface/manager.py
pyuic5 welcome.ui > ../app/userinterface/welcome.py
pyuic5 filmManager.ui > ../app/userinterface/filmManager.py
pyuic5 rating.ui > ../app/userinterface/rating.py
pyuic5 addFilm.ui > ../app/userinterface/addFilm.py
pyuic5 addPerson.ui > ../app/userinterface/addPerson.py
pyuic5 changeFilm.ui > ../app/userinterface/changeFilm.py
pyuic5 changePerson.ui > ../app/userinterface/changePerson.py
pyuic5 crewManager.ui > ../app/userinterface/crewManager.py
pyuic5 rating.ui > ../app/userinterface/rating.py
pyuic5 recommandation.ui > ../app/userinterface/recommandation.py
pyuic5 userManagement.ui > ../app/userinterface/userManagement.py
pyuic5 searchForPerson.ui > ../app/userinterface/searchForPerson.py

echo done.
pause
exit
