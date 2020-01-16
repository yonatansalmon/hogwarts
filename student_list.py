import time
import random

magic_skills = ["Alchemy", "Animation", "Conjuror", "Disintegration", "Elemental", "Healing", "Illusion", "Immortality",
                "Invisibility", "Invulnerability", "Necromancer", "Omnipresent", "Omniscient", "Poison", "Possession",
                "Self-detonation", "Summoning", "Water-breathing"]
level = [1, 2, 3, 4, 5]

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

months =["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

courses = ["Alchemy basics", "Alchemy advanced", "Magic for day-to-day life", "Magic for medical professionals",
           "Dating with magic", ]

students = [
    {
        "id": 1,
        "first_name": "Harry",
        "last_name": "Potter",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": [{"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            ],

        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest": random.choices(courses, k=2),
    },
    {"id": 2,
     "first_name": "Hermionie",
     "last_name": "Granger",
     "creation_time": time.ctime(),
     "last_update": time.ctime(),
     "existing_skills": [{"skill": random.choice(magic_skills),
                          "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         ],
     "level": random.choice(level),
     "desired_skills": random.choices(magic_skills, k=2),
     "course_interest": random.choices(courses, k=2),
     },
    {
        "id": 3,
        "first_name": "Ron",
        "last_name": "Weasley",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": [{"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                            ],
        "level": random.choice(level),
        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest": random.choices(courses, k=2),
    },
    {"id": 4,
     "first_name": "Lord",
     "last_name": "Voldemort",
     "creation_time": time.ctime(),
     "last_update": time.ctime(),
     "existing_skills": [{"skill": random.choice(magic_skills),
                          "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         ],
     "level": random.choice(level),
     "desired_skills": random.choices(magic_skills, k=2),
     "course_interest": random.choices(courses, k=2),
     },

    {"id": 5,
     "first_name": "Professor",
     "last_name": "Snape",
     "creation_time": time.ctime(),
     "last_update": time.ctime(),
     "existing_skills": [{"skill": random.choice(magic_skills),
                          "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         {"skill": random.choice(magic_skills),
                             "level": random.choice(level)},
                         ],
     "level": random.choice(level),
     "desired_skills": random.choices(magic_skills, k=2),
     "course_interest": random.choices(courses, k=2),
     },
]



labels = [
    'Alchemy', 'Animation', 'Conjuror', 'Disintegration',
    'Elemental', 'Healing', 'Illusion', 'Immortality',
    'Invisibility', 'Invulnerability', 'Necromancer', 'Omnipresent',
    "Omniscient", "Poison", "Possession", "Self-detonation", "Summoning",
    "Water breathing"]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#8B0000",
    "#7FFF00", "#6495ED", "#00008B", "	#A9A9A9",
    "#8B008B", "#FF1493"
]
