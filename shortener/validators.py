from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    reg_val = value
    if "http" in reg_val:
        new_value = reg_val
        print("yes http")
        print(new_value)
    else:
        new_value = "http://" + value
        print("no http")
        print(new_value)

    try:
        url_validator(new_value)
        print(new_value)
    except:
        raise ValidationError("Invalid URL For This Field")




    # try:
    #     url_validator(value)
    # except:
    #     raise ValidationError("Invalid URL For This Field")
    return new_value
