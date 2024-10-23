import cv2
import numpy as np

# Load the template image
template = cv2.imread('C:/Users/Vishal/Desktop/fore/travel_expense/testimg.jpeg')

# Function to write text on the image at a specific location
def write_text(image, text, position, font_scale=0.7, color=(0, 0, 0), thickness=1):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, position, font, font_scale, color, thickness)

# Define employee details
employee_name = "John Doe"
designation = "Software Engineer"
department = "IT"
purpose = "Client Meeting"
place_visited = "New York"
departure_datetime = "2024-10-05 10:00 AM"
arrival_datetime = "2024-10-06 06:00 PM"

# Define bus/train fare details
fare_date = "2024-10-05"
station_from = "Station A"
station_to = "Station B"
travel_mode = "Train"
fare_amount = "$50"
fare_remarks = "N/A"
fare_total = "$50"

# Define local conveyance details
local_date = "2024-10-06"
local_from = "Hotel"
local_to = "Office"
local_travel_mode = "Bus"
local_amount = "$20"
local_remarks = "N/A"
local_total = "$20"

# Define other expenses
bill_no = "12345"
bill_description = "Hotel Stay"
bill_purpose = "Accommodation"
bill_amount = "$100"
bill_remarks = "N/A"
bill_total = "$100"

# Define daily allowance details
daily_allowance = "$30"
days = "2"
allowance_total = "$60"

# Define total bill details
total_A = "$50"  # Bus/Train fare
total_B = "$20"  # Local conveyance
total_C = "$100"  # Other expenses
total_D = "$60"  # Daily allowance
bill_total = "$230"
advance_taken = "$100"
balance_amount = "$130"

# Write employee details on the image
write_text(template, f"Name: {employee_name}", (50, 100))
write_text(template, f"Designation: {designation}", (50, 130))
write_text(template, f"Department: {department}", (50, 160))
write_text(template, f"Purpose: {purpose}", (50, 190))
write_text(template, f"Place Visited: {place_visited}", (50, 220))
write_text(template, f"Departure: {departure_datetime}", (50, 250))
write_text(template, f"Arrival: {arrival_datetime}", (50, 280))

# Write bus/train fare details
write_text(template, f"Date: {fare_date}", (50, 320))
write_text(template, f"From: {station_from}", (50, 350))
write_text(template, f"To: {station_to}", (50, 380))
write_text(template, f"Mode: {travel_mode}", (50, 410))
write_text(template, f"Amount: {fare_amount}", (50, 440))
write_text(template, f"Remarks: {fare_remarks}", (50, 470))
write_text(template, f"Total (A): {fare_total}", (50, 500))

# Write local conveyance details
write_text(template, f"Date: {local_date}", (350, 320))
write_text(template, f"From: {local_from}", (350, 350))
write_text(template, f"To: {local_to}", (350, 380))
write_text(template, f"Mode: {local_travel_mode}", (350, 410))
write_text(template, f"Amount: {local_amount}", (350, 440))
write_text(template, f"Remarks: {local_remarks}", (350, 470))
write_text(template, f"Total (B): {local_total}", (350, 500))

# Write other expenses
write_text(template, f"Bill No: {bill_no}", (50, 540))
write_text(template, f"Description: {bill_description}", (50, 570))
write_text(template, f"Purpose: {bill_purpose}", (50, 600))
write_text(template, f"Amount: {bill_amount}", (50, 630))
write_text(template, f"Remarks: {bill_remarks}", (50, 660))
write_text(template, f"Total (C): {bill_total}", (50, 690))

# Write daily allowance details
write_text(template, f"Daily Allowance: {daily_allowance}", (50, 730))
write_text(template, f"For: {days} days", (50, 760))
write_text(template, f"Total (D): {allowance_total}", (50, 790))

# Write total bill details
write_text(template, f"Bill Total (A+B+C+D): {bill_total}", (50, 830))
write_text(template, f"Advance Taken: {advance_taken}", (50, 860))
write_text(template, f"Balance Amount: {balance_amount}", (50, 890))

# Save the filled form as an image
cv2.imwrite('output.png', template)

# Display the image (optional)
cv2.imshow('Filled Travel Expense Form', template)
cv2.waitKey(0)
cv2.destroyAllWindows()
