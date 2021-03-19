from django.db import models
from django.db.models import fields


class FileControlRecord(models.Model):
    """Model definition for FileControlRecord."""

    register_type = models.PositiveSmallIntegerField(
        verbose_name="Tipo de registro", default=1)
    NIT = models.CharField(verbose_name="NIT", max_length=13)
    entity_name = models.CharField(
        verbose_name="Nombre de entidad recaudadora", max_length=20, blank=True, null=True)
    agreement_code = models.CharField(
        verbose_name="Código del convenio", max_length=15)
    transmission_date = models.DateField(
        verbose_name="Fecha de transmisión del archivo", auto_now=False, auto_now_add=False)
    tracking_number = models.CharField(
        verbose_name="Secuencia de envío", max_length=1)
    expiration_date = models.DateField(
        verbose_name="Fecha de vencimiento", auto_now=False, auto_now_add=False)
    register_number = models.IntegerField(verbose_name="Número de registros")
    total_transaction_value = models.FloatField(
        verbose_name="Valor total de las transacciones")

    class Meta:
        """Meta definition for FileControlRecord."""

        verbose_name = 'Registro de control de archivo'
        verbose_name_plural = 'Registros de control de archivo'


    def save(self, *args, **kwargs):
        model_fields = self._meta.get_fields()
        for field in model_fields:
            # Clean Charfields removing tabs or spaces
            if type(field) == fields.CharField:
                value = self.__getattribute__(field.name)
                self.__setattr__(field.name, value.strip())
        super().save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of FileControlRecord."""
        return f'Registro de {self.entity_name} NIT: {self.NIT}'


class RegisterDetail(models.Model):
    """Model definition for RegisterDetail."""
    INDICATOR = (
        ('S', 'Si'),
        ('N', 'No')
    )

    register_type = models.PositiveSmallIntegerField(
        verbose_name="Tipo de registro", default=6)
    client_id = models.CharField(
        verbose_name="NIT del pagador", max_length=13, blank=True, null=True)
    client_name = models.CharField(
        verbose_name="Nombre del pagador", max_length=20, blank=True, null=True)
    bank_account = models.CharField(
        verbose_name="Cuenta bancaria del pagador", max_length=9, blank=True, null=True)
    bank_account_number = models.CharField(
        verbose_name="Número de la cuenta a debitar", max_length=17, blank=True, null=True)
    transaction_type = models.CharField(
        verbose_name="Tipo de transacción", max_length=2, blank=True, null=True)
    transaction_value = models.FloatField(
        verbose_name="Valor de la transacción")
    validation_indicator = models.CharField(
        verbose_name="Indicador validación NIT/CTA", max_length=1, choices=INDICATOR, null=True, default='N'
    )
    reference1 = models.CharField(
        verbose_name="Referencia 1", max_length=30, blank=True, null=True)
    reference2 = models.CharField(
        verbose_name="Referencia 2", max_length=30, blank=True, null=True)
    expiration_date = models.DateField(
        verbose_name="Fecha de vencimiento", auto_now=False, auto_now_add=False, null=True)
    billed_period = models.CharField(
        verbose_name="Periodos facturados", max_length=2, blank=True, null=True)
    cycle = models.CharField(
        verbose_name="Ciclo", max_length=3, blank=True, null=True)

    class Meta:
        """Meta definition for RegisterDetail."""

        verbose_name = 'Detalle de registros de cobros'
        verbose_name_plural = 'Detalle de registros de cobros'

    def save(self, *args, **kwargs):
        model_fields = self._meta.get_fields()
        for field in model_fields:
            if type(field) == fields.CharField:
                value = self.__getattribute__(field.name)
                self.__setattr__(field.name, value.strip())
        super().save(*args, **kwargs)

    def __str__(self):
        """Unicode representation of RegisterDetail."""
        return f'Registro de {self.client_name} NIT: {self.client_id}'
        
