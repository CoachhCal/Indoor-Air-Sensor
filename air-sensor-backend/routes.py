from datetime import datetime
from sqlalchemy import create_engine, Integer, Float, DateTime, text
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, sessionmaker
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")
host = 'localhost'
port = '3306'
database = os.getenv("MYSQL_DB_NAME")

Base = declarative_base()

class Data(Base):

    __tablename__ = "sensor_data"

    id: Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = True)
    temperature: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    humidity: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    pressure: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    gas_resistance: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


# Create the engine
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}')

Session = sessionmaker(bind=engine)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE();"))
        db_name = result.scalar()
        print(f"✅ Successfully connected to the database: {db_name}")
except Exception as e:
    print("❌ Failed to connect to the database.")
    print(f"Error: {e}")


def insert_sensor_data(temperature, humidity, pressure, gas_resistance):
    try:

        with Session() as session: 
            current_data = Data(
                temperature = temperature,
                humidity = humidity,
                pressure = pressure,
                gas_resistance = gas_resistance,
                created_at = datetime.now()
            )

            session.add(current_data)
            session.commit()
            print(f"Data inserted successfully: {current_data.created_at}")

    except Exception as e:
        # session.rollback()
        print(f"Error inserting data: {e}")


def retrieve_recent_data():
    try:
        with Session() as session:
            latest_entry = (
                session.query(Data)
                .order_by(Data.created_at.desc())
                .first()
            )

            if latest_entry:
                return {
                    "id": latest_entry.id,
                    "temperature": latest_entry.temperature,
                    "humidity": latest_entry.humidity,
                    "pressure": latest_entry.pressure,
                    "gas_resistance": latest_entry.gas_resistance,
                    "created_at": latest_entry.created_at.isoformat()
                }
            else:
                return {"message": "No data found"}
            
    except Exception as e:
        print(f"Error retrieving recent data: {e}")
        return {"error": str(e)}
    
def retrieve_all_data():
    try:
        with Session() as session:
            records = (
                session.query(Data)
                .order_by(Data.created_at.asc())
                .all()
            )

            if records:
                return {
                    "timestamps": [r.created_at.isoformat() for r in records],
                    "temperature": [r.temperature for r in records],
                    "humidity": [r.humidity for r in records],
                    "pressure": [r.pressure for r in records],
                    "gas_resistance": [r.gas_resistance for r in records]
                }
            
            else:
                return {"message": "No data found"}
            
    except Exception as e:
        print(f"Error retrieving all data: {e}")
        return {"error": str(e)}





# CREATE DATABASE indoor_air_sensor_db;
# USE indoor_air_sensor_db;

# CREATE TABLE sensor_data (
# 	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#     temperature FLOAT,
#     humidity FLOAT,
#     pressure FLOAT,
#     gas_resistance FLOAT,
#     created_at DATETIME
#     );
