from django.contrib import admin

from app.models import Booking, Profile, Review, Station, Bike
admin.site.register(Profile)
admin.site.register(Station)
admin.site.register(Bike)
admin.site.register(Review)

class BookingAdmin(admin.ModelAdmin):
    list_display= ('id','duration','user','start_time')

admin.site.register(Booking,BookingAdmin)

# Register your models here.
