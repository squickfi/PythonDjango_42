import ex04.forms
import psycopg2
from django.http import HttpResponse
from django.shortcuts import render, redirect


def init(request):
    try:
        with psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port='5432',
        ) as connection:
            with connection.cursor() as curs:
                curs.execute('''
                    CREATE TABLE IF NOT EXISTS ex04_movies(
                    title VARCHAR(64) UNIQUE NOT NULL,
                    episode_nb INT PRIMARY KEY,
                    opening_crawl TEXT,
                    director VARCHAR(32) NOT NULL,
                    producer VARCHAR(128) NOT NULL,
                    release_date DATE NOT NULL
                    );
                ''')
            connection.commit()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('OK')


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
    INSERT INTO ex04_movies
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
            port='5432'
        )
        with connection.cursor() as curs:
            curs.execute('SELECT * FROM ex04_movies;')
            movies = curs.fetchall()
        return render(request, 'ex04/display.html', {"movies": movies})
    except Exception as e:
        return HttpResponse('No data available')


def remove(request):

    conn = psycopg2.connect(
        dbname='djangotraining',
        user='djangouser',
        password='secret',
        host='127.0.0.1',
        port='5432'
    )
    if not request.method == 'POST':
        select = """
            SELECT * FROM ex04_movies;
            """
        try:
            with conn.cursor() as curs:
                curs.execute(select)
                movies = curs.fetchall()
            context = {'form': ex04.forms.RemovalForm(choices=(
                (movie[0], movie[0]) for movie in movies))}
            return render(request, 'ex04/remove.html', context)
        except Exception as e:
            print(e)
            return HttpResponse("No data available")
    else:
        select = """
                    SELECT title FROM ex04_movies;
                    """
        try:
            with conn.cursor() as curs:
                curs.execute(select)
                movies = curs.fetchall()
            choices = (
                (movie[0], movie[0]) for movie in movies)
        except Exception as e:
            print(e)
        data = ex04.forms.RemovalForm(choices, request.POST)
        delete = """
                    DELETE FROM ex04_movies WHERE title = %s
                    """
        if data.is_valid():
            try:
                with conn.cursor() as curs:
                    curs.execute(delete, [data.cleaned_data['film_to_remove']])
                conn.commit()
            except Exception as e:
                print(e)
        return redirect(request.path)
