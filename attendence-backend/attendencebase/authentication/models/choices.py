from djchoices import DjangoChoices, ChoiceItem


class GenderChoices(DjangoChoices):
    MALE = ChoiceItem("M")
    FEMALE = ChoiceItem("F")


class PasswordResetStateChoices(DjangoChoices):
    INITIATED = ChoiceItem("INI")
    RESET_CODE_VERIFIED = ChoiceItem("RCV")
    PASSWORD_CHANGED = ChoiceItem("PCH")


