'''Creates a webpage with some of my favorite movies'''

import media
import fresh_tomatoes

TITLE = 'Adam\'s Movie Time'

the_game = media.Movie('The Game',
                       'Wealthy San Francisco financier Nicholas Van Orton '
                       'gets a strange birthday present from wayward '
                       'brother Conrad: a live-action game that consumes '
                       'his life.',
                       'https://upload.wikimedia.org/wikipedia/en/5/53/The'
                       'Game_poster323.jpg',
                       'https://www.youtube.com/watch?v=0kqQNBR09Rc',
                       '1997')

boyz_n_the_hood = media.Movie('Boys n the Hood',
                              'Follows the lives of three young males '
                              'living in the Crenshaw ghetto of Los '
                              'Angeles, dissecting questions of race, '
                              'relationships, violence and future prospects.',
                              'https://upload.wikimedia.org/wikipedia/en/c/'
                              'c3/Boyz_n_the_hood_poster.jpg',
                              'https://www.youtube.com/watch?v=MVDl7k_xkpo',
                              '1991')

das_boot = media.Movie('Das Boot',
                       'The journey of a German uboat and it\'s crew during '
                       'World War 2.',
                       'https://upload.wikimedia.org/wikipedia/en/a/a3/Das_'
                       'boot_ver1.jpg',
                       'https://www.youtube.com/watch?v=fQ15Q5XkkxU',
                       '1981')


gangs_of_new_york = media.Movie('Gangs of New York',
                                'In 1863, Amsterdam Vallon returns to the '
                                'Five Points area of New York City seeking '
                                'revenge against Bill the Butcher, his'
                                'father\'s killer.',
                                'https://upload.wikimedia.org/wikipedia/en/'
                                'a/ae/Gangs_of_New_York_Poster.jpg',
                                'https://www.youtube.com/watch?v=1_CDJiYux1A',
                                '2002')

goodfellas = media.Movie('Goodfellas',
                         'Henry Hill and his friends work their way up '
                         'through the mob hierarchy.',
                         'https://upload.wikimedia.org/wikipedia/en/7/7b/'
                         'Goodfellas.jpg',
                         'https://www.youtube.com/watch?v=qo5jJpHtI1Y',
                         '1990')

fury = media.Movie('Fury',
                   'April, 1945. As the Allies make their final push in '
                   'the European Theatre, a battle-hardened Army sergeant '
                   'named Wardaddy commands a Sherman tank and his '
                   'five-man crew on a deadly mission behind enemy lines. '
                   'Outnumbered, out-gunned, and with a rookie soldier '
                   'thrust into their platoon, Wardaddy and his men face '
                   'overwhelming odds in their heroic attempts to strike '
                   'at the heart of Nazi Germany.',
                   'https://upload.wikimedia.org/wikipedia/en/1/17/Fury_'
                   '2014_poster.jpg',
                   'https://www.youtube.com/watch?v=-OGvZoIrXpg',
                   '2014')

movies = [the_game,
          boyz_n_the_hood,
          das_boot,
          gangs_of_new_york,
          goodfellas,
          fury]

fresh_tomatoes.open_movies_page(movies, TITLE)
