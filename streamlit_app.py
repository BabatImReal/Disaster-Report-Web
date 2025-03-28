import streamlit as st
import requests
import geocoder
from typing import Optional, Tuple

def get_location_geocoder() -> Tuple[Optional[float], Optional[float]]:
    """
    Get location using geocoder library.
    """
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng[0], g.latlng[1]
    return None, None

def get_location_ipapi() -> Tuple[Optional[float], Optional[float]]:
    """
    Fallback method using ipapi.co service.
    """
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            data = response.json()
            lat = data.get('latitude')
            lon = data.get('longitude')
            if lat is not None and lon is not None:
                # Store additional location data in session state
                st.session_state.location_data = {
                    'city': data.get('city'),
                    'region': data.get('region'),
                    'country': data.get('country_name'),
                    'ip': data.get('ip')
                }
                return lat, lon
    except requests.RequestException as e:
        st.error(f"Error retrieving location from ipapi.co: {str(e)}")
    return None, None

def get_location() -> Tuple[Optional[float], Optional[float]]:
    """
    Tries to get location first using geocoder, then falls back to ipapi.co.
    """
    lat, lon = get_location_geocoder()
    if lat is None:
        st.info("Primary geolocation method unsuccessful, trying alternative...")
        lat, lon = get_location_ipapi()
    return lat, lon

def show_location_details(lat, lon):
    """
    Displays the additional location details and a map.
    """
    if 'location_data' in st.session_state:
        data = st.session_state.location_data
        st.write("**Location Details:**")
        col1, col2 = st.columns(2)
        with col1:
            st.write("📍 City:", data['city'])
            st.write("🏘️ Region:", data['region'])
        with col2:
            st.write("🌍 Country:", data['country'])
            st.write("🔍 IP:", data['ip'])
    st.write("📍 Location on Map:")
    st.map(data={'lat': [lat], 'lon': [lon]}, zoom=10)

def main():
    st.set_page_config(page_title="Disaster Report Form", layout="wide")
    
    # Custom CSS to beautify the UI
    st.markdown("""
    <style>
    .report-form {
        background: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .report-form h2 {
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.title("Disaster Report Form")
    st.write("Please fill out the following information:")
    
    # Location retrieval section outside the form
    with st.expander("Location Retrieval", expanded=False):
        if st.button("Get My Location"):
            with st.spinner("Retrieving your location..."):
                lat, lon = get_location()
                if lat is not None and lon is not None:
                    st.session_state["lat"] = lat
                    st.session_state["lon"] = lon
                    st.success("Location retrieved successfully!")
                    st.write(f"**Latitude:** {lat:.4f}  |  **Longitude:** {lon:.4f}")
                    show_location_details(lat, lon)
                else:
                    st.error("Could not determine your location. Please try again.")
    
    # The disaster report form
    with st.container():
        st.markdown('<div class="report-form">', unsafe_allow_html=True)
        with st.form(key="disaster_report_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Name of Informant")
                contact = st.text_input("Contact Information")
                disaster_type = st.selectbox("Type of Disaster", 
                                             ["Flood", "Earthquake", "Wildfire", "Hurricane", "Tornado", "Other"])
            
            with col2:
                # Prepopulate location field if available
                if "lat" in st.session_state and "lon" in st.session_state:
                    default_location = f"Latitude: {st.session_state['lat']:.4f}, Longitude: {st.session_state['lon']:.4f}"
                else:
                    default_location = ""
                location_manual = st.text_input("Share Location of Informant", value=default_location)
            
            note = st.text_area("Further Note")
            
            submit_button = st.form_submit_button("Submit Report")
            
            if submit_button:
                st.success("Report submitted successfully!")
                st.write("### Report Summary")
                st.write(f"**Name:** {name}")
                st.write(f"**Contact:** {contact}")
                st.write(f"**Disaster Type:** {disaster_type}")
                st.write(f"**Location:** {location_manual}")
                st.write(f"**Further Note:** {note}")
        st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
