from empresas.models import User  # Import your custom User model
from django.db import models
from django.urls import reverse_lazy

from core.models import TimeStampedModel
from produto.models import Produto

from .managers import EstoqueEntradaManager, EstoqueSaidaManager

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'


class EstoqueEntrada(Estoque):

    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'
        
    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_detail', kwargs={'pk': self.pk})


class EstoqueSaida(Estoque):

    objects = EstoqueSaidaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque saída'
        verbose_name_plural = 'estoque saída'

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_detail', kwargs={'pk': self.pk})


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoques'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{}'.format(self.produto)


class ProtocoloEntrega(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estoque_atualizado = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse_lazy('estoque:protocolo_de_entrega_detail', kwargs={'pk': self.pk})


class ProtocoloEntregaItens(models.Model):
    protocolo_entrega = models.ForeignKey(
        ProtocoloEntrega,
        on_delete=models.CASCADE,
        related_name='protocolo_entrega'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.protocolo_entrega.pk, self.produto)