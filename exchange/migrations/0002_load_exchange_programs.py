from django.db import migrations

INSERT_SQL = """
INSERT INTO exchange_exchangeprogram
    (university, languages, seats, deadline, description)
VALUES
    ('Uniwersytet Warszawski, Польща', 'польська, англійська', '5', '2026-11-15',
     'Один із провідних університетів Польщі, розташований у Варшаві. Приймає іноземних студентів за програмами академічного обміну.'),
    ('KU Leuven (Бельгія)', 'English', '2 місця', '2026-12-01',
     'Дослідницький університет у місті Левен, заснований 1425 року. Один із найстаріших університетів Європи.'),
    ('Vilnius University, Литва', 'англійська', 'до 4', '2026-10-20',
     'Найстаріший університет Литви, заснований 1579 року у Вільнюсі. Пропонує програми обміну англійською мовою.'),
    ('Uniwersytet Jagielloński, Польща', 'Польська, Англійська', '3', '2026-11-15',
     'Один із найстаріших університетів Європи, заснований 1364 року в Кракові. Приймає студентів за програмами обміну польською та англійською мовами.'),
    ('University of Tartu - Естонія', 'англійська, естонська', '2', '2027-01-10',
     'Найстаріший університет Естонії, заснований 1632 року в місті Тарту. Пропонує програми обміну англійською та естонською мовами.'),
    ('Masaryk University, Чехія', 'англійська', '1 місце', '2026-09-30',
     'Один із найбільших університетів Чехії, розташований у Брно. Приймає студентів за програмами обміну англійською мовою.');
"""

DELETE_SQL = """
DELETE FROM exchange_exchangeprogram
WHERE university LIKE 'Uniwersytet Warszawski%'
   OR university LIKE 'KU Leuven%'
   OR university LIKE 'Vilnius University%'
   OR university LIKE 'Uniwersytet Jagielloński%'
   OR university LIKE 'University of Tartu%'
   OR university LIKE 'Masaryk University%';
"""


class Migration(migrations.Migration):

    dependencies = [
        ("exchange", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(sql=INSERT_SQL, reverse_sql=DELETE_SQL),
    ]
