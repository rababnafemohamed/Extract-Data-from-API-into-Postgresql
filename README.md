# **ETL**  

## **Extracting Data from the API**  

I have created a **Databricks** job pipeline to run **notebooks in parallel** to load data from the API in **JSON format**. The JSON data was then formatted into a readable **DataFrame**.  

![Screenshot 2025-02-28 10 54 00 AM](https://github.com/user-attachments/assets/280c5a5f-9ddf-4669-9161-bb4502ce76f8)
![Screenshot 2025-02-28 11 13 31 AM](https://github.com/user-attachments/assets/ec223fd0-621e-4f86-8dcd-170c4570f0fc)


I removed **duplicate values** but decided **not to remove all missing values**, as this could affect the final analysis. Additionally, I **renamed columns** for better readability, created **tables in a PostgreSQL database**, and built **data models**. 

## **PostgreSQL**  

- I created a **PostgreSQL database** in the **AWS cloud** and configured **EC2 VPC security groups** with the necessary **inbound and outbound network settings** to enable connections from the **Databricks workspace**.  
- I then **utilized pgAdmin4** to manage the PostgreSQL database.  

#### ERD: Entity Relationship Diagram

Create a Cow´s Foot Notation (Information Engineering Notation) a method that represent complex database structures in a clear and straightforward manner. 
- Formed one to too many relationship between Cars table and KMS_Cloud
- Formed many any to many relationship between Cars and Mileage_logs
- one to many relationship between Mileage_logs and Internal_Deals
![image](https://github.com/user-attachments/assets/35c18234-9774-466c-a8d0-87506c3bd6c4)

Finally, I **performed data analysis** using **Google Analytics** to answer the following questions:  
- **How many deals became customers?**

![image](https://github.com/user-attachments/assets/2ee3341b-34d1-46bd-9ee2-b73c7a29806e)
![image](https://github.com/user-attachments/assets/66dc8f8a-b86a-4ca6-a2ac-fc7bd7459221)


- **Which brands are most of the customers interested in?**
  - ![graph_visualiser-1740709397977](https://github.com/user-attachments/assets/a4424739-09d7-4dbd-a26f-ee8a0a46f24b) 
- **What are the top 5 selling brands for each province?**
  ![image](https://github.com/user-attachments/assets/f452f70b-aeac-4153-ad99-cfaf759e6908)

- **How many kilometers do customers travel on average per month?**
  
 ![image](https://github.com/user-attachments/assets/21f5d4d8-ec09-49f9-8813-ac4bf39b93d8)




  
