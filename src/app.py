"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the soccer team and compete in inter-school tournaments",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "james@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice basketball and participate in local competitions",
        "schedule": "Wednesdays and Fridays, 3:00 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["luke@mergington.edu", "mason@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art techniques and create your own masterpieces",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Learn acting skills and perform in school plays",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["isabella@mergington.edu", "amelia@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 25,
        "participants": ["ethan@mergington.edu", "logan@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:00 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["harper@mergington.edu", "ella@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up")
    # Validate max participants not reached
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")
    # Validate email format
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email format")
    # Validate email domain
    if not email.endswith("@mergington.edu"):
        raise HTTPException(status_code=400, detail="Invalid email domain")
    # Validate email is not empty
    if not email:
        raise HTTPException(status_code=400, detail="Email cannot be empty")
    # Validate email is not too long
    if len(email) > 50:
        raise HTTPException(status_code=400, detail="Email is too long")
    # Validate email is not too short
    # if len(email) < 5:
    #     raise HTTPException(status_code=400, detail="Email is too short")
    # Validate email is not a duplicate
    for activity in activities.values():
        if email in activity["participants"]:
            raise HTTPException(status_code=400, detail="Email already signed up for another activity")
    # Validate email is not a teacher
    if email.startswith("teacher@"):
        raise HTTPException(status_code=400, detail="Email is a teacher email")
    # Validate email is not a staff
    if email.startswith("staff@"):
        raise HTTPException(status_code=400, detail="Email is a staff email")
    # Validate email is not a parent
    if email.startswith("parent@"):
        raise HTTPException(status_code=400, detail="Email is a parent email")
    # Validate email is not a student
    if email.startswith("student@"):
        raise HTTPException(status_code=400, detail="Email is a student email")
    # Validate email is not a alumni
    if email.startswith("alumni@"):
        raise HTTPException(status_code=400, detail="Email is a alumni email")
    # Validate email is not a guest
    if email.startswith("guest@"):
        raise HTTPException(status_code=400, detail="Email is a guest email")
    # Validate email is not a vendor
    if email.startswith("vendor@"):
        raise HTTPException(status_code=400, detail="Email is a vendor email")
    # Validate email is not a contractor
    if email.startswith("contractor@"):
        raise HTTPException(status_code=400, detail="Email is a contractor email")
    # Validate email is not a volunteer
    if email.startswith("volunteer@"):
        raise HTTPException(status_code=400, detail="Email is a volunteer email")           
    # Validate email is not a coach
    if email.startswith("coach@"):
        raise HTTPException(status_code=400, detail="Email is a coach email")
    # Validate email is not a mentor
    if email.startswith("mentor@"):
        raise HTTPException(status_code=400, detail="Email is a mentor email")
    # Validate email is not a counselor       
    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
