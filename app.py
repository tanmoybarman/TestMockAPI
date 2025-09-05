import streamlit as st
import subprocess
import time
import requests
import json

# Set page config
st.set_page_config(
    page_title="Healthcare Mock API",
    page_icon="🏥",
    layout="wide"
)

# Title
st.title("🏥 Healthcare Mock API")
st.write("A mock API service for healthcare data")

# Start FastAPI server in a subprocess
@st.cache_resource
def start_fastapi():
    process = subprocess.Popen(
        ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Give it a moment to start
    time.sleep(2)
    return process

# Start the server
server = start_fastapi()

# Display API status
st.subheader("API Status")
status_placeholder = st.empty()

try:
    response = requests.get("http://localhost:8000/")
    if response.status_code == 200:
        status_placeholder.success("✅ API is running!")
        api_info = response.json()
        st.json(api_info)
    else:
        status_placeholder.error(f"❌ API returned status code: {response.status_code}")
except Exception as e:
    status_placeholder.error(f"❌ Could not connect to API: {str(e)}")

# API Documentation
st.subheader("API Documentation")
st.markdown("""
The API is running and available at `http://localhost:8000`

### Available Endpoints:

#### Member Endpoints
- `GET /searchMemberById/m-a` - Get member details for ID 'm-a'
- `GET /searchMemberById/m-b-m-n` - Get member details for ID 'm-b-m-n'
- `GET /searchMemberById/m-n-a-c` - Get member details for ID 'm-n-a-c'
- `GET /searchMemberById/m-e-r` - Simulate error response for member search

#### Coverage Endpoints
- `GET /searchCoverageById/c-s` - Get coverage details for ID 'c-s'
- `GET /searchCoverageById/c-n-m-id` - Get coverage details for ID 'c-n-m-id'
- `GET /searchCoverageById/c-n-a-c` - Get coverage details for ID 'c-n-a-c'
- `GET /searchCoverageById/c-e-r` - Simulate error response for coverage search

#### Accumulator Endpoints
- `GET /searchAccums/acc-succ` - Get accumulator details for ID 'acc-succ'
- `GET /searchAccums/acc-rem-amt-miss` - Get accumulator details for ID 'acc-rem-amt-miss'
- `GET /searchAccums/acc-f` - Simulate error response for accumulator search

### Interactive Testing
You can test the endpoints using the interactive documentation at:
[http://localhost:8000/docs](http://localhost:8000/docs)
""")

# Add a way to stop the server when the Streamlit app is closed
import atexit

def stop_server():
    server.terminate()
    server.wait()

atexit.register(stop_server)
