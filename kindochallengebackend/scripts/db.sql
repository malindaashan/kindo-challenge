CREATE TABLE school (
    id SERIAL PRIMARY KEY,
    school_name VARCHAR
    );

insert into school(id, school_name) values (1, 'Henderson Valley School'),
(2,'Summerland Primary'),
(3, 'Lincoln Heights School');

CREATE TABLE tripdetail (
    id SERIAL PRIMARY KEY,
    trip_name VARCHAR(255),
    trip_location VARCHAR(255),
    school_id VARCHAR(255),
    grade INTEGER,
    date DATE,
    cost FLOAT,
    CONSTRAINT fk_school
        FOREIGN KEY(school_id)
        REFERENCES school(id)
);


CREATE TABLE registration (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR,
    lastname VARCHAR,
    grade INTEGER,
    parent_name VARCHAR,
    relationship VARCHAR,
    contact VARCHAR,
    email VARCHAR,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tripdetail_id INTEGER NOT NULL,
    CONSTRAINT fk_tripdetail
        FOREIGN KEY(tripdetail_id)
        REFERENCES tripdetail(id)
);


CREATE TABLE payment (
    id SERIAL PRIMARY KEY,
    amount REAL NOT NULL,
    card_number VARCHAR NOT NULL,
    expiry_date VARCHAR NOT NULL,
    success Boolean NOT NULL,
    transaction_id VARCHAR NOT NULL,
    registration_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    CONSTRAINT fk_registration
        FOREIGN KEY (registration_id)
        REFERENCES registration(id)
);















