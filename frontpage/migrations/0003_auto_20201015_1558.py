# Generated by Django 3.1.2 on 2020-10-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_photo_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislike_target', to='frontpage.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender_identity',
            field=models.IntegerField(choices=[('1', 'Agender'), ('2', 'Androgyne'), ('3', 'Androgynous'), ('4', 'Bigender'), ('5', 'Cis'), ('6', 'Cisgender'), ('7', 'Cis Female'), ('8', 'Cis Male'), ('9', 'Cis Man'), ('10', 'Cis Woman'), ('11', 'Cisgender Female'), ('12', 'Cisgender Male'), ('13', 'Cisgender Man'), ('14', 'Cisgender Woman'), ('15', 'Female'), ('16', 'Female to Male'), ('17', 'FTM'), ('18', 'Gender Fluid'), ('19', 'Gender F*ck'), ('20', 'Gender Nonconforming'), ('21', 'Gender Questioning'), ('22', 'Gender Variant'), ('23', 'Genderqueer'), ('24', 'Male'), ('25', 'Male to Female'), ('26', 'MTF'), ('27', 'Neither'), ('28', 'Neutrois'), ('29', 'Non-binary'), ('30', 'Other'), ('31', 'Pangender'), ('32', 'Trans'), ('33', 'Trans Man'), ('34', 'Trans Person'), ('35', 'Trans Woman'), ('36', 'Transfeminine'), ('37', 'Transgender'), ('38', 'Transgender Female'), ('39', 'Transgender Male'), ('40', 'Transgender Man'), ('41', 'Transgender Person'), ('42', 'Transgender Woman'), ('43', 'Transmasculine'), ('44', 'Transsexual'), ('45', 'Transsexual Female'), ('46', 'Transsexual Male'), ('47', 'Transsexual Man'), ('48', 'Transsexual Person'), ('49', 'Transsexual Woman'), ('50', 'Two Spirit')], max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like_target', to='frontpage.User'),
        ),
    ]
