-- Table to store trade transactions
CREATE TABLE trades (
    transaction_id SERIAL PRIMARY KEY,
    source_station_id INT,
    destination_station_id INT,
    cargo_id INT,
    quantity INT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store cargo shipments
CREATE TABLE cargo (
    shipment_id SERIAL PRIMARY KEY,
    source_station_id INT,
    destination_station_id INT,
    quantity INT,
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store inventory levels
CREATE TABLE inventory (
    station_id INT PRIMARY KEY,
    item_name VARCHAR(100),
    quantity INT
);
