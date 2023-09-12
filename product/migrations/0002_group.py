from django.db import migrations

def create_customer_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    # Create the "customer" group
    customer_group, created = Group.objects.get_or_create(name='customer')

class Migration(migrations.Migration):

    dependencies = [
       ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_customer_group),
    ]
