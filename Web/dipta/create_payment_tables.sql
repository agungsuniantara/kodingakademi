-- Table for orders
CREATE TABLE orders (
    id_order INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) NOT NULL,
    status ENUM('pending', 'paid', 'cancelled') DEFAULT 'pending',
    payment_method VARCHAR(50),
    shipping_address TEXT,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

-- Table for order details
CREATE TABLE order_details (
    id_order_detail INT PRIMARY KEY AUTO_INCREMENT,
    id_order INT NOT NULL,
    id_product INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_order) REFERENCES orders(id_order),
    FOREIGN KEY (id_product) REFERENCES product(id_product)
);

-- Table for payments
CREATE TABLE payments (
    id_payment INT PRIMARY KEY AUTO_INCREMENT,
    id_order INT NOT NULL,
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10,2) NOT NULL,
    payment_status ENUM('pending', 'success', 'failed') DEFAULT 'pending',
    payment_proof VARCHAR(255),
    FOREIGN KEY (id_order) REFERENCES orders(id_order)
); 