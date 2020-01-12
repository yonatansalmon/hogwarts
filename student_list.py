import time
import random

magic_skills = ["Alchemy", "Animation", "Conjuror", "Disintegration", "Elemental", "Healing", "Illusion", "Immortality", "Invisibility", "Invulnerability", "Necromancer", "Omnipresent", "Omniscient", "Poison", "Possession", "Self-detonation", "Summoning", "Water breathing"]
enum_skills = [(i,j) for i,j in enumerate(magic_skills)]
existing_skills = random.choices(enum_skills, k=5)
existing_skillsToStr = ' '.join([str(elem) for elem in existing_skills])
desired_skills = random.choices(enum_skills, k=2)
desired_skillsToStr = ' '.join([str(elem) for elem in desired_skills])

courses = ["Alchemy basics", "Alchemy advanced", "Magic for day-to-day life", "Magic for medical professionals", "Dating with magic",]
course_interest = random.choices(courses, k=2)


students = [
    {
        "id": 1,
        "first_name": "Yonatan",
        "last_name": "Salmon",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": existing_skillsToStr,
        "desired_skills": desired_skillsToStr,
        "course_interest": course_interest,
    },
        {"id": 2,
        "first_name": "Mark",
        "last_name": "Something",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": existing_skillsToStr,
        "desired_skills": desired_skillsToStr,
        "course_interest":course_interest,
    },
    {
        "id": 3,
        "first_name": "Jhons",
        "last_name": "Mosokfn",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": existing_skillsToStr,
        "desired_skills": desired_skillsToStr,
        "course_interest":course_interest,
    },
    {"id": 4,
        "first_name": "Susan",
        "last_name": "Salmafafafafon",
        "creation_time": time.ctime(),
        "last_update": time.ctime(),
        "existing_skills": existing_skillsToStr,
        "desired_skills": desired_skillsToStr,
        "course_interest":course_interest,
     },

    {"id": 5,
     "first_name": "uguian",
     "last_name": "yfyuSalmafafafafon",
     "creation_time": time.ctime(),
     "last_update": time.ctime(),
     "existing_skills": existing_skillsToStr,
     "desired_skills": desired_skillsToStr,
     "course_interest": course_interest,
     },
]