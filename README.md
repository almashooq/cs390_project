# CS390 Project

## Running the Project
Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
First, clone the project repository to your local machine using the following command:
```bash
git clone <https://github.com/almashooq/cs390_project>
```

### 2. Request MongoDB Access
This project uses a MongoDB cluster for data storage. To ensure the system functions correctly, follow these steps:

- Provide your IP address to the project admin.
- The admin will grant your IP access to the MongoDB cluster.

Without this step, the application will not be able to connect to the database.

### 3. Start the Server
Navigate to the project directory and start the server by running:
```bash
python3 server.py
```
Ensure that Python 3 is installed on your machine and the required dependencies are properly configured.

## Prerequisites
Make sure you have the following installed:

- **Python 3.11 and above**: Install the latest version of Python 3 from [Python.org](https://www.python.org/).
- **Required Python Libraries**: Install dependencies using `pip`. A `requirements.txt` file is recommended if it's part of the project. Run:
  ```bash
  pip install -r requirements.txt
  ```

- **MongoDB Access**: Confirm that the admin has provided access to the cluster.

For additional support, contact the admins or refer to the project documentation.


