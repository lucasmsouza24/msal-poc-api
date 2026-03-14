-- init.sql
CREATE TABLE IF NOT EXISTS log_users_access (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);
