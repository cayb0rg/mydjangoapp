echo "YOOOOO WHATS UP"

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "MySQL started"
fi

echo "Appling database migrations..."
python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001


exec "$@"

