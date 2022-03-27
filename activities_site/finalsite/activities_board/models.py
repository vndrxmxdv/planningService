from django.db import models


class Event(models.Model):

	eventName = models.CharField(max_length=50, verbose_name='Название')
	content = models.TextField(null=True, blank=True, verbose_name='Описание')
	eventFormat = models.BooleanField(default=False, verbose_name='Онлайн')
	startTime = models.DateTimeField(db_index=True, verbose_name='Время начала') # присваиваем индекс, чтобы сортировать по дате проведения
	endTime = models.DateTimeField(null=True, blank=True, verbose_name='Время окончания') # не обязательно к заполнению
	location = models.TextField(null=True, blank=True, verbose_name='Место проведения')

	published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Время публикации')
	# автоматически вносим текущее время, присваиваем индекс, чтобы сортировать по дате публикаци
	organizer = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Организатор')


	category = models.ManyToManyField('Category', blank=True, verbose_name='Категория') # связи категорий с ивентами


	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'
		ordering = ['-published']

	def __str__(self):
		return self.eventName

class User(models.Model):
	username = models.CharField(max_length=30, verbose_name='Никнейм')
	name = models.CharField(max_length=20, verbose_name='Имя')
	surname = models.CharField(max_length=20, verbose_name='Фамилия')
	email = models.EmailField()
	password = models.CharField(max_length=30, verbose_name='Пароль')
	events = models.ManyToManyField(Event, blank=True, verbose_name='Зарегестрирован на мероприятия', through='Registrations') # здесь будут связи пользователей с ивентами
	userStatus = models.IntegerField(default=0)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

	def __str__(self):
		return self.name

class Registrations(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	event = models.ForeignKey(Event, on_delete=models.CASCADE)

	def save(self, *args, **kwargs):
		q = Registrations.objects.filter(
			user=self.user,
			event=self.event
		)
		if q.exists() <= 0:
			super(Registrations, self).save(*args, **kwargs)

	class Meta:
		ordering = ['user']

	def __str__(self):
		return self.user.name +' - '+ self.event.eventName


class Category(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.title



class Comment(models.Model):
	event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
	body = models.TextField()
	published = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['published']

	def __str__(self):
		return self.body