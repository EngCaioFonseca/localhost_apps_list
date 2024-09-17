import streamlit as st
import socket
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import random

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    return port if result == 0 else None

def get_app_title(port):
    try:
        response = requests.get(f"http://localhost:{port}/_stcore/config", timeout=2)
        if response.status_code == 200:
            config = json.loads(response.text)
            return config.get('pageTitle', f"App on port {port}")
        
        response = requests.get(f"http://localhost:{port}", timeout=2)
        if response.status_code == 200:
            import re
            match = re.search(r'st_page:{"pageName":"([^"]+)"', response.text)
            if match:
                return match.group(1)
    except:
        pass
    return f"App on port {port}"

def get_app_metadata(port):
    try:
        response = requests.get(f"http://localhost:{port}", timeout=2)
        content_length = len(response.content)
        return {
            "response_time": response.elapsed.total_seconds(),
            "content_size": content_length,
            "status": "Active" if response.status_code == 200 else "Error"
        }
    except:
        return {
            "response_time": None,
            "content_size": None,
            "status": "Error"
        }

def find_running_apps(start_port=8501, end_port=8520):
    running_apps = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_port = {executor.submit(check_port, port): port for port in range(start_port, end_port + 1)}
        for future in as_completed(future_to_port):
            port = future.result()
            if port:
                title = get_app_title(port)
                metadata = get_app_metadata(port)
                running_apps.append((port, title, metadata))
    return running_apps

def get_color_for_app(app_title):
    # Generate a pseudo-random color based on the app title
    random.seed(app_title)
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def main():
    st.title("App Launcher")

    running_apps = find_running_apps()

    if not running_apps:
        st.write("No Streamlit apps currently running.")
    else:
        st.write(f"Found {len(running_apps)} running Streamlit app(s):")
        for port, title, metadata in running_apps:
            col1, col2, col3 = st.columns([1, 3, 2])
            with col1:
                color = get_color_for_app(title)
                st.markdown(f'<div style="width:50px;height:50px;background-color:{color};border-radius:50%;"></div>', unsafe_allow_html=True)
            with col2:
                if st.button(f"{title} (Port {port})", key=f"btn_{port}"):
                    st.markdown(f'<meta http-equiv="refresh" content="0;url=http://localhost:{port}">', unsafe_allow_html=True)
            with col3:
                st.write(f"Status: {metadata['status']}")
                if metadata['response_time']:
                    st.write(f"Response time: {metadata['response_time']:.2f}s")
                if metadata['content_size']:
                    st.write(f"Content size: {metadata['content_size'] / 1024:.2f} KB")

    if st.button("Refresh"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
