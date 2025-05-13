CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    course VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert some test data
INSERT INTO students (name, email, course) VALUES
    ('John Doe', 'john@example.com', 'Computer Science'),
    ('Jane Smith', 'jane@example.com', 'Mathematics'),
    ('Bob Johnson', 'bob@example.com', 'Physics'); 