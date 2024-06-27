import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sql
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
    Boolean,
    Enum,
    BigInteger,
    # pr,
    DECIMAL,
    Date
)
from sqlalchemy.sql import func
from database import  Base, engine, _add_tables
from sqlalchemy.ext.declarative import declarative_base



# Define the DIM_DEVICE_DIRECTORY table
class DIM_DEVICE_DIRECTORY(Base):
    __tablename__ = 'DEVICE_DIRECTORY'

    TAC = Column(Integer, nullable=False, primary_key=True)
    MODEL_NAME = Column(String(200), nullable=True)
    VENDOR_NAME = Column(String(200), nullable=True)
    GSM_BANDS = Column(String(200), nullable=True)
    SUPPORTS_LTE = Column(Integer, nullable=True)
    SUPPORTS_VOLTE = Column(Integer, nullable=True)
    BATTERY_CAPACITY = Column(String(50), nullable=True)
    BATTERY_TYPE = Column(String(50), nullable=True)
    BODY_DEPTH = Column(DECIMAL(9, 2), nullable=True)
    BODY_HEIGHT = Column(DECIMAL(9, 2), nullable=True)
    BODY_WIDTH = Column(DECIMAL(9, 2), nullable=True)
    BODY_TYPE = Column(String(50), nullable=True)
    OS_TYPE = Column(String(50), nullable=True)
    OS_VENDOR = Column(String(100), nullable=True)
    OS_VERSION = Column(String(50), nullable=True)
    CAMERA_FLASHLIGHT = Column(Integer, nullable=True)
    CAMERA_MATRIX = Column(DECIMAL(9, 2), nullable=True)  
    CAMERA_PHOTOSIZE = Column(String(50), nullable=True)  
    FRONTCAM_FLASHLIGHT = Column(Integer, nullable=True) 
    FRONTCAM_MATRIX = Column(DECIMAL(9, 2), nullable=True)
    FRONTCAM_PHOTOSIZE = Column(String(50), nullable=True) 
    SUPPORTS_MULTISIM = Column(Integer, nullable=True)  
    SUPPORTS_ESIM = Column(Integer, nullable=True)  
    SUPPORT_5G = Column(Integer, nullable=True)
    SIM_COUNT = Column(Integer, nullable=True)
    SCREEN_RESOLUTION = Column(String(50), nullable=True)  
    CPU_CORES = Column(DECIMAL(20,2), nullable=True) 
    DATA_ONLY = Column(Integer, nullable=True)  
    GPU = Column(String(900), nullable=True) 
    GPU_FREQ = Column(DECIMAL(20,2), nullable=True)
    MULTISIM_MODE = Column(String(50), nullable=True)  
    PIXEL_DENSITY = Column(Integer, nullable=True)
    PROCESSOR = Column(String(200), nullable=True)  
    RAM_SIZE = Column(String(50), nullable=True)
    VIDEO_RESOLUTION = Column(String(50), nullable=True)  
    ANNOUNCE_DATE = Column(Date, nullable=True)
    RELEASE_DATE = Column(Date, nullable=True)
    LOAD_DATE = Column(Date, nullable=True)
    INSERT_DATE = Column(Date, nullable=True)
    BEST_SUPPORT_G_INT = Column(Integer, nullable=True)
    


class DIM_SUB_DEVICE_DIRECTORY(Base):
    __tablename__ = 'SUB_DEVICE_DIRECTORY'

    id = Column(Integer,primary_key=True, autoincrement=True)
    DEVICE_ID = Column(Integer, ForeignKey('DEVICE_DIRECTORY.TAC'), nullable=False)
    MSISDN = Column(String(8), nullable=True)
    IMEI = Column(String(20), nullable=True)
    BRAND = Column(String(100), nullable=True)
    MODEL = Column(String(200), nullable=True)
    NETTYPE = Column(String(10), nullable=True)
    OS = Column(String(50), nullable=True)
    OS_Type = Column(String(50), nullable=True)
    START_DATE = Column(Date, nullable=True)
    END_DATE = Column(Date, nullable=True)
    IMSI_NO = Column(String(15), nullable=True)
    FULL_IMEI = Column(String(20), nullable=True)
    INSERT_DATE = Column(Date, nullable=True)
    DURATION_DAYS = Column(String(10), nullable=True)

recreate = True
if recreate:
    Base.metadata.drop_all(engine)
    print('The Schema is deleted')
    Base.metadata.create_all(bind=engine)
    print('new schema is created')
