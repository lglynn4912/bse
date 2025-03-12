import streamlit as st
import pandas as pd
import datetime

# Page config
st.set_page_config(
    page_title="BSE Course Tracker",
    page_icon="📚",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .header {
        font-size: 24px;
        font-weight: bold;
        padding: 10px;
        background-color: #e63946;
        color: white;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 18px;
        font-weight: bold;
        padding: 8px;
        background-color: #f1c40f;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .section-header {
        font-size: 16px;
        font-weight: bold;
        padding: 6px;
        background-color: #90ee90;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .todo {
        background-color: #ffcccb;
    }
    .in-progress {
        background-color: #ffffcc;
    }
    .completed {
        background-color: #ccffcc;
    }
    .presentations {
        background-color: #4682b4;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
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

# Initialize session state for course status if it doesn't exist
if 'course_status' not in st.session_state:
    st.session_state.course_status = {
        'MATH221': 'To Do',
        'PHYSICS': 'To Do',
        'MATH222': 'To Do',
        'MATH240': 'To Do',
        'BSE900': 'Completed',
        'BSE901': 'To Do',
        'BSE990': 'To Do',
        'BSE367': 'To Do',
        'ME536': 'To Do',
        'BSE530': 'To Do',
        'ME_CS532': 'To Do',
    }

# Initialize session state for presentations if it doesn't exist
if 'presentations' not in st.session_state:
    st.session_state.presentations = [
        {
            'title': 'Research Proposal',
            'date': datetime.date(2025, 2, 15),
            'type': 'Committee Meeting',
            'status': 'In Progress'
        },
        {
            'title': 'Progress Update',
            'date': datetime.date(2025, 4, 5),
            'type': 'Department Seminar',
            'status': 'To Do'
        },
        {
            'title': 'Conference Abstract',
            'date': datetime.date(2025, 5, 20),
            'type': 'External Submission',
            'status': 'To Do'
        }
    ]

# Pre-BSE Courses Section
st.markdown('<div class="header">Pre-BSE Courses to Fulfill</div>', unsafe_allow_html=True)

# Complete before BSE Admission
st.markdown('<div class="subheader">Complete (with min 3.0 GPA) before BSE Admission Considered</div>', unsafe_allow_html=True)

# MATH221
col1, col2, col3 = st.columns([4, 1, 2])
with col1:
    st.markdown("MATH221/Transferology Equivalent")
with col2:
    st.markdown("5 credits")
with col3:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['MATH221']),
        key="MATH221_status"
    )
    st.session_state.course_status['MATH221'] = status

# PHYSICS
col1, col2, col3 = st.columns([4, 1, 2])
with col1:
    st.markdown("PHYSICS 103, 104, 201, or 202/Transferology Equivalent")
with col2:
    st.markdown("4 credits")
with col3:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['PHYSICS']),
        key="PHYSICS_status"
    )
    st.session_state.course_status['PHYSICS'] = status

# Additional Courses Section
st.markdown('<div class="section-header">Additional Courses to Complete</div>', unsafe_allow_html=True)

# MATH222
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("MATH222/Transferology Equivalent")
with col2:
    st.markdown("4 credits")
with col3:
    st.markdown("Fall/Winter 2024-2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['MATH222']),
        key="MATH222_status"
    )
    st.session_state.course_status['MATH222'] = status

# MATH240
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("MATH240/Transferology Equivalent")
with col2:
    st.markdown("3 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['MATH240']),
        key="MATH240_status"
    )
    st.session_state.course_status['MATH240'] = status

# BSE Grad Course Plan
st.markdown('<div class="header">BSE Grad Course Plan</div>', unsafe_allow_html=True)

# Research/Seminars
st.markdown('<div class="subheader">Research/Seminars</div>', unsafe_allow_html=True)

# BSE900
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("BSE 900")
with col2:
    st.markdown("1 credit")
with col3:
    st.markdown("Waived")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['BSE900']),
        key="BSE900_status"
    )
    st.session_state.course_status['BSE900'] = status

# BSE901
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("BSE 901")
with col2:
    st.markdown("1 credit")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['BSE901']),
        key="BSE901_status"
    )
    st.session_state.course_status['BSE901'] = status

# BSE990
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("BSE 990")
with col2:
    st.markdown("10 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['BSE990']),
        key="BSE990_status"
    )
    st.session_state.course_status['BSE990'] = status

# Science/Engineering Coursework
st.markdown('<div class="section-header">Science/Engr. Coursework (3 credit left) - Listing Options</div>', unsafe_allow_html=True)

# BSE367
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("BSE 367(Renewable Energy Systems)/Transferology Equivalent")
with col2:
    st.markdown("3 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['BSE367']),
        key="BSE367_status"
    )
    st.session_state.course_status['BSE367'] = status

# ME536
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("M E 536 (DATA DRIVEN ENGINEERING DESIGN)/Transferology Equivalent")
with col2:
    st.markdown("3 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['ME536']),
        key="ME536_status"
    )
    st.session_state.course_status['ME536'] = status

# BSE530
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("BSE 530 (Intro Data Science for Agric. And Life)/Transferology Equivalent")
with col2:
    st.markdown("3 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['BSE530']),
        key="BSE530_status"
    )
    st.session_state.course_status['BSE530'] = status

# ME/CS532
col1, col2, col3, col4 = st.columns([3, 1, 2, 1])
with col1:
    st.markdown("M E / CS 532 (MATRIX METHODS IN MACHINE LEARNING)/Transferology Equivalent")
with col2:
    st.markdown("3 credits")
with col3:
    st.markdown("Spring 2025")
with col4:
    status = st.selectbox(
        "Status",
        ["To Do", "In Progress", "Completed"],
        index=["To Do", "In Progress", "Completed"].index(st.session_state.course_status['ME_CS532']),
        key="ME_CS532_status"
    )
    st.session_state.course_status['ME_CS532'] = status

# Presentations Section
st.markdown('<div class="presentations">Presentations & Milestones</div>', unsafe_allow_html=True)

# Display existing presentations in a table
presentations_df = pd.DataFrame(st.session_state.presentations)
st.dataframe(presentations_df, use_container_width=True)

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
        st.session_state.presentations.append({
            'title': new_title,
            'date': new_date,
            'type': new_type,
            'status': new_status
        })
        st.experimental_rerun()

# Summary Section
st.markdown('<div class="header">Summary Dashboard</div>', unsafe_allow_html=True)

# Count status
status_counts = {
    'To Do': 0,
    'In Progress': 0,
    'Completed': 0
}

for status in st.session_state.course_status.values():
    status_counts[status] += 1

# Add presentations to counts
for pres in st.session_state.presentations:
    status_counts[pres['status']] += 1

# Display summary
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("To Do", status_counts['To Do'])
with col2:
    st.metric("In Progress", status_counts['In Progress'])
with col3:
    st.metric("Completed", status_counts['Completed'])

# Progress bar
total_items = sum(status_counts.values())
completed_percentage = (status_counts['Completed'] / total_items) * 100 if total_items > 0 else 0
st.markdown("### Overall Progress")
st.progress(completed_percentage / 100)
st.write(f"{completed_percentage:.1f}% Complete")

# Add download button for CSV export
def convert_to_csv():
    # Prepare course data
    courses_data = []
    for course, status in st.session_state.course_status.items():
        courses_data.append({
            'Item': course,
            'Type': 'Course',
            'Status': status,
            'Date': ''
        })
    
    # Add presentation data
    for pres in st.session_state.presentations:
        courses_data.append({
            'Item': pres['title'],
            'Type': pres['type'],
            'Status': pres['status'],
            'Date': pres['date'].strftime('%Y-%m-%d')
        })
    
    return pd.DataFrame(courses_data).to_csv(index=False)

csv = convert_to_csv()
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name="bse_course_tracker.csv",
    mime="text/csv",
)
