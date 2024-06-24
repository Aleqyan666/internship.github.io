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
from schema import CallStatus, MessageStatus



# Define the DIM_DEVICE_DIRECTORY table
class DIM_DEVICE_DIRECTORY(Base):
    __tablename__ = 'DEVICE_DIRECTORY'

    TAC = Column(String(50), nullable=False, primary_key=True)
    MODEL_NAME = Column(String(200), nullable=False)
    VENDOR_NAME = Column(String(200), nullable=False)
    GSM_BANDS = Column(String(200), nullable=False)
    SUPPORTS_LTE = Column(Boolean, nullable=False)
    SUPPORTS_VOLTE = Column(Boolean, nullable=False)
    SUPPORTS_VOWIFI = Column(Boolean, nullable=False)
    NFC_TYPE = Column(String(50), nullable=False)
    BODY_TYPE = Column(String(50), nullable=False)
    OS_TYPE = Column(String(50), nullable=False)
    OS_VENDOR = Column(String(100), nullable=False)
    OS_VERSION = Column(String(50), nullable=False)
    RELEASE_DATE = Column(Date, nullable=False)
    CAMERA_FLASHLIGHT = Column(Boolean, nullable=False)
    CAMERA_MATRIX = Column(DECIMAL(9, 2), nullable=False)
    CAMERA_PHOTOSIZE = Column(String(50), nullable=False)
    FRONTCAM_FLASHLIGHT = Column(Boolean, nullable=False)
    FRONTCAM_MATRIX = Column(DECIMAL(9, 2), nullable=False)
    FRONTCAM_PHOTOSIZE = Column(String(50), nullable=False)
    VIDEO_RESOLUTION = Column(String(50), nullable=False)
    BATTERY_CAPACITY = Column(String(50), nullable=False)
    BATTERY_TYPE = Column(String(50), nullable=False)
    BODY_DEPTH = Column(DECIMAL(9, 2), nullable=False)
    BODY_HEIGHT = Column(DECIMAL(9, 2), nullable=False)
    BODY_WIDTH = Column(DECIMAL(9, 2), nullable=False)
    CPU_CORES = Column(String(50), nullable=False)
    DATA_ONLY = Column(Boolean, nullable=False)
    DIMENSIONS = Column(String(50), nullable=False)
    GPU = Column(String(900), nullable=False)
    GPU_FREQ = Column(String(50), nullable=False)
    MULTISIM_MODE = Column(String(50), nullable=False)
    PIXEL_DENSITY = Column(String(50), nullable=False)
    PROCESSOR = Column(String(200), nullable=False)
    PROCESSOR_CLOCK = Column(String(50), nullable=False)
    RAM_SIZE = Column(String(50), nullable=False)
    SCREEN_RESOLUTION = Column(String(50), nullable=False)
    SIM_COUNT = Column(String(50), nullable=False)
    SUPPORTS_MULTISIM = Column(String(50), nullable=False)
    SUPPORTS_ESIM = Column(Boolean, nullable=False)
    SUPPORT_5G = Column(Boolean, nullable=False)
    


class DIM_SUB_DEVICE_DIRECTORY(Base):
    __tablename__ = 'SUB_DEVICE_DIRECTORY'

    DEVICE_ID = Column(BigInteger, ForeignKey('DEVICE_DIRECTORY.TAC'), nullable=False)
    MSISDN = Column(String(8), nullable=False)
    IMEI = Column(String(20), nullable=True)
    BRAND = Column(String(100), nullable=True)
    MODEL = Column(String(200), nullable=True)
    NETTYPE = Column(String(10), nullable=True)
    OS = Column(String(50), nullable=True)
    OS_Type = Column(String(50), nullable=True)
    START_DATE = Column(Date, nullable=False)
    END_DATE = Column(Date, nullable=False)
    IMSI_NO = Column(String(15), nullable=False)
    FULL_IMEI = Column(String(20), nullable=False)
    INSERT_DATE = Column(Date, nullable=False)

recreate = True
if recreate:
	Base.metadata.drop_all(engine)
	print('The Schema is deleted')
	Base.metadata.create_all(bind=engine)
#     print('new schema is created')
