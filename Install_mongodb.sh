#!/bin/bash

# Step 1: Installing MongoDB
echo "Importing the public GPG key for MongoDB..."
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -

echo "Verifying that the key was added successfully..."
sudo apt-key list | grep "MongoDB 4.4 Release Signing Key"

echo "Adding MongoDB's dedicated package repository to APT sources..."
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list

echo "Updating the local package index..."
sudo apt update

echo "Installing MongoDB..."
sudo apt install -y mongodb-org

# Step 2: Starting the MongoDB Service and Testing the Database
echo "Starting the MongoDB service..."
sudo systemctl start mongod.service

echo "Checking the status of the MongoDB service..."
sudo systemctl status mongod

echo "Enabling MongoDB to start up at boot..."
sudo systemctl enable mongod

echo "Verifying the database connection and status..."
mongo --eval 'db.runCommand({ connectionStatus: 1 })'

echo "MongoDB installation and setup completed successfully."
