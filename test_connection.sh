#!/bin/bash

echo "Sprawdzanie połączenia frontend -> backend"
curl -s http://localhost:8080 && echo "Frontend działa" || echo "Błąd: Frontend nie działa"

echo "Sprawdzanie połączenia backend -> MongoDB"
curl -s http://localhost:5000/data && echo "Backend działa i łączy się z MongoDB" || echo "Błąd: Backend nie działa lub brak połączenia z MongoDB"

