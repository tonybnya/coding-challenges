#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip3 install -r requirements.txt

# Static files always need to be collected
python3 manage.py collectstatic --no-input

# IMPORTANT: Check if we're running on Render
if [ -n "$RENDER" ]; then
    echo "Running on Render - setting up persistent database storage"
    
    # Define persistent storage locations
    PERSISTENT_DIR="/var/data"
    PERSISTENT_DB_PATH="$PERSISTENT_DIR/db.sqlite3"
    
    # Create the persistent directory if it doesn't exist
    mkdir -p $PERSISTENT_DIR
    
    # Check if we need to copy the existing database to persistent storage
    if [ ! -f "$PERSISTENT_DB_PATH" ] && [ -f "db.sqlite3" ]; then
        echo "Initial deployment: Copying existing database to persistent storage"
        cp db.sqlite3 $PERSISTENT_DB_PATH
        chmod 664 $PERSISTENT_DB_PATH
    fi
    
    # Set environment variable to use persistent database
    export DATABASE_URL="sqlite:///$PERSISTENT_DB_PATH"
    echo "Using database at: $PERSISTENT_DB_PATH"
    
    # Create a flag file to track if this is the first deployment
    FIRST_DEPLOY_FLAG="$PERSISTENT_DIR/.first_deploy_completed"
fi

# Apply model changes - this is safe and won't reset data
echo "Running makemigrations..."
python manage.py makemigrations challenges --no-input

# Run migrations - this updates schema but preserves data
echo "Running migrate..."
python3 manage.py migrate --no-input

# Only load initial data if this is the first deployment and the flag doesn't exist
if [ -n "$RENDER" ] && [ ! -f "$FIRST_DEPLOY_FLAG" ]; then
    echo "First deployment: Loading initial data"
    # Uncomment next line if you want to load initial data on first deployment only
    python manage.py loaddata data.json
    
    # Create the flag file to indicate first deployment is complete
    touch $FIRST_DEPLOY_FLAG
    echo "Initial data load completed. Future deployments will preserve data."
fi

echo "Build script completed successfully."
