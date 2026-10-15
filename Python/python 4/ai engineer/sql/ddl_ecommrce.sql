CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

CREATE TABLE customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    country VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    membership_tier VARCHAR(20),
    registration_date DATE,
    total_orders INT,
    total_spend_usd DECIMAL(12,2),
    avg_order_value_usd DECIMAL(10,2),
    days_since_last_purchase INT,
    preferred_category VARCHAR(50),
    preferred_device VARCHAR(20),
    preferred_payment_method VARCHAR(30),
    acquisition_channel VARCHAR(30),
    reviews_given INT,
    avg_review_score DECIMAL(3,1),
    returns_made INT,
    wishlist_items INT,
    newsletter_subscribed TINYINT(1),
    churned TINYINT(1)
);

CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    customer_id VARCHAR(10),
    order_date DATE,
    year INT,
    month INT,
    quarter VARCHAR(2),
    day_of_week VARCHAR(10),
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price_usd DECIMAL(10,2),
    quantity INT,
    subtotal_usd DECIMAL(10,2),
    discount_pct DECIMAL(5,2),
    discount_amount_usd DECIMAL(10,2),
    shipping_fee_usd DECIMAL(10,2),
    tax_pct DECIMAL(5,2),
    tax_amount_usd DECIMAL(10,2),
    total_amount_usd DECIMAL(10,2),
    payment_method VARCHAR(30),
    device_used VARCHAR(20),
    delivery_days INT,
    delivery_date DATE,
    order_status VARCHAR(20),
    returned TINYINT(1),
    customer_rating DECIMAL(3,1),
    session_duration_minutes DECIMAL(8,2),
    pages_viewed_before_purchase INT,
    is_repeat_customer TINYINT(1),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_name VARCHAR(100) PRIMARY KEY,
    category VARCHAR(50),
    total_orders INT,
    total_revenue_usd DECIMAL(12,2),
    avg_price DECIMAL(10,2),
    avg_rating DECIMAL(3,1),
    return_rate DECIMAL(5,2),
    avg_discount_pct DECIMAL(5,2),
    avg_delivery_days DECIMAL(5,2)
);

CREATE TABLE monthly_revenue (
    year INT,
    month INT,
    quarter VARCHAR(2),
    orders INT,
    revenue_usd DECIMAL(12,2),
    avg_order_value DECIMAL(10,2),
    avg_discount_pct DECIMAL(5,2),
    return_rate DECIMAL(5,2),
    unique_customers INT,
    new_customers INT,
    PRIMARY KEY (year, month)
);