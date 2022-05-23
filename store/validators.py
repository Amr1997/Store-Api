from django.core.validators import ValidationError


def validate_image_size(image):
    max_size_kb = 50 
    
    if image.size > max_size_kb * 1024:
        raise ValidationError(
            'Image size should not exceed %s KB' % max_size_kb
        )