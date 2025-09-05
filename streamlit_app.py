import streamlit as st
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

# Display API status
st.subheader("API Status")
st.success("✅ API is running!")

# Mock data
MEMBER_RESPONSE_MA = {
    "members": [
        {
            "subscriberID": "1234567890000",
            "memberId": "00",
            "socialSecurityID": "12345678",
            "accountNumber": "7634526",
            "masterRecordID": "123qwerty",
            "personNumberExtID": "1234567890000TAN",
            "groupNumber": "7634526",
            "memberEffective": {
                "startDate": "2025-08-15",
                "endDate": "3000-12-31",
                "originalEffectiveDate": "2025-08-15"
            },
            "active": True,
            "name": {
                "memberName": {
                    "fullName": "TEST USER",
                    "lastName": "USER",
                    "firstName": "TEST"
                },
                "normalizedName": {
                    "normalizedLastName": "USER",
                    "normalizedFirstName": "TEST"
                }
            },
            "telecom": [
                {
                    "phoneType": "G",
                    "phoneNumber1": "0000000000",
                    "phoneNumber2": "0000000000",
                    "phoneRank": "1"
                }
            ],
            "address": [
                {
                    "addressType": "P",
                    "addressLine1": "123 TEST ST",
                    "city": "TEST CITY",
                    "state": "NJ",
                    "zipCode": "12345",
                    "addressRank": "1"
                }
            ],
            "dateOfBirth": "1990-01-01",
            "gender": "M",
            "relationshipCode": "18",
            "relationshipDescription": "Self",
            "subscriberIndicator": True,
            "subscriber": {
                "subscriberID": "1234567890000",
                "memberId": "00"
            },
            "memberStatus": "Active"
        }
    ]
}

# Mock responses
MEMBER_RESPONSES = {
    "m-a": MEMBER_RESPONSE_MA,
    "m-b-m-n": {"members": [{"memberId": "01", "name": "John Doe"}]},
    "m-n-a-c": {"members": [{"memberId": "02", "name": "Jane Smith"}]},
    "m-e-r": {"error": "Member not found"}
}

COVERAGE_RESPONSES = {
    "c-s": {"coverageId": "c-s", "status": "Active"},
    "c-n-m-id": {"coverageId": "c-n-m-id", "status": "Pending"},
    "c-n-a-c": {"coverageId": "c-n-a-c", "status": "Inactive"},
    "c-e-r": {"error": "Coverage not found"}
}

ACCUM_RESPONSES = {
    "acc-succ": {"accumulatorId": "acc-succ", "value": 1000},
    "acc-rem-amt-miss": {"accumulatorId": "acc-rem-amt-miss", "value": 0},
    "acc-f": {"error": "Accumulator not found"}
}

# API Documentation
st.subheader("API Documentation")
st.markdown("""
### Available Endpoints:

#### Member Endpoints
- `searchMemberById/m-a` - Get member details for ID 'm-a'
- `searchMemberById/m-b-m-n` - Get member details for ID 'm-b-m-n'
- `searchMemberById/m-n-a-c` - Get member details for ID 'm-n-a-c'
- `searchMemberById/m-e-r` - Simulate error response for member search

#### Coverage Endpoints
- `searchCoverageById/c-s` - Get coverage details for ID 'c-s'
- `searchCoverageById/c-n-m-id` - Get coverage details for ID 'c-n-m-id'
- `searchCoverageById/c-n-a-c` - Get coverage details for ID 'c-n-a-c'
- `searchCoverageById/c-e-r` - Simulate error response for coverage search

#### Accumulator Endpoints
- `searchAccums/acc-succ` - Get accumulator details for ID 'acc-succ'
- `searchAccums/acc-rem-amt-miss` - Get accumulator details for ID 'acc-rem-amt-miss'
- `searchAccums/acc-f` - Simulate error response for accumulator search
""")

# Interactive Testing
st.subheader("Test Endpoints")

# Create tabs for different endpoint categories
tab1, tab2, tab3 = st.tabs(["Member Endpoints", "Coverage Endpoints", "Accumulator Endpoints"])

with tab1:
    st.header("Member Endpoints")
    member_id = st.selectbox(
        "Select Member ID",
        ["m-a", "m-b-m-n", "m-n-a-c", "m-e-r"],
        key="member_select"
    )
    
    if st.button("Search Member"):
        result = MEMBER_RESPONSES.get(member_id, {"error": "Invalid member ID"})
        st.json(result)

with tab2:
    st.header("Coverage Endpoints")
    coverage_id = st.selectbox(
        "Select Coverage ID",
        ["c-s", "c-n-m-id", "c-n-a-c", "c-e-r"],
        key="coverage_select"
    )
    
    if st.button("Search Coverage"):
        result = COVERAGE_RESPONSES.get(coverage_id, {"error": "Invalid coverage ID"})
        st.json(result)

with tab3:
    st.header("Accumulator Endpoints")
    accum_id = st.selectbox(
        "Select Accumulator ID",
        ["acc-succ", "acc-rem-amt-miss", "acc-f"],
        key="accum_select"
    )
    
    if st.button("Search Accumulator"):
        result = ACCUM_RESPONSES.get(accum_id, {"error": "Invalid accumulator ID"})
        st.json(result)

# Add some spacing
st.markdown("---")
st.write("✨ Mock API Service - No FastAPI required!")

# Run with: streamlit run streamlit_app.py
