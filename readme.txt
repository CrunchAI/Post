sudo apt-get install libpq-dev
pip install psycopg2
pip install pillow
conda install -c conda-forge postgresql
sudo apt install postgresql-contrib
sudo systemctl start postgresql
sudo -i -u postgres
psql
    CREATE USER bbox_user WITH PASSWORD 'your_password';
#   GRANT ALL PRIVILEGES ON DATABASE postgres TO bbox_user;
    GRANT ALL PRIVILEGES ON DATABASE postgres to admin;
