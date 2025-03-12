import streamlit as st
import datetime

# Page config
st.set_page_config(
    page_title="BSE Course Tracker",
    page_icon="📚",
    layout="wide"
)

st.title("BSE Course Progress Tracker")

# Status legend
st.markdown("### Status Legend")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div style="background-color: #ffcccb; padding: 10px; border-radius: 5px;">To Do</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="background-color: #ffffcc; padding: 10px; border-radius: 5px;">In Progress</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div style="background-color: #ccffcc; padding: 10px; border-radius: 5px;">Completed</div>', unsafe_allow_html=True)

# Simple course list without pandas
courses = [
    {"name": "MATH221/Transferology Equivalent", "credits": 5, "term": "Fall 2024", "status": "To Do"},
    {"name": "PHYSICS 103, 104, 201, or 202", "credits": 4, "term": "Fall 2024", "status": "To Do"},
    {"name": "MATH222/Transferology Equivalent", "credits": 4, "term": "Fall/Winter 2024-2025", "status": "To Do"},
    {"name": "MATH240/Transferology Equivalent", "credits": 3, "term": "Spring 2025", "status": "To Do"},
    {"name": "BSE 900", "credits": 1, "term": "Waived", "status": "Completed"},
    {"name": "BSE 901", "credits": 1, "term": "Spring 2025", "status": "To Do"},
    {"name": "BSE 990", "credits": 10, "term": "Spring 2025", "status": "To Do"},
    {"name": "BSE 367(Renewable Energy Systems)", "credits": 3, "term": "Spring 2025", "status": "To Do"},
    {"name": "M E 536 (DATA DRIVEN ENGINEERING DESIGN)", "credits": 3, "term": "Spring 2025", "status": "To Do"},
    {"name": "BSE 530 (Intro Data Science for Agric. And Life)", "credits": 3, "term": "Spring 2025", "status": "To Do"},
    {"name": "M E / CS 532 (MATRIX METHODS IN MACHINE LEARNING)", "credits": 3, "term": "Spring 2025", "status": "To Do"}
]

# Pre-BSE Courses Section
st.markdown("## Pre-BSE Courses to Fulfill")

# Complete before BSE Admission
st.markdown("### Complete (with min 3.0 GPA) before BSE Admission Considered")

for i, course in enumerate(courses[:2]):
    col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
    with col1:
        st.markdown(course["name"])
    with col2:
        st.markdown(f"{course['credits']} credits")
    with col3:
        st.markdown(course["term"])
    with col4:
        new_status = st.selectbox(
            "Status",
            ["To Do", "In Progress", "Completed"],
            index=["To Do", "In Progress", "Completed"].index(course["status"]),
            key=f"course_{i}_status"
        )
        courses[i]["status"] = new_status

# Additional Courses Section
st.markdown("### Additional Courses to Complete")

for i, course in enumerate(courses[2:4], 2):
    col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
    with col1:
        st.markdown(course["name"])
    with col2:
        st.markdown(f"{course['credits']} credits")
    with col3:
        st.markdown(course["term"])
    with col4:
        new_status = st.selectbox(
            "Status",
            ["To Do", "In Progress", "Completed"],
            index=["To Do", "In Progress", "Completed"].index(course["status"]),
            key=f"course_{i}_status"
        )
        courses[i]["status"] = new_status

# BSE Grad Course Plan
st.markdown("## BSE Grad Course Plan")

# Research/Seminars
st.markdown("### Research/Seminars")

for i, course in enumerate(courses[4:7], 4):
    col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
    with col1:
        st.markdown(course["name"])
    with col2:
        st.markdown(f"{course['credits']} credits")
    with col3:
        st.markdown(course["term"])
    with col4:
        new_status = st.selectbox(
            "Status",
            ["To Do", "In Progress", "Completed"],
            index=["To Do", "In Progress", "Completed"].index(course["status"]),
            key=f"course_{i}_status"
        )
        courses[i]["status"] = new_status

# Science/Engineering Coursework
st.markdown("### Science/Engr. Coursework (3 credit left) - Listing Options")

for i, course in enumerate(courses[7:], 7):
    col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
    with col1:
        st.markdown(course["name"])
    with col2:
        st.markdown(f"{course['credits']} credits")
    with col3:
        st.markdown(course["term"])
    with col4:
        new_status = st.selectbox(
            "Status",
            ["To Do", "In Progress", "Completed"],
            index=["To Do", "In Progress", "Completed"].index(course["status"]),
            key=f"course_{i}_status"
        )
        courses[i]["status"] = new_status

# Presentations Section
st.markdown("## Presentations & Milestones")

# Simple presentations list
presentations = [
    {"title": "Research Proposal", "date": "2025-02-15", "type": "Committee Meeting", "status": "In Progress"},
    {"title": "Progress Update", "date": "2025-04-05", "type": "Department Seminar", "status": "To Do"},
    {"title": "Conference Abstract", "date": "2025-05-20", "type": "External Submission", "status": "To Do"}
]

# Display presentations
for i, pres in enumerate(presentations):
    col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
    with col1:
        st.markdown(pres["title"])
    with col2:
        st.markdown(pres["date"])
    with col3:
        st.markdown(pres["type"])
    with col4:
        new_status = st.selectbox(
            "Status",
            ["To Do", "In Progress", "Completed"],
            index=["To Do", "In Progress", "Completed"].index(pres["status"]),
            key=f"pres_{i}_status"
        )
        presentations[i]["status"] = new_status

# Add new presentation
st.markdown("### Add New Presentation or Milestone")
with st.form("new_presentation_form"):
    col1, col2 = st.columns(2)
    with col1:
        new_title = st.text_input("Title")
        new_date = st.date_input("Date")
    with col2:
        new_type = st.text_input("Type (e.g., Committee Meeting, Conference)")
        new_status = st.selectbox("Status", ["To Do", "In Progress", "Completed"])
    
    submit_button = st.form_submit_button("Add Presentation")
    if submit_button and new_title and new_type:
        presentations.append({
            'title': new_title,
            'date': new_date.strftime('%Y-%m-%d'),
            'type': new_type,
            'status': new_status
        })
        st.experimental_rerun()

# Summary
todo_count = len([c for c in courses if c["status"] == "To Do"]) + len([p for p in presentations if p["status"] == "To Do"])
in_progress_count = len([c for c in courses if c["status"] == "In Progress"]) + len([p for p in presentations if p["status"] == "In Progress"])
completed_count = len([c for c in courses if c["status"] == "Completed"]) + len([p for p in presentations if p["status"] == "Completed"])

st.markdown("## Summary Dashboard")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("To Do", todo_count)
with col2:
    st.metric("In Progress", in_progress_count)
with col3:
    st.metric("Completed", completed_count)

# Progress bar
total_items = len(courses) + len(presentations)
completed_percentage = (completed_count / total_items) * 100 if total_items > 0 else 0
st.markdown("### Overall Progress")
st.progress(completed_percentage / 100)
st.write(f"{completed_percentage:.1f}% Complete")
