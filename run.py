from sqlalchemy import create_engine, text

# Define the connection string with your database credentials
DATABASE_URI = 'mysql+pymysql://root:Tejesh%402001@localhost:3306/denton_amusement'

# Create an engine instance
engine = create_engine(DATABASE_URI)

# Try connecting to the database
try:
    # Establish connection
    connection = engine.connect()
    print("Connection successful!")
    
    # Execute a simple query to confirm it's working
    result = connection.execute(text("SELECT DATABASE();"))
    db_name = result.fetchone()
    print(f"Connected to database: {db_name[0]}")
    
    # Close the connection
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")
