# Generated by Django 4.2.3 on 2023-07-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThirdsParties',
            fields=[
                ('third_verification_code', models.PositiveIntegerField(null=True, verbose_name='Código de Verificación')),
                ('id_third_parties', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='Identificación del Tercero')),
                ('alternate_id', models.CharField(default=None, max_length=100, null=True, verbose_name='ID alterno')),
                ('third_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre del Tercero')),
                ('third_type_id', models.CharField(choices=[('NIT', 'Nit'), ('CC', 'CÃ©dula de Ciudadania'), ('CE', 'CÃ©dula de Extranjeria'), ('PA', 'Pasaporte'), ('TI', 'Tarjeta de Identidad'), ('NU', 'Nu'), ('RC', 'Registro Civil'), ('NE', 'Sin identificaciÃ³n del exterior o para uso definido por la DIAN')], default='CC', max_length=3, verbose_name='Tipo de Identificación del Tercero')),
                ('third_adress', models.CharField(max_length=200, null=True, verbose_name='Dirección del Tercero')),
                ('third_phone', models.PositiveIntegerField(null=True, verbose_name='Telefono del Tercero')),
                ('third_mail', models.CharField(max_length=100, null=True, verbose_name='Mail del Tercero')),
                ('third_firts_name', models.CharField(max_length=100, null=True, verbose_name='Primer Nombre de Tercero')),
                ('third_second_name', models.CharField(max_length=100, null=True, verbose_name='Segundo Nombre de Tercero')),
                ('third_first_surname', models.CharField(max_length=100, null=True, verbose_name='Primer Apellido de Tercero')),
                ('third_second_surname', models.CharField(max_length=100, null=True, verbose_name='Segundo Apellido de Tercero')),
                ('third_regime', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Regimen Simple'), (2, 'Regimen Ordinario'), (3, 'Responsable de IVA'), (4, 'No Responsable de IVA')], default=1, null=True, verbose_name='Regimen Tributario de Tercero')),
                ('third_is', models.CharField(choices=[('client', 'Cliente'), ('provider', 'Proveedor')], default='client', max_length=100, verbose_name='Tercero es')),
            ],
            options={
                'verbose_name': 'Third Parties',
                'verbose_name_plural': 'third parties',
                'db_table': 'third_parties',
            },
        ),
    ]
