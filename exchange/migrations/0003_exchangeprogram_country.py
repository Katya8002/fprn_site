
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0002_load_exchange_programs'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeprogram',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
