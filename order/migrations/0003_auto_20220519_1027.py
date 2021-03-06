# Generated by Django 3.2.7 on 2022-05-19 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_pasta_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.IntegerField()),
                ('password', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('numberPage', models.CharField(max_length=64)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.author')),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.book')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalPrice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.clothes')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=64)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.address')),
            ],
        ),
        migrations.CreateModel(
            name='FullName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('color', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LaptopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=64)),
                ('image', models.CharField(max_length=64)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.laptop')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOrder', models.CharField(max_length=64)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.cart')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customer')),
            ],
        ),
        migrations.CreateModel(
            name='PayCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payCastId', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTransaction', models.CharField(max_length=64)),
                ('method', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paypal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paypalId', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemId', models.IntegerField()),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costShip', models.IntegerField()),
                ('nameOptionShip', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gender', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Dinner_Platter',
        ),
        migrations.DeleteModel(
            name='Pasta',
        ),
        migrations.DeleteModel(
            name='Regular_Pizza',
        ),
        migrations.DeleteModel(
            name='Salad',
        ),
        migrations.DeleteModel(
            name='Sicilian_Pizza',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='extras',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.DeleteModel(
            name='Extra',
        ),
        migrations.DeleteModel(
            name='Sub',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.shipment'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.producer'),
        ),
        migrations.AddField(
            model_name='laptop',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.types'),
        ),
        migrations.AddField(
            model_name='customer',
            name='fullName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.fullname'),
        ),
        migrations.AddField(
            model_name='comment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customer'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.material'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.styles'),
        ),
        migrations.AddField(
            model_name='cart',
            name='listItem',
            field=models.ManyToManyField(to='order.Product'),
        ),
        migrations.AddField(
            model_name='bookitem',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.comment'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.publisher'),
        ),
    ]
