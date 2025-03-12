import streamlit as st
import datetime

# Page config
st.set_page_config(
    page_title="BSE Course Tracker",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better visual representation and alignment fixes
st.markdown("""
<style>
    .header {
        font-size: 20px;
        font-weight: bold;
        background-color: #e63946;
        color: white;
        padding: 8px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .subheader {
        font-size: 16px;
        font-weight: bold;
        background-color: #ffcdb2;
        padding: 6px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .complete {
        background-color: #ccffcc;
        padding: 2px 5px;
        border-radius: 3px;
    }
    .in-progress {
        background-color: #ffffcc;
        padding: 2px 5px;
        border-radius: 3px;
    }
    .to-do {
        background-color: #ffcccb;
        padding: 2px 5px;
        border-radius: 3px;
    }
    .preparing {
        background-color: #e6f3ff;
        padding: 2px 5px;
        border-radius: 3px;
    }
    
    /* Strong alignment fixes for all dropdowns */
    div.row-widget.stSelectbox {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Remove all extra spacing around selectboxes */
    .stSelectbox > div {
        min-height: 0 !important;
        line-height: 1 !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }
    
    /* Make all selectbox components aligned */
    .stSelectbox [data-baseweb="select"] {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }
    
    /* Make rows very compact */
    .element-container {
        margin-bottom: 0 !important;
        padding: 0 !important;
    }
    
    /* Align text in columns */
    .stMarkdown p {
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        padding-top: 0.25rem !important;
        padding-bottom: 0 !important;
    }
    
    /* Make sure horizontal alignment is consistent */
    .row-widget {
        display: flex;
        align-items: center;
    }
</style>
""", unsafe_allow_html=True)

st.title("BSE M.S. Progress Tracker for Lauren Glynn")

# Initialize session state for courses if not exists
if 'pre_bse_courses' not in st.session_state:
    st.session_state.pre_bse_courses = [
        {
            "name": "MATH221", 
            "credits": 5, 
            "term": "Winter/Spring 2024", 
            "where": "ExtensionLearning (UW)",
            "status": "In Progress",
            "ets": "--",
            "etd": "4/28/25"
        },
        {
            "name": "PHYSICS 103, 104, 201, or 202", 
            "credits": 4, 
            "term": "Fall 2024", 
            "where": "MATC",
            "status": "Complete",
            "ets": "8/25/2024",
            "etd": "12/15/2024"
        },
        {
            "name": "MATH222", 
            "credits": 4, 
            "term": "Winter/Spring 2025", 
            "where": "ExtensionLearning (UW)",
            "status": "In Progress",
            "ets": "--",
            "etd": "6/27/2025",
            "online": True
        },
        {
            "name": "MATH240", 
            "credits": 3, 
            "term": "Spring/Summer 2025", 
            "where": "UW-Madison (Summer Semester)",
            "status": "To Do",
            "ets": "6/16/2025",
            "etd": "8/10/2025",
            "online": True
        }
    ]

if 'bse_grad_courses' not in st.session_state:
    st.session_state.bse_grad_courses = [
        {
            "name": "BSE 900", 
            "credits": 1, 
            "term": "Waived", 
            "where": "",
            "status": "Complete",
            "ets": "",
            "etd": ""
        },
        {
            "name": "BSE 901", 
            "credits": 1, 
            "term": "Spring 2025", 
            "where": "UW-Madison (Spring Semester)",
            "status": "In Progress",
            "ets": "1/22/2025",
            "etd": "4/30/2025",
            "online": True
        },
        {
            "name": "BSE 990", 
            "credits": 10, 
            "term": "Spring 2025", 
            "where": "UW-Madison (Spring Semester)",
            "status": "In Progress",
            "ets": "1/22/2025",
            "etd": "4/30/2025",
            "online": True
        }
    ]

if 'science_eng_courses' not in st.session_state:
    st.session_state.science_eng_courses = [
        {
            "name": "BSE 367 (Renewable Energy Systems)", 
            "credits": 3, 
            "term": "Spring/Summer 2025", 
            "where": "UW-Madison (Summer Semester)",
            "status": "To Do",
            "ets": "6/16/2025",
            "etd": "8/10/2025",
            "online": True
        },
        {
            "name": "M E / CS 532 (MATRIX METHODS IN MACHINE LEARNING)", 
            "credits": 3, 
            "term": "Spring/Summer 2025", 
            "where": "UW-Madison (Summer Semester)",
            "status": "To Do",
            "ets": "6/16/2025",
            "etd": "8/10/2025",
            "online": True
        }
    ]

if 'presentations' not in st.session_state:
    st.session_state.presentations = [
        {
            "title": "BSE 901 Presentation", 
            "term": "Spring 2025", 
            "where": "UW-Madison",
            "status": "Preparing",
            "ets": "--",
            "etd": "4/9/2025"
        },
        {
            "title": "Thesis Defense", 
            "term": "Summer 2025", 
            "where": "UW-Madison",
            "status": "To Do",
            "ets": "--",
            "etd": "August 2025"
        }
    ]

if 'committee_meetings' not in st.session_state:
    st.session_state.committee_meetings = [
        {
            "title": "1st Committee Meeting", 
            "term": "Fall 2025", 
            "where": "UW-Madison",
            "status": "Complete",
            "ets": "--",
            "etd": "12/9/25"
        },
        {
            "title": "2nd Committee Meeting",  
            "term": "Spring 2025", 
            "where": "UW-Madison",
            "status": "To Do",
            "ets": "--",
            "etd": "April 2025"
        },
        {
            "title": "Circulate thesis outline (papers 1, 2)", 
            "term": "Spring 2025", 
            "where": "--",
            "status": "To Do",
            "ets": "--",
            "etd": "Once submitted for pre-print"
        }
    ]

if 'paperwork' not in st.session_state:
    st.session_state.paperwork = [
        {
            "title": "Submit Committee Paperwork", 
            "term": "Spring 2025", 
            "where": "--",
            "status": "To Do",
            "ets": "--",
            "etd": "April 2025"
        },
        {
            "title": "Warrant Request Form", 
            "term": "Spring 2025", 
            "where": "--",
            "status": "To Do",
            "ets": "--",
            "etd": "Three weeks prior to defense"
        },
        {
            "title": "Submit pre-reqs to BSE once complete", 
            "term": "Summer 2025", 
            "where": "--",
            "status": "To Do",
            "ets": "--",
            "etd": "After all pre-reqs are completed"
        },
        {
            "title": "Sign up for summer courses", 
            "term": "Spring 2025", 
            "where": "--",
            "status": "To Do",
            "ets": "--",
            "etd": "Once assigned summer enrollment date"
        }
    ]

# Function to display status with colored background
def display_status(status):
    if status == "Complete":
        return f'<span class="complete">{status}</span>'
    elif status == "In Progress":
        return f'<span class="in-progress">{status}</span>'
    elif status == "To Do":
        return f'<span class="to-do">{status}</span>'
    elif status == "Preparing":
        return f'<span class="preparing">{status}</span>'
    else:
        return status

# Count status across all categories for progress bar at top
all_items = (
    st.session_state.pre_bse_courses + 
    st.session_state.bse_grad_courses + 
    st.session_state.science_eng_courses + 
    st.session_state.presentations + 
    st.session_state.committee_meetings + 
    st.session_state.paperwork
)

todo_count = len([item for item in all_items if item.get("status") == "To Do"])
in_progress_count = len([item for item in all_items if item.get("status") == "In Progress"])
complete_count = len([item for item in all_items if item.get("status") == "Complete"])
preparing_count = len([item for item in all_items if item.get("status") == "Preparing"])

# # Progress bar at the top
# total_items = len([item for item in all_items if item.get("status") != ""])
# completed_percentage = (complete_count / total_items) * 100 if total_items > 0 else 0
# st.markdown("### Overall Progress")
# st.progress(completed_percentage / 100)
# st.write(f"{completed_percentage:.1f}% Complete")

# Status options
status_options = ["To Do", "In Progress", "Complete", "Preparing", ""]

# Display Pre-BSE Courses Section
st.markdown('<div class="header">Pre-Reqs to Fulfill</div>', unsafe_allow_html=True)

# Create column headers
cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
cols[0].markdown("**Course To Take**")
cols[1].markdown("**Credit Count**")
cols[2].markdown("**Term**")
cols[3].markdown("**Where**")
cols[4].markdown("**Status**")
cols[5].markdown("**Start Date**")
cols[6].markdown("**End Date**")

# Complete before BSE Admission
st.markdown('<div class="subheader">Complete (with min 3.0 GPA) prior to BSE Admission</div>', unsafe_allow_html=True)

# Display and manage pre-BSE courses
for i, course in enumerate(st.session_state.pre_bse_courses[:2]):
    cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
    cols[0].markdown(course["name"])
    cols[1].markdown(str(course["credits"]))
    cols[2].markdown(course["term"])
    cols[3].markdown(course["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(course["status"]) if course["status"] in status_options else 0,
        key=f"pre_bse_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != course["status"]:
        st.session_state.pre_bse_courses[i]["status"] = new_status
    
    cols[5].markdown(course["ets"])
    cols[6].markdown(course["etd"])

# Additional Courses to Complete
st.markdown('<div class="subheader">Additional Courses to Complete</div>', unsafe_allow_html=True)

# Display and manage additional pre-BSE courses
for i, course in enumerate(st.session_state.pre_bse_courses[2:], 2):
    cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
    
    # Add "Online" tag if applicable
    if course.get("online"):
        cols[0].markdown(f"{course['name']} (Online)")
    else:
        cols[0].markdown(course["name"])
    
    cols[1].markdown(str(course["credits"]))
    cols[2].markdown(course["term"])
    cols[3].markdown(course["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(course["status"]) if course["status"] in status_options else 0,
        key=f"pre_bse_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != course["status"]:
        st.session_state.pre_bse_courses[i]["status"] = new_status
    
    cols[5].markdown(course["ets"])
    cols[6].markdown(course["etd"])

# BSE Grad Course Plan
st.markdown('<div class="header">BSE Grad Course Plan</div>', unsafe_allow_html=True)

# Create column headers
cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
cols[0].markdown("**Course To Take**")
cols[1].markdown("**Credit Count**")
cols[2].markdown("**Term**")
cols[3].markdown("**Where**")
cols[4].markdown("**Status**")
cols[5].markdown("**Start Date**")
cols[6].markdown("**End Date**")

# Research/Seminars
st.markdown('<div class="subheader">Research/Seminars</div>', unsafe_allow_html=True)

# Display and manage BSE grad courses
for i, course in enumerate(st.session_state.bse_grad_courses):
    cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
    
    # Add "Online" tag if applicable
    if course.get("online"):
        cols[0].markdown(f"{course['name']} (Online)")
    else:
        cols[0].markdown(course["name"])
    
    cols[1].markdown(str(course["credits"]))
    cols[2].markdown(course["term"])
    cols[3].markdown(course["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(course["status"]) if course["status"] in status_options else 0,
        key=f"bse_grad_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != course["status"]:
        st.session_state.bse_grad_courses[i]["status"] = new_status
    
    cols[5].markdown(course["ets"])
    cols[6].markdown(course["etd"])

# Science/Engineering Coursework
st.markdown('<div class="subheader">Science/Engr. Coursework (3 credit left) - Listing Options (two available online for summer semester)</div>', unsafe_allow_html=True)

# Display and manage science/eng courses
for i, course in enumerate(st.session_state.science_eng_courses):
    cols = st.columns([3, 1, 1.5, 2, 1.5, 1, 1])
    
    # Add "Online" tag if applicable
    if course.get("online"):
        cols[0].markdown(f"{course['name']} (Online)")
    else:
        cols[0].markdown(course["name"])
    
    cols[1].markdown(str(course["credits"]))
    cols[2].markdown(course["term"])
    cols[3].markdown(course["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(course["status"]) if course["status"] in status_options else 0,
        key=f"science_eng_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != course["status"]:
        st.session_state.science_eng_courses[i]["status"] = new_status
    
    cols[5].markdown(course["ets"])
    cols[6].markdown(course["etd"])

# Presentations Section
st.markdown('<div class="header">Presentations</div>', unsafe_allow_html=True)

# Create column headers for presentations
cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
cols[0].markdown("**Title**")
cols[2].markdown("**Term**")
cols[3].markdown("**Where**")
cols[4].markdown("**Status**")
cols[5].markdown("**Start Date**")
cols[6].markdown("**End Date**")

# Display presentations
for i, pres in enumerate(st.session_state.presentations):
    cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
    cols[0].markdown(pres["title"])
    cols[2].markdown(pres["term"])
    cols[3].markdown(pres["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(pres["status"]) if pres["status"] in status_options else 0,
        key=f"pres_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != pres["status"]:
        st.session_state.presentations[i]["status"] = new_status
    
    cols[5].markdown(pres["ets"])
    cols[6].markdown(pres["etd"])

# Committee Meetings Section
st.markdown('<div class="header">Committee Meetings</div>', unsafe_allow_html=True)

# Create column headers for committee meetings
cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
cols[0].markdown("**Title**")
cols[2].markdown("**Term**")
cols[3].markdown("**Where**")
cols[4].markdown("**Status**")
cols[5].markdown("**Start Date**")
cols[6].markdown("**End Date**")

# Display committee meetings
for i, meeting in enumerate(st.session_state.committee_meetings):
    cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
    cols[0].markdown(meeting["title"])
    cols[2].markdown(meeting["term"])
    cols[3].markdown(meeting["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(meeting["status"]) if meeting["status"] in status_options else 0,
        key=f"meeting_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != meeting["status"]:
        st.session_state.committee_meetings[i]["status"] = new_status
    
    cols[5].markdown(meeting["ets"])
    cols[6].markdown(meeting["etd"])

# Paperwork Section
st.markdown('<div class="header">Paperwork</div>', unsafe_allow_html=True)

# Create column headers for paperwork
cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
cols[0].markdown("**Title**")
cols[2].markdown("**Term**")
cols[3].markdown("**Where**")
cols[4].markdown("**Status**")
cols[5].markdown("**Start Date**")
cols[6].markdown("**Due Date**")

# Display paperwork
for i, paper in enumerate(st.session_state.paperwork):
    cols = st.columns([3, 1.5, 1.5, 1.5, 1.5, 1, 1])
    cols[0].markdown(paper["title"])
    cols[2].markdown(paper["term"])
    cols[3].markdown(paper["where"])
    
    # Status dropdown with improved styling - using label_visibility="collapsed"
    new_status = cols[4].selectbox(
        "",
        status_options,
        index=status_options.index(paper["status"]) if paper["status"] in status_options else 0,
        key=f"paper_{i}_status",
        label_visibility="collapsed"
    )
    if new_status != paper["status"]:
        st.session_state.paperwork[i]["status"] = new_status
    
    cols[5].markdown(paper["ets"])
    cols[6].markdown(paper["etd"])

# Summary dashboard section - Now without the progress bar
st.markdown("## Summary Dashboard")

# Display summary metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("To Do", todo_count)
with col2:
    st.metric("In Progress", in_progress_count)
with col3:
    st.metric("Complete", complete_count)
with col4:
    st.metric("Preparing", preparing_count)

# Add new item section
st.markdown("## Add New Item")
with st.form("new_item_form"):
    # Create columns for form fields
    col1, col2 = st.columns(2)
    
    with col1:
        item_type = st.selectbox(
            "Item Type",
            ["Course", "Presentation", "Committee Meeting", "Paperwork"]
        )
        item_name = st.text_input("Title/Name")
        term = st.text_input("Term (e.g., Spring 2025)")
    
    with col2:
        where = st.text_input("Where (Institution)")
        status = st.selectbox("Status", status_options)
        ets = st.text_input("Start Date")
        etd = st.text_input("End Date/Due Date")
    
    # Add credits field for courses
    if item_type == "Course":
        credits = st.number_input("Credits", min_value=1, max_value=15, value=3)
    
    submit_button = st.form_submit_button("Add Item")
    
    if submit_button and item_name and term:
        if item_type == "Course":
            # Check which course list to add to
            if "BSE" in item_name.upper():
                if "900" in item_name or "901" in item_name or "990" in item_name:
                    st.session_state.bse_grad_courses.append({
                        "name": item_name,
                        "credits": credits,
                        "term": term,
                        "where": where,
                        "status": status,
                        "ets": ets,
                        "etd": etd,
                        "online": False  # Fixed the location.upper() reference that was causing errors
                    })
                else:
                    st.session_state.science_eng_courses.append({
                        "name": item_name,
                        "credits": credits,
                        "term": term,
                        "where": where,
                        "status": status,
                        "ets": ets,
                        "etd": etd,
                        "online": False  # Fixed the location.upper() reference that was causing errors
                    })
            else:
                st.session_state.pre_bse_courses.append({
                    "name": item_name,
                    "credits": credits,
                    "term": term,
                    "where": where,
                    "status": status,
                    "ets": ets,
                    "etd": etd,
                    "online": False  # Fixed the location.upper() reference that was causing errors
                })
        elif item_type == "Presentation":
            st.session_state.presentations.append({
                "title": item_name,
                "term": term,
                "where": where,
                "status": status,
                "ets": "--",
                "etd": etd
            })
        elif item_type == "Committee Meeting":
            st.session_state.committee_meetings.append({
                "title": item_name,
                "term": term,
                "where": where,
                "status": status,
                "ets": "--",
                "etd": etd,
            })
        elif item_type == "Paperwork":
            st.session_state.paperwork.append({
                "title": item_name,
                "term": term,
                "where": where,
                "status": status,
                "ets": "--",
                "etd": etd
            })
        
        st.rerun()

# Export options
st.markdown("## Export Options")
export_format = st.selectbox("Export Format", ["CSV", "JSON"])

if st.button(f"Export as {export_format}"):
    if export_format == "CSV":
        import csv
        import io
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write headers
        writer.writerow(["Type", "Name", "Credits", "Term", "Where", "Status", "Start Date", "End Date"])
        
        # Write Pre-BSE courses
        for course in st.session_state.pre_bse_courses:
            writer.writerow([
                "Pre-BSE Course", 
                course.get("name", ""), 
                course.get("credits", ""), 
                course.get("term", ""),
                course.get("where", ""),
                course.get("status", ""),
                course.get("ets", ""),
                course.get("etd", "")
            ])
        
        # Write BSE grad courses
        for course in st.session_state.bse_grad_courses:
            writer.writerow([
                "BSE Grad Course", 
                course.get("name", ""), 
                course.get("credits", ""), 
                course.get("term", ""),
                course.get("where", ""),
                course.get("status", ""),
                course.get("ets", ""),
                course.get("etd", "")
            ])
        
        # Write Science/Eng courses
        for course in st.session_state.science_eng_courses:
            writer.writerow([
                "Science/Eng Course", 
                course.get("name", ""), 
                course.get("credits", ""), 
                course.get("term", ""),
                course.get("where", ""),
                course.get("status", ""),
                course.get("ets", ""),
                course.get("etd", "")
            ])
        
        # Write presentations
        for pres in st.session_state.presentations:
            writer.writerow([
                "Presentation", 
                pres.get("title", ""), 
                "", 
                pres.get("term", ""),
                pres.get("where", ""),
                pres.get("status", ""),
                pres.get("ets", ""),
                pres.get("etd", "")
            ])
        
        # Write committee meetings
        for meeting in st.session_state.committee_meetings:
            writer.writerow([
                "Committee Meeting", 
                meeting.get("title", ""), 
                "", 
                meeting.get("term", ""),
                meeting.get("where", ""),
                meeting.get("status", ""),
                meeting.get("ets", ""),
                meeting.get("etd", "")
            ])
        
        # Write paperwork
        for paper in st.session_state.paperwork:
            writer.writerow([
                "Paperwork", 
                paper.get("title", ""), 
                "", 
                paper.get("term", ""),
                paper.get("where", ""),
                paper.get("status", ""),
                paper.get("ets", ""),
                paper.get("etd", "")
            ])
        
        # Create download button
        st.download_button(
            label="Download CSV",
            data=output.getvalue(),
            file_name="bse_course_tracker.csv",
            mime="text/csv"
        )
    
    elif export_format == "JSON":
        import json
        
        export_data = {
            "pre_bse_courses": st.session_state.pre_bse_courses,
            "bse_grad_courses": st.session_state.bse_grad_courses,
            "science_eng_courses": st.session_state.science_eng_courses,
            "presentations": st.session_state.presentations,
            "committee_meetings": st.session_state.committee_meetings,
            "paperwork": st.session_state.paperwork
        }
        
        # Create download button
        st.download_button(
            label="Download JSON",
            data=json.dumps(export_data, indent=2),
            file_name="bse_course_tracker.json",
            mime="application/json"
        )
