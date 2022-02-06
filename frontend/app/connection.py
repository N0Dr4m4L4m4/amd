from configparser import ConfigParser
import psycopg2

class database():
    conn = None
    cur = None

    def __init__(self):
        params = self.config()
        self.conn = psycopg2.connect(**params)
        self.cur = self.conn.cursor()

    def config(self,filename='database.ini', section='postgresql'):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
    
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            return None
        return db

    def addFilm(self, title, release, genre, minAge, duration, seriesName, episodeNr=None, seasonNr=None):
        if episodeNr == '' or seasonNr == '':
            episodeNr = 1
            seasonNr = None

        self.cur.callproc('insert_video', (title,release,genre,minAge,duration,episodeNr,seasonNr,seriesName,))
        self.conn.commit()
        return self.cur.fetchall()

    def addFilmRelatedPerson(self, title, release, surname, forname, role):
        self.cur.callproc('edit_video_role', (title,release,surname,forname,role,))
        self.conn.commit()
        return self.cur.fetchall()

    def addPerson(self, surname, forname, sex, dateOfBirth):
        self.cur.callproc('insert_person', (surname,forname,dateOfBirth,sex,))
        self.conn.commit()
        return self.cur.fetchall()

    def getCrew(self):
        self.cur.callproc('show_all_persons')
        return self.cur.fetchall()

    def getRating(self):
        self.cur.callproc('show_all_ratings')
        return self.cur.fetchall()

    def getSuggestion(self,name):
        self.cur.callproc('suggestion',(name,))
        return self.cur.fetchall()

    def getAllFilms(self):
        self.cur.callproc('show_all_videos')
        return self.cur.fetchall()

    def getPersonInfo(self, forname, surname):
        self.cur.callproc('show_person',(forname, surname, ))
        return self.cur.fetchall()

    def getFilmInfo(self, title, year):
        self.cur.callproc('show_film_attributes',(title,year))
        return self.cur.fetchall()

    def getFilmRelatedPerson(self, title, year):
        self.cur.callproc('show_to_film_related_persons',(title,year))
        return self.cur.fetchall()

    def getUserFilmRate(self, title, year, name):
        self.cur.callproc('show_film_rating',(title,year,name,))
        return self.cur.fetchall()

    def getAllEpisodes(self, name, season):
        self.cur.callproc('show_episodes',(name,season,))
        return self.cur.fetchall()

    def changeUsername(self, oldUsername,newUsername):
        self.cur.callproc('change_username',(oldUsername,newUsername,))
        self.conn.commit()
        return self.cur.fetchall()

    def changeRating(self, title, release, username, rating):
        self.cur.callproc('edit_rating',(title, release, username, rating,))
        self.conn.commit()
        return self.cur.fetchall()

    def changeFilmAttributes(self,oldTitle, oldRelease, title, release, genre, age, duration, episode, season, seriesName):
        self.cur.callproc('update_video',(oldTitle, oldRelease, title, release, genre, age, duration, episode, season, seriesName,))
        self.conn.commit()
        return self.cur.fetchall()

    def changePersonAttributes(self, oldSurname,oldForname, surname,forname,dateOfBirth,sex):
        self.cur.callproc('update_person',(oldSurname,oldForname,surname,forname,dateOfBirth,sex,))
        self.conn.commit()
        return self.cur.fetchall()

    def getFilmSeason(self, name):
        self.cur.callproc('show_films_seasons',(name,))
        return self.cur.fetchall()

    def getAllNotFilmRelatedPersons(self, title, year):
        self.cur.callproc('show_not_to_film_related_persons', (title,year,))
        return self.cur.fetchall()

    def deleteFilm(self, title, year):
        self.cur.callproc('del_video',(title,year,))
        self.conn.commit()
        return self.cur.fetchall()

    def deleteRole(self, title, year, surname, forname):
        self.cur.callproc('del_video_role',(title, year, surname, forname))
        self.conn.commit()
        return self.cur.fetchall()

    def deletePerson(self, surname, forname):
        self.cur.callproc('del_person',(surname, forname))
        self.conn.commit()
        return self.cur.fetchall()

    def disconnect(self):
            self.conn.close()
            self.cur.close()

    def login(self,name):
        self.cur.callproc('check_user', (name,))
        return self.cur.fetchone()[0]
