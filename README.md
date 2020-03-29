person = Person.objects.create(username='admin', email='asd@mailinator.com', is_active=True, is_staff=True, is_superuser=True, identification=123456789, gender='male', phone=3005184942)
person.set_password('admin')
person.save()