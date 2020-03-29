from modelchoices import Choices


class GenderChoices(Choices):
    Female = ('F', 'Femenino')
    Male = ('M', 'Masculino')


class StatusChoices(Choices):
    rejected = ('rejected', 'Rejected')
    pending = ('pending', 'Pending')
    Analyzing = ('analyzing', 'Analyzing')
    analyzed = ('analyzed', 'Analyzed')
