# **REVEL_DE_Technical-Test**  

## **Extracting Data from the API**  

I have created a **Databricks** job pipeline to run **notebooks in parallel** to load data from the API in **JSON format**. The JSON data was then formatted into a readable **DataFrame**.  

I removed **duplicate values** but decided **not to remove all missing values**, as this could affect the final analysis. Additionally, I **renamed columns** for better readability, created **tables in a PostgreSQL database**, and built **data models**.  

Finally, I **performed data analysis** using **Google Analytics** to answer the following questions:  
- **How many deals became customers?**  
- **Which brands are most of the customers interested in?**  
- **What are the top 5 selling brands for each province?**  
- **How many kilometers do customers travel on average per month?**  
- **Which community was most visited in November 2024?**  

---

## **PostgreSQL**  

- I created a **PostgreSQL database** in the **AWS cloud** and configured **EC2 VPC security groups** with the necessary **inbound and outbound network settings** to enable connections from the **Databricks workspace**.  
- I then **utilized pgAdmin4** to manage the PostgreSQL database.  

#### ERD: Entity Relationship Diagram

Create a Cow´s Foot Notation (Information Engineering Notation) a method that represent complex database structures in a clear and straightforward manner. 
- Formed one to too many relationship between Cars table and KMS_Cloud
- Formed many any to many relationship between Cars and Mileage_logs
- one to many relationship between Mileage_logs and Internal_Deals
![image](https://github.com/user-attachments/assets/8d9f675d-666c-4d60-a03f-82ade4da58e0)

  
