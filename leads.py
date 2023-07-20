import pandas as pd
import random
from faker import Faker

# Create a Faker object to generate synthetic data
fake = Faker()

# Set the number of leads you want to generate
num_leads = 100

# Load Indian city names
indian_cities = ['Mumbai', 'Delhi', 'Bengaluru', 'Kolkata', 'Chennai', 'Hyderabad', 'Ahmedabad', 'Pune', 'Surat', 'Jaipur', 'Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Pimpri-Chinchwad', 'Patna', 'Vadodara', 'Ghaziabad', 'Ludhiana', 'Agra', 'Nashik', 'Faridabad', 'Meerut', 'Rajkot', 'Kalyan-Dombivli', 'Vasai-Virar', 'Varanasi', 'Srinagar', 'Aurangabad', 'Dhanbad', 'Amritsar', 'Navi Mumbai', 'Allahabad', 'Ranchi', 'Howrah', 'Coimbatore', 'Jabalpur']
indian_names = ['Aarav Sharma', 'Aashi Gupta', 'Aditi Patel', 'Advait Khan', 'Aisha Singh', 'Akshara Mehta', 'Ananya Verma', 'Aniket Joshi', 'Aaradhya Reddy', 'Aman Shah', 'Amrita Gupta', 'Ananya Khanna', 'Anushka Kumar', 'Arnav Singhania', 'Aarohi Desai', 'Ayush Sengupta', 'Bhavya Sharma', 'Bhavesh Kapoor', 'Chaitanya Singh', 'Dhruv Shah', 'Divya Sharma', 'Diya Choudhury', 'Esha Yadav', 'Ekansh Agarwal', 'Farhan Rana', 'Gauri Singh', 'Gautam Rajput', 'Gopika Nair', 'Harsh Kapoor', 'Ishaan Malhotra', 'Ishika Gupta', 'Ishant Sharma', 'Ishan Verma', 'Ishaani Patel', 'Jai Choudhury', 'Jay Sharma', 'Kabir Kumar', 'Kaira Sengupta', 'Kartik Khanna', 'Krishna Singh', 'Kriti Kapoor', 'Keshav Nair', 'Laksh Gupta', 'Lavya Sharma', 'Mannat Verma', 'Manya Patel', 'Meera Sharma', 'Mihir Shah', 'Nandini Choudhury', 'Navya Singh', 'Nikita Kapoor', 'Nishant Rajput', 'Ojas Gupta', 'Oviya Yadav', 'Pranav Sharma', 'Preeti Patel', 'Purva Kapoor', 'Parth Shah', 'Qamar Khan', 'Raghav Kapoor', 'Rajdeep Verma', 'Rajveer Singh', 'Rashi Gupta', 'Rohit Choudhury', 'Rudra Nair', 'Saanvi Sharma', 'Sahil Yadav', 'Samar Verma', 'Sana Patel', 'Sara Khan', 'Shaurya Kapoor', 'Shivani Shah', 'Shreya Choudhury', 'Siddharth Sharma', 'Siya Nair', 'Tarun Gupta', 'Tanisha Kapoor', 'Tanvi Rajput', 'Udayan Singh', 'Utkarsh Verma', 'Vanya Patel', 'Ved Khanna', 'Vihaan Sharma', 'Vrinda Gupta', 'Vivaan Choudhury', 'Yash Rajput', 'Yashasvi Kapoor', 'Yuvraj Nair', 'Zara Verma']
# Load Indian company names (You can add more company names to this list)
indian_company_names = ['Infosys', 'Tata Consultancy Services', 'Reliance Industries', 'Wipro', 'HDFC Bank', 'ICICI Bank', 'HCL Technologies', 'Bharti Airtel', 'ITC', 'Larsen & Toubro']

# Create empty lists to store data
leads = []

# Generate lead data
for _ in range(num_leads):
    company_name = random.choice(indian_company_names)
    contact_name = random.choice(indian_names)
    email = fake.email()
    phone = fake.phone_number()
    city = random.choice(indian_cities)
    software_type = random.choice(['Web Application', 'Mobile App', 'Custom Software'])
    leads_description = fake.text(max_nb_chars=100)
    lead_converted = random.choice(['Yes', 'No'])

    leads.append({
        'Company Name': company_name,
        'Contact Name': contact_name,
        'Email': email,
        'Phone': phone,
        'City': city,
        'Software Type': software_type,
        'lead Description': leads_description,
        'lead Converted': lead_converted
    })

# Create a DataFrame from the leads list
df = pd.DataFrame(leads)

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('free_lead_dataset.csv', index=False)

print("Free lead dataset for software development company with Indian city and company names and 'Converted' column has been created and saved to 'free_lead_dataset.csv'")

