# Generated by Django 3.2 on 2021-04-25 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bond_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pricing', models.FloatField()),
                ('avg_return', models.FloatField()),
                ('current_profit_predition', models.FloatField()),
                ('updated_date', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='administrator',
            options={'permissions': [('can_add_bond', 'Can create a new bond'), ('can_delete_bond', 'can delete an old bond only if it is not holded by any customer'), ('can_see_customers', 'can see all the customer for a bond'), ('can_see_bonds', 'can see all the customer for a bond')]},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': []},
        ),
        migrations.AlterModelOptions(
            name='salesperson',
            options={'permissions': [('can_sell_bond', 'can sell bond to customer')]},
        ),
        migrations.CreateModel(
            name='SalesRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('bond', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bond_portfolio.bond')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='bond_portfolio.customer')),
                ('sales_person', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sales_person', to='bond_portfolio.salesperson')),
            ],
        ),
    ]
