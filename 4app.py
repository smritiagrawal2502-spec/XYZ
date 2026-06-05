import streamlit as st
import pandas as pd
from datetime import date

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Global Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("✈️ Global Travel Planner")
st.markdown(
    "Plan trips anywhere in the world — India or International destinations."
)

# -----------------------------------
# SIDEBAR
# -----------------------------------
st.sidebar.header("🌍 Trip Details")

destination = st.sidebar.text_input(
    "Destination",
    placeholder="e.g. Goa, Manali, Paris, Tokyo, Dubai"
)

country = st.sidebar.text_input(
    "Country",
    placeholder="e.g. India, France, Japan"
)

start_date = st.sidebar.date_input(
    "Trip Start Date",
    value=date.today()
)

trip_days = st.sidebar.slider(
    "Trip Duration (Days)",
    min_value=1,
    max_value=30,
    value=5
)

budget = st.sidebar.number_input(
    "Total Budget",
    min_value=5000,
    value=50000,
    step=5000
)

travel_style = st.sidebar.selectbox(
    "Travel Style",
    ["Budget", "Standard", "Luxury"]
)

interests = st.sidebar.multiselect(
    "Travel Interests",
    [
        "Adventure",
        "Food",
        "Nature",
        "Shopping",
        "Historical Places",
        "Nightlife",
        "Photography",
        "Beach",
        "Wildlife"
    ]
)

# -----------------------------------
# SUMMARY
# -----------------------------------
st.header("📍 Trip Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Destination", destination if destination else "-")

with col2:
    st.metric("Country", country if country else "-")

with col3:
    st.metric("Duration", f"{trip_days} Days")

with col4:
    st.metric("Budget", f"₹{budget:,.0f}")

# -----------------------------------
# BUDGET ALLOCATION
# -----------------------------------
st.header("💰 Budget Planner")

if travel_style == "Budget":
    accommodation = 25
    food = 20
    transport = 25
    activities = 20
    shopping = 10

elif travel_style == "Standard":
    accommodation = 35
    food = 20
    transport = 20
    activities = 15
    shopping = 10

else:
    accommodation = 45
    food = 20
    transport = 15
    activities = 10
    shopping = 10

budget_df = pd.DataFrame({
    "Category": [
        "Accommodation",
        "Food",
        "Transport",
        "Activities",
        "Shopping"
    ],
    "Amount": [
        budget * accommodation / 100,
        budget * food / 100,
        budget * transport / 100,
        budget * activities / 100,
        budget * shopping / 100
    ]
})

col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        budget_df,
        values="Amount",
        names="Category",
        title="Budget Distribution",
        hole=0.4
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.dataframe(
        budget_df.style.format({"Amount": "₹{:,.0f}"})
    )

# -----------------------------------
# DAILY EXPENSE
# -----------------------------------
st.header("📊 Daily Budget")

daily_budget = budget / trip_days

st.metric(
    "Average Daily Spending",
    f"₹{daily_budget:,.0f}"
)

# -----------------------------------
# ITINERARY GENERATOR
# -----------------------------------
st.header("🗓️ Suggested Itinerary")

for day in range(1, trip_days + 1):

    with st.expander(f"Day {day}"):

        st.write("🌅 Morning: Explore famous attractions")

        if "Historical Places" in interests:
            st.write("🏛 Visit heritage sites")

        if "Adventure" in interests:
            st.write("🏔 Adventure activities")

        if "Nature" in interests:
            st.write("🌳 Visit parks and scenic viewpoints")

        if "Beach" in interests:
            st.write("🏖 Relax at beaches and waterfronts")

        if "Wildlife" in interests:
            st.write("🦁 Visit wildlife reserves or zoos")

        st.write("🍽 Lunch at a local restaurant")

        if "Shopping" in interests:
            st.write("🛍 Explore local markets")

        if "Photography" in interests:
            st.write("📸 Capture scenic locations")

        if "Food" in interests:
            st.write("🍜 Try local cuisine")

        if "Nightlife" in interests:
            st.write("🌃 Enjoy nightlife and entertainment")

# -----------------------------------
# INTEREST CHART
# -----------------------------------
if interests:

    st.header("🎯 Travel Interest Analysis")

    interest_df = pd.DataFrame({
        "Interest": interests,
        "Count": [1] * len(interests)
    })

    fig2 = px.bar(
        interest_df,
        x="Interest",
        y="Count",
        title="Selected Interests"
    )

    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------------
# DESTINATION INFO
# -----------------------------------
st.header("🌍 Destination Notes")

if destination:
    st.info(
        f"""
        Destination: {destination}

        Country: {country}

        Travel Style: {travel_style}

        Duration: {trip_days} Days

        Suggested: Research weather, visa requirements,
        local transport, and major attractions before travelling.
        """
    )

# -----------------------------------
# PACKING CHECKLIST
# -----------------------------------
st.header("🎒 Packing Checklist")

packing_items = [
    "Passport / ID",
    "Visa Documents",
    "Flight Tickets",
    "Hotel Booking",
    "Mobile Charger",
    "Power Bank",
    "Medicines",
    "Toiletries",
    "Cash / Cards",
    "Camera",
    "Travel Insurance",
    "Extra Clothes"
]

for item in packing_items:
    st.checkbox(item)

# -----------------------------------
# TRIP COST SUMMARY
# -----------------------------------
st.header("💵 Trip Cost Summary")

st.success(
    f"""
    Estimated Trip Cost: ₹{budget:,.0f}

    Daily Budget: ₹{daily_budget:,.0f}

    Duration: {trip_days} Days
    """
)

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")
st.caption("✈️ Global Travel Planner Dashboard | Built with Streamlit")
