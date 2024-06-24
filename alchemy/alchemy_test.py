from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///sample.db")

with engine.connect() as connection:
    result = connection.execute(text('select "HELLO"'))
    print(result.all())