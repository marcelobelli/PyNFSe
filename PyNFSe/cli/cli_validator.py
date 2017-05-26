from prompt_toolkit.validation import Validator, ValidationError


class EmptyValidator(Validator):
    def validate(self, document):
        value = document.text

        if not value:
            raise ValidationError(message='Campo Obrigatório')


class NumberValidator(EmptyValidator):
    def validate(self, document):
        super(NumberValidator, self).validate(document)
        text = document.text

        if text and not text.isdigit():
            i = 0

            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='This input contains non-numeric characters',
                                  cursor_position=i)


class CPFouCNPJChoiceValidator(EmptyValidator):
    def validate(self, document):
        super(CPFouCNPJChoiceValidator, self).validate(document)
        value = document.text.upper()

        if value != 'CPF' and value != 'CNPJ' :
            raise ValidationError(message='CPF ou CNPJ')


class CPFouCNPJValueValidator(NumberValidator):

    def __init__(self, tipo_documento):
        self.tipo_documento = tipo_documento


    def validate(self, document):
        super(NumberValidator, self).validate(document)
        value = document.text

        if self.tipo_documento == 'CPF' and len(value) != 11:
            raise ValidationError(message='CPF deve ser composto de 11 números')

        elif self.tipo_documento == 'CNPJ' and len(value) != 14:
            raise ValidationError(message='CPF deve ser composto de 14 números')
