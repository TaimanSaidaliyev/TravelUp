from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


IMAGE_SECTION = (
    ('tour', 'Тур'),
    ('attraction', 'Достопримечательности'),
    ('location', 'Локации')
)


class ImagesUpload(models.Model):
    section = models.CharField(max_length=10, choices=IMAGE_SECTION)
    item_id = models.IntegerField(blank=False, verbose_name='ID материала')
    image = models.ImageField(upload_to='media/uploads/%Y/%m/%d', blank=True, null=True,
                              verbose_name='Изображение')
    image_thumbnail_100_75 = ImageSpecField(source='image', processors=[ResizeToFill(100, 75)], format='JPEG',
                                            options={'quality': 100})
    image_thumbnail_200_150 = ImageSpecField(source='image', processors=[ResizeToFill(200, 150)], format='JPEG',
                                             options={'quality': 100})
    image_thumbnail_300_200 = ImageSpecField(source='image', processors=[ResizeToFill(300, 200)], format='JPEG',
                                             options={'quality': 100})

    class Meta:
        verbose_name = 'Дополнительные изображения'
        verbose_name_plural = 'Дополнительные изображения'

    def __str__(self):
        return self.section + ' - ' + str(self.item_id) + ' - ' + str(self.image)