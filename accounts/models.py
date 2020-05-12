from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _ 
from django.db.models.signals import post_save
from django.utils.text import slugify 
import datetime
from django.utils import timezone
# Create your models here.
TYPE_OF_PERSON = (
	('M', 'Male'),
	('F', 'Female'),
)
DOCTOR_IN = (
	('جلدية', 'جلدية'),
	('أسنان', 'أسنان'),
	('نفسي', 'نفسي'),
	('أطفال حديثي الولادة', 'أطفال حديثي الولادة'),
	('مخ وأعصاب', 'مخ وأعصاب'),
	('عظام', 'عظام'),
	('نساء وتوليد', 'نساء وتوليد'),
	('أنف وأذن وحنجرة', 'أنف وأذن وحنجرة'),
	('قلب وأوعية دموية', 'قلب وأوعية دموية'),
	('أمراض دم', 'أمراض دم'),
	('أورام', 'أورام'),
	('باطنة', 'باطنة'),
	('تخسيس وتغذية', 'تخسيس وتغذية'),

)
class Profile(models.Model):
	user = models.OneToOneField(User, verbose_name=('user'), on_delete=models.CASCADE)
	name = models.CharField(_("الاسم :"), max_length=100)
	subtitle = models.CharField(_("نبذة عنك :"),max_length=50)
	address = models.CharField(_("المحافظة :"),max_length=50)
	address_details = models.CharField(_(" : العنوان بالتفصيل"),max_length=100)
	phone_number = models.CharField(_("الهاتف :"),max_length=20)
	work_hours = models.CharField(_("ساعات العمل :"),max_length=10)
	waiting_time = models.IntegerField(_("مدة الانتظار :"), blank=True, null=True)
	specialist_doctor = models.CharField(_("متخصص في ؟"), max_length=150 , blank=True, null=True)
	about = models.TextField(_(" من أنا :"), max_length=300)
	price = models.IntegerField(_("سعر الكشف :"), blank=True, null=True)
	image = models.ImageField(_("الصورة الشخصية :"), upload_to='profile', blank=True, null=True)
	slug = models.SlugField(_("slug"),  blank=True, null=True)
	doctor = models.CharField(_("دكتور ؟"), choices=DOCTOR_IN  ,max_length=50, blank=True, null=True)
	joined_us = models.DateTimeField(_("وقت الانضمام :"),auto_now_add=True)
	type_of_person = models.CharField(_("النوع :"), choices=TYPE_OF_PERSON, max_length=50)

	google = models.CharField(max_length=50, blank=True, null=True)
	facebook = models.CharField(max_length=50, blank=True, null=True)
	twitter = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return "%s" %(self.user.username)
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.user.username)	
		super(Profile, self).save(*args, **kwargs)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
