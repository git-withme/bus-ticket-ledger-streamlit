import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Bus Ticket Ledger", layout="centered")

st.title("🚌 Bus Ticket Ledger")

# Initialize session state for data
if 'ledger' not in st.session_state:
    st.session_state.ledger = pd.DataFrame(columns=['Date', 'Passenger Name', 'Destination', 'Fare'])

# Input form
with st.form("ticket_form"):
    name = st.text_input("Passenger Name")
    destination = st.text_input("Destination")
    fare = st.number_input("Fare", min_value=0.0, format="%.2f")
    date = st.date_input("Travel Date", value=datetime.today())
    submit = st.form_submit_button("Add Ticket")

    if submit:
        if name and destination and fare:
            new_entry = {'Date': date, 'Passenger Name': name, 'Destination': destination, 'Fare': fare}
            st.session_state.ledger = pd.concat(
                [st.session_state.ledger, pd.DataFrame([new_entry])],
                ignore_index=True
            )
            st.success("Ticket added to ledger.")
        else:
            st.error("Please fill out all fields.")

# Display ledger
st.subheader("📋 Ticket Ledger")
st.dataframe(st.session_state.ledger, use_container_width=True)

# Download option
if not st.session_state.ledger.empty:
    csv = st.session_state.ledger.to_csv(index=False).encode('utf-8')
    st.download_button("Download Ledger as CSV", data=csv, file_name="bus_ticket_ledger.csv", mime="text/csv")
