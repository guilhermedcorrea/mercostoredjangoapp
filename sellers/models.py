from django.db import models
from django.utils import timezone
from datetime import datetime

class Seller(models.Model):
    #classe tabela Sellers
    idseller = models.IntegerField(primary_key=True)
    sellerid = models.CharField(max_length=255, null=True,blank=True)
    sellername = models.CharField(max_length=255, null=True,blank=True)
    selleremail = models.CharField(max_length=255, null=True,blank=True)
    bitAtivo = models.BooleanField()
    sellerresponsavel = models.CharField(max_length=255, null=True,blank=True)
    senha = models.CharField(max_length=255, null=True,blank=True)
    logoseller = models.CharField(max_length=255, null=True,blank=True)
    dataatualizado = models.DateField(default=datetime.now(), null=True,blank=True)


    def __init__(self, sellerid, sellername, selleremail, bitAtivo, sellerresponsavel, senha,logoseller = ''):
        self.sellerid = sellerid
        self.sellername = sellername
        self.selleremail = selleremail
        self.bitAtivo = bitAtivo
        self.sellerresponsavel = sellerresponsavel
        self.senha = senha
        self.logoseller = logoseller

    
class User(models.Model):
    #Classe Tabela Usuarios
    idusuario = models.IntegerField(primary_key=True)
    sellernome = models.CharField(max_length=255, null=True, blank=True)
    idseller = models.CharField(max_length=255, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    senha = models.CharField(max_length=255, null=True, blank=True)
    perfil = models.CharField(max_length=1000, null=True,blank=True)
    logoseller = models.CharField(max_length=1000, null=True, blank=True)
    ref_idseller = models.IntegerField(null=True, blank=True)


    def __init__(self, sellernome, nome, email, senha,idseller, perfil='',logoseller='',ref_idseller=' ',):
        self.sellernome = sellernome
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil
        self.logoseller = logoseller
        self.idseller = idseller

 

class Produtos(models.Model):
    #Classe tabela produtos
    idproduto = models.IntegerField(primary_key=True)
    idseller = models.IntegerField(null=True, blank=True)
    id_vtex = models.IntegerField(null=True, blank=True)
    referenciaseller = models.CharField(max_length=255, blank=True)
    nomeseller = models.CharField(max_length=255, blank=True)
    ref_ean = models.CharField(max_length=255, null=True, blank=True)
    ref_cod = models.CharField(max_length=255, null=True, blank=True)
    nome_produto = models.CharField(max_length=255, null=True, blank=True)
    imagem = models.CharField(max_length=255, null=True, blank=True)
    perfilprod = models.CharField(max_length=255, null=True, blank=True)
    perfilgoogle = models.CharField(max_length=1000, null=True, blank=True)
    marcaproduto = models.CharField(max_length=255, null=True, blank=True)
    preco_seller = models.FloatField(null=True, blank=True)
    diferenca_preco = models.FloatField(null=True, blank=True)
    bitAtivo = models.BooleanField()
    sellermenorpreco = models.CharField(max_length=255, null=True,blank=True)
    menorpreco = models.FloatField(null=True, blank=False)
    sellermaiorpreco = models.CharField(max_length=255, null=True,blank=True)
    maiorpreco = models.FloatField(null=True, blank=False)
    idcategoriaproduto = models.CharField(max_length=255, null=True, blank=True)
    categoriaproduto = models.CharField(max_length=255, null=True, blank=True)
    dataatualizado = models.DateField(default=datetime.now(),null=True, blank=True)
    #refidprodutos = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)


    def __init__(self,idseller,id_vtex,referenciaseller, nomeseller, ref_ean,
        ref_cod,nome_produto, imagem,perfilprod = 'Nao Informado', perfilgoogle = 'Nao Informado',marcaproduto='Nao Informado',preco_seller = 0,diferenca_preco = 0, bitAtivo=True,
        sellermenorpreco='Nao Informado',menorpreco=0,sellermaiorpreco='Nao Informado', maiorpreco= 0,idcategoriaproduto= 0,categoriaproduto='Nao Informado'):

        self.idseller = idseller
        self.id_vtex = id_vtex
        self.referenciaseller = referenciaseller
        self.nomeseller = nomeseller
        self.ref_ean = ref_ean
        self.ref_cod = ref_cod
        self.nome_produto = nome_produto
        self.imagem = imagem
        self.perfilprod = perfilprod
        self.perfilgoogle = perfilgoogle
        self.marcaproduto = marcaproduto
        self.preco_seller = preco_seller
        self.diferenca_preco = diferenca_preco
        self.bitAtivo = bitAtivo
        self.sellermenorpreco = sellermenorpreco
        self.menorpreco = menorpreco
        self.sellermaiorpreco = sellermaiorpreco
        self.maiorpreco = maiorpreco
        self.idcategoriaproduto = idcategoriaproduto
        self.categoriaproduto = categoriaproduto


class CategoriasProdutos(models.Model):
    #Classe Categorias MercoStore
    id = models.IntegerField(primary_key=True)
    iddepartamento = models.IntegerField(null=True, blank=False)
    nomedepartamento = models.CharField(max_length=255, null=True, blank=True)
    idcategoria = models.IntegerField(null=True, blank=False)
    noemcategoria = models.CharField(max_length=255, null=True, blank=True)
    urlcategoria = models.CharField(max_length=1000, null=True,blank=True)
    #refsprods = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    nomecategoria = models.CharField(max_length=255, null=True, blank=True)


    def __init__(self,iddepartamento, nomedepartamento, idcategoria, noemcategoria,urlcategoria):
        self.iddepartamento = iddepartamento
        self.nomedepartamento = nomedepartamento
        self.idcategoria = idcategoria
        self.noemcategoria = noemcategoria
        self.urlcategoria = urlcategoria


class Googleshopping(models.Model):
    #Classe Google Shopping
    googleid = models.IntegerField(primary_key=True)
    eangoogle = models.CharField(max_length=255,null=True, blank=True)
    urlgoogle = models.CharField(max_length=100,null=True, blank=True)
    sellermen = models.CharField(max_length=255,null=True, blank=True)
    menorpreco = models.FloatField(null=True, blank=True)
    sellermai = models.CharField(max_length=255,null=True, blank=True)
    maiorpreco = models.CharField(max_length=255,null=True, blank=True)
    bitAtivo = models.BooleanField()
    dataatualizado = models.DateField(default=datetime.now(),null=True, blank=True)
    #refgoogle = models.ForeignKey(Seller, on_delete=models.CASCADE)


    def __init__(self,eangoogle, urlgoogle,sellermen, menorpreco,sellermai,maiorpreco, bitAtivo):
        self.eangoogle = eangoogle
        self.urlgoogle = urlgoogle
        self.sellermen = sellermen
        self.menorpreco = menorpreco
        self.sellermai = sellermai
        self.maiorpreco = maiorpreco
        self.bitAtivo = bitAtivo