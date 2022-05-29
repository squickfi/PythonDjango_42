import psycopg2
from django.http import HttpResponse
from django.shortcuts import render


def init(request):
    try:
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432',
        )
        with connection.cursor() as curs:
            try:
                curs = connection.cursor()
                curs.execute("""
                    CREATE TABLE IF NOT EXISTS ex02_movies(
                        title VARCHAR(64) UNIQUE NOT NULL,
                        episode_nb INT PRIMARY KEY,
                        opening_crawl TEXT,
                        director VARCHAR(32) NOT NULL,
                        producer VARCHAR(128) NOT NULL,
                        release_date DATE NOT NULL
                        );
                    """)
            except Exception as e:
                connection.close()
                return e
        connection.commit()
        connection.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def populate(request):
    movies = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    insert = '''
    INSERT INTO ex02_movies
        (
            episode_nb,
            title,
            director,
            producer,
            release_date
        )
        VALUES
        (
            %s, %s, %s, %s, %s
        );
    '''

    result = []

    try:
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432',
        )
        try:
            for movie in movies:
                with connection.cursor() as curs:
                    try:
                        curs.execute(insert, [
                            movie['episode_nb'],
                            movie['title'],
                            movie['director'],
                            movie['producer'],
                            movie['release_date'],
                        ])
                        result.append('OK<br>')
                    except Exception as e:
                        result.append(e.__str__() + '<br>')
                connection.commit()
        except psycopg2.DatabaseError as e:
            connection.rollback()
            result.append(e.__str__() + '<br>')
        return HttpResponse(result)
    except Exception as e:
        return HttpResponse(e)


def display(request):
    try:
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432',
        )
        with connection.cursor() as curs:
            curs.execute('SELECT * FROM ex02_movies;')
            movies = curs.fetchall()
        return render(request, 'ex02/display.html', {"movies": movies})
    except Exception as e:
        return HttpResponse('No data available')
