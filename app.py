import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from PIL import Image

@st.cache_resource
def load_lottie(filepath):
    try:
        with open(filepath, 'r') as file:
            lottie_data = json.load(file)
        return lottie_data
    except Exception as e:
        st.error(f"Error loading Lottie animation: {e}")
        return None


def load_contact():
    lottie_contact = load_lottie("Home-image/Animation - 1713080652663.json")
    return lottie_contact

def display_about_me(lottie_image):
    if 'show_tcet_details' not in st.session_state: 
        st.session_state.show_tcet_details = False
    
    if 'show_jbs_details' not in st.session_state: 
        st.session_state.show_jbs_details = False
    
    if 'show_kapol_details' not in st.session_state: 
        st.session_state.show_kapol_details = False

    with st.container():
        left,right = st.columns([2,2])
        with  right:
            st_lottie(lottie_image,width="100%", height=800)
        with left:
            st.write('##')
            st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)
            st.subheader("I am Raj Singh")
            st.title("Undergraduate at TCET")
            st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)

     # Displaying programming languages
    with left:
        st.subheader("Programming Languages")
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg", caption="Python", width=50)
    
    # Displaying tools
    with left:
        st.subheader("Tools and   Database")
        first, second= st.columns(2)
    with first:
        st.image("https://i.ibb.co/wWBxv2x/images-1.png", width=70)
    with second:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg", width=60)
    
    
    with left:
        st.subheader("Libraries")
        col1, col2 = st.columns([1,1])
    
    with col1:
        st.image("https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg", caption="Pandas", width=60)
    with col2:
        st.image("https://i.ibb.co/QfLKRj5/download-3.png",caption="Numpy", width=60)
    st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)

    
    # Education detail
    st.subheader("Education Detail")
    engg, college , school = st.columns(3)
    image_width = ["100%","100%","100%"]
    image_height = "200px"  # Adjust the height as needed

    with engg:
        st.markdown(f'<img src="https://www.tcetmumbai.in/images/sliders/slider-2.webp" width="{image_width[0]}" height="{image_height}" style="object-fit: cover;">', unsafe_allow_html=True)
        st.write("##")
        if st.button("TCET(Engineering College)"):
            st.session_state.show_tcet_details = not st.session_state.show_tcet_details
            st.session_state.show_jbs_details = False
            st.session_state.show_kapol_details = False
            if st.session_state.show_tcet_details:
                st.subheader("TCET")
                st.write("""
                - Bachelor of Engineering - Computer Engineering
                - Year - 2022-2026
                - CGPA - 8.91/10 (till sem3)
                """)
            else:
                st.subheader("")

    with college:
        st.markdown(f'<img src="https://www.adarsh-educationsociety.com/images/about-2.jpg" width="{image_width[1]}" height="{image_height}" style="object-fit: cover;">', unsafe_allow_html=True)
        st.write("##")
        if st.button("Adarsh Eduction Society(college)"):
            st.session_state.show_kapol_details = not st.session_state.show_kapol_details
            st.session_state.show_tcet_details = False
            st.session_state.show_jbs_details = False
            if st.session_state.show_kapol_details:
                st.subheader("Kapol COllege")
                st.write("""
                - class - 11th & 12th
                - Year - 2020 - 2022
                - subject - PCM & CS
                - Percentage - 78
                """)
            else:
                st.subheader("")
                
    with school:
        st.markdown(f'<img src="https://raw.githubusercontent.com/rajsingh162120/Portfolio/master/Home-image/jbs.jpeg" width="{image_width[2]}" height="{image_height}" style="object-fit: cover;">', unsafe_allow_html=True)     
        st.write("##")
        if st.button("JBS high school"):
            st.session_state.show_jbs_details = not st.session_state.show_jbs_details
            st.session_state.show_tcet_details = False
            st.session_state.show_kapol_details = False
            if st.session_state.show_jbs_details:
                st.subheader("JBS School")
                st.write("""
                - class - 1st - 10th
                - Year - 2010 - 2020
                - Percentage - 82.80
                """)
            else:
                st.subheader("")


def display_projects():
    st.header("My Projects")
    st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)
    
    projects = [
        {
            "name": "Smart-grid-prediction using Machine learning",
            "images": ["Project-image/smart-grid-1.png", "Project-image/smart-grid-2.png"],  # List of paths to your project images
            "description": "Our team developed a sophisticated Smart Grid prediction model using machine learning algorithms such as Random Forest Regression and Gradient Boosting. This model effectively predicts grid behavior, contributing to optimized energy management and resource allocation. We also make a website for the user input of air pressure , Temperature and wind speed to get the power generated . Also , we have integrated the power bi dashboard for the analysis of last 5 year data.",
            "link": "https://smart-grid.streamlit.app/",
            "github": "https://github.com/UtkarshTiwari1750/9_Sustainability_and_Environment"
        },
        {
            "name": "World-Cup-2022-dashboard",
            "images": ["Project-image/world-1.png", "Project-image/world-2.png"],  # List of paths to your project images
            "description": "Check out my Power BI dashboard for the thrilling 2022 T20 World Cup cricket analysis! 🌍🏆 Dive into dynamic insights through four dashboards covering overview, batsman stats, bowler stats, and more.",
            "link": "https://www.linkedin.com/posts/raj01singh_netflixanalysis-powerbi-dataanalysis-activity-7145809862436859905-irqN?utm_source=share&utm_medium=member_desktop"
        },
        {
            "name": "Netflix-analysis",
            "images": ["Project-image/web01.png", "Project-image/web1.png"],  # List of paths to your project images
            "description": "Exploring the World of Netflix: A Data Visualization Journey 🌐 Discover country-wise variations in Netflix content, explore ratings across genres and directors, and analyze the distribution of movies and shows. Dive into the specifics of Netflix shows, from release years to top directors and cast members.",
            "link": "https://net-flix.streamlit.app/",
            "linkedin": "https://www.linkedin.com/posts/raj01singh_netflix-datavisualization-streamlit-activity-7154436806883651584-DxTX?utm_source=share&utm_medium=member_desktop"
        },
        {
            "name": "Netflix Dashboard",
            "images": ["Project-image/netflix-1.png", "Project-image/netflix-2.png"],  # List of paths to your project images
            "description": "🎬📊 Excited to share my first Power BI project focusing on Netflix Analysis! 🚀🔍 Encountering a data challenge with missing country names for a significant portion of Netflix's dataset, I dedicated myself to rectifying this gap. Through meticulous research and cross-referencing, I filled in these missing details, enriching the dataset for a deeper analysis. This project has been a valuable learning experience in Power BI, expanding my skills and enabling me to derive actionable insights from the dataset.",
            "linkedin": "https://www.linkedin.com/posts/raj01singh_netflixanalysis-powerbi-dataanalysis-activity-7145809862436859905-irqN?utm_source=share&utm_medium=member_desktop"
        },
        # Add more projects with their respective images
    ]
    
    for project in projects:
        st.subheader(project['name'])
        col1, col2 = st.columns(2)
        with col1:
            st.image(project['images'][0], use_column_width=True)
        with col2:
            st.image(project['images'][1], use_column_width=True)
        st.write(project['description'])
        if 'link' in project:
            st.markdown(f"[Explore the Website]({project['link']})")
        if 'github' in project:
            st.markdown(f"[Github]({project['github']})")
        if 'linkedin' in project:
            st.markdown(f"[LinkedIn]({project['linkedin']})")
        st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)


def display_contact():
    st.header("Get in touch")
    st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)
    
    contact_form = """
    <form id="contactform" action="https://formsubmit.io/send/singhraj200416@gmail.com" method="POST" style="max-width: 400px;">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" style="background-color: white; width: 100%; margin-bottom: 10px; color: black;" required><br>
        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" style="background-color: white; width: 100%; margin-bottom: 10px; color: black;" required><br>
        <label for="comment">Comment:</label><br>
        <textarea id="comment" name="comment" rows="5" style="background-color: white; width: 100%; margin-bottom: 10px; resize: vertical; color: black;" placeholder="Write your message here..." required></textarea><br>
        <input type="hidden" name="_formsubmit_id" style="display:none">
        <input type="submit" value="Submit" style="width: 100%; background-color: #FF4B4B; color: white; border: none; padding: 10px; cursor: pointer;">
    </form>
    """

    left_cell , right_cell = st.columns([2,1])
    with left_cell:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_cell:
        lottie_contact = load_contact()
        st_lottie(lottie_contact, height=310)
        

def display_experience():
    st.write(f"## My Experience")
    st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)
    
    hackathons = [
        {
            "name": "Hackwave: National Level Hackathon -> 6th - 7th April 2024 - 24Hr",
            "college": "A.P. Shah Engineering College",
            "images": ["Experience-image/codedev.jpg", "Experience-image/top5.jpg", "Experience-image/apshah.jpg", "Experience-image/3.jpg", "Experience-image/ApShah_certficate.jpg","Experience-image/hackwave-id.jpeg"],
            "description": "Engaged in an offline hackathon hosted at Ap Shah Engineering College, focusing on the development of a predictive model for smart grid management. Our team successfully achieved a precision rate of 99.7% in forecasting power grid trends. Additionally, we created a user-friendly website enabling input parameters for wind, temperature, and air pressure to estimate power generation. Integration of a Power BI dashboard facilitated analysis of historical data over the past five years.",
            "position": "Secured a Top 5 position in the Final Round",
            "github": "https://github.com/UtkarshTiwari1750/9_Sustainability_and_Environment",
            "website": "https://smart-grid.streamlit.app/",
            "info": None,
            "linkedin": None
        },
        {
            "name": "Hacksparrow: National Level Hackathon -> 22nd to 24th March 2024 - 36Hr",
            "college": "Terna Engineering College",
            "images": ["Experience-image/T-14.jpg","Experience-image/fusion.jpg", "Experience-image/canva.jpg","Experience-image/55 (1).png", "Experience-image/video.jpg","Experience-image/coder.jpg"],  
            "description": "Engaged in an offline hackathon hosted at Terna Engineering College, where our team attained a notable Top 8 position among a pool of talented participants. Collaborated closely to develop 'Fusion Flow,' an innovative collaborative workspace platform. Leveraged cutting-edge technologies including Next.js, TypeScript, Shadcn/ui, Fabric, Express.js, Node.js, Socket.io, and Liveblock, fostering a seamless user experience. Grateful for the enriching opportunity to explore emerging technologies and engage in collaborative projects.",
            "position": "Secured a Top 8 position in the Final Round",
            "github": "https://github.com/UtkarshTiwari1750/Hacksparrow",
            "website":None,
            "info": "https://hackodyssey.devfolio.co/",
            "linkedin": "https://www.linkedin.com/posts/raj01singh_hackathon-learning-webdevelopment-activity-7178439591312433155-9z4O?utm_source=share&utm_medium=member_desktop"
        },
        {
            "name": "Hack It Out : National Level Hackathon -> 29th Oct to 5th Nov 2023 ",
            "college": "IIT Patna",
            "images": ["Experience-image/iit.png","Experience-image/iit-codedev.png", "Experience-image/issue.png","Experience-image/description.png", "Experience-image/IIT-Patna-certificate.jpg","Experience-image/solution.png"],  
            "description": "Participated in an online hackathon hosted by IIT-Patna, where our team achieved a notable Top 15 position among a pool of talented participants. Collaborated closely to develop a healthcare website providing comprehensive information for patients and doctors, facilitating informed decision-making. Utilized cutting-edge technologies to deliver a seamless user experience. Grateful for the opportunity to engage in collaborative projects and explore emerging technologies.",
            "position": "Secured a Top 15 position in the Final Round",
            "github": "https://github.com/UtkarshTiwari1750/Hack_it_Out",
            "website": None,
            "info":"https://unstop.com/hackathons/hack-it-out-celesta-2023-indian-institute-of-technology-iit-patna-795714",
            "linkedin": None
        },
    
    ]
    
    for hackathon in hackathons:
        st.write(f"## {hackathon['name']}")
        st.write(f"#### {hackathon['college']}")
        num_images = len(hackathon['images'])
        num_columns = min(3, num_images)  # Limit to 3 columns
        num_rows = num_images // num_columns
        first_image_width, first_image_height = Image.open(hackathon['images'][4]).size
        first_image_aspect_ratio = first_image_width / first_image_height
        fixed_image_height = 350  # Adjust the fixed height as needed
        
        for row in range(num_rows):
            cols = st.columns(num_columns)
            for col_index in range(num_columns):
                image_index = row * num_columns + col_index
                if image_index < num_images:
                    with cols[col_index]:
                        image = Image.open(hackathon['images'][image_index])
                        resized_image = image.resize((int(fixed_image_height * first_image_aspect_ratio), fixed_image_height))
                        st.image(resized_image, use_column_width=True)
        st.write(hackathon["description"])
        st.write(f"## {hackathon['position']}")
        if hackathon['github']:
            st.markdown(f"[GitHub]({hackathon['github']})")
        if hackathon['website']:
            st.markdown(f"[Exlore the website]({hackathon['website']})")
        if hackathon['info']:
            st.markdown(f"[Info about this]({hackathon['info']})")
        if hackathon['linkedin']:
            st.markdown(f"[LinkedIn]({hackathon['linkedin']})")
            
        st.markdown('<hr class="rainbow-divider">', unsafe_allow_html=True)


def display_home():
    st.write("##")
    st.subheader("Hey Guys 👋")
    st.title("My Portfolio website")
    
@st.cache_resource
def load_data():
    lottie_image = load_lottie("Home-image/Animation - 1707578638389.json")
    return lottie_image

def display_page():
    lottie_image = load_data()
    display_home()
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["About Me", "Projects", "Experience", "Contact"],
            icons=['person', 'code-slash', 'suitcase', 'chat-left-text-fill'],
            orientation='horizontal'
        )

    # Apply custom CSS to set the text color of the option_menu
    custom_css= """
    <style>
        .streamlit-option-menu span {
            color: #000000 !important;
        }
        .streamlit-option-menu .menu-button {
            color: #000000 !important;
        }
    </style>
    """
    st.write(custom_css, unsafe_allow_html=True)

    if selected == 'About Me':
        display_about_me(lottie_image)
    elif selected == 'Projects':
        display_projects()
    elif selected == 'Contact':
        display_contact()
    elif selected == 'Experience':
        display_experience()

# Set theme colors
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🎈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set theme colors and rainbow divider CSS animation
st.markdown(
    """
    <style>
    body {
        background-color: #000000; /* Change background color to black */
        color: #FFFFFF; /* Change text color to white */
    }
   
    .stTextArea, .stTextInput, .stSelectbox div[role="button"], .stNumberInput .input-container input {
        background-color: #F0F2F6; /* Change secondary background color */
    }
    .rainbow-divider {
        border: none;
        height: 2px;
        background-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
        animation: rainbow 2s linear infinite;
    }
    @keyframes rainbow {
        0% {
            background-position: 0% 50%;
        }
        100% {
            background-position: 100% 50%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

display_page()
