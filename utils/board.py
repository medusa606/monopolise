class Board():
    spaces = dict
    groups = []
    site_cost = []
    rents = dict
    special = []
    owner = []
    no_houses = []
    free_parking: int = 0
    max_len: int

    def __init__(self):
        self.spaces = {1: 'Go',
                        2: 'Old Kent Road',
                        3: 'Community Chest',
                        4: 'Whitechapel Road',
                        5: 'Income Tax',
                        6: 'Kings Cross Station',
                        7: 'The Angel Islington',
                        8: 'Chance',
                        9: 'Euston Road',
                        10: 'Pentonville Road',
                        11: 'Jail / Just Visiting',
                        12: 'Pall Mall',
                        13: 'Electric Company',
                        14: 'Whitehall',
                        15: 'Northumberland Avenue',
                        16: 'Marylebone Station',
                        17: 'Bow Street',
                        18: 'Community Chest',
                        19: 'Marlborough Street',
                        20: 'Vine Street',
                        21: 'Free Parking',
                        22: 'Strand',
                        23: 'Chance',
                        24: 'Fleet Street',
                        25: 'Trafalgar Square',
                        26: 'Fenchurch St. Station',
                        27: 'Leicester Square',
                        28: 'Coventry Street',
                        29: 'Water Works',
                        30: 'Piccadilly',
                        31: 'Go To Jail',
                        32: 'Regent Street',
                        33: 'Oxford Street',
                        34: 'Community Chest',
                        35: 'Bond Street',
                        36: 'Liverpool St. Station',
                        37: 'Chance',
                        38: 'Park Lane',
                        39: 'Super Tax',
                        40: 'Mayfair'}
        self.groups = {1:        'none',
        2: 'brown',
        3: 'none',
        4: 'brown',
        5: 'none',
        6: 'station',
        7: 'blue',
        8: 'none',
        9: 'blue',
        10: 'blue',
        11: 'none',
        12: 'pink',
        13: 'utility',
        14: 'pink',
        15: 'pink',
        16: 'station',
        17: 'orange',
        18: 'none',
        19: 'orange',
        20: 'orange',
        21: 'none',
        22: 'red',
        23: 'none',
        24: 'red',
        25: 'red',
        26: 'station',
        27: 'yellow',
        28: 'yellow',
        29: 'utility',
        30: 'yellow',
        31: 'none',
        32: 'green',
        33: 'green',
        34: 'none',
        35: 'green',
        36: 'station',
        37: 'none',
        38: 'purple',
        39: 'none',
        40: 'purple', }
        self.site_cost = {1 : 0,
                            2 : 60 ,
                            3 : 0,
                            4 : 60 ,
                            5 : 0,
                            6 : 200,
                            7 : 100,
                            8 : 0,
                            9 : 100,
                            10: 120,
                            11: 0,
                            12: 140,
                            13: 150,
                            14: 140,
                            15: 160,
                            16: 200,
                            17: 180,
                            18: 0,
                            19: 180,
                            20: 200,
                            21: 0,
                            22: 220,
                            23: 0,
                            24: 220,
                            25: 240,
                            26: 200,
                            27: 260,
                            28: 260,
                            29: 150,
                            30: 280,
                            31: 0,
                            32: 300,
                            33: 300,
                            34: 0,
                            35: 320,
                            36: 200,
                            37: 0,
                            38: 350,
                            39: 0,
                            40: 400
                            }
        self.rents =  {      2 : [2,     10	,      30	,   90		,160	,	250],
                             4 : [4,     20	,      60	,   180		,320	,	450],
                             7 : [6,     30	,      90	,   270		,400	,	550],
                             9 : [6,     30	,      90	,   270		,400	,	550],
                            10 : [8,     40	,      100, 	300		,450	,	600],
                            11 : [10,    50	,      150, 	450		,625	,	750],
                            14 : [10,    50	,      150, 	450		,625	,	750],
                            15 : [12,    60	,      180, 	500		,700	,	900],
                            17 : [14,    70	,      200, 	550		,750	,	950],
                            19 : [14,    70	,      200, 	550		,750	,	950],
                            20 : [16,    80	,      220, 	600		,800	,	1000],
                            22 : [18,    90	,      250, 	700		,875	,	1050],
                            24 : [18,    90	,      250, 	700		,875	,	1050],
                            25 : [20,    100,      300, 	750		,925	,	1100],
                            27 : [22,    110,      330, 	800		,975	,	1150],
                            28 : [22,    110,      330, 	800		,975	,	1150],
                            30 : [22,    120,      360, 	850		,1025   ,	1200],
                            32 : [26,    130,      390, 	900		,1100   ,	1275],
                            33 : [26,    130,      390, 	900		,1100   ,	1275],
                            35 : [28,    150,      450, 	1000	,1200   ,	1400],
                            38 : [35,    175,      500, 	1100	,1300   ,	1500],
                            40 : [50,    200,      600, 	1400	,1700   ,	2000]}
        self.special = [1,3,5,8,11,18,21,23,31,34,37,39]
        self.owner = {	1 :		  'none',
                 2 :      'none',
                 3 :      'none',
                 4 :      'none',
                 5 :      'none',
                 6 :      'none',
                 7 :      'none',
                 8 :      'none',
                 9 :      'none',
                 10:      'none',
                 11:      'none',
                 12:      'none',
                 13:      'none',
                 14:      'none',
                 15:      'none',
                 16:      'none',
                 17:      'none',
                 18:      'none',
                 19:      'none',
                 20:      'none',
                 21:      'none',
                 22:      'none',
                 23:      'none',
                 24:      'none',
                 25:      'none',
                 26:      'none',
                 27:      'none',
                 28:      'none',
                 29:      'none',
                 30:      'none',
                 31:      'none',
                 32:      'none',
                 33:      'none',
                 34:      'none',
                 35:      'none',
                 36:      'none',
                 37:      'none',
                 38:      'none',
                 39:      'none',
                 40:      'none'}
        self.max_len = 40   #  max([len(x) for x in self.spaces])
        self.no_houses = {	 1 :	  0,
                 2 :      0,
                 3 :      0,
                 4 :      0,
                 5 :      0,
                 6 :      0,
                 7 :      0,
                 8 :      0,
                 9 :      0,
                 10:      0,
                 11:      0,
                 12:      0,
                 13:      0,
                 14:      0,
                 15:      0,
                 16:      0,
                 17:      0,
                 18:      0,
                 19:      0,
                 20:      0,
                 21:      0,
                 22:      0,
                 23:      0,
                 24:      0,
                 25:      0,
                 26:      0,
                 27:      0,
                 28:      0,
                 29:      0,
                 30:      0,
                 31:      0,
                 32:      0,
                 33:      0,
                 34:      0,
                 35:      0,
                 36:      0,
                 37:      0,
                 38:      0,
                 39:      0,
                 40:      0}

# self.spaces = ['Go',
#                        'Old Kent Road',
#                        'Community Chest',
#                        'Whitechapel Road',
#                        'Income Tax',
#                        'Kings Cross Station',
#                        'The Angel Islington',
#                        'Chance',
#                        'Euston Road',
#                        'Pentonville Road',
#                        'Jail / Just Visiting',
#                        'Pall Mall',
#                        'Electric Company',
#                        'Whitehall',
#                        'Northumberland Avenue',
#                        'Marylebone Station',
#                        'Bow Street',
#                        'Community Chest',
#                        'Marlborough Street',
#                        'Vine Street',
#                        'Free Parking',
#                        'Strand',
#                        'Chance',
#                        'Fleet Street',
#                        'Trafalgar Square',
#                        'Fenchurch St. Station',
#                        'Leicester Square',
#                        'Coventry Street',
#                        'Water Works',
#                        'Piccadilly',
#                        'Go To Jail',
#                        'Regent Street',
#                        'Oxford Street',
#                        'Community Chest',
#                        'Bond Street',
#                        'Liverpool St. Station',
#                        'Chance',
#                        'Park Lane',
#                        'Super Tax',
#                        'Mayfair', ]