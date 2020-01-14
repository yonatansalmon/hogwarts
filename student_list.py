import time
import random

magic_skills = ["Alchemy", "Animation", "Conjuror", "Disintegration", "Elemental", "Healing", "Illusion", "Immortality", "Invisibility", "Invulnerability", "Necromancer", "Omnipresent", "Omniscient", "Poison", "Possession", "Self-detonation", "Summoning", "Water breathing"]

courses = ["Alchemy basics", "Alchemy advanced", "Magic for day-to-day life", "Magic for medical professionals", "Dating with magic",]



students = [
    {
        "id": 1,
        "first_name": "Yonatan",
        "last_name": "Salmon",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": random.choices(magic_skills, k=5),
        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest": random.choices(courses, k=2),
    },
        {"id": 2,
        "first_name": "Mark",
        "last_name": "Something",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": random.choices(magic_skills, k=5),
        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest": random.choices(courses, k=2),
    },
    {
        "id": 3,
        "first_name": "Jhons",
        "last_name": "Mosokfn",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": random.choices(magic_skills, k=5),
        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest":random.choices(courses, k=2),
    },
    {"id": 4,
        "first_name": "Susan",
        "last_name": "Salmafafafafon",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": random.choices(magic_skills, k=5),
        "desired_skills": random.choices(magic_skills, k=2),
        "course_interest":random.choices(courses, k=2),
     },

    {"id": 5,
     "first_name": "uguian",
     "last_name": "yfyuSalmafafafafon",
     "creation_time": time.ctime(),
     "last_update": time.ctime(),
     "existing_skills":random.choices(magic_skills, k=5),
     "desired_skills": random.choices(magic_skills, k=2),
     "course_interest": random.choices(courses, k=2),
     },
]