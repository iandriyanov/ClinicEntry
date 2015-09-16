from django.db import models as m


class Doctor(m.Model):
    job = m.CharField(max_length=50)
    abbr = m.CharField(max_length=10)

    def __str__(self):
        return self.job

class IsIt(m.Model):
    ch_tm = m.CharField(max_length=10)

    def __str__(self):
        return self.ch_tm

class Patient(m.Model):
    first_name = m.CharField(max_length=50)
    last_name = m.CharField(max_length=100)
    doctor = m.ForeignKey(Doctor)
    dt = m.DateField("At date")
    tm = m.ForeignKey(IsIt)

    def __str__(self):
        return '%s %s' %(self.first_name, self.last_name)
