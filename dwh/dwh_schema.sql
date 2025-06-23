-- Customer Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    income FLOAT,
    region VARCHAR(50)
);

-- Transaction Summary Table
CREATE TABLE customer_summary (
    customer_id INT,
    avg_spent FLOAT,
    total_txn INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Segment Assignment Table
CREATE TABLE segments (
    customer_id INT,
    cluster INT,
    assigned_date DATE DEFAULT GETDATE(),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Campaign Response Table
CREATE TABLE campaign_responses (
    customer_id INT,
    campaign_id INT,
    channel VARCHAR(20),
    response BIT,
    response_date DATE
);
