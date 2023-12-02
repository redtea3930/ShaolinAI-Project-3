import streamlit as st
import pandas as pd

# Sample text extraction from dataframe
# import dataframe from csv
presentation_df = pd.read_csv('presentation.csv')

# Start Streamlit App
st.set_page_config(layout="wide")

# Create header
st.header('H.R.133 - Consolidated Appropriations Act, 2021')

# Dropdown box for title selection
plot_choice = st.selectbox(" ",
                               ("DIVISION C--Department of Defense Appropriations Act, 2021 TITLE I--Military Personnel",
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE II--Operation and Maintenance',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE III--Procurement',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE Title IV--Research, Development, Test and Evaluation',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE Title V--Revolving and Management Funds',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VI--Other Department of Defense Programs',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VII--Related Agencies',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VIII--General Provisions',
                                'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE IX--Overseas Contingency Operations',
                                'DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE I--Departmental Management, Operations, Intelligence, and Oversight',
                                'DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE II--Security, Enforcement, and Investigations',
                                'DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE III--Protection, Preparedness, Response, and Recovery',
                                "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE IV--Research, Development, Training, and Services",           
                                'DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE V--General Provisions',
                                'DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE I',
                                'DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE II',
                                'DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE III',
                                'DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE IV',
                                'DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE V--General Provisions',
                                
                               )
                              )

# Set each dropdown option to return corresponding row of dataframe
if (plot_choice == 'DIVISION C--Department of Defense Appropriations Act, 2021 TITLE I--Military Personnel'):
    row_index = 0
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE II--Operation and Maintenance"):
    row_index = 1      
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE III--Procurement"):
    row_index = 2
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE Title IV--Research, Development, Test and Evaluation"):
    row_index = 3
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE Title V--Revolving and Management Funds"):
    row_index = 4
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VI--Other Department of Defense Programs"):
    row_index = 5
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VII--Related Agencies"):
    row_index = 6
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE VIII--General Provisions"):
    row_index = 7
elif (plot_choice == "DIVISION C--Department of Defense Appropriations Act, 2021 TITLE IX--Overseas Contingency Operations"):
    row_index = 8
elif (plot_choice == "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE I--Departmental Management, Operations, Intelligence, and Oversight"):
    row_index = 9
elif (plot_choice == "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE II--Security, Enforcement, and Investigations"):
    row_index = 10
elif (plot_choice == "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE III--Protection, Preparedness, Response, and Recovery"):
    row_index = 11
elif (plot_choice == "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE IV--Research, Development, Training, and Services"):
    row_index = 12
elif (plot_choice == "DIVISION F--Department of Homeland Security Appropriations Act, 2021 TITLE V--General Provisions"):
    row_index = 13
elif (plot_choice == "DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE I"):
    row_index = 14
elif (plot_choice == "DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE II"):
    row_index = 15
elif (plot_choice == "DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE III"):
    row_index = 16
elif (plot_choice == "DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE IV"):
    row_index = 17
elif (plot_choice == "DIVISION M--Coronavirus Response and Relief Supplemental Appropriations Act, 2021 TITLE V--General Provisions"):
    row_index = 18

# Retrieve summary and full text from dataframe
summary_column = 'summary'
full_text_column = 'Content'
summary = presentation_df.at[row_index, summary_column]
full_text = presentation_df.at[row_index, full_text_column]

# Create two columns
col1, col2 = st.columns(2)

# Display text area for 'Summary' in the left column
col1.markdown('### Summary')
col1.text_area(' ', summary, height=500)

# Display text area for 'Full Text' in the right column
col2.markdown('### Full Text')
col2.text_area(" ", full_text, height=500)